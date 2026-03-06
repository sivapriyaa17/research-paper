import re
from transformers import pipeline

# Small model (faster and less memory)
model_name = "sshleifer/distilbart-cnn-12-6"

summarizer = pipeline(
    "summarization",
    model=model_name
)


# --------------------
# CLEAN TEXT
# --------------------
def clean_text(text):

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)

    return text


# --------------------
# ANALYZE PAPER
# --------------------
def analyze_paper(text):

    text = clean_text(text)

    # limit input
    text = text[:3500]

    prompt = f"""
Convert this research paper into easy student notes.

Include:
1. Problem Statement
2. Methodology
3. Key Components
4. Advantages
5. Results
6. Conclusion

Paper:
{text}
"""

    result = summarizer(
        prompt,
        max_length=400,
        min_length=120,
        do_sample=False
    )

    return result[0]["summary_text"]