import streamlit as st
from pdf_parser import extract_text
from ai_dialogue import ask_question

st.set_page_config(page_title="Interactive Study Tool")

st.title("Interactive Study Tool (PDF Based)")

pdf_path = st.text_input(
    "Enter PDF path (quotes allowed)",
    value='"C:\\Users\\ANISHA\\Downloads\\chapter.pdf"'
)

question = st.text_input("Ask a question from the PDF")

if st.button("Submit"):
    try:
        cleaned_path = pdf_path.strip().strip('"').strip("'")

        with st.spinner("Reading PDF..."):
            pdf_text = extract_text(cleaned_path)

        if not pdf_text.strip():
            st.error("No readable text found in PDF.")
        else:
            with st.spinner("Generating answer..."):
                answer = ask_question(pdf_text, question)
            st.success("Answer:")
            st.write(answer)

    except Exception as e:
        st.error(str(e))
