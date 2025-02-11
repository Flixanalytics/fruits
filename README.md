# **Fruit Classification App 🍎🍌🥑**

## **Overview**

The **Fruit Classification App** is a user-friendly web application that allows users to upload an image of a fruit and classify it into one of the following categories using a pre-trained deep learning model:

### **Available Classes:**
- Apple  
- Banana  
- Avocado  
- Mango  
- Orange  
- Pineapple  
- Watermelon  

The app is built using **Streamlit**, leveraging a TensorFlow/Keras-based deep learning model trained to recognize fruits with high accuracy.

---

## **Features**
- **Upload Image**: Allows users to upload images in `.jpg`, `.jpeg`, or `.png` formats.  
- **Image Preview**: Displays the uploaded image in the app for confirmation.  
- **Fruit Classification**: Uses the model to classify the uploaded image into one of the predefined fruit categories.  
- **Prediction Results**: Displays the predicted fruit class with a clean and simple UI.

---

## **Technologies Used**
1. **Python**  
2. **Streamlit** - For building the web interface.  
3. **TensorFlow/Keras** - For loading and using the pre-trained model.  
4. **Pillow (PIL)** - For image preprocessing and manipulation.  
5. **NumPy** - For numerical operations.  

---

## **How to Run the App**
### **Prerequisites**
- Python 3.7 or later installed on your system.
- Install the required libraries:
  ```bash
  pip install streamlit tensorflow keras pillow numpy
