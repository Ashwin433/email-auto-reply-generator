import os
from pathlib import Path

ROOT = Path.cwd() / "email-replyer"

dirs = [
    "data",
    "src",
    "src/model",
    "web/app",
    "web/static",
    "logs"
]

files_content = {
    "data/labeled_emails.csv": "id,subject,body,intent\n",
    "data/templates.json": """{
  "meeting_request": [
    "Hi {name}, I can do {time1} or {time2}. Which works for you?"
  ],
  "spam": [
    "This looks like spam. Do not click links."
  ]
}
""",
    "src/train_intent.py": "# train_intent.py - you will paste full code later\n",
    "src/slot_extractor.py": "# slot_extractor starter\n",
    "src/generator.py": "# generator starter\n",
    "src/ranker.py": "# ranker starter\n",
    "src/server.py": """from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def health():
    return {'status': 'ok'}
"""
}

# Create the folder structure
ROOT.mkdir(parents=True, exist_ok=True)

for d in dirs:
    (ROOT / d).mkdir(parents=True, exist_ok=True)

# Create starter files
for path, content in files_content.items():
    fp = ROOT / path
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(content, encoding="utf-8")

# Create empty model file
(ROOT / "src/model/intent_pipeline.joblib").write_text("")

print("Project scaffold created at:", ROOT)

