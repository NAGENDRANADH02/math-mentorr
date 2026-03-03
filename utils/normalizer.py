def normalize_math_text(text):
    replacements = {
        "square root of": "sqrt",
        "raised to": "^",
        "power of": "^",
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    return text