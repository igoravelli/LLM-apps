import streamlit as st
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
import os

# importing functions that will be used throughout the code
import sys
sys.path.append('../packages')
from functions import *

# functions loaded
## -- load_document
## -- chunk_documents
## -- create_embeddings
## -- ask_and_get_answer
## -- calculate_embedding_cost



## --- THE STREAMLIT APP ---

if __name__ == '__main__':
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv(), override=True)

    st.image('./files/header_image.png')
    st.subheader('LLM Question-Answering Machine 🎮')
    with st.sidebar:
        api_key = st.text_input('OpenAI API Key', type='password')
        if api_key:
            os.environ['OPENAI_API_KEY'] = api_key

        uploaded_file = st.file_uploader('Upload a file', type=['pdf', 'txt', 'docx'])
        chunk_size = st.number_input('Chunk Size', min_value=100, max_value=2048, value=512)
        k = st.number_input('k', min_value=1, max_value=20, value=3)
        add_data = st.button('Add Data')

        if uploaded_file and add_data:
            with st.spinner('Reading, chunking and embedding file ...'):
                bytes_data = uploaded_file.read()
                file_name = os.path.join('./files/uploaded_files', uploaded_file.name)
                with open(file_name, 'wb') as f:
                    f.write(bytes_data)
                
                print(sys.path)
                data = load_document(file_name)
                chunks = chunk_documents(data, chunk_size=chunk_size)
                st.write(f'Chunk size: {chunk_size}, Chunks: {len(chunks)}')

                tokens, embeddings_cost = calculate_embedding_cost(chunks)
                st.write(f'Embeddings cost: ${embeddings_cost:.4f}')
                
                vector_store = create_embeddings(chunks)

                st.session_state.vs = vector_store
                st.success('Data added successfully')

    question = st.text_input('Ask a question about your file')
    if question:
        if 'vs' in st.session_state:
            vector_store = st.session_state.vs
            st.write(f'k: {k}')
            answer = ask_and_get_answer(vector_store, question, k)
            st.text_area('ChatBot Answer: ', value=answer)