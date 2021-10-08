import streamlit as st

PAGES = ["FTC Paragraph Extractor", "Summarizer", "Question and Answering"]


def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Go to", PAGES)
    if selection == "FTC Paragraph Extractor":
        from ftc import ftc
        ftc()
    elif selection == "Summarizer":
        from summarizer import summary
        summary()
    elif selection == "Question and Answering":
        from qna import qna
        qna()
    st.sidebar.title("About")
    st.sidebar.info(
        """
        Made with ♥ by Team IIIT-H Analytica 
        as a part of Online Privacy Course M21.
"""
    )


if __name__ == "__main__":
    main()
