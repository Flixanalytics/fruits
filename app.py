import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.utils import image_dataset_from_directory,img_to_array,array_to_img,load_img






model = load_model("fruits.keras")

## Class labels
class_names = ['Apple', 'Banana', 'Avocado', 'Mango', 'Orange', 'Pineapple', 'Watermelon']

# App title
st.title("Fruit Classification App 🍎🍌🥑")
st.markdown("""
# Fruit Classification Model Documentation

## Overview

The **Fruit Classification Model** is designed to classify images of fruits into one of the following categories: 

**Available Classes**:
- Apple  
- Banana  
- Avocado  
- Mango  
- Orange  
- Pineapple  
- Watermelon  

This model leverages deep learning techniques to identify fruits in images with high accuracy.

---


""")
# File uploader for images

img = st.file_uploader("Upload an image of a fruit", type=["jpg", "jpeg", "png"])
img_width,img_height=180,180
if img:
    img = load_img(img,target_size=(img_width,img_height))
    st.image(img, caption="Uploaded Image",  use_container_width=False)

    img_arr = array_to_img(img)
    img_1 = tf.expand_dims(img_arr,0)

        # Make a prediction
    if st.button("predict"):
        prediction = model.predict(img_1)
        predicted_class = class_names[np.argmax(prediction)]

            # Display prediction result
        st.markdown(
            f"""
            ### Prediction Result 🎯
            The uploaded image is classified as:
            **:green[{predicted_class}]**
            """
                )

                # Display the uploaded image and prediction together
        st.success("Prediction successful!")

