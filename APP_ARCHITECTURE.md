# Application Architecture and ML Model Documentation

## How the App is Running

### 1. **Application Framework**
- **Technology**: Flask web application (Python)
- **Frontend**: HTML/CSS/JavaScript with Bootstrap styling
- **Dependencies**: Listed in `requirements.txt`

### 2. **Application Flow**

```
User Interface (index.html) 
    ↓
Upload CT Scan Image
    ↓
Base64 Encoding (Frontend JavaScript)
    ↓
POST /predict endpoint (app.py)
    ↓
Image Decoding (utils.py)
    ↓
ML Model Prediction (predict.py)
    ↓
JSON Response (Fibrosis/NonFibrosis)
    ↓
Display Results (Frontend)
```

### 3. **Key Components**

#### **app.py** - Main Application File
- **Route `/`**: Serves the main HTML interface
- **Route `/predict`**: Handles image prediction requests
- **ClientApp Class**: Initializes the prediction system
- **CORS enabled**: For cross-origin requests

#### **templates/index.html** - Web Interface
- File upload functionality
- Image preview with webcam fallback
- AJAX calls to prediction endpoint
- Real-time results display

#### **com_in_ineuron_ai_utils/utils.py** - Utility Functions
- `decodeImage()`: Converts base64 to image file
- `encodeImageIntoBase64()`: Converts image to base64

### 4. **Deployment Options**
- **Local Development**: `python app.py` (debug mode)
- **Production**: Using gunicorn WSGI server
- **Cloud**: Currently deployed on Azure (https://fibrosisweb.azurewebsites.net/)

## Where the ML Model is Written

### 1. **Model Implementation Location**

#### **predict.py** - Core ML Logic
```python
class dogcat:  # Note: Misleading name for medical classification
    def __init__(self, filename):
        self.filename = filename
    
    def predictiondogcat(self):
        # Loads pre-trained model
        model = load_model('Model.h5')
        
        # Image preprocessing
        test_image = image.load_img(filename, target_size=(135, 135, 3))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Prediction
        result = model.predict(test_image)
        
        # Binary classification
        if result[0][0] == 1:
            return [{"image": "NonFibrosis"}]
        else:
            return [{"image": "Fibrosis"}]
```

### 2. **Model Architecture Details**

#### **Model Type**: Transfer Learning with ResNet50v2
- **Base Architecture**: ResNet50v2 (pre-trained on ImageNet)
- **Fine-tuning**: Optimized for pulmonary fibrosis detection
- **Training Data**: 2299 CT scan samples (75% train, 15% validation, 10% test)

#### **Model Performance** (from README):
- **Training Accuracy**: 99.92%
- **Validation Accuracy**: 99.22%
- **Metrics**: Perfect score (1.0) in accuracy, precision, recall, F1-score, MCC, ROC-AUC, AUC-PR

#### **Input Specifications**:
- **Image Size**: 135×135×3 pixels
- **Format**: RGB images
- **Data Type**: CT scan images of chest

#### **Output**:
- **Binary Classification**: "Fibrosis" vs "NonFibrosis"
- **Format**: JSON response with prediction

### 3. **Model File Structure**

```
Repository Root/
├── Model.h5              # ⚠️ MISSING - Pre-trained model file
├── predict.py            # ML prediction logic
├── app.py               # Flask application
├── requirements.txt     # TensorFlow/Keras dependencies
└── ...
```

## Critical Issues Identified

### 1. **Missing Model File**
- The `Model.h5` file is referenced but not present in the repository
- This file contains the trained ResNet50v2 weights
- **Impact**: Application will crash when trying to make predictions

### 2. **Misleading Code Names**
- Class named `dogcat` for medical image classification
- Method named `predictiondogcat()` for pulmonary fibrosis detection

### 3. **Hard-coded Dependencies**
- Model path hard-coded as 'Model.h5'
- No error handling for missing model file

## Technical Stack

### **Backend Dependencies**:
- `tensorflow>=2.9.1` - Deep learning framework
- `Flask>=2.2.2` - Web framework
- `numpy==1.20` - Numerical computing
- `Keras==2.9.0` - High-level neural networks API
- `pillow>=9.3.0` - Image processing
- `h5py==3.7.0` - HDF5 file format support

### **Frontend**:
- Bootstrap 4.0.0 for styling
- jQuery for AJAX requests
- HTML5 Canvas for image processing

## Running the Application

### **Prerequisites**:
1. Install Python dependencies: `pip install -r requirements.txt`
2. **Required**: Place trained `Model.h5` file in root directory
3. Run: `python app.py`

### **Usage**:
1. Navigate to `http://localhost:5000`
2. Upload a chest CT scan image
3. Click "Predict" to get classification result
4. View result as "Fibrosis" or "NonFibrosis"

## Research Context

This application implements the research from:
> Syed, A.H.; Khan, T.; Khan, S.A. Deep Transfer Learning Techniques-Based Automated Classification and Detection of Pulmonary Fibrosis from Chest CT Images. Processes 2023, 11, 443.

The research compares six state-of-the-art Deep Transfer Learning techniques, with ResNet50v2 achieving the best performance for pulmonary fibrosis detection in CT images.