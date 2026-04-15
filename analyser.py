# analyser.py ✅ Updated for Groq API (Free & Fast)
import os
import re
from dotenv import load_dotenv
from groq import Groq

# Load your API key from .env
load_dotenv()

# Initialize Groq Client
# Ensure you have GROQ_API_KEY in your .env file
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    return text.strip()

def analyze_paper(text):
    # Clean and limit text to fit API context window
    text = clean_text(text)[:6000]
    
    # Import prompt from your prompts.py
    from prompts import create_prompt
    prompt = create_prompt(text)
    
    try:
        # Call Groq's LLM API
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Fast, free model on Groq
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=1024
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}\n\nTip: Check your GROQ_API_KEY in .env"