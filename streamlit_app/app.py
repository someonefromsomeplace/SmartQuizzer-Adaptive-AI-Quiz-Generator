
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from src.extraction.text_extractor import extract_text

st.title("SmartQuizzer – Document Upload")

uploaded_file = st.file_uploader(
    "Upload a PDF or Text file",
    type=["pdf", "txt"]
)

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1].lower()

    try:
        extracted_text = extract_text(uploaded_file, file_type)
        st.success("Text extracted successfully!")

        with st.expander("Preview Extracted Text"):
            st.write(extracted_text[:2000])

    except Exception as e:
        st.error(f"Error extracting text: {str(e)}")
