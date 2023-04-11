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

### 1. Clone or download the repository to your local machine.

  ![image](https://user-images.githubusercontent.com/72374116/231289126-8b234ec5-4b66-4e48-b0e2-8a9c7ce6c407.png)

### 2. Open the project folder, navigate to the main folder, right click and press Open in Terminal.

  ![image](https://user-images.githubusercontent.com/72374116/231289558-fab9d8f8-3d99-464b-b8fb-353e4f18c99c.png)

### 3. Run the following command to start the application:
``` 
python barcode_reader.py
```
![image](https://user-images.githubusercontent.com/72374116/231289979-a8b24f4c-a110-489c-aa17-236226d515e8.png)


### 4. A dialog box will pop<br>

  ![image](https://user-images.githubusercontent.com/72374116/231287989-a4789988-f02e-4fe8-8506-26b7a2ee13d3.png)

### 5. Click the "Select barcode image" button and choose a barcode image file from your computer.<br>

  ![image](https://user-images.githubusercontent.com/72374116/231288395-ab2a8520-caeb-4329-99ff-8ccdae76ae40.png)


### 6. Click the "Decode barcode" button to decode the selected image and display the decoded data in the GUI.

  ![image](https://user-images.githubusercontent.com/72374116/231288200-1bb68940-6961-4b5d-913d-c83bdaa1b119.png)




## Acknowledgments

- The [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) library
- The [opencv-python](https://github.com/opencv/opencv-python) library
- The [Pillow]( https://github.com/python-pillow/Pillow) library

