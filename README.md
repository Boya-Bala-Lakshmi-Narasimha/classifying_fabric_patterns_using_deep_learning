Classifying Fabric Patterns Using Deep Learning
This project classifies fabric patterns into five categories using a Convolutional Neural Network (CNN): Checked, Dotted, Floral, Plain, and Striped.
📂 Project Structure

classifying_fabric_patterns_using_deep_learning/
├── dataset/
│   ├── checked/
│   ├── dotted/
│   ├── floral/
│   ├── plain/
│   └── striped/
├── img_preprocessing.py
├── model_building.py
├── train_model.py
├── predict.py
├── app.py
├── gui_demo.py
├── data_collection.py
├── evaluate_model.py
├── fabric_model.h5
├── README.md
└── test_image.jpg


🔧 Requirements

- Python 3.8+
- TensorFlow / Keras
- NumPy
- Matplotlib
- Streamlit (for GUI)
- OpenCV (optional for image handling)


Install all dependencies:
pip install -r requirements.txt
🧠 How It Works

1. Image Preprocessing (img_preprocessing.py): Loads dataset and splits into training and validation using ImageDataGenerator.
2. Model Building (model_building.py): Defines and compiles the CNN architecture.
3. Model Training (train_model.py): Trains the model and saves it as fabric_model.h5.
4. Prediction (predict.py): Predicts a fabric class for a test image.
5. GUI Demo (app.py): Streamlit interface for image classification.


🚀 Run the Project
1. Train the Model
python train_model.py
2. Predict a Test Image
python predict.py
3. Run Streamlit App
streamlit run app.py
🧪 Sample Output

Classes detected: {'checked': 0, 'dotted': 1, 'floral': 2, 'plain': 3, 'striped': 4}
Predicted Class: Floral
Confidence: 94.67%


📈 Accuracy and Evaluation
You can visualize training accuracy/loss and evaluate model performance using:
python evaluate_model.py
📽️ Demo Video
Coming soon... (Include a YouTube or Google Drive link here)
👨‍💻 Author
Boya Bala Lakshmi Narasimha
GitHub: https://github.com/Boya-Bala-Lakshmi-Narasimha
📄 License
This project is licensed under the MIT License - feel free to use, modify, and share it.

