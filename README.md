# Captcha-Tester

## Overview
This is a Streamlit web application that allows users to upload a CAPTCHA image for analysis, determine its strength (weak or strong), and generate a complex CAPTCHA code. The project uses a deep learning model to recognize CAPTCHA text and the secrets library to generate strong CAPTCHA codes.

## Screenshot:

![image](https://github.com/Mayankaenium20/Captcha-Tester/assets/89603698/6584d94f-1a8d-41eb-8cda-ef5bd0e4e3d9)


## Features
1. Upload a CAPTCHA image for analysis.
2. Check the strength of the recognized CAPTCHA text.
3. Suggest a complex CAPTCHA code.
4. Display the recognized text and strength in real-time.
5. Generate and display a complex CAPTCHA code.

## Prerequisites
###### Before running the application, ensure you have the following dependencies installed:

1. Python 3.x
2. Required Python libraries (install using pip):
    + Streamlit
    + OpenCV (cv2)
    + Numpy
    + Keras (for the CAPTCHA recognition model)
    + Secrets
    + Flask(optional)

## Usage
1. Upload a CAPTCHA image using the "Upload a captcha image..." button.

2. The application will recognize the text in the CAPTCHA image and determine its strength (weak or strong).

3. You can click "Reveal Text" to display the recognized text and its strength in real-time.

4. To suggest a complex CAPTCHA code, click "Suggest a complex CAPTCHA code?".

5. The suggested complex CAPTCHA code will be displayed in green, preceded by "Suggested captcha is:" in white.

## Future Scope: 
1. Integration of GAN for Real-Time CAPTCHA Suggestions: Explore the integration of Generative Adversarial Networks (GANs) to generate CAPTCHA suggestions in real-time. GANs can enhance the diversity and complexity of generated CAPTCHAs, improving security and providing more challenging tests.

2. Training on Multiple Datasets: Extend the model's capabilities by training it on a diverse range of datasets, particularly focusing on CAPTCHAs with more than 5 characters. This enhancement can further improve recognition accuracy and broaden the application's usability.

## License
This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt). You are free to use, modify, and distribute the code as per the terms of this license.
