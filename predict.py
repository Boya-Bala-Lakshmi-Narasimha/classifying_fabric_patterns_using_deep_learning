import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

print("Step 1: Starting prediction...")

# Check if model exists
if not os.path.exists("fabric_model.h5"):
    print("❌ Error: fabric_model.h5 not found.")
    exit()

print("Step 2: Loading model...")
model = tf.keras.models.load_model("fabric_model.h5")
print("✅ Model loaded.")

# Image file
img_path = "test_image.jpg"

# Check if image exists
if not os.path.exists(img_path):
    print(f"❌ Error: test image '{img_path}' not found.")
    exit()

print("Step 3: Loading image...")
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

print("Step 4: Making prediction...")
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction, axis=1)

# Replace class labels with your actual folder names
class_labels = ["cotton", "wool"]  # Example - adjust this
print(f"✅ Step 5: Predicted class is: {predicted_class[0]} → {class_labels[predicted_class[0]]}")