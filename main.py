import cv2
import pytesseract
import numpy as np
from utils import removeMetaData, removeNewLines, organizeData, OCR, strengthen

imageName = "000001-WO02_027004_PD_20020404.tif"
img = cv2.imread(imageName)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#MNIST(img)
strengthened= strengthen(img)
text = OCR(strengthened)
text = removeMetaData(text)
text = removeNewLines(text)
organizeData(text, imageName)