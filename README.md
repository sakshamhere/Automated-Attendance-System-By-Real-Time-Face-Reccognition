# **Automated Attendance System by Face Recognition**

Hi there! , this is a college project made by me , as heading says the aim is to detect ,recognize and mark attendance by face recognition but the project has a lot more objctives:

1. **Detection**
2. **Recognition**
3. **Updating record in Excel**
4. **Managing students data and faculty data through excel by the help of GUI**
5. **Notifying students and teachers about attendance statistics via email**

## - **Detection**

_Detection is done by the help of OpenCV and Haar cascades_

_Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. Today we will be using the face classifier. You can experiment with other classifiers as well._

## - **Recognition**

\_Recognition is done by LBPH recogniser

Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.

LBPH is one of the easiest face recognition algorithms.
It can represent local features in the images.
It is possible to get great results (mainly in a controlled environment).
It is robust against monotonic gray scale transformations.
It is provided by the OpenCV library (Open Source Computer Vision Library).\_

## - **Updating record in Excel**

## - **Managing students data and faculty data through excel by the help of GUI**

## - **Notifying students and teachers about attendance statistics via email**

dataset folder contains orignal images

by to_grayscale.py
image is being cropped
histogram normalisation is done (equ = cv2.equalizeHist(gray))
noise removal is done ( final = cv2.medianBlur(equ, 3))

    and images are saved to gray_images

    further these images are being trained and .yml is obtained


    rest all files like data.csv data.xls , update.py, are for attendance marking and all

    ignore other folders like cropped_images

    folder tkinter-gui is for all gui work
