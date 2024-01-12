from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()


class InputData(BaseModel):
    Age: int
    Gender: str
    Height: float
    Weight: float
    Fitness_Level: str
    Fitness_Goal: str
    Medical_History: str


# Load your scikit-learn models
try:
    meal_model = pickle.load(open('meal_plan.pkl', 'rb'))
    calories_model = pickle.load(open('calories.pkl', 'rb'))
    workout_model = pickle.load(open('workout_plan.pkl', 'rb'))
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading models: {str(e)}")


@app.post("/predict_all")
def predict_all(Age: int = Query(..., description="Age of the person"),
                Gender: str = Query(..., description="Gender of the person"),
                Height: float = Query(..., description="Height of the person"),
                Weight: float = Query(..., description="Weight of the person"),
                Fitness_Level: str = Query(..., description="Fitness level of the person"),
                Fitness_Goal: str = Query(..., description="Fitness goal of the person"),
                Medical_History: str = Query(..., description="Medical history of the person"),):
    try:
        # Create a pandas DataFrame with named columns
        input_df = pd.DataFrame({
            'Age': [Age],
            'Gender': [Gender],
            'Height': [Height],
            'Weight': [Weight],
            'Fitness_Level': [Fitness_Level],
            'Fitness_Goal': [Fitness_Goal],
            'Medical_History': [Medical_History],
        })

        # Make predictions using the loaded models
        meal_plan = meal_model.predict(input_df)
        calories = calories_model.predict(input_df)
        workout_plan = workout_model.predict(input_df)

        # Directly return the predictions
        return {
            "meal_plan": meal_plan[0],
            "calories": calories[0],
            "workout_plan": workout_plan[0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(r)}")