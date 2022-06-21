import cv2
import numpy

PREVIEW  = 0   # Preview Mode
BLUR     = 1   # Blurring Filter
CANNY    = 2  # Canny Edge Detector

feature_params = dict( maxCorners = 500,
                       qualityLevel = 0.2,
                       minDistance = 15,
                       blockSize = 9)

image_filter = PREVIEW
alive = True

win_name = 'Camera Filters'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(0)

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv2.flip(frame,1)

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 80, 150)
    elif image_filter == BLUR:
        result = cv2.blur(frame, (13,13))


    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        alive = False
    elif key == ord('C') or key == ord('c'):
        image_filter = CANNY
    elif key == ord('B') or key == ord('b'):
        image_filter = BLUR
    elif key == ord('P') or key == ord('p'):
        image_filter = PREVIEW

source.release()
cv2.destroyWindow(win_name)
