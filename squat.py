import cv2
import time
import numpy as np
import poseMethod as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0

while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280,720), interpolation=cv2.INTER_AREA)
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)

        if len(lmList) != 0:
            shoulder = detector.findAngle(img, 7, 11, 23)
            knee = detector.findAngle(img, 23, 25, 27)
            
            per = np.interp(knee, (90, 160), (0, 100))
            color = (255, 0, 255)

            if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0

            bar = np.interp(knee, (90, 160), (650, 100))
            cv2.rectangle(img, (1140, 100), (1215, 658), color, 3)
            cv2.rectangle(img, (1140, int(bar)), (1215, 658), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1140, 75), cv2.FONT_HERSHEY_PLAIN, 3, color, 3)

            cv2.putText(img, f'{count}', (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

