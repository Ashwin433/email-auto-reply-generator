from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_candidates

app = FastAPI()

class EmailIn(BaseModel):
    subject: str = ""
    body: str = ""
    sender_name: str = "there"   # ✅ ADD THIS

@app.post("/suggest")
def suggest(email: EmailIn):
    return generate_candidates(
        email.subject,
        email.body,
        sender_name=email.sender_name   # ✅ NOW THIS EXISTS
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Email Auto Reply API is running"}
