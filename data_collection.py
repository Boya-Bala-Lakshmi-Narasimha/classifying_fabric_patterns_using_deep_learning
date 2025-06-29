import os

dataset_path = 'dataset/'

if os.path.exists(dataset_path):
    print("✅ Dataset folder found.")
else:
    print("❌ Dataset folder not found. Please add your dataset.")