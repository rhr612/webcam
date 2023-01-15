import cv2             #opencv-Python library

camera=cv2.VideoCapture(0)   #kon camrea capture korbo???

while True:
    _, video=camera.read()   #camera theke read kore content nissi
    video=cv2.flip(video,1)  #video flip korsi
    cv2.imshow('Tech Gyro',video) #camera content print kortesi
    cv2.waitKey(1)
