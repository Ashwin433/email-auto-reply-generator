import re

def extract_name(text):
    if not text:
        return "there"

    patterns = [
        r"hi\s+([A-Z][a-z]+)",
        r"hello\s+([A-Z][a-z]+)",
        r"dear\s+([A-Z][a-z]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)

    return "there"


def extract_times(text):
    if not text:
        return []

    time_words = [
        "tomorrow", "today", "next week",
        "monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday",
        "morning", "afternoon", "evening"
    ]

    found = []
    text_lower = text.lower()

    for word in time_words:
        if word in text_lower:
            found.append(word)
        if len(found) >= 2:
            break

    return found


def extract_invoice(text):
    if not text:
        return ""

    match = re.search(r"(INV[-_]?\d+(?:-\d+)*)", text, re.IGNORECASE)
    return match.group(1) if match else ""
