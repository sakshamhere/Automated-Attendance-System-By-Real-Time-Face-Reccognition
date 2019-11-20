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
