import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('cat', img)


cv.waitKey(0)


''''
capture = cv.VideoCapture('Resources/Videos/sample.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()
''''