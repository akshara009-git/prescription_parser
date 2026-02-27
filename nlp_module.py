import openai

def parse_prescription(text, api_key):
    """
    Uses OpenAI LLM to parse prescription text, extract key info, and simplify explanations.
    """
    openai.api_key = api_key
    prompt = f"""
    Parse this prescription text:
    {text}
    
    Extract medicines, dosages, and instructions.
    Provide a simple, easy-to-understand explanation in plain English.
    Structure it like:
    - Medicine 1: Name - Dosage - Instructions
    - Medicine 2: ...
    - General advice: ...
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()