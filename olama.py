from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from langchain_community.llms import Ollama


os.environ["Langchain_Ap_Key"]="ls__1b9ad6adfb1c4292935984c9d973bf86"
os.environ["LANGCHAIN_TRACING_V2"]="true"


# Create prompt which will be passed to LLM 

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You need to act as a NLP expert"),
        ("user","Question:{Question}")
    ]
)

# Create fronend using streamlit

st.title("NLP ChatBot")
input_text=st.text_input("Enter whatever you want to ask")
st.button("Enter")


# Define the model and pass prompt to it 



llm=Ollama(model="llama2")
output_parser=StrOutputParser()

# Using chain we will combine all (LLM model , Prompt , Output Parser)

chain=prompt|llm|output_parser

# Whaever we will type into the given box that question will be passed to variable Question 

if input_text:
    st.write(chain.invoke({"Question": input_text}))
