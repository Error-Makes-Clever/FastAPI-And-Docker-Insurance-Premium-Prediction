from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.prediction_respose import PredictionResponse
from schema.user_input import UserInput
from models.predict import predict_output, MODEL_VERSION, model

app = FastAPI()

# Human readable
@app.get('/')
def home():
    return {'message': 'Welcome to the Insurance Premium Prediction API'}

# Machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded' : model is not None
    }

@app.post("/predict", response_model= PredictionResponse)
def predict_premium(user_input: UserInput):
    
    user_input = {
        'bmi' : user_input.bmi,
        'age_group' : user_input.age_group,
        'lifestyle_risk' : user_input.lifestyle_risk,
        'city_tier' : user_input.city_tier,
        'income_lpa' : user_input.income_lpa,
        'occupation' : user_input.occupation
    }

    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code= 200, content= {"response" : prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content= str(e))