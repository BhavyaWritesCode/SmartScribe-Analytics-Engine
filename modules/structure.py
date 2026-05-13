import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_structure(text: str) -> dict:
    """Extract structured components from content using Groq LLM."""

    prompt = f"""You are a technical documentation expert.

Analyze the following content and extract these components:
1. Title: A clear, concise title
2. Summary: A 2-3 sentence overview
3. Steps: Key action steps (as a numbered list)
4. Notes: Important warnings or additional notes

Content:
{text}

Respond in this exact format:
TITLE: <title here>
SUMMARY: <summary here>
STEPS:
1. <step 1>
2. <step 2>
3. <step 3>
NOTES: <notes here>"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.2
    )

    raw = response.choices[0].message.content.strip()
    return parse_structure(raw)


def parse_structure(raw: str) -> dict:
    """Parse the structured LLM response into a dictionary."""

    result = {
        "title": "",
        "summary": "",
        "steps": [],
        "notes": ""
    }

    lines = raw.split('\n')
    current_section = None

    for line in lines:
        line = line.strip()
        if line.startswith("TITLE:"):
            result["title"] = line.replace("TITLE:", "").strip()
        elif line.startswith("SUMMARY:"):
            result["summary"] = line.replace("SUMMARY:", "").strip()
        elif line.startswith("STEPS:"):
            current_section = "steps"
        elif line.startswith("NOTES:"):
            current_section = None
            result["notes"] = line.replace("NOTES:", "").strip()
        elif current_section == "steps" and line and line[0].isdigit():
            step = line.split('.', 1)[-1].strip()
            result["steps"].append(step)

    return result