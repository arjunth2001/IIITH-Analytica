import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd


def getHTML(url):
    try:
        r = requests.get(url)
        return r.text
    except:
        return ""


def getContent(url):
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    paras_tmp = soup.select('div')
    paras = paras_tmp
    return paras


def download_text(text):
    f = []
    for t in text:
        if len(t) > 0:
            f.append(t.get_text())
    return f


def main():
    text = getContent(url)
    return download_text(text)

if __name__ == '__main__':
    summary = []
    content = []
    for i in tqdm(range(601,630)):
        try:
            url = 'https://edit.tosdr.org/points/'+str(i)
            a=main()
            summary.append(a[11].strip('\n ""'))
            content.append(a[21].strip('\n ""'))
        except:
            pass
    data = pd.DataFrame({'Content':content,'Summary':summary})
    data.to_csv('tosdr.csv', index=False)