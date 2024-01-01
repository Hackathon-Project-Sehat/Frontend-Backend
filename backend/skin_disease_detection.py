import os
import cv2
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model,Model
from keras.layers import Dense,Dropout
from keras.optimizers import Adamax
from keras.applications import EfficientNetB2
from keras import regularizers
import numpy as np


model_path = 'EfficientNetB3-skin disease-83.79.h5'
csv_path = 'class_dict.csv'
model = load_model(model_path)
class_df = pd.read_csv(csv_path)

def preprocess_image(image_path):
    # Load and preprocess the image
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB (if needed)
    img = cv2.resize(img, (300, 300))  # Resize to match model input shape
    img = img / 255.0  # Normalize pixel values (assuming the model was trained with normalized data)
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Function to make predictions
def predict_skin_disease(image_path):
    # Preprocess the input image
    img = preprocess_image(image_path)
    
    # Make a prediction
    predictions = model.predict(img)
    class_indices = class_df['class_index'].tolist()
    predicted_class_index = np.argmax(predictions)
    
    # Map the class index to the class label
    predicted_class_label = class_df[class_df['class_index'] == predicted_class_index]['class'].values[0]
    
    # Get the predicted probability
    predicted_probability = predictions[0, predicted_class_index]
    
    return predicted_class_label, predicted_probability

# Input image path
image_path = '0_left.jpg'  # Update with the path to your input image

# Make predictions
predicted_class, probability = predict_skin_disease(image_path)

# Display the results
print(f'Predicted Class: {predicted_class}')
print(f'Predicted Probability: {probability * 100:.2f}%')
