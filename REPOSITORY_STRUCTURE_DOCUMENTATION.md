# Repository Structure Documentation

## Project Overview

This repository contains a **Deep Transfer Learning-based web application** for automated classification and detection of **Pulmonary Fibrosis** from chest CT images. The project implements a Flask web application that uses a pre-trained ResNet50v2 model to classify medical images as either showing signs of pulmonary fibrosis or being normal.

## 📁 Repository Folder Structure

```
Deep-Transfer-Learning-Techniques-Based-Automated-Classification-and-Detection-of-Pulmonary-Fibrosis/
│
├── 📄 README.md                           # Project documentation and research abstract
├── 🐍 app.py                             # Main Flask application entry point
├── 🔬 predict.py                         # Core prediction logic and model inference
├── 📋 requirements.txt                   # Python dependencies and packages
│
├── 📁 templates/                         # Web interface templates
│   └── 🌐 index.html                   # Main web page with upload interface
│
├── 📁 images/                           # Documentation images and screenshots
│   ├── 🖼️ HomePage.jpg                 # Screenshot of application home page
│   ├── 🖼️ UploadFibronosis.jpg         # Screenshot of upload interface
│   ├── 📊 FlowDigram.jpg               # Process flow diagram
│   ├── ⚙️ OpratinalFlowDiagram.jpg     # Operational workflow diagram
│   ├── 📈 AugRVFinal.jpg               # Data augmentation visualization
│   └── 📋 Result.jpg                   # Results visualization
│
├── 📁 com_in_ineuron_ai_utils/         # Custom utility package
│   ├── 🐍 __init__.py                  # Package initialization
│   └── 🛠️ utils.py                     # Image processing utilities
│
└── 🤖 Model.h5                         # ⚠️ MISSING: Trained deep learning model
```

## 📖 Detailed File Analysis

### 🎯 Core Application Files

#### `app.py` - Main Flask Application
**Purpose**: Entry point for the web application
**Key Features**:
- Flask web server setup with CORS enabled
- Route definitions for home page (`/`) and prediction API (`/predict`)
- ClientApp class that manages the prediction workflow
- Handles HTTP requests and responses

**Key Components**:
```python
- Route "/": Renders the main web interface
- Route "/predict": Processes image uploads and returns predictions
- ClientApp: Manages the prediction workflow
```

#### `predict.py` - Prediction Engine
**Purpose**: Contains the core machine learning inference logic
**Key Features**:
- Loads the pre-trained ResNet50v2 model
- Processes uploaded images (resizes to 135x135x3)
- Performs binary classification (Fibrosis vs NonFibrosis)
- Returns structured prediction results

**Technical Details**:
- **Input**: 135x135x3 RGB images
- **Model**: ResNet50v2 (loaded from Model.h5)
- **Output**: Binary classification with confidence
- **Classes**: "Fibrosis" (diseased) vs "NonFibrosis" (healthy)

### 🌐 Web Interface

#### `templates/index.html` - User Interface
**Purpose**: Complete web interface for image upload and prediction
**Features**:
- **Responsive Design**: Bootstrap-based responsive layout
- **Image Upload**: File upload with preview functionality
- **Real-time Prediction**: AJAX-based prediction without page reload
- **Results Display**: JSON formatted results with visual feedback
- **Loading Animation**: User feedback during processing

**Technical Implementation**:
- **Frontend**: HTML5, CSS3, JavaScript, jQuery
- **Styling**: Bootstrap 4.0 framework
- **Image Processing**: Canvas-based image conversion to base64
- **API Communication**: AJAX POST requests to `/predict` endpoint

### 🛠️ Utility Package

#### `com_in_ineuron_ai_utils/utils.py`
**Purpose**: Image processing and encoding utilities
**Functions**:
- `decodeImage()`: Converts base64 string to image file
- `encodeImageIntoBase64()`: Converts image file to base64 string

### 📊 Documentation Assets

#### `images/` Directory
Contains visual documentation of the project:
- **HomePage.jpg**: Application interface screenshot
- **UploadFibronosis.jpg**: Upload process demonstration
- **FlowDigram.jpg**: High-level process workflow
- **OpratinalFlowDiagram.jpg**: Detailed operational steps
- **AugRVFinal.jpg**: Data augmentation techniques used
- **Result.jpg**: Sample prediction results

## 🧠 Deep Learning Architecture

### Model Details
- **Architecture**: ResNet50v2 (Residual Network 50 v2)
- **Task**: Binary Classification
- **Input Size**: 135 × 135 × 3 (RGB images)
- **Training Data**: 2,299 CT scan samples
- **Data Split**: 75% training, 15% validation, 10% testing
- **Performance**: 99.92% training accuracy, 99.22% validation accuracy

### Training Specifications
- **Optimizer**: Adam with learning rate 0.0000625
- **Epochs**: 26 epochs for optimal performance
- **Loss Function**: Binary crossentropy
- **Metrics**: Accuracy, Precision, Recall, F1-score, MCC, ROC-AUC, AUC-PR

## 🔄 Application Workflow

### 1. User Interaction Flow
```
User uploads CT image → Frontend converts to base64 → 
AJAX POST to /predict → Image decoded → Model inference → 
Classification result → JSON response → UI update
```

### 2. Technical Processing Pipeline
```
Input Image (any format) → 
Resize to 135×135×3 → 
Normalize pixel values → 
Model prediction → 
Threshold at 0.5 → 
Classification result
```

## 🚀 Setup and Deployment

### Dependencies (requirements.txt)
```
Flask>=2.2.2          # Web framework
Flask-Cors==3.0.10    # Cross-origin resource sharing
tensorflow>=2.9.1     # Deep learning framework
Keras==2.9.0          # High-level neural networks API
numpy==1.20           # Numerical computing
pillow>=9.3.0         # Image processing
h5py==3.7.0           # HDF5 file format support
Werkzeug>=2.2.2       # WSGI utility library
gunicorn>=19.5.0      # Production WSGI server
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```

### Production Deployment
- **Platform**: Azure Web Services
- **URL**: https://fibrosisweb.azurewebsites.net/
- **Server**: Gunicorn WSGI server

## ⚠️ Missing Components

### Critical Missing File
- **Model.h5**: The trained deep learning model file is not present in the repository
  - This file should contain the trained ResNet50v2 weights
  - Without this file, the application cannot make predictions
  - File size is likely large (>100MB) and may need Git LFS or external storage

### Recommended Additions
1. **Model file**: Add Model.h5 or provide download instructions
2. **Training code**: Include scripts used to train the model
3. **Test data**: Sample CT images for testing
4. **API documentation**: Detailed API endpoint documentation
5. **Docker support**: Containerization for easier deployment

## 📚 Research Context

This implementation is based on the research paper:
**"Deep Transfer Learning Techniques-Based Automated Classification and Detection of Pulmonary Fibrosis from Chest CT Images"**
- Published in: Processes 2023, 11, 443
- DOI: https://doi.org/10.3390/pr11020443
- Authors: Syed, A.H.; Khan, T.; Khan, S.A.

## 🎯 Use Cases

### Medical Applications
- **Automated Screening**: Rapid screening of chest CT scans
- **Diagnostic Support**: Assist radiologists in identifying pulmonary fibrosis
- **Telemedicine**: Remote diagnosis capabilities

### Technical Applications
- **Research Tool**: Platform for testing different deep learning models
- **Educational**: Demonstrate medical AI applications
- **Prototype**: Foundation for larger medical imaging systems

## 🔧 Technical Specifications

### System Requirements
- **Python**: 3.7+
- **Memory**: Minimum 4GB RAM (8GB+ recommended)
- **Storage**: 2GB+ for dependencies and model
- **GPU**: Optional but recommended for faster inference

### Browser Compatibility
- **Modern browsers**: Chrome, Firefox, Safari, Edge
- **JavaScript**: Required for image upload and AJAX functionality
- **HTML5**: Required for file upload and canvas operations

## 📈 Performance Metrics

Based on the research paper, the optimized ResNet50v2 model achieved:
- **Accuracy**: 100% (1.0)
- **Precision**: 100% (1.0)
- **Recall**: 100% (1.0)
- **F1-Score**: 100% (1.0)
- **MCC**: 100% (1.0)
- **ROC-AUC**: 100% (1.0)
- **AUC-PR**: 100% (1.0)

## 🛡️ Security Considerations

### Data Privacy
- Medical images should be handled according to HIPAA/GDPR guidelines
- Consider implementing encryption for uploaded images
- Ensure secure deletion of temporary files

### Application Security
- Implement input validation for uploaded files
- Add file type and size restrictions
- Consider rate limiting for API endpoints
- Use HTTPS in production

## 🔮 Future Enhancements

### Technical Improvements
1. **Model versioning**: Support for multiple model versions
2. **Batch processing**: Handle multiple images simultaneously
3. **Model explanability**: Add heat maps showing decision regions
4. **Performance monitoring**: Real-time model performance tracking

### User Experience
1. **Mobile optimization**: Better mobile device support
2. **Progress indicators**: Detailed upload and processing progress
3. **History**: Save and review previous predictions
4. **Export functionality**: Download results in various formats

This documentation provides a comprehensive overview of the repository structure, functionality, and technical implementation of the Pulmonary Fibrosis detection application.