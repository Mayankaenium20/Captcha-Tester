from flask import Flask, request, render_template
import cv2
import numpy as np
from keras.models import load_model
import string

app = Flask(__name__)

model = load_model("captcha_model.hdf5")  # Load your pre-trained model

symbols = string.ascii_lowercase + "0123456789"  # All symbols the captcha can contain
num_symbols = len(symbols)

def predict_captcha(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = img / 255.0
    else:
        return "Image not detected"
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    for a in ans:
        l_ind.append(np.argmax(a))

    captcha_text = ''.join(symbols[i] for i in l_ind)
    return captcha_text

@app.route('/', methods=['GET', 'POST'])
def index():
    captcha_text = ""

    if request.method == 'POST':
        if 'captcha_image' in request.files:
            captcha_image = request.files['captcha_image']
            if captcha_image.filename != '':
                captcha_image.save("uploaded_captcha.png")
                captcha_text = predict_captcha("uploaded_captcha.png")

    return render_template('index.html', captcha_text=captcha_text)

if __name__ == '__main__':
    app.run(debug=True)
