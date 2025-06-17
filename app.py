import streamlit as st
import os

st.title("Welcome to class 10 PW Hub")
st.title("Here you find class 10 All subjects All chapters short notes")
# Set main directory to your notes folder
main_dir = "your_file.pdf"

# List all subjects (subdirectories) in main directory
subjects = [d for d in os.listdir(main_dir) if os.path.isdir(os.path.join(main_dir, d))]
selected_subject = st.selectbox("select a subject",["biology","chemistry","english","maths","physics","SST"] )

# List PDF files in the selected subject directory
subject_dir = os.path.join(main_dir, selected_subject)
pdf_files = [f for f in os.listdir(subject_dir) if f.endswith('.pdf')]

selected_file = st.selectbox("Select a PDF", pdf_files)

if selected_file:
    pdf_path = os.path.join(subject_dir, selected_file)
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    st.download_button("Download PDF", pdf_bytes, file_name=selected_file)

