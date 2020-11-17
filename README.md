# **Automated Attendance System by Face Recognition**
[Achievement](https://www.linkedin.com/posts/saksham-doshi_innovationchallenge-activity-6592034102013202432-zNVq)

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

_Recognition is done by LBPH recogniser_

_Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number._

_LBPH is one of the easiest face recognition algorithms._
_It can represent local features in the images._
_It is possible to get great results (mainly in a controlled environment)._
_It is robust against monotonic gray scale transformations._
_It is provided by the OpenCV library (Open Source Computer Vision Library)._

## - **Manage record in Excel files by GUI**

_By the help of gui CRUD operations can be performed in excel files_

## - **Notifying students and teachers about attendance statistics via email**

_After recognition code automatically calculates statistics like attendance percentage keeping in all constraints_
_like working days holidays ._

## - **Python libraries used**

- **OpenCV-python**
- **Pandas**
- **Numpy**
- **csv**
- **Pilow**
- **smtplib**
- **calender**
- **holidays**
- **datetime**
- **openpyxl**
- **tkinter**
- **xlrd**
