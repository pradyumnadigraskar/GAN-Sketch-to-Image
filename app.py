# === FLASK BACKEND: app.py ===
from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename
import cv2

# === CONFIG ===
UPLOAD_FOLDER = 'static/uploads/'
PREDICTED_FOLDER = 'static/predicted/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
SIZE = 256

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PREDICTED_FOLDER'] = PREDICTED_FOLDER

# === Load Trained Model ===
model = tf.keras.models.load_model("best_model.keras", compile=False)

# === Utilities ===
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (SIZE, SIZE))
    img = img.astype('float32') / 255.0
    return np.expand_dims(img, axis=0)

def postprocess_image(prediction):
    pred = prediction[0]
    pred = np.clip(pred, 0, 1)
    pred = (pred * 255).astype(np.uint8)
    return pred

# === Routes ===
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Preprocess and Predict
    sketch = preprocess_image(filepath)
    prediction = model.predict(sketch)
    predicted_img = postprocess_image(prediction)

    predicted_path = os.path.join(PREDICTED_FOLDER, 'predicted_' + filename)
    cv2.imwrite(predicted_path, cv2.cvtColor(predicted_img, cv2.COLOR_RGB2BGR))

    return render_template('result.html', sketch_image=filepath, predicted_image=predicted_path)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PREDICTED_FOLDER, exist_ok=True)
    app.run(debug=True)
