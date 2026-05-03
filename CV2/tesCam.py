import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cv2.namedWindow('glitch', cv2.WINDOW_NORMAL)
cv2.resizeWindow('glitch', 800, 600)

while 1:
    flag, frame = cam.read()

    if flag:
        b, g, r = cv2.split(frame)

        # shift channel
        r_shift = np.roll(r, 10, axis=1)   # geser kanan
        b_shift = np.roll(b, -10, axis=1)  # geser kiri

        glitch = cv2.merge([b_shift, g, r_shift])
        cv2.imshow("glitch", glitch)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()