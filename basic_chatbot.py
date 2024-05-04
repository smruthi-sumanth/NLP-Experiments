# Bring in deps
import os 

import streamlit as st 
from langchain.llms import ollama 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

# App framework
st.title('🦜🔗 tweet toot')
prompt = st.text_input('Plug in your prompt here') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia research:{wikipedia_research} '
)

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# Initialize the Llama API
llm = ollama(model="llama2")  # Adjusted to use the Llama API

# Wikipedia API Wrapper
wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt: 
    title = llm.invoke(title_template.format(topic=prompt))  # Adjusted to use the Llama API
    wiki_research = wiki.run(prompt) 
    script = llm.invoke(script_template.format(title=title, wikipedia_research=wiki_research))  # Adjusted to use the Llama API
st.write(title)
st.write(script) 
with st.expander('Title History'): 
    st.info(title_memory.buffer)
with st.expander('Script History'): 
    st.info(script_memory.buffer)
with st.expander('Wikipedia Research'): 
    st.info(wiki_research)
