# src/train_intent.py
# Simple, clean, working version

import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, f1_score

print("Starting training script...")

DATA_PATH = "data/labeled_email.csv"
MODEL_PATH = "src/model/intent_pipeline.joblib"

# Make sure model directory exists
os.makedirs("src/model", exist_ok=True)


def load_data():
    print("Loading dataset from:", DATA_PATH)
    if not os.path.exists(DATA_PATH):
        print("ERROR: File not found →", DATA_PATH)
        return None

    df = pd.read_csv(DATA_PATH)
    print("Dataset shape:", df.shape)

    df = df.fillna("")
    df["text"] = df["subject"] + ". " + df["body"]

    return df


def train():
    df = load_data()
    if df is None:
        return

    print("Label counts:\n", df["intent"].value_counts())

    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=42, stratify=df["intent"]
    )

    X_train = train_df["text"].tolist()
    y_train = train_df["intent"].tolist()

    X_test = test_df["text"].tolist()
    y_test = test_df["intent"].tolist()

    print("Training model...")
    model = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=20000)),
        ("lr", LogisticRegression(max_iter=1000))
    ])

    model.fit(X_train, y_train)
    print("Training finished.")

    preds = model.predict(X_test)

    print("\nTest results:")
    print(classification_report(y_test, preds))
    print("Accuracy:", accuracy_score(y_test, preds))
    print("Macro F1:", f1_score(y_test, preds, average="macro"))

    joblib.dump(model, MODEL_PATH)
    print("Saved model to:", MODEL_PATH)


if __name__ == "__main__":
    train()
