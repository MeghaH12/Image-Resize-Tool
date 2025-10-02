import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageResizerApp:
    def _init_(self, root):
        self.root = root
        self.root.title("📸 Image Resizer Tool")
        self.root.geometry("700x500")
        self.root.configure(bg="#f3f4f6")

        self.image = None
        self.tk_img = None

        # Title
        tk.Label(root, text="✨ Image Resizer Tool ✨", font=("Arial", 18, "bold"), bg="#f3f4f6", fg="#333").pack(pady=10)

        # Buttons
        self.btn_frame = tk.Frame(root, bg="#f3f4f6")
        self.btn_frame.pack(pady=5)

        tk.Button(self.btn_frame, text="📂 Open Image", command=self.open_image, bg="#4f46e5", fg="white", font=("Arial", 12), width=15).grid(row=0, column=0, padx=10)
        tk.Button(self.btn_frame, text="💾 Save Image", command=self.save_image, bg="#059669", fg="white", font=("Arial", 12), width=15).grid(row=0, column=1, padx=10)

        # Image display
        self.img_label = tk.Label(root, bg="#f3f4f6")
        self.img_label.pack(pady=10)

        # Resize inputs
        input_frame = tk.Frame(root, bg="#f3f4f6")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Width:", font=("Arial", 12), bg="#f3f4f6").grid(row=0, column=0, padx=5)
        self.width_entry = tk.Entry(input_frame, font=("Arial", 12), width=8)
        self.width_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Height:", font=("Arial", 12), bg="#f3f4f6").grid(row=0, column=2, padx=5)
        self.height_entry = tk.Entry(input_frame, font=("Arial", 12), width=8)
        self.height_entry.grid(row=0, column=3, padx=5)

        tk.Button(input_frame, text="⚡ Resize", command=self.resize_image, bg="#f59e0b", fg="white", font=("Arial", 12), width=12).grid(row=0, column=4, padx=10)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.show_image(self.image)

    def show_image(self, img):
        img_resized = img.copy()
        img_resized.thumbnail((400, 300))  # preview size
        self.tk_img = ImageTk.PhotoImage(img_resized)
        self.img_label.config(image=self.tk_img)

    def resize_image(self):
        if self.image:
            try:
                width = int(self.width_entry.get())
                height = int(self.height_entry.get())
                resized = self.image.resize((width, height))
                self.image = resized
                self.show_image(self.image)
                messagebox.showinfo("Success", f"Image resized to {width}x{height}")
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for width and height.")
        else:
            messagebox.showwarning("No Image", "Please open an image first!")

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                     filetypes=[("JPEG", ".jpg"), ("PNG", ".png"), ("BMP", "*.bmp")])
            if file_path:
                self.image.save(file_path)
                messagebox.showinfo("Saved", f"Image saved at:\n{file_path}")
        else:
            messagebox.showwarning("No Image", "No image to save!")

if _name_ == "_main_":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()