import streamlit as st

# Import the Ollama class from the langchain_community.llms module
from langchain_community.llms import Ollama

# Initialize the Llama API with the specified model
llm = Ollama(model="llama2")

# Streamlit app title
st.title('Llama spitz')

# Streamlit text input for the user's prompt
user_prompt = st.text_input('Enter your prompt here:')

# Button to trigger the API call
if st.button('Generate Joke'):
    # Invoke the Llama API with the user's prompt
    result = llm.invoke(user_prompt)
    
    # Display the result
    st.write(result)
