import cv2
import pytesseract
import numpy as np

def OCR(img):
    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(img, config = config)
    return text

def strengthen(img):
    try:
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except Exception:
        imgray = img
    blur2 = cv2.GaussianBlur(imgray,(5,5),0)
    thresh2 = cv2.adaptiveThreshold(blur2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    kernel = np.ones((2,1),np.uint8)
    return thresh2

def removeMetaData(text):
    text = text.split("\n")
    for i in range(len(text)):
        try:
            if text[i][:5] == "<110>":
                return text[i:]
        except:
            pass

def removeNewLines(text):
    i = 0
    while i < len(text):
        if text[i] == '':
            text = text[:i] + text[i+1:]
        i += 1
    return text

def organizeData(text, fileName):
    key, val = '', ''
    txtName = getPN(fileName)
    filePointer = open(f"{txtName}.txt", "a")

    for i in range(len(text)):
        if '<' in text[i]:
            if key != '' and val != '':
                filePointer.write(f"{key} {val}\n")
            leftIndex = text[i].index('<')
            rightIndex = text[i].index('>')
            key = text[i][leftIndex:rightIndex+1]
            val = text[i][rightIndex+1:].strip()
        else:
            val += f"\n{text[i].strip()}"
    filePointer.write(f"{key} {val}")
    filePointer.close()

def getPN(fileName):
    temp = fileName.split('-')[-1]
    count = 0
    result = ''
    for i in temp:
        if i == '_':
            count += 1
            if count == 2:
                break
            continue
        result += i
    return result