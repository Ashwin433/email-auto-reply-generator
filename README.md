
# 📧 Email Auto-Reply Generator (ML Powered)

An intelligent **Email Auto-Reply Generator** that suggests context-aware replies using  
**Machine Learning–based intent classification** and **template-driven response generation**.

This project demonstrates how real-world systems like **Gmail Smart Reply** work at a simplified,
explainable level.

---

## 🚀 Features

- 📩 Email intent classification using ML
- ✍️ Smart reply generation with templates
- 🧠 Slot extraction (name, time, invoice number)
- 🏆 Ranking of multiple reply candidates
- ⚡ REST API built using FastAPI
- 👤 Sender-name aware replies (realistic email behavior)

---

## 🧠 Supported Intents

- Meeting Request  
- Reschedule  
- Thank You  
- Job Inquiry  
- Support / Bug Report  
- Billing Query  
- Call Request  
- Spam Detection  

---

## 🏗️ Tech Stack

- **Language:** Python 3.10+
- **Backend:** FastAPI
- **Machine Learning:** Scikit-learn (TF-IDF + Logistic Regression)
- **Model Storage:** Joblib
- **API Server:** Uvicorn
- **Validation:** Pydantic

---

## 📁 Project Structure


email-auto-reply-generator/
│
├── email-replyer/
│ ├── src/
│ │ ├── server.py # FastAPI server
│ │ ├── generator.py # Reply generation logic
│ │ ├── ranker.py # Reply ranking logic
│ │ ├── slot_extractor.py # Slot extraction utilities
│ │ ├── train_intent.py # ML model training script
│ │ └── model/ # Trained model (ignored in Git)
│ │
│ ├── data/
│ │ ├── templates.json # Reply templates
│ │ └── labeled_email.csv # Training dataset
│
├── requirements.txt
├── scaffold_create.py
└── README.md
