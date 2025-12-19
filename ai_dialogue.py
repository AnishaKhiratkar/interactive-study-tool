# ai_dialogue.py
from gtts import gTTS
from groq import Groq

# --- Hardcode your API key here ---
api_key = "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"

# Initialize Groq client
client = Groq(api_key=api_key)

# --- Function to ask AI tutor a question ---
def ask_question(context, question):
    prompt = f"""
You are an economics teacher.
Use the following content to answer the student.

CONTENT:
{context}

STUDENT QUESTION:
{question}

Explain simply and clearly.
"""
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content

# --- Function to convert text to speech ---
def speak_text(text, filename="answer.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename
