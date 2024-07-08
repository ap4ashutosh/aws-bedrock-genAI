import streamlit as st
import base64
def set_gif_from_url(url:str):
    """### gif from url"""
    st.markdown(f"![Alt Text]({url})")
def set_gif_from_local(path:str):
    """### gif from local file"""
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )