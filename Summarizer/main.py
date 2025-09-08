import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)
st.header("Reaserch Paper Summarizer")


PaperInput = st.text_input( "Input Research-Paper-Name You Want to Summarize", )
StyleInput = st.selectbox( "Select Explaination Style you want", ["Select Style...", "Begineer Friendly", "Technical", "Code Oriented", "Mathematical"])
LengthInput = st.selectbox( "Select Explaination Length", ["Select Length...", "Short: 1-2 Paragraph", "Medium: 3-5 Paragraph", "Long: Detailed Explaination"])

template = load_prompt("template.json")

if st.button("Summarize"):
    if not PaperInput:
        st.warning("Please paste a paper link to summarize.")
        st.stop()

    with st.spinner("Fetching and summarizing the paper..."):
        try:    
            chain = template | model
            result = chain.invoke({
                 "PaperInput" : PaperInput,
                 "StyleInput" : StyleInput,
                 "LengthInput" : LengthInput
        
            })
            st.subheader("Summary")
            st.write(result.content)

        except Exception as e:
            st.error(f"An error occurred: {e}. Please check the URL and try again.")    