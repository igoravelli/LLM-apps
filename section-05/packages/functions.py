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
