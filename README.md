# 🖌️ GAN Sketch to Image

<p align="center">
  <img src="images/banner.png" alt="Project Banner" width="70%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Welcome-Creative%20AI%20Art-blueviolet?style=for-the-badge"/>
</p>

<h2 align="center">Turn your sketches into stunning, realistic images with AI ✨</h2>

---

## ✨ Features

- 🎨 **Sketch to Photo:** Upload a sketch and generate a realistic photo
- ⚡ **Fast Web Interface:** Interactive, modern UI (Flask)
- 🧠 **Deep Learning:** Powered by TensorFlow and OpenCV
- 🗂️ **Batch Processing:** Utilities for dataset/image handling
- 💎 **Beautiful Results:** See your art come to life!

---

## 🚀 Demo
<p align="center">
  <img src="images/demo.gif" alt="Demo GIF" width="60%"/>
</p>

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gan-sketch-to-image.git
   cd gan-sketch-to-image
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your trained model:**
   - Place your `best_model.keras` file in the project root.

---

## 🖼️ Usage

1. **Start the web app:**
   ```bash
   python app.py
   ```
2. **Open your browser:**
   - Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. **Upload a sketch:**
   - Click 'Choose File', select your sketch, and hit 'Generate Photo'.
4. **View results:**
   - See your input and the generated image side by side!

---

## 🛠️ Project Structure

```
GAN Sketch to Image/
├── app.py                # Flask web app
├── convert.py            # Batch image utilities
├── sketch-to-image.ipynb # Model training & experiments
├── static/               # CSS, uploads, predicted images
├── templates/            # HTML templates
└── requirements.txt      # Dependencies
```

---

## 📸 Gallery
<p align="center">
  <img src="Main Page.png" alt="Main Page" width="45%" style="margin:10px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.2);"/>
  <img src="Project page.png" alt="Project Page" width="45%" style="margin:10px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.2);"/>
</p>

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](LICENSE)

---

<p align="center">
  <b>Made with ❤️ for creative AI art!</b>
</p> 