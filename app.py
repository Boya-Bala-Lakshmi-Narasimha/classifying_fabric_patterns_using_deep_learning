# ✅ app.py — Streamlit Web App for Fabric Classification

import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load the model
model = load_model("fabric_model.h5")
class_labels = ['checked', 'dotted', 'floral', 'plain', 'striped'] # Update this based on your classes

st.title("🧵 Fabric Classifier")
st.write("Upload a fabric image to predict its type")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = image.resize((150, 150))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    st.success(f"✅ Predicted Class: {class_labels[predicted_class]} ({confidence:.2f}% confidence)")
