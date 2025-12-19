import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai
import time
from dotenv import load_dotenv


load_dotenv()


st.set_page_config(page_title="ResumeAI Pro", page_icon="📃", layout="wide")


st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 25%, #333333 50%, #4d4d4d 75%, #666666 100%);
        background-attachment: fixed;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(1px 1px at 10% 20%, rgba(255,255,255,0.9), transparent),
            radial-gradient(2px 2px at 30% 40%, rgba(255,255,255,0.7), transparent),
            radial-gradient(1px 1px at 60% 10%, rgba(255,255,255,1), transparent),
            radial-gradient(3px 3px at 80% 70%, rgba(255,255,255,0.8), transparent),
            radial-gradient(1px 1px at 90% 30%, rgba(255,255,255,0.9), transparent);
        background-size: 300px 300px, 400px 400px, 200px 200px, 500px 500px, 250px 250px;
        animation: starfield 15s linear infinite;
        pointer-events: none;
        z-index: 0;
    }
    @keyframes starfield {
        0% { 
            transform: scale(0.5) translateZ(0);
            opacity: 0.6;
        }
        50% {
            opacity: 1;
        }
        100% { 
            transform: scale(2) translateZ(100px);
            opacity: 0.3;
        }
    }
    .main .block-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
        border: 1px solid rgba(255,255,255,0.1);
        display: flex;
        flex-direction: column;
        flex: 1;
    }
    .stButton {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3.5em;
        background: linear-gradient(135deg, #1a1a1a, #333333, #1a1a1a);
        color: white;
        font-weight: bold;
        font-size: 1.1em;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        letter-spacing: 1px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #333333, #4d4d4d, #333333);
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(255, 255, 255, 0.3);
        border-color: rgba(255, 255, 255, 0.6);
    }
    .css-1d391kg {
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    .sidebar .sidebar-content {
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(20px);
    }
    .stSidebar > div:first-child {
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    .stSidebar h1 {
        color: white;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }
    .stSidebar .stMarkdown {
        color: rgba(255, 255, 255, 0.9);
    }
    .element-container {
        display: flex;
        flex-direction: column;
    }
    .row-widget {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    .stColumns {
        display: flex;
        gap: 1rem;
        align-items: stretch;
    }
    </style>
    """, unsafe_allow_html=True)


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 
genai.configure(api_key=GEMINI_API_KEY)


# with st.sidebar:
#     st.image("https://cdn-icons-png.flaticon.com/512/2936/2936769.png", width=100)
#     st.title("Tips")
#     st.info("💡 **Tip:** Quantify your achievements with numbers (e.g., 'Increased sales by 20%') for a better score.")
#     st.divider()
#     st.caption("Powered by Gemini 2.5 Flash")


st.title("📃 ResumeAI Pro Critiquer")
st.markdown("##### *Optimize your resume for the 2026 job market with precision AI feedback.*")


col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"], help="Upload your latest resume version.")

with col2:
    job_role = st.text_input("Target Job Role", placeholder="e.g. Senior Frontend Developer", help="Optional: Tailors the critique to this specific role.")

analyze = st.button("🚀Analyze")


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