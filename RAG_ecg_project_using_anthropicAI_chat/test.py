import os
from langchain.document_loaders import PyPDFLoader


data_load = PyPDFLoader('C:\proj_S\survey.pdf')
data_test = data_load.load_and_split()
print(len(data_test))
print(data_test[0])

