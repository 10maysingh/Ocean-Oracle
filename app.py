import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from datetime import datetime

# Create Flask app
flask_app = Flask(__name__)

# Load the trained model and trained feature names
model = pickle.load(open("model.pkl", "rb"))
trained_features = pickle.load(open("trained_features.pkl", "rb"))


# Preprocessing function
def preprocess_input(lat, lon, day, month, year, trained_features):
    # Create a date object from day, month, and year
    date = datetime(year, month, day)

    input_data = pd.DataFrame([{
        'LAT': lat,
        'LON': lon,
        'date': date
    }])

    # Process the input data (referencing your ML preprocessing code)
    input_data['year'] = input_data['date'].dt.year
    input_data['month'] = input_data['date'].dt.month
    input_data['day_of_week'] = input_data['date'].dt.dayofweek
    input_data['quarter'] = input_data['date'].dt.quarter
    input_data.drop(columns=['date'], inplace=True)

    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'

    input_data['SEASON'] = input_data['month'].apply(get_season)
    input_data = pd.get_dummies(input_data, columns=['SEASON'], drop_first=True)
    input_data['YEAR'] = input_data['year']

    coords = np.radians(input_data[['LAT', 'LON']])
    from sklearn.neighbors import BallTree
    tree = BallTree(coords, metric='haversine')
    radius = 10 / 6371
    input_data['LOCAL_DENSITY'] = tree.query_radius(coords, r=radius, count_only=True)

    # Add missing columns as zeros to match trained features
    for col in trained_features:
        if col not in input_data.columns:
            input_data[col] = 0

    # Reorder columns to match the training data
    input_data = input_data[trained_features]
    return input_data


@flask_app.route("/")
def Home():
    return render_template("index.html")


@flask_app.route("/predict", methods=["POST"])
def predict():
    # Retrieve input features from form
    lat = float(request.form['Latitude'])
    lon = float(request.form['Longitude'])
    day = int(request.form['Day'])
    month = int(request.form['Month'])
    year = int(request.form['Year'])

    # Preprocess the input
    processed_input = preprocess_input(lat, lon, day, month, year, trained_features)

    # Make a prediction
    prediction = model.predict(processed_input)
    prediction_proba = model.predict_proba(processed_input)

    # Customize output message based on prediction
    if prediction[0] == 0:
        result_message = f"Whale is present around. Confidence: {prediction_proba[0][0]*100:.2f}"
    else:
        result_message = f"Whale may not be present. Confidence: {prediction_proba[0][1]*100:.2f}"

    return render_template("index.html", prediction_text=result_message)


if __name__ == "__main__":
    flask_app.run(port=3000, debug=True)
