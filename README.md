# Deep Transfer Learning Techniques-Based Automated Classification and Detection of Pulmonary Fibrosis

## 🎯 Project Overview
A Flask web application that uses deep transfer learning (ResNet50v2) to automatically classify and detect Pulmonary Fibrosis from chest CT images. This research-based implementation achieves 100% accuracy across all performance metrics.

## 📁 Repository Structure
For a detailed explanation of the repository structure and all components, see our comprehensive documentation:

- **🔍 [QUICK_OVERVIEW.md](./QUICK_OVERVIEW.md)** - High-level summary and key information
- **📚 [REPOSITORY_STRUCTURE_DOCUMENTATION.md](./REPOSITORY_STRUCTURE_DOCUMENTATION.md)** - Complete technical documentation
- **🏗️ [visualize_structure.py](./visualize_structure.py)** - Interactive structure visualization tool

### Quick Overview:
```
├── app.py                      # Main Flask application
├── predict.py                  # ML prediction engine
├── requirements.txt            # Dependencies
├── templates/index.html        # Web interface
├── com_in_ineuron_ai_utils/    # Utility functions
└── images/                     # Documentation assets
```

## Abstract
Pulmonary Fibrosis (PF) is a non-curable chronic lung disease. Therefore, a quick and accurate PF diagnosis is imperative. In the present study, we aim to compare the performance of the six state-of-the-art Deep Transfer Learning techniques to classify patients accurately and perform abnormality localization in Computer Tomography (CT) scan images. A total of 2299 samples comprising normal and PF-positive CT images were preprocessed. The preprocessed images were split into training (75%), validation (15%), and test data (10%). These transfer learning models were trained and validated by optimizing the hyperparameters, such as the learning rate and the number of epochs. The optimized architectures have been evaluated with different performance metrics to demonstrate the consistency of the optimized model. At epoch 26, using an optimized learning rate of 0.0000625, the ResNet50v2 model achieved the highest training and validation accuracy (training = 99.92%, validation = 99.22%) and minimum loss (training = 0.00428, validation = 0.00683) for CT images. The experimental evaluation on the independent testing data confirms that optimized ResNet50v2 outperformed every other optimized architecture under consideration achieving a perfect score of 1.0 in each of the standard performance measures such as accuracy, precision, recall, F1-score, Mathew Correlation Coefficient (MCC), Area under the Receiver Operating Characteristic (ROC-AUC) curve, and the Area under the Precision recall (AUC_PR) curve. Therefore, we can propose that the optimized ResNet50v2 is a reliable diagnostic model for automatically classifying PF-positive patients using chest CT images.
Keywords: pulmonary fibrosis; transfer learning techniques; ResNet50v2; chest computed tomography; classification and detection
### Screenshot
###### Home page
![](/images/HomePage.jpg)
######Upload Page
![](/images/UploadFibronosis.jpg)
###### Prediction page
![](/Result/4.JPG)
# Flow Diagram
![](/images/FlowDigram.jpg)
# Operational Diagram
![](/images/OpratinalFlowDiagram.jpg)
# Augmentation
![](/images/AugRVFinal.jpg)
## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/7Chethan007/Deep-Transfer-Learning-Techniques-Based-Automated-Classification-and-Detection-of-Pulmonary-Fibrosis.git

# Navigate to project directory
cd Deep-Transfer-Learning-Techniques-Based-Automated-Classification-and-Detection-of-Pulmonary-Fibrosis

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### ⚠️ Important Note
The trained model file (`Model.h5`) is not included in this repository due to size constraints. You'll need to:
1. Train your own model using the methodology described in the research paper
2. Or obtain the pre-trained model file separately
3. Place the `Model.h5` file in the root directory

## 🖥️ Usage
1. Navigate to `http://localhost:5000` in your browser
2. Upload a chest CT image using the "Upload" button
3. Click "Predict" to get the classification result
4. View results showing either "Fibrosis" or "NonFibrosis"

## Requirements
## 📦 Dependencies
```
Werkzeug>=2.2.2         # WSGI utility library
Flask-Cors==3.0.10      # Cross-Origin Resource Sharing
Flask>=2.2.2            # Web framework
numpy==1.20             # Numerical computing
Keras==2.9.0            # Deep learning API
pillow>=9.3.0           # Image processing
h5py==3.7.0             # HDF5 file support
tensorflow>=2.9.1       # Machine learning framework
gunicorn>=19.5.0        # Production WSGI server
```

## 🎯 Model Performance
The optimized ResNet50v2 model achieved perfect scores:
- **Training Accuracy**: 99.92%
- **Validation Accuracy**: 99.22%
- **Test Accuracy**: 100%
- **All Metrics**: 1.0 (Precision, Recall, F1-Score, MCC, ROC-AUC, AUC-PR)

## 🏥 Medical Application
This application provides automated screening for Pulmonary Fibrosis, a chronic lung disease that requires early detection for better patient outcomes. The system can assist healthcare professionals in:
- Rapid screening of chest CT scans
- Diagnostic support for radiologists
- Telemedicine applications

## 🌐 Live Demo
<a href="https://fibrosisweb.azurewebsites.net/">https://fibrosisweb.azurewebsites.net/</a>

## 📚 Research Citation
Syed, A.H.; Khan, T.; Khan, S.A. Deep Transfer Learning Techniques-Based Automated Classification and Detection of Pulmonary Fibrosis from Chest CT Images. Processes 2023, 11, 443. https://doi.org/10.3390/pr11020443
