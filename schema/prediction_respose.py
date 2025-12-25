from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):

    predicted_category: str = Field(
        ..., description="Predicted Insurance Premium category", example="Low"
    )
    confidence_score: float = Field(
        ..., description="Confidence score for the predicted Insurance Premium category", example=0.99
    )
    class_probabilities: Dict[str, float] = Field(
        ..., description="Probability distribution across all possible Insurance Premium category", example={"Low": 0.99, "Medium": 0.005, "High": 0.005}
    )
