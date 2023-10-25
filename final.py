import streamlit as st
import cv2
import numpy as np
from keras.models import load_model
from string import ascii_lowercase, ascii_letters, digits, punctuation
import tempfile
import os
import secrets

symbols = ascii_lowercase + "0123456789"
model = load_model("captcha_model.hdf5")


def predict(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = img / 255.0
    else:
        print("Not detected")
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))

    capt = ""
    for l in l_ind:
        capt += symbols[l]
    return capt

def generate_complex_captcha():
    characters = ascii_letters + digits + punctuation
    captcha_length = 8  # Adjust the length as needed
    return ''.join(secrets.choice(characters) for _ in range(captcha_length))

st.title("Captcha Tester App")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a captcha image...", type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    # temporary directory to store the uploaded image
    temp_directory = tempfile.TemporaryDirectory()
    image_path = os.path.join(temp_directory.name, uploaded_file.name)

    # uploaded image to the temporary directory
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    # uploaded image
    st.image(
        uploaded_file, caption="Uploaded Image", use_column_width=True
    )  # uploaded_file here

    # Process and recognize the captcha
    captcha_text = predict(
        image_path
    )  

    if len(captcha_text) >= 8:  # You can adjust the length threshold as needed
        strength_feedback = "Strong"
        strength_color = "green"
    else:
        strength_feedback = "Weak"
        strength_color = "red"

    st.sidebar.image(
        uploaded_file, caption="Uploaded Image", use_column_width=True
    )

    st.sidebar.markdown(f"**Recognized Text:** {captcha_text}")
    st.sidebar.markdown(f"**Strength:** <font color='{strength_color}'>{strength_feedback}</font>", unsafe_allow_html=True)

    if st.button("Suggest a complex CAPTCHA code"):
        suggested_captcha = generate_complex_captcha()
        st.markdown("<font color='white'>Suggested captcha is: </font>" +
            "<font color='green'>" + suggested_captcha + "</font>", unsafe_allow_html=True)
