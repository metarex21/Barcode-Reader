# Barcode Reader

This is a simple Python application that allows you to decode barcodes from image files using the `pyzbar` library and display the decoded data in a graphical user interface (GUI) built with the `tkinter` library.

## Prerequisites

Before you can run this application, you need to have the following libraries installed:

- `pyzbar`: A Python wrapper for the ZBar barcode library, which provides functions to decode barcodes from image files.
- `opencv-python`: A Python wrapper for the OpenCV computer vision library, which provides functions to read and manipulate image files.
- `Pillow`: A Python imaging library that provides functions to resize and display images.

You can install these libraries using pip, the package installer for Python. Open a terminal or command prompt and run the following commands:
```
pip install pyzbar
pip install opencv-python
pip install Pillow
```

## How to Use

To use this application, follow these steps:

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the application:
``` 
python barcode_decoder.py
```

4. Click the "Select barcode image" button and choose a barcode image file from your computer.
5. Click the "Decode barcode" button to decode the selected image and display the decoded data in the GUI.


## Acknowledgments

- The [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) library
- The [opencv-python](https://github.com/opencv/opencv-python) library
- The [Pillow]( https://github.com/python-pillow/Pillow) library
