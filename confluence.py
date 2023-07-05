import streamlit as st
from langchain.document_loaders import ConfluenceLoader

loader = ConfluenceLoader(url="", token="")
documents = loader.load(
    space_key="", include_attachments=True, limit=50, max_pages=50)

st.write(documents)