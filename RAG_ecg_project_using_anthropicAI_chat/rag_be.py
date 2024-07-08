import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms.bedrock import Bedrock

def index():
    data_load = PyPDFLoader(r'./book2.pdf')
    data_split = RecursiveCharacterTextSplitter(separators=['\n\n','\n',' ',''],
                                                chunk_size = 100,
                                                chunk_overlap = 10)

    data_embedding = BedrockEmbeddings(
        credentials_profile_name= 'default',
        model_id='amazon.titan-embed-text-v1')

    data_index = VectorstoreIndexCreator(vectorstore_cls=FAISS,
                                        text_splitter=data_split,
                                        embedding=data_embedding,)

    db_index = data_index.from_loaders([data_load])
    return db_index

# def llm():
#     LLM = Bedrock(credentials_profile_name='default',
#                   model_id='meta.llama2-13b-chat-v1',
#                   model_kwargs={"temperature": 0.4, # How creative the model will be
#                                 "top_p": 0.7,       
#                                 "max_gen_len": 512
#                             })
#     return LLM
def llm():
    LLM = Bedrock(credentials_profile_name='default',
                  model_id='anthropic.claude-instant-v1',
                  model_kwargs={"temperature": 0.4, # How creative the model will be
                                "top_p": 0.7,       
                                "max_tokens_to_sample": 512
                            })
    return LLM

def rag_response(index, question):
    rag_query = index.query(question = question, llm = llm())
    return rag_query