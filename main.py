from fastapi import FastAPI
from pydantic import BaseModel
from prediction_model import predict
import numpy as np
from sklearn.linear_model import LinearRegression
import sklearn

app = FastAPI()

@app.get("/")
def home_page():
    return{
        "message": "FastAPI app"
    }

@app.get("/login")
def login_page():
    return{
        "message": "Login For Quant Trading"
    }


#create request body schema
class StockInputs(BaseModel):
    High: float
    Low: float
    Open: float 
    Volume: float
    MA20: float
    Volume_MA20: float
    Volume_Change: float
    Relative_Volume: float 
    Daily_Range:float 
    MA10: float
    MA50: float
    MA10_MA20: float
    MA50_Close: float
    Daily_Return: float
    Day: float
    Weekday: float
    Month: float
    Year: float


@app.post("/prediction_endpoint")
def prediction_page(inputs: StockInputs):

    print(f"data type {inputs.Daily_Range}")
    input_data = [[
            inputs.High,
            inputs.Low,
            inputs.Open,
            inputs.Volume,
            inputs.MA20,
            inputs.Volume_MA20,
            inputs.Volume_Change,
            inputs.Relative_Volume,
            inputs.Daily_Range,
            inputs.MA10,
            inputs.MA50,
            inputs.MA10_MA20,
            inputs.MA50_Close,
            inputs.Daily_Return,
            inputs.Day,
            inputs.Weekday,
            inputs.Month,
            inputs.Year
    ]]

    # make predictions
    predicted_price = predict(input_data)

    print(f"pred{predicted_price}")
    # return prediction result
    return {"Predicted price": predicted_price[0]}