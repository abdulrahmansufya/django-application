from venv import logger

from.utils import validate_title , generate_ai_content

def _build_generate_prompt(title: str, tone: str = None) -> str:
    prompt = f"Write a short blog post about {title}."

    if tone:
        prompt += f" The tone of the blog post should be {tone}."

    prompt += " keep the total output under 120 characters."

    return prompt


def _generate_post(title: str, tone: str = None) -> dict:
    cleaned_title = validate_title(title, min_length=5)
    prompt = _build_generate_prompt(cleaned_title, tone)
    try:
        cleaned_content = generate_ai_content(prompt)

    except Exception:
        logger.error("Error generating content for title: %s", cleaned_title)
        raise
    
    if len(cleaned_content) > 120:
        cleaned_content = cleaned_content[:120]

    return {
        "title": cleaned_title,
        "content": cleaned_content,
        "length": len(cleaned_content)
    }