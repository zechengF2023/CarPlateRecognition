from PIL import Image, ImageDraw, ImageFont
import pytesseract
import cv2
print(pytesseract.image_to_string(cv2.medianBlur(cv2.cvtColor(cv2.imread('tImg.png'), cv2.COLOR_BGR2GRAY),5)))
