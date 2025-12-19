
# Interactive Study Tool (NotebookLM Inspired)

This project is an AI-powered interactive study tool built as part of an internship assignment.

It allows students to:
- Study an economics chapter
- Ask questions in an interactive teacher-student format
- Receive clear explanations powered by AI

---

## Features

- Interactive Q&A mode for students
- AI-generated explanations from study material
- Simple and clean Streamlit interface
- Uses real educational content (PDF / text)

---

## Tech Stack

- Python
- Streamlit
- Groq LLM API
- PDF/Text processing

---

## Project Structure

InteractiveStudyTool/
├── main.py
├── pdf_parser.py
├── ai_dialogue.py
├── video_summary.py (optional)
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not pushed to GitHub)

---

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies:

   pip install -r requirements.txt

4. Create a `.env` file and add:

   GROQ_API_KEY=your_api_key_here

5. Run the app:

   streamlit run main.py

---

## Demo

The application runs locally using Streamlit and can be deployed to Streamlit Cloud for a public demo.

---

## Author

<Your Name>
