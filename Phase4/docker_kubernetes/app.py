# A simple Flask-based ML API

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained ML model (for demo, use a dummy model)
# Save this model using: joblib.dump(model, 'model.pkl') in your training notebook
try:
    model = joblib.load("model.pkl")
except:
    # Fallback dummy model
    class DummyModel:
        def predict(self, X):
            return [sum(x) for x in X]
    model = DummyModel()

@app.route('/')
def home():
    return "ML Model API Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X = np.array(data['features'])
    prediction = model.predict(X)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
