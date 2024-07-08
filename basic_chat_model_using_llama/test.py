from langchain.llms.bedrock import Bedrock

def myllama_chatbot(input_txt): #for test i have put input_text input_text:str
    bedrock_llm = Bedrock(
        credentials_profile_name = 'default',
        model_id = 'meta.llama2-13b-chat-v1',
        model_kwargs={
        "temperature": 0.7, # How creative the model will be
        "top_p": 0.5,       
        "max_gen_len": 1024 #max length of number of generated tokens
        }
    )
    return bedrock_llm.invoke(input_txt)

response = myllama_chatbot('What is the capitol?')
print(response)