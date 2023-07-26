from flask import Flask
from flask import request
from flask import jsonify
from modules.insurance_predict import InsurancePredict
import pandas as pd



app =  Flask(__name__)

@app.route("/")
def home():
    return "API Modeling"

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    predict_code = InsurancePredict().runModel(df, typed='single')

    result_predict = 'Interested' if predict_code == 1 else 'Not Interested'
    return jsonify({
        "status": "Predicted",
        "predict_code": predict_code,
        "result": result_predict,
        "data": data
    })