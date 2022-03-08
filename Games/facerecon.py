import cv2
 # cv2.imread(path, flag) -> input image -> path - file path, flag - specifies whether image is in color or grayscale
 # cv2.imshow(window name, image) -> output image -> displays image on that window, displays image
 # cv2.imwrite(file, image to save) -> write changes to input image -> name of file, save success/unsuccess value

#STEPS:
# read image -> extract rgb values -> resize -> work on pixels -> mark borders

xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) #live feed input

# cap = cv2.VideoCapture('') #sample input

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = xml.detectMultiScale(gray, 1.1, 4)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
