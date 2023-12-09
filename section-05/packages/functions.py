def load_document(file_path):
    import os
    from packages.loaders import pdf_loader, docx_loader
    
    file_name, extension = os.path.splitext(file_path)
       
    print(f'Loading {file_name} with {extension} extension')

    loaders = {
        '.pdf': pdf_loader,
        '.docx': docx_loader
    }
    
    if extension in loaders.keys():
        loader = loaders[extension](file=file_path)
    else:
        raise Exception('Document format not supported')

    data = loader.load()
    return data

def load_from_wikipedia(query, lang='en', load_max_docs=2):
    from packages.loaders import wikipedia_loader
    loader = wikipedia_loader(query=query, lang=lang, load_max_docs=load_max_docs)
    data = loader.load()

    return data

def chunk_documents(data, chunk_size=256):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
    chunks = text_splitter.split_documents(data)
    
    return chunks

def print_embedding_cost(texts):
    import tiktoken
    enc = tiktoken.encoding_for_model('text-embedding-ada-002')
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    print(f'Total Tokens: {total_tokens}')
    print(f'Embedding Cost in USD: {total_tokens / 1000 * 0.0004:.6f}')

def insert_or_fetch_embeddings(index_name):
    import pinecone
    from langchain.vectorstores import Pinecone
    from langchain.embeddings.openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings()
    pinecone.init(
        api_key=os.environ.get('PINECONE_API_KEY'),
        environment=os.environ.get('PINECONE_ENV')
    )

    if index_name in pinecone.list_indexes():
        print(f'Index {index_name} already exists. Loading embeddings...')
        vector_store = Pinecone.from_existing_index(index_name, embeddings)
        print('OK')
    else:
        print(f'Creating index {index_name} and embeddings..')
        pinecone.create_index(index_name, dimension=1536, metric='cosine')
        vector_store = Pinecone.from_documents(chunks, embeddings, index_name=index_name)
        print('OK')

    return vector_store

def delete_pinecone_index(index_name='all'):
    import pinecone
    pinecone.init(
        api_key=os.environ.get('PINECONE_API_KEY'),
        environment=os.environ.get('PINECONE_ENV')
    )

    if index_name == 'all':
        indexes = pinecone.list_indexes()
        print('Deleting all indexes...')
        for index in indexes:
            pinecone.delete_index(index)
        print('OK')
    else:
        print(f'Deleting index {index_name}')
        pinecone.delete_index(index_name)
        print('OK')

def ask_and_get_answer(vector_store, question):
    from langchain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1)

    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})
    chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retriever)

    answer = chain.run(question)
    return answer