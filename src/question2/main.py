"""
  2 - Implemente uma solução que leia um vídeo e rotule/indique o(s) objeto(s) 
  em movimento na cena.
"""

import numpy as np
import cv2 as cv


def readVideo():
    cap = cv.VideoCapture("ManSurfing.mp4")

    while True:
        ret, frame = cap.read()

        if ret:
            frame = cv.resize(frame, (500, 400))

            cv.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 1)

            cv.imshow("Frame", frame)

            if cv.waitKey(1) == ord('q'):
                break
        else:
            break

    cap.release()
    cv.destroyAllWindows()
