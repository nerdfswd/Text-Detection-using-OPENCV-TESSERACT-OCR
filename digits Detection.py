import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
###########################################################

                # Digits detection

############################################################
img = cv2.imread('Resources/o.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hImg, wImg, _ = img.shape
conf = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, config=conf)
for b in boxes.splitlines():
    print(b)
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
    cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('For Digits detection', img)
cv2.waitKey(0)
