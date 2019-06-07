import cv2
import time

k = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # codec
out = cv2.VideoWriter('outt.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)
c1 = 7
c2 = 5
while (True):
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        k = 1
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        u1 = x+w//2
        u2 = y+h//2
        cir = cv2.circle(img, (u1, u2), 3, (0, 255, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        if len(eyes) == 2:
            for (ex, ey, ew, eh) in eyes:
                k = 0
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


        # smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        # for (sx, sy, sw, sh) in smile:
        #     cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 3)

    if k == 1:
        print("Blink")
    elif k == 0:
        print("No Blink")
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("img", 600, 450)
    cv2.imshow('img', img)
    out.write(img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
