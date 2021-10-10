import cv2
from PIL import Image
import pytesseract as tess
from prepare import clean2_plate, ratioCheck, ratio_and_rotation, isMaxWhite

img = cv2.imread("samples/5.png")

print("Number input image...",)

cv2.imshow('input', img)
if cv2.waitKey(0) & 0xff == ord('q'):
    pass

img2 = cv2.GaussianBlur(img, (3, 3), 0)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('input', img2)
if cv2.waitKey(0) & 0xff == ord('q'):
    pass

img2 = cv2.Sobel(img2, cv2.CV_8U, 1, 0, ksize=3)
_, img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('input', img2)
if cv2.waitKey(0) & 0xff == ord('q'):
    pass

element = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(10, 2))
morph_img_threshold = img2.copy()
cv2.morphologyEx(src=img2, op=cv2.MORPH_CLOSE,
                 kernel=element, dst=morph_img_threshold)
num_contours, hierarchy = cv2.findContours(
    morph_img_threshold, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img2, num_contours, -1, (0, 255, 0), 1)


for i, cnt in enumerate(num_contours):
    min_rect = cv2.minAreaRect(cnt)

    if ratio_and_rotation(min_rect):
        x, y, w, h = cv2.boundingRect(cnt)
        plate_img = img[y:y+h, x:x+w]
        print("Number  identified number plate...")
        cv2.imshow("num plate image", plate_img)
        if cv2.waitKey(0) & 0xff == ord('q'):
            pass
        if(isMaxWhite(plate_img)):
            clean_plate, rect = clean2_plate(plate_img)
            if rect:
                fg = 0
                x1, y1, w1, h1 = rect
                x, y, w, h = x+x1, y+y1, w1, h1
                plate_im = Image.fromarray(clean_plate)
                text = tess.image_to_string(plate_im, lang='eng')
                print("Number  Detected Plate Text : ", text)
