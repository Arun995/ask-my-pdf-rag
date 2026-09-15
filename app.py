import os

import streamlit as st

from rag_utility import process_document_to_chroma_db, answer_question


# set the working directory
working_dir = os.path.dirname(os.path.abspath((__file__)))

st.title("openai/gpt-oss-120b - Document RAG")

# file uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    file_id = f"{uploaded_file.name}-{uploaded_file.size}"

    if st.session_state.get("processed_file_id") != file_id:
        # define save path
        save_path = os.path.join(working_dir, uploaded_file.name)
        #  save the file
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.session_state["processed_file_id"] = file_id
        st.info("Document Processed Successfully")

# text widget to get user input
user_question = st.text_area("Ask your question about the document")

if st.button("Answer"):

    answer = answer_question(user_question)

    st.markdown("### openai/gpt-oss-120b Response")
    st.markdown(answer)
