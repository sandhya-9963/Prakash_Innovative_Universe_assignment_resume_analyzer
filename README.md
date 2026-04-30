# Prakash_Innovative_Universe_assignment_resume_analyzer

#Smart ATS Resume Analyzer
A streamlined NLP-powered web application designed to help job seekers bridge the gap between their resumes and job requirements. This tool uses Machine Learning techniques to quantify how well a resume matches a specific Job Description (JD).

__Key Features__
Automated Text Extraction: Converts PDF resumes into processable string data using PyPDF2.
Vectorization & Similarity: Transforms text into numerical vectors and applies Cosine Similarity to calculate the match percentage.
Real-time UI: Built with a responsive Streamlit interface for easy user interaction.

__Technical Architecture__
Language: Python 3.x
Framework: Streamlit (Web UI)
Machine Learning: Scikit-Learn (CountVectorizer, Cosine Similarity)
PDF Engine: PyPDF2

__Installation & Setup__
Clone the Repository
git clone https://github.com/sandhya-9963/Prakash_Innovative_Universe_assignment_resume_analyzer.git
cd Prakash_Innovative_Universe_assignment_resume_analyzer

__Install Dependencies__
pip install streamlit PyPDF2 scikit-learn

__Run the Application__
streamlit run app.py

__How It Works__
Parsing: The app reads the uploaded PDF and extracts raw text.
Preprocessing: The text from the Resume and JD is combined into a corpus.
Vectorization: The CountVectorizer converts the text into a frequency-based matrix.
Math: The Cosine Similarity formula is applied:
Similarity=cos(θ)= A.B/(∥A∥∥B∥)
​Output: The resulting coefficient is converted into a percentage and displayed to the user.

 __Project Structure__

├── app.py              # Main application logic and UI
├── README.md           # Project documentation
└── requirements.txt    # List of dependencies

__Future Roadmap__
Integrate TF-IDF for improved keyword weighting.
Add a Keyword Gap Analysis feature to highlight missing skills.
Implement support for .docx and .txt file formats.
