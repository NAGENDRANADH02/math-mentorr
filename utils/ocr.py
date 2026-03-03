import easyocr

# Load model once
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    result = reader.readtext(image_path)

    extracted_text = ""
    confidence_scores = []

    for (bbox, text, confidence) in result:
        extracted_text += text + " "
        confidence_scores.append(confidence)

    avg_confidence = (
        sum(confidence_scores) / len(confidence_scores)
        if confidence_scores
        else 0
    )

    return extracted_text.strip(), avg_confidence