import numpy as np
from tensorflow import keras
from keras.preprocessing import image
from keras.models import load_model

loaded_model = load_model("my_model.h5")  

def preprocess_image(image_path, target_size):
    img = image.load_img(image_path, target_size=target_size)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  
    return img


def predict_cataract(model, image_path, target_size):
    img = preprocess_image(image_path, target_size)
    prediction = model.predict(img)
    return prediction[0]  


image_path_to_predict = "0_left.jpg"  
target_size = (224, 224)

prediction = predict_cataract(loaded_model, image_path_to_predict, target_size)

threshold = 0.65  
result = "Cataract" if prediction >= threshold else "Normal"

print(f"The image is classified as: {result}")