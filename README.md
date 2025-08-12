# Deep-Transfer-Learning-Techniques-Based-Automated-Classification-and-Detection-of-Pulmonary-Fibrosis

Deep Transfer Learning Techniques-Based Automated Classification and Detection of Pulmonary Fibrosis from Chest CT Images

## 🏥 How the Application Runs

### Application Architecture
This is a **Flask web application** that provides an automated system for detecting pulmonary fibrosis from chest CT scan images using deep learning.

### 🔄 Application Flow
1. **Web Interface**: User accesses the HTML interface (`templates/index.html`)
2. **Image Upload**: User uploads a chest CT scan image through the web form
3. **Image Processing**: Image is base64 encoded and sent to the Flask server
4. **ML Prediction**: Server processes the image using a ResNet50v2 transfer learning model
5. **Result Display**: Binary classification result (Fibrosis/NonFibrosis) returned to user

### 🚀 Running the Application
```bash
# Install dependencies
pip install -r requirements.txt

# ⚠️ IMPORTANT: Place the trained Model.h5 file in the project root directory

# Run the application
python app.py

# Access the web interface
# Local: http://localhost:5000
# Production: https://fibrosisweb.azurewebsites.net/
```

## 🧠 Where the ML Model is Written

### 📍 Primary Location: `predict.py`
The machine learning model logic is implemented in the `predict.py` file:

```python
class PulmonaryFibrosisPredictor:
    def __init__(self, filename):
        self.filename = filename
        self.model_path = 'Model.h5'
    
    def predict_pulmonary_fibrosis(self):
        # Load pre-trained ResNet50v2 model
        model = load_model(self.model_path)
        
        # Preprocess CT image (135x135x3 pixels)
        test_image = image.load_img(self.filename, target_size=(135, 135, 3))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Binary classification: Fibrosis vs NonFibrosis
        result = model.predict(test_image)
        prediction = 'NonFibrosis' if result[0][0] == 1 else 'Fibrosis'
        return [{"image": prediction}]
```

### 🏛️ Model Architecture Details
- **Model Type**: ResNet50v2 (Transfer Learning)
- **Pre-trained on**: ImageNet dataset
- **Fine-tuned for**: Pulmonary fibrosis detection
- **Input Size**: 135×135×3 pixels (RGB CT images)
- **Output**: Binary classification (Fibrosis/NonFibrosis)
- **Model File**: `Model.h5` (Keras HDF5 format)

### 📊 Model Performance
- **Training Accuracy**: 99.92%
- **Validation Accuracy**: 99.22%
- **Training Loss**: 0.00428
- **Validation Loss**: 0.00683
- **Perfect Score (1.0)** in: Accuracy, Precision, Recall, F1-score, MCC, ROC-AUC, AUC-PR

### 🗂️ Complete File Structure
```
📁 Project Root/
├── 🌐 app.py                     # Flask web application
├── 🧠 predict.py                 # ML model prediction logic
├── 🎨 templates/index.html       # Web interface
├── 🔧 com_in_ineuron_ai_utils/   # Image processing utilities
├── 📋 requirements.txt           # Python dependencies
├── 📖 APP_ARCHITECTURE.md        # Detailed documentation
├── 🔍 app_demo.py               # Application analysis script
└── ⚠️ Model.h5                  # Pre-trained model (REQUIRED but missing)
```

## 📚 Research Context

**Abstract**
Pulmonary Fibrosis (PF) is a non-curable chronic lung disease. Therefore, a quick and accurate PF diagnosis is imperative. In the present study, we aim to compare the performance of the six state-of-the-art Deep Transfer Learning techniques to classify patients accurately and perform abnormality localization in Computer Tomography (CT) scan images. A total of 2299 samples comprising normal and PF-positive CT images were preprocessed. The preprocessed images were split into training (75%), validation (15%), and test data (10%). These transfer learning models were trained and validated by optimizing the hyperparameters, such as the learning rate and the number of epochs. The optimized architectures have been evaluated with different performance metrics to demonstrate the consistency of the optimized model. At epoch 26, using an optimized learning rate of 0.0000625, the ResNet50v2 model achieved the highest training and validation accuracy (training = 99.92%, validation = 99.22%) and minimum loss (training = 0.00428, validation = 0.00683) for CT images. The experimental evaluation on the independent testing data confirms that optimized ResNet50v2 outperformed every other optimized architecture under consideration achieving a perfect score of 1.0 in each of the standard performance measures such as accuracy, precision, recall, F1-score, Mathew Correlation Coefficient (MCC), Area under the Receiver Operating Characteristic (ROC-AUC) curve, and the Area under the Precision recall (AUC_PR) curve. Therefore, we can propose that the optimized ResNet50v2 is a reliable diagnostic model for automatically classifying PF-positive patients using chest CT images.

**Keywords**: pulmonary fibrosis; transfer learning techniques; ResNet50v2; chest computed tomography; classification and detection

## 📱 Screenshots
### Home page
![](/images/HomePage.jpg)
### Upload Page
![](/images/UploadFibronosis.jpg)
### Prediction page
![](/Result/4.JPG)

## 📊 Technical Diagrams
### Flow Diagram
![](/images/FlowDigram.jpg)
### Operational Diagram
![](/images/OpratinalFlowDiagram.jpg)
### Augmentation
![](/images/AugRVFinal.jpg)

## ⚙️ Requirements
```
Werkzeug>=2.2.2
Flask-Cors==3.0.10
Flask>=2.2.2
numpy==1.20
Keras==2.9.0
pillow>=9.3.0
h5py==3.7.0
tensorflow>=2.9.1
gunicorn>=19.5.0
```

## 🌐 Live Application
<a href="https://fibrosisweb.azurewebsites.net/">https://fibrosisweb.azurewebsites.net/</a>

## 📄 Additional Documentation
- **[APP_ARCHITECTURE.md](APP_ARCHITECTURE.md)** - Comprehensive technical documentation
- **[app_demo.py](app_demo.py)** - Interactive application analysis script

## 📖 How to cite ?
Syed, A.H.; Khan, T.; Khan, S.A. Deep Transfer Learning Techniques-Based Automated Classification and Detection of Pulmonary Fibrosis from Chest CT Images. Processes 2023, 11, 443. https://doi.org/10.3390/pr11020443
