# 🚀 ResumeAI Pro Critiquer

A Python-powered resume analysis tool that provides AI-driven feedback to optimize your resume for the 2026 job market. Built with Streamlit and powered by Google's Gemini AI.

## 📋 About This Project

**Note:** This is a learning project as I'm exploring Python development and AI integration.

ResumeAI Pro analyzes your resume like a Fortune 500 HR executive, providing:
- Professional resume scoring (0-100)
- Executive summary of your resume's strengths
- Detailed feedback on what's working and what needs improvement
- Actionable roadmap for immediate improvements
- ATS compatibility metrics

## ✨ Features

- **PDF & TXT Support**: Upload resumes in multiple formats
- **Job-Specific Analysis**: Tailor feedback to specific job roles
- **Real-time Processing**: Get instant AI-powered feedback
- **Professional UI**: Clean, modern interface with progress indicators
- **Downloadable Reports**: Save your feedback as TXT files
- **ATS Metrics**: Track compatibility scores and keyword matching

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **Google Gemini AI** - AI-powered resume analysis
- **PyPDF2** - PDF text extraction
- **python-dotenv** - Environment variable management

## 📦 Installation

1. **Clone or download this project**
   ```bash
   git clone <your-repo-url>
   cd project1
   ```

2. **Install required packages**
   ```bash
   pip install streamlit PyPDF2 google-generativeai python-dotenv
   ```

3. **Set up environment variables**
   - Create a `.env` file in the project directory
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Get a Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add it to your `.env` file

## 🚀 Usage

1. **Run the application**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser** to `http://localhost:8501`

3. **Upload your resume** (PDF or TXT format)

4. **Optional**: Enter your target job role for tailored feedback

5. **Click "Analyze My Resume"** and get instant AI feedback

## 📁 Project Structure

```
project1/
├── main.py          # Main Streamlit application
├── .env             # Environment variables (create this)
├── README.md        # This file
└── requirements.txt # Dependencies (optional)
```

## 🔧 Requirements

Create a `requirements.txt` file with:
```
streamlit
PyPDF2
google-generativeai
python-dotenv
```

## 🎯 Learning Goals

As someone new to Python, this project helped me learn:
- Building web apps with Streamlit
- Working with AI APIs (Google Gemini)
- File handling and PDF processing
- Environment variable management
- Creating user-friendly interfaces

## ⚠️ Important Notes

- **API Limits**: Free Gemini API has rate limits
- **File Size**: Large PDFs may take longer to process
- **Privacy**: Files are processed locally and sent to Gemini API
- **Learning Project**: Code may not follow all production best practices

## 🐛 Troubleshooting

**Rate limit errors**: Wait a moment or upgrade your Gemini API plan

**Empty file errors**: Ensure your PDF has extractable text

**API key errors**: Check your `.env` file and API key validity

## 🚀 Future Improvements

- Add more file format support
- Implement resume templates
- Add comparison features
- Include industry-specific analysis
- Add resume builder functionality

## 📝 License

This is a personal learning project. Feel free to use and modify as needed.

---

*Built with ❤️ while learning Python*