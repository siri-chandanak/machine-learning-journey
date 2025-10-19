# app.py
from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# -------------------------------
# Load ML model or use DummyModel
# -------------------------------
try:
    model = joblib.load("model.pkl")
    print("Model loaded successfully!")
except Exception as e:
    print("Model not found, using DummyModel. Error:", e)
    class DummyModel:
        def predict(self, X):
            # Simple sum of features as dummy prediction
            return [float(np.sum(x)) for x in X]
    model = DummyModel()

# -------------------------------
# Home Route
# -------------------------------
@app.route('/')
def home():
    return "<h2>✅ Flask ML API is running! Use POST /predict to get predictions.</h2>"

# -------------------------------
# Predict Route
# -------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)  # force=True ensures JSON parsing
        if 'features' not in data:
            return jsonify({'error': 'Missing "features" key in JSON payload'}), 400
        
        X = np.array(data['features'])
        prediction = model.predict(X)

        # Ensure predictions are converted to list for JSON
        prediction_list = prediction.tolist() if hasattr(prediction, 'tolist') else list(prediction)
        return jsonify({'prediction': prediction_list})

    except Exception as e:
        # Return the error as JSON for debugging
        return jsonify({'error': str(e)}), 500

# -------------------------------
# Run the Flask App
# -------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
