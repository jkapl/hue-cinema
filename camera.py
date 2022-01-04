import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np

cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("B", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("G", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("R", "Trackbars", 0, 255, nothing)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30