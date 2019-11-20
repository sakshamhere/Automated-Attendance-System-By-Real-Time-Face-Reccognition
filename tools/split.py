import cv2
vidcap = cv2.VideoCapture('rohit2.mp4')
success,image = vidcap.read()
count = 300
success = True
while success:
  success,image = vidcap.read()
  #image = cv2.rotate(image, rotateCode=cv2.ROTATE_90_CLOCKWISE)
  image = cv2.rotate(image, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  print('Read a new frame: ', success)
  count += 1
  
else:
  pass
