🖼️ Image Resizer Tool  

A simple yet powerful *Image Resizer Tool* built with Python. 🚀  
This tool allows you to resize images to any custom dimensions or scale them while maintaining aspect ratio. Perfect for developers, designers, and photographers!  

---

## ✨ Features  
- 📂 Resize single or multiple images at once  
- 🔄 Maintain aspect ratio  
- 📝 Supports JPG, PNG, and more  
- ⚡ Lightweight and fast  
- 💻 Easy to use CLI  

---

## 📸 Demo  
```bash
# Resize image to specific width & height
python resizer.py --input input.jpg --output output.jpg --width 800 --height 600

# Resize by percentage
python resizer.py --input input.jpg --output output.jpg --scale 0.5

# Resize all images in a folder
python resizer.py --input_folder images/ --output_folder resized/ --width 1024

🛠️ Installation

1. Clone this repository

git clone https://github.com/your-username/image-resizer.git
cd image-resizer


2. Install dependencies

pip install -r requirements.txt


📦 Requirements

Python 3.7+

Pillow library


Install Pillow:

pip install pillow


📂 Project Structure

📦 image-resizer
 ┣ 📂 images
 ┣ 📂 resized
 ┣ 📜 resizer.py
 ┣ 📜 requirements.txt
 ┣ 📜 README.md


🧑‍💻 How It Works

1. Load the input image(s)


2. Apply resizing logic (width, height, or scale)


3. Save the resized image(s) in the output folder


🚀 Future Enhancements

🖼️ Add GUI with Tkinter / PyQt

🌐 Build a Flask/Django Web App

📱 Create a mobile-friendly version


🤝 Contributing

Contributions are always welcome!
Feel free to fork this repo, submit issues, and create pull requests.


📜 License

This project is licensed under the MIT License.
