def create_prompt(text):

    prompt = f"""
    Analyze the following research paper and provide:

    1. Summary
    2. Key Contributions
    3. Methodology
    4. Advantages
    5. Limitations
    6. Future Work

    Paper Content:
    {text[:4000]}
    """

    return prompt