# LLM study code
Repository with code about LLM and OpenAI API.

Each section is intended to study some part of langchain capability. The structure of the folders is as the following:

## Packages
In this folder are some functions that are used throughout the sections. 
We created this to improve maintenance and not have to import the same functions for every notebook.

## Sections
### Section-02
At this section we explore some basics about LLM.

    - Simple Requests
    - Model GPT-2.5-turbo
    - Templates
    - Simple Chains
    - Sequetial Chains
    - Agents
    - Index database Pinecone
    - Splitting and Embedding Text

### Section-04
Here we build a simple ChatBot using the ChatOpenAI model.

### Section-05
In this section, we build a question-answering system that uses some local file, or even a Wikipedia page, as a source. With it, we can ask anything about the previously loaded data and the system responds in a chatGPT style.

In addition, we implemented the chat history to save all questions and answers, serving as context for the next ones.

### Section-06
Here, we use Streamlit to create a web app application to make the previous chatbot system accessible to anyone, even those who have no coding skills.

To do that, we create a front-end using Streamlit where the user can upload a file (pdf, txt, or docx) and ask questions about the uploaded file.

### Section-07

Section 07 is dedicated to learning about summarization techniques. Here we learn how to summarize documents using AI through its differents methods, like:

    - Basic Prompt
    - Prompt Template
    - Stuff Documents Chain
    - Map_Reduce Prompts
    - Refine Chain
    - Agents


### Section-08
The final section is where we build a real custom ChatGPT application using the streamlit_chat package.