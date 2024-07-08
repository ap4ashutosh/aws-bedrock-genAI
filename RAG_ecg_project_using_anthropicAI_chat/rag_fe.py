import streamlit as st
import rag_be as demo
from PIL import Image
from langchain_core.messages import AIMessage, HumanMessage
from utils import set_gif_from_local

st.set_page_config(page_title='rag qna', page_icon='✨')

with st.sidebar:
    # st.image(im)
    set_gif_from_local(r'./ekg-heart-rate.gif')
    st.write("Your personal Health Assistant ECHO")

if 'vector_index' not in st.session_state:
    with st.spinner("Please wait till index is loaded, All beautiful things in life take time :-)"):
        st.session_state.vector_index = demo.index()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_history.append({'role':'assistant','text':'Hi I am ECHO.\nHow can I help you'})
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['text'])

input_text = st.chat_input("Chat with ECHO 🤖")
if input_text:
    with st.chat_message('user'):
        st.markdown(input_text)

    st.session_state.chat_history.append({'role':'user','text':input_text})
    
    chat_response = demo.rag_response(question=input_text, index=st.session_state.vector_index)
    
    with st.chat_message('assistant'):
        st.markdown(chat_response)

    st.session_state.chat_history.append({'role':'assistant', 'text':chat_response})



# if "chat_history" not in st.session_state:
#         st.session_state.chat_history = [
#             AIMessage(content="Hello, I am a bot. How can I help you?"),
#         ] 

# for message in st.session_state.chat_history:
#         if isinstance(message, AIMessage):
#             with st.chat_message("AI"):
#                 st.write(message.content)
#         elif isinstance(message, HumanMessage):
#             with st.chat_message("Human"):
#                 st.write(message.content)


# # user input
# user_query = st.chat_input("Type your message here...")
# if user_query is not None and user_query != "":
#     response = demo.rag_response(question=user_query, index=st.session_state.vector_index)
#     st.session_state.chat_history.append(HumanMessage(content=user_query))
#     st.session_state.chat_history.append(AIMessage(content=response))
        
       

# # conversation
# for message in st.session_state.chat_history:
#     if isinstance(message, AIMessage):
#         with st.chat_message("AI"):
#             st.write(message.content)
#     elif isinstance(message, HumanMessage):
#         with st.chat_message("Human"):
#             st.write(message.content)