# gui_demo.py
import tkinter as tk
from tkinter import filedialog
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image, ImageTk

# Load the trained model
model = load_model("fabric_model.h5")

# Class names (update if more classes are used)
class_labels = ['checked', 'dotted', 'floral', 'plain', 'striped']

def predict_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Load and preprocess the image
    img = image.load_img(file_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]

    # Show result
    result_label.config(text=f"Predicted Class: {class_labels[predicted_class]}")

    # Show image
    img_display = Image.open(file_path)
    img_display = img_display.resize((150, 150))
    img_display = ImageTk.PhotoImage(img_display)
    panel.config(image=img_display)
    panel.image = img_display

# Create GUI window
root = tk.Tk()
root.title("🧵 Fabric Pattern Classifier")

# UI elements
panel = tk.Label(root)
panel.pack()

btn = tk.Button(root, text="Select Image", command=predict_image)
btn.pack()

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack()

# Start the GUI loop
root.mainloop()
