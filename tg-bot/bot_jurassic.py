import os
import requests
import configparser
from pyrogram import Client, filters

prefix = "/"
config = configparser.ConfigParser()
config.read('config.ini')

POLICY_TEXT = ""
API_KEY = config['jurassic']['api_key']
bot = Client("op_jurassic")


@bot.on_message(filters.regex(f"^{prefix}(raw)"))
async def raw_stick(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDVVZhmmwMUPwUzdwYis1KWridoAW1JgACWgUAApr-2FRN4S4TaViA3iIE")

@bot.on_message(filters.regex(f"^{prefix}(philosoraptor)"))
async def philosoraptor_stick(_, message):
    await message.reply_sticker("CAACAgUAAxkBAAEDVVhhmmwiBs8-RAYdHU0HyDYlFlq7LAACmwQAAhFd0VRXzs1L7t75vCIE")

@bot.on_message(filters.regex(f"^{prefix}(start|help)"))
async def help(_, message):
    await message.reply_text(
        f"This bot runs Jurassic-1 under the hood. It is fine-tuned for QnA on privacy policies annotated as part of the project.\n\nPaste the part of the privacy policy which you want to question. Reply to this message with **__\\policy__**.\n\nNow you can ask any question in the format **__\\ask <question>__**.",
        parse_mode="markdown")

@bot.on_message(filters.regex(f"^{prefix}(policy|context)"))
async def set_policy(_, message):
    global POLICY_TEXT
    if not message.reply_to_message:
        await message.reply_text(f"Please reply to a message containing the policy text", parse_mode="markdown")
    else:
        POLICY_TEXT = message.reply_to_message.text
        await message.reply_text(f"Policy set", parse_mode="markdown")

@bot.on_message(filters.regex(f"^{prefix}ask"))
async def answer_question(_, message):
    if len(POLICY_TEXT) == 0:
        await message.reply_text(f"Please set a policy first", parse_mode="markdown")
    else:
        context = POLICY_TEXT.replace("\n", "")
        question = message.text.replace("\n", "").replace("/ask ", "")
        prompt = f"Answer the Question based upon the Context.\nContext: {context}\nQuestion: {question}\nAnswer:\n"
        res = requests.post(
            "https://api.ai21.com/studio/v1/j1-jumbo/complete",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "prompt": prompt,
                "numResults": 1,
                "maxTokens": 64,
                "stopSequences": ["."],
                "topKReturn": 0,
                "temperature": 0.7
            }
        )
        answer = res.json()["completions"][0]["data"]["text"]
        await message.reply_text(f"{answer}", parse_mode="markdown")

bot.run()
