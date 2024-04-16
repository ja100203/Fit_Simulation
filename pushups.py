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
        # Calculate angles for both arms
        angle_right = detector.findAngle(img, 12, 14, 16)
        angle_left = detector.findAngle(img, 11, 13, 15)

        # Normalize angles to percentage
        per_right = np.interp(angle_right, (60, 160), (0, 100))
        per_left = np.interp(angle_left, (60, 160), (0, 100))

        # Check for push-up completion for right arm
        color_right = (255, 0, 255)
        if per_right == 100:
            color_right = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per_right == 0:
            color_right = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

        # Check for push-up completion for left arm
        color_left = (255, 0, 255)
        if per_left == 100:
            color_left = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per_left == 0:
            color_left = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0

        # Draw progress bar and percentage for right arm
        # bar_right = np.interp(angle_right, (60, 160), (650, 100))
        # cv2.rectangle(img, (1100, 100), (1175, 658), color_right, 3)
        # cv2.rectangle(img, (1100, int(bar_right)), (1175, 658), color_right, cv2.FILLED)
        # cv2.putText(img, f'{int(per_right)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 3, color_right, 3)

        # # Draw progress bar and percentage for left arm
        # bar_left = np.interp(angle_left, (60, 160), (650, 100))
        # cv2.rectangle(img, (1050, 100), (1125, 658), color_left, 3)
        # cv2.rectangle(img, (1050, int(bar_left)), (1125, 658), color_left, cv2.FILLED)
        # cv2.putText(img, f'{int(per_left)} %', (1050, 75), cv2.FONT_HERSHEY_PLAIN, 3, color_left, 3)
        

        # Draw progress bar and percentage for right arm
        bar_right = np.interp(angle_right, (60, 160), (650, 100))
        cv2.rectangle(img, (1140, 100), (1215, 658), color_right, 3)
        cv2.rectangle(img, (1140, int(bar_right)), (1215, 658), color_right, cv2.FILLED)
        cv2.putText(img, f'{int(per_right)} %', (1140, 75), cv2.FONT_HERSHEY_PLAIN, 3, color_right, 3)

        # Draw progress bar and percentage for left arm
        bar_left = np.interp(angle_left, (60, 160), (650, 100))
        cv2.rectangle(img, (1020, 100), (1095, 658), color_left, 3)
        cv2.rectangle(img, (1020, int(bar_left)), (1095, 658), color_left, cv2.FILLED)
        cv2.putText(img, f'{int(per_left)} %', (1020, 75), cv2.FONT_HERSHEY_PLAIN, 3, color_left, 3)



        # Draw push-up count
        cv2.putText(img, f'{count}', (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()