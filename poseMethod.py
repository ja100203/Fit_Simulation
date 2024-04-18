import cv2
import mediapipe as mp
import time
import math

class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,True,True,self.detectionCon,self.trackCon)
        
    def findPose(self, resized_frame, draw=True):
        imgRGB = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(resized_frame,self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return resized_frame
    
    def findPosition(self,resized_frame,draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = resized_frame.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(resized_frame,(cx,cy), 10, (255,0,0), cv2.FILLED)
        return self.lmList

    def findAngle(self, resized_frame, p1,p2,p3, draw=True):
        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        x3, y3 = self.lmList[p3][1], self.lmList[p3][2]

        # Calculate the angle
        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))

        if draw:
            cv2.line(resized_frame, (x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(resized_frame, (x3,y3),(x2,y2),(255,255,255),3)
            cv2.circle(resized_frame, (x1,y1), 10, (0,0,255), cv2.FILLED)
            cv2.circle(resized_frame, (x2,y2), 10, (0,0,255), cv2.FILLED)
            cv2.circle(resized_frame, (x3,y3), 10, (0,0,255), cv2.FILLED)

        return angle

def main():
    cap = cv2.VideoCapture("./video1.mp4")
    pTime = 0
    new_width = 640  # Adjust as needed
    new_height = 480  # Adjust as needed

    detector = poseDetector()

    while True:
        success, img = cap.read()
        resized_frame = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        resized_frame = detector.findPose(resized_frame=resized_frame)
        lmList = detector.findPosition(resized_frame=resized_frame)
        print(lmList[10])
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(resized_frame,str(int(fps)),(50,30), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)

        cv2.imshow("Image",resized_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
