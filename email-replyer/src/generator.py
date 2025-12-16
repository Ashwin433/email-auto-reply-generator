import joblib
import json

from slot_extractor import extract_invoice, extract_times
from ranker import rank_candidates

MODEL_PATH = "src/model/intent_pipeline.joblib"
TEMPLATE_PATH = "data/templates.json"

model = None
templates = None


def safe_fill(template, slots):
    reply = template
    for key, value in slots.items():
        reply = reply.replace("{" + key + "}", value)
    return reply


def load_resources():
    global model, templates

    if model is None:
        model = joblib.load(MODEL_PATH)

    if templates is None:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            templates = json.load(f)

    return model, templates


def generate_candidates(subject, body, sender_name="there", topk=3):
    model, templates = load_resources()

    text = (subject or "") + " " + (body or "")

    probs = model.predict_proba([text])[0]
    labels = model.classes_

    best_idx = probs.argmax()
    intent = labels[best_idx]
    intent_conf = float(probs[best_idx])

    # ✅ USE sender name (NOT extracted from body)
    name = sender_name or "there"

    times = extract_times(text)
    invoice = extract_invoice(text)

    # normalize times
    if len(times) == 0:
        time1, time2 = "next week", "another time"
    elif len(times) == 1:
        time1, time2 = times[0], "another time"
    elif times[0] == times[1]:
        time1, time2 = times[0], "another time"
    else:
        time1, time2 = times[:2]

    slot_values = {
        "name": name,
        "time1": time1,
        "time2": time2,
        "invoice": invoice or "your invoice"
    }

    intent_templates = templates.get(intent, [])

    candidates = []
    filled_counts = []

    for t in intent_templates:
        reply = safe_fill(t, slot_values)
        candidates.append(reply)
        filled_counts.append(sum(1 for v in slot_values.values() if v))

    ranked = rank_candidates(candidates, filled_counts)

    if not ranked:
        ranked = ["Thanks for reaching out. We'll get back to you shortly."]

    return {
        "intent": intent,
        "intent_conf": round(intent_conf, 3),
        "candidates": ranked[:topk]
    }
