import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PERSONA_INSTRUCTIONS = {
    "Engineer": "Use precise technical language. Keep technical terms. Add clarity and structure.",
    "End Customer": "Simplify language. Avoid jargon. Use friendly, easy-to-understand tone.",
    "Sales": "Make it benefit-focused. Highlight value. Use persuasive, professional tone."
}

def improve_content(text: str, persona: str = "Engineer") -> str:
    """Rewrite content using Groq LLM based on target audience persona."""

    instruction = PERSONA_INSTRUCTIONS.get(persona, PERSONA_INSTRUCTIONS["Engineer"])

    prompt = f"""You are a technical documentation expert.

Rewrite the following content to be clearer, more concise, and better structured.
Target audience: {persona}
Instruction: {instruction}

Original content:
{text}

Rewritten content:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.3
    )

    return response.choices[0].message.content.strip()