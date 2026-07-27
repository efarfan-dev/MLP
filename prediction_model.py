import joblib

def predict(data):
    saved_model = joblib.load('linear_regression_model.pkl')
    return saved_model.predict(data)