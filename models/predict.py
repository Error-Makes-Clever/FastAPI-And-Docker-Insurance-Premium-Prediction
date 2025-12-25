import pandas as pd
import pickle

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Mlflow
MODEL_VERSION = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    
    input_df = pd.DataFrame([user_input])

    predicted_class = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence_score = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambda p: round(p, 2), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence_score": round(confidence_score, 4),
        "class_probabilities": class_probs
    }