import joblib
from pathlib import Path

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "final_spam_detection_model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict_sms(message):
    if not isinstance(message, str) or not message.strip():
        raise ValueError("Please enter a valid SMS message.")

    prediction = model.predict([message])[0]

    return "SPAM" if prediction == 1 else "HAM"
