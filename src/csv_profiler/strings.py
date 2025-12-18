def slugify(text: str) -> str:
    text = text.strip().lower()
    text = text.replace(" ", "-")
    return text
