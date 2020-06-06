import cv2
import pytesseract
#import numpy as np
#from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('Resources/Test image.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))

cv2.imshow('Result image', img)
cv2.waitKey(0)