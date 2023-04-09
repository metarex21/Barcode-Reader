import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

class BarcodeDecoderApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a button to select barcode image file
        self.select_button = tk.Button(self, text="Select barcode image", command=self.select_image)
        self.select_button.pack(side="top")

        # Create a label to display the selected image filename
        self.filename_label = tk.Label(self, text="")
        self.filename_label.pack(side="top")

        # Create a canvas to display the barcode image
        self.image_canvas = tk.Canvas(self, width=400, height=200)
        self.image_canvas.pack(side="top")

        # Create a button to decode the selected barcode image
        self.decode_button = tk.Button(self, text="Decode barcode", command=self.decode_image)
        self.decode_button.pack(side="top")

        # Create a label to display the decoded data
        self.data_label = tk.Label(self, text="", font=("Helvetica", 24), padx=20, pady=10, wraplength=400) #To adjust Output Text Size, color, etc
        self.data_label.pack(side="top")

    def select_image(self):
        # Open a file dialog to select a barcode image file
        file_path = filedialog.askopenfilename()
        self.filename_label.configure(text=file_path)

        # Load the selected image and display it on the canvas
        if file_path:
            img = Image.open(file_path)
            img = img.resize((400, 200), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(img)
            self.image_canvas.create_image(0, 0, anchor="nw", image=self.image)

    def decode_image(self):
        # Get the selected image filename
        file_path = self.filename_label.cget("text")

        # Read the barcode image and decode it using zbar
        img = cv2.imread(file_path)
        decoded = decode(img)

        # Extract the data from the barcode
        data = decoded[0].data.decode("utf-8")

        # Display the decoded data
        self.data_label.configure(text=data)

# Create the application window
root = tk.Tk()

# Set the window title
root.title("Barcode Decoder")

# Set the window size
root.geometry("400x400")

# Create the app instance
app = BarcodeDecoderApp(master=root)

# Start the app
app.mainloop()