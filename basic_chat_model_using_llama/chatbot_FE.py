import streamlit as st
import chatbot_BE as cb
from PIL import Image

st.set_page_config(page_title="Chat with myllama", page_icon="🤖")
# st.header()
st.title("Hello User, This is myllama")


# main thing which will do the bg work with the help of be
    
if 'memory' not in st.session_state:
    st.session_state.memory = cb.myllama_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['text'])

input_text = st.chat_input("Chat with myllama :robot_face:")
if input_text:
    with st.chat_message('user'):
        st.markdown(input_text)

    st.session_state.chat_history.append({'role':'user','text':input_text})
    
    chat_response = cb.myllama_conversation(input_txt=input_text, memory=st.session_state.memory)
    
    with st.chat_message('assistant'):
        st.markdown(chat_response)

    st.session_state.chat_history.append({'role':'assistant', 'text':chat_response})
