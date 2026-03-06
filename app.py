import streamlit as st
from analyser import analyze_paper
from pdf import extract_text

st.title("📄 Research Paper Analyzer (LLM Mini Project)")

uploaded_file = st.file_uploader(
    "Upload Research Paper (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF Uploaded Successfully")

    text = extract_text(uploaded_file)

    if st.button("Analyze Paper"):

        with st.spinner("Analyzing paper using LLM..."):

            result = analyze_paper(text)

        st.subheader("Analysis Result")
        st.write(result)