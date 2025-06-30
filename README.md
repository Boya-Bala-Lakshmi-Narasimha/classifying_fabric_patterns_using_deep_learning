# Fabric Pattern Classification using Deep Learning (CNN)

This project uses a **Convolutional Neural Network (CNN)**, a type of **deep learning model**, to classify different types of fabric patterns using image data.

## 📌 Project Description

This deep learning project aims to automatically classify fabric images into categories:

* Cotton
* Wool
* Silk
* Denim
* Nylon

The CNN model learns from training data and predicts the fabric type by analyzing the texture and pattern features of images.

---

## 📁 Dataset Structure

The dataset is structured with separate folders for training and validation:

```
dataset/
├── train/
│   ├── cotton/
│   ├── wool/
│   ├── silk/
│   ├── denim/
│   └── nylon/
└── val/
    ├── cotton/
    ├── wool/
    ├── silk/
    ├── denim/
    └── nylon/
```

Each folder contains `.jpg` images of that specific fabric class.

---

## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install tensorflow numpy matplotlib pillow
```

### 2. Train the Model

```bash
python train_model.py
```

This will train the CNN model and save it as `fabric_model.h5`.

### 3. Make Predictions

You can test the model using:

```bash
python predict.py
```

Make sure `test_image.jpg` exists in the same directory.

### 4. GUI App (Optional)

```bash
python gui_demo.py
```

A Tkinter GUI will open where you can upload an image and see the predicted class.

### 5. Streamlit Web App (Optional)

```bash
streamlit run app.py
```

You can test predictions via a browser interface.

---

## 🧠 Model Architecture

This CNN model includes the following layers:

* Conv2D (32 filters)
* MaxPooling2D
* Conv2D (64 filters)
* MaxPooling2D
* Flatten
* Dense (128)
* Dropout
* Dense (Output: 5 classes, Softmax)

**Loss Function:** Categorical Crossentropy
**Optimizer:** Adam

---

## 📦 Requirements

* Python 3.x
* TensorFlow
* NumPy
* Pillow
* Matplotlib
* (Optional) Streamlit

You can install all at once using:

```bash
pip install -r requirements.txt
```

---

## 🙋‍♀️ Author

Developed by \[Boya Bala Lakshmi Narasimha]

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

Feel free to improve the model, add more fabric types, or deploy it as a web application!