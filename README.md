# **Automated Attendance System by Face Recognition**

Hi there , this is a college project made by me , as heading says the aim is to detect ,recognize and mark attendance by face recognition but the project has a lot more objctives:

1. **Detection**
2. **Recognition**
3. **Updating record in Excel**
4. **Managing students data and faculty data through excel by the help of GUI**
5. **Notifying students and teachers about attendance statistics via email**

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
