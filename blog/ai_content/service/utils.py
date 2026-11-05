from ..client import content_client

def validate_text_input(text: str, min_length: int = 20, field_name: str = "Content") -> str:
    if not text or not text.strip():
        raise ValueError(f"{field_name} cannot be empty or whitespace.")

    cleaned_text = text.strip()
    if len(cleaned_text) < min_length:
        raise ValueError(f"{field_name} must be at least {min_length} characters long.")
    return cleaned_text

def validate_title(title:str, min_length:int = 5) -> str:
    return validate_text_input(title, min_length, field_name="Title")

def generate_ai_content(prompt: str, system: str = None) -> str:
    result = content_client.generate(prompt, system=system)

    print("result", result)

    cleaned_result = result.strip()

    print(f"cleaned result: {cleaned_result}")

    if not cleaned_result:
        raise ValueError("Generated content is empty.")

    return cleaned_result

