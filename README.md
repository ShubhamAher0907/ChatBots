# NLP ChatBot with LangChain and Streamlit
This project showcases the development of an NLP ChatBot using LangChain, OpenAI's GPT-3.5-turbo model, and Streamlit. The chatbot allows users to ask questions and receive expert NLP responses in real-time.

# Project Overview

This application uses the following technologies:

**LangChain:** A framework for developing applications powered by language models. It enables the chaining of various     
               components like prompts, models, and output parsers.
               
**OpenAI GPT-3.5-turbo:** The language model used to generate responses.

**Streamlit:** A Python framework for building web applications, used here to create a simple frontend for the chatbot.

**Key Components**

Environment Variables:
**OpenAI_Api_Key:** Your OpenAI API key.
**Langchain_Ap_Key:** Your LangChain API key.
**Langchain_Tracing_V2:** Set to true for enabling tracing in LangChain.


**Prompt Template:**

The **ChatPromptTemplate** is used to define the structure of the conversation. In this case, the system is instructed to act as an NLP expert, and the user's question is passed as input.

**Frontend:**

Built using Streamlit, the frontend consists of a text input box where users can type their questions, and a button to submit their queries.

**Model Definition:**

The model used is OpenAI's **gpt-3.5-turbo**, integrated via **LangChain's ChatOpenAI**.
An output parser (StrOutputParser) is used to format the model's response.

**Chain Integration:**

LangChain's chaining capability is leveraged to link the prompt template, language model, and output parser. This chain is invoked when the user submits a question.

**Execution:**

When a user inputs text and clicks the **"Enter"** button, the question is passed to the chain, which processes it through the model and returns the response, displayed on the Streamlit interface.

**How to Run**

Clone the repository.
Install the necessary dependencies via pip install -r requirements.txt.
Set your environment variables (OpenAI_Api_Key, Langchain_Ap_Key).
Run the Streamlit application using streamlit run app.py.
Open the provided local URL in your web browser.
Ask your questions and get real-time NLP expert answers!
Future Enhancements
Add user authentication.
Enhance the UI for better user experience.
Implement more advanced NLP features.
