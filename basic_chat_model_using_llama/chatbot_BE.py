#  Import all the required libraries and functions
import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

#create the chatbot model from aws bedrock
def myllama_chatbot(): #for test i have put input_text input_text:str
    bedrock_llm = Bedrock(
        credentials_profile_name = 'default',
        model_id = 'meta.llama2-70b-chat-v1',
        model_kwargs={
        "temperature": 0.7, # How creative the model will be
        "top_p": 0.5,       
        "max_gen_len": 256 #max length of number of generated tokens
        }
    )
    return bedrock_llm


# Create function for Conversation Memory Buffer as models are stateless
def myllama_memory():
    llm_data = myllama_chatbot()
    memory = ConversationBufferMemory(
        llm = llm_data,
        max_token_limit = 256
    )
    return memory

# Create a function for Conversation chain
def myllama_conversation(input_txt, memory):
    llm_chain_data = myllama_chatbot()
    llm_conversation = ConversationChain(
        llm = llm_chain_data,
        memory = memory,
        verbose = True
    )

    chat_reply = llm_conversation.predict(input = input_txt)
    return chat_reply

