import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

def set_env_variables():
    load_dotenv(find_dotenv(), override=True)
    print("It's all right!")


def instantiate_llm(model_name="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model_name=model_name)
    
    return llm

def print_embedding_cost(texts):
    import tiktoken
    enc = tiktoken.encoding_for_model('text-embedding-ada-002')
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    print(f'Total Tokens: {total_tokens}')
    print(f'Embedding Cost in USD: {total_tokens / 1000 * 0.0004:.6f}')