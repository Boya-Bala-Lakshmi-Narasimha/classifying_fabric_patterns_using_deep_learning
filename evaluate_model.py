from tensorflow.keras.models import load_model
from img_preprocessing import val_data

model = load_model("fabric_model.h5")

loss, accuracy = model.evaluate(val_data)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")