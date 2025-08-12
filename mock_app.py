#!/usr/bin/env python3
"""
Mock version of the Flask app for testing without TensorFlow dependencies
This demonstrates how the application structure works
"""

from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin

# Mock prediction class for testing
class MockPulmonaryFibrosisPredictor:
    def __init__(self, filename):
        self.filename = filename
        self.model_path = 'Model.h5'
    
    def predict_pulmonary_fibrosis(self):
        """Mock prediction method that simulates the real prediction logic"""
        if not os.path.exists(self.model_path):
            return [{"error": f"Model file '{self.model_path}' not found. Please ensure the trained model is available."}]
        
        if not os.path.exists(self.filename):
            return [{"error": f"Image file '{self.filename}' not found."}]
        
        # Simulate prediction (in real app, this would use TensorFlow/Keras)
        import random
        mock_prediction = random.choice(['Fibrosis', 'NonFibrosis'])
        return [{"image": f"MOCK_{mock_prediction}"}]

# Mock utility function
def decodeImage(imgstring, fileName):
    """Mock function that would normally decode base64 image"""
    print(f"Mock: Would decode image to {fileName}")

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = MockPulmonaryFibrosisPredictor(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict_pulmonary_fibrosis()
        return jsonify(result)
    except Exception as e:
        error_response = [{"error": f"Request processing failed: {str(e)}"}]
        return jsonify(error_response), 500

clApp = ClientApp()

if __name__ == "__main__":
    print("🚀 Starting Mock Pulmonary Fibrosis Detection Application")
    print("📍 Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"   {rule.methods} {rule.rule}")
    print("\n🔗 Access the application at: http://localhost:5000")
    print("⚠️  This is a MOCK version - install TensorFlow for full functionality")
    app.run(debug=True, port=5000)