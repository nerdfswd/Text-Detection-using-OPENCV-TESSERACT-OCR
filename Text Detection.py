import cv2
import pytesseract
#import numpy as np
#from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

#####################################################################
 #Here we just  turning the image into RGB
  #As in OPencv the images pixels are in order BGR
  #As we are using pytesseract we need to convert the image into RGB
  #thats why COLOR_BGR2RGB
  
  #The output will be just a image is shown.
  ####################################################################
  

img = cv2.imread('Resources/Test image.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))

cv2.imshow('Result image', img)
cv2.waitKey(0)
