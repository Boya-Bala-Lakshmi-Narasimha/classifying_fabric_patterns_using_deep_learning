from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(rescale=1./255)

train_data = datagen.flow_from_directory(
    'dataset',                # make sure it's 'dataset', not 'dataset/train'
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical',
    subset='training'
)

val_data=train_data

print("✅ Classes detected:", train_data.class_indices)