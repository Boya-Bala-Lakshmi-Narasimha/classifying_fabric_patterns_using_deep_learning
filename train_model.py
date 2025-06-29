from model_building import build_model
from img_preprocessing import train_data, val_data

model = build_model(train_data.num_classes)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(train_data, validation_data=val_data, epochs=10)

# Save the model
model.save("fabric_model.h5")
print("✅ Model trained and saved as fabric_model.h5")