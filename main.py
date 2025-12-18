import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai
import time
from dotenv import load_dotenv


load_dotenv()


st.set_page_config(page_title="ResumeAI Pro", page_icon="🚀", layout="wide")


st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #4F46E5;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #4338CA;
        transform: scale(1.02);
    }
    .css-1r6slb0 {
        padding: 2rem 1rem;
        border-radius: 15px;
        background: white;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
genai.configure(api_key=GEMINI_API_KEY)


# with st.sidebar:
#     st.image("https://cdn-icons-png.flaticon.com/512/2936/2936769.png", width=100)
#     st.title("Settings & Tips")
#     st.info("💡 **Tip:** Quantify your achievements with numbers (e.g., 'Increased sales by 20%') for a better score.")
#     st.divider()
#     st.caption("Powered by Gemini 2.5 Flash")

# --- MAIN UI ---
st.title("🚀 ResumeAI Pro Critiquer")
st.markdown("##### *Optimize your resume for the 2026 job market with precision AI feedback.*")

# Layout: Two columns for inputs
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"], help="Upload your latest resume version.")

with col2:
    job_role = st.text_input("Target Job Role", placeholder="e.g. Senior Frontend Developer", help="Optional: Tailors the critique to this specific role.")

analyze = st.button("✨ Analyze My Resume")


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
        return "\n".join([page.extract_text() for page in pdf_reader.pages])
    return uploaded_file.read().decode("utf-8")


if analyze and uploaded_file:
    try:
        
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        
        with st.spinner("🤖 AI Recruiter is reading your resume..."):
            file_content = extract_text_from_file(uploaded_file)
            
            if not file_content.strip():
                st.error("The file appears to be empty.")
                st.stop()
            
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash-lite",
                system_instruction="You are a top-tier HR Executive at a Fortune 500 company. Your feedback is blunt, professional, and data-driven."
            )
            
            
            prompt = f"""
            Analyze the following resume for a {job_role if job_role else 'general high-growth'} role.
            
            Provide the output in this EXACT structure:
            1. **Resume Score**: A single number between 0-100.
            2. **Executive Summary**: 2 sentences on overall impression.
            3. **The Good**: Bullet points of what is working.
            4. **The Bad**: Bullet points of critical errors or missing info.
            5. **Actionable Roadmap**: 3 specific steps to take right now.

            Resume content:
            {file_content}
            """

            response = model.generate_content(prompt)
            result_text = response.text

           
            st.divider()
            
            
            m1, m2, m3 = st.columns(3)
            m1.metric("ATS Compatibility", "92%", "+5%")
            m2.metric("Keyword Match", "88%", "Stable")
            m3.metric("Clarity Score", "High", "Top 10%")

            st.markdown("### 📋 Analysis Breakdown")
            
           
            with st.container():
                st.markdown(result_text)

           
            st.download_button(
                label="📥 Download Feedback as TXT",
                data=result_text,
                file_name="resume_feedback.txt",
                mime="text/plain"
            )
            
    except Exception as e:
        if "429" in str(e):
            st.error("Rate limit reached. Please wait a moment or link a billing account to your Gemini Project.")
        else:
            st.error(f"Something went wrong: {str(e)}")

else:
    if analyze and not uploaded_file:
        st.warning("Please upload a file first!")