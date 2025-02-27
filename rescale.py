import cv2 as cv
from numpy import shape

#img = cv.imread('Resources/Photos/Pluem.jpg')
#cv.imshow('Pluem', img)

def rescaleFrame(frame , scale = 0.75) :
    width = int(frame, shape[1] * scale)
    height = int(frame, shape[0] * scale)

    dismensions = (width , height)

    return cv.resize(frame , dismensions , interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Resources/Videos/Pluem.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()


capture = cv.VideoCapture('Resources/Videos/Pluem.mp4')

while True:
    isTrue , frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized' ,frame_resized )

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()