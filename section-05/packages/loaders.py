def pdf_loader(file):
    from langchain.document_loaders import PyPDFLoader
    loader = PyPDFLoader(file)

    return loader

def docx_loader(file):
    from langchain.document_loaders import Docx2txtLoader
    loader = Docx2txtLoader(file)

    return loader

def wikipedia_loader(query, lang, load_max_docs):
    from langchain.document_loaders import WikipediaLoader
    loader = WikipediaLoader(query, lang=lang, load_max_docs=load_max_docs)

    return loader