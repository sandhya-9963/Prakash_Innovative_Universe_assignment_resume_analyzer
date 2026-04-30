# extracting the text into strings
import PyPDF2
def extract_text_from_pdf(file):
    pdf_reader=PyPDF2.PdfReader(file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
    return text
# coverting the strings into the vectors and checking the cosine similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_ats_score(resume_text, job_description):
    content=[resume_text,job_description]
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(content)
    similarity_matrix=cosine_similarity(count_matrix)
    match_percentage=similarity_matrix[0][1]*100
    return round(match_percentage,2)
# BUILDING THE STRAMLIT UI
import streamlit as st

st.set_page_config(page_title="ATS Resume Expert", layout="centered")
st.title("Smart ATS Resume Analyzer")

# Input Sections
jd = st.text_area("Paste the Job Description here:", height=200)
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if st.button("Analyze"):
    if uploaded_file is not None and jd != "":
        # Process
        resume_text = extract_text_from_pdf(uploaded_file)
        score = get_ats_score(resume_text, jd)
        
        # Display Results
        st.subheader(f"ATS Match Score: {score}%")
        if score > 70:
            st.success("Great match! Your resume aligns well with this role.")
        else:
            st.warning("You might want to add more keywords from the JD to your resume.")
    else:
        st.error("Please provide both the Job Description and the Resume.")