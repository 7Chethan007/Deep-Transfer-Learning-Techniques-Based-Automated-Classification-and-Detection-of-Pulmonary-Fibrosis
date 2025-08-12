#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img


class PulmonaryFibrosisPredictor:  # Renamed from 'dogcat' for clarity
    def __init__(self, filename):
        self.filename = filename
        self.model_path = 'Model.h5'


    def predict_pulmonary_fibrosis(self):  # Renamed from 'predictiondogcat'
        try:
            # Check if model file exists
            if not os.path.exists(self.model_path):
                return [{"error": f"Model file '{self.model_path}' not found. Please ensure the trained model is available."}]
            
            # Load model
            model = load_model(self.model_path)

            # Check if image file exists
            if not os.path.exists(self.filename):
                return [{"error": f"Image file '{self.filename}' not found."}]

            # Load and preprocess image
            test_image = image.load_img(self.filename, target_size=(135, 135, 3))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            
            # Make prediction
            result = model.predict(test_image)
            print(f"Prediction result: {result[0][0]}")

            # Binary classification: 1 = NonFibrosis, 0 = Fibrosis
            if result[0][0] == 1:
                prediction = 'NonFibrosis'
            else:
                prediction = 'Fibrosis'
                
            return [{"image": prediction}]
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return [{"error": f"Prediction failed: {str(e)}"}]


# For backward compatibility, keep the old class name as an alias
dogcat = PulmonaryFibrosisPredictor


