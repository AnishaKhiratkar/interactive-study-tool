# pdf_parser.py
import PyPDF2
import requests
import os

def download_pdf(url, save_path="chapter.pdf"):
    """
    Downloads PDF from Google Drive link
    """
    # Extract file id from Google Drive URL
    file_id = url.split("/d/")[1].split("/")[0]
    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    
    # Only download if file does not exist
    if not os.path.exists(save_path):
        response = requests.get(download_url)
        with open(save_path, "wb") as f:
            f.write(response.content)
    return save_path

def extract_text(pdf_path):
    """
    Extract text from PDF
    """
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text
