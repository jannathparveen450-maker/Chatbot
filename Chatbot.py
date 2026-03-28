"""
LLM Text Generator using Streamlit + Ollama

Description:
This app allows users to interact with a local Large Language Model (LLM)
(using Ollama) and generate responses based on user prompts.

Requirements:
- streamlit
- ollama (running locally with a pulled model, e.g., llama3.2)

Run the app:
streamlit run app.py
"""

import streamlit as st
import ollama


# Function to generate LLM response

def generate_llm_response(prompt, model="llama3.2"):
    """
    Sends a prompt to the Ollama LLM and returns the generated response.

    Args:
        prompt (str): User input text
        model (str): Model name (default: llama3.2)

    Returns:
        str: Generated response from the model
    """
    
    # Format messages as required by Ollama chat API
    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    # Call the Ollama model
    response = ollama.chat(model=model, messages=messages)

    # Extract and return the text response
    return response["message"]["content"]


# Streamlit UI Layout

#page layout
st.set_page_config(page_icon="📝",
                   page_title="Text Generator")

# App title
st.title("🧠 LLM Text Generator")

# Description
st.write("Interact with a Large Language Model (LLM) using Ollama.")


# User input box
user_prompt = st.text_area("Enter your prompt:")


# Button to trigger response generation

if st.button("Generate Response"):

    # Check if user entered something
    if user_prompt.strip() != "":

        # Show loading spinner while processing
        with st.spinner("Generating response..."):

            try:
                # Generate response from LLM
                answer = generate_llm_response(user_prompt)

                # Show success message
                st.success("Response generated successfully!")

                # Display the result
                st.text_area("Response:", value=answer, height=200)

            except Exception as e:
                # Handle errors gracefully
                st.error(f"Error: {str(e)}")

    else:
        # Warn if input is empty
        st.warning("Please enter a prompt before generating a response.")