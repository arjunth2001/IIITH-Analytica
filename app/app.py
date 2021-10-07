import streamlit as st

PAGES = ["OPP 115", "Summarize", "QnA"]


def main():
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Go to", PAGES)
    if selection == "OPP 115":
        st.subheader("OPP 115 Classifaction and Visualisation")
        st.write("Under Construction")
    elif selection == "Summarize":
        from summarizer import summary
        summary()
    elif selection == "QnA":
        st.subheader("QnA")
        st.write("Under Construction")
    st.sidebar.title("About")
    st.sidebar.info(
        """
        Made with ♥ by Team IIIT-H Analytica 
        as a part of Online Privacy Course M21.
"""
    )


if __name__ == "__main__":
    main()
