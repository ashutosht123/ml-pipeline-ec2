import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model
with open("deployed_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X_new = np.array(data["features"]).reshape(-1, 1)
    predictions = model.predict(X_new).tolist()
    return jsonify({"predictions": predictions})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
