import os
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

def set_env_variables():
    load_dotenv(find_dotenv(), override=True)
    print("It's all right!")


def instantiate_llm(model_name="gpt-3.5-turbo"):
    llm = ChatOpenAI(temperature=0, model_name=model_name)
    
    return llm

