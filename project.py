# import cv2
# import mediapipe as mp
# import numpy as np
# mp_drawing=mp.solutions.drawing_utils
# mp_pose=mp.solutions.pose

# cap = cv2.VideoCapture(0)

# def calculate_angle_right(a, b, c, right_hand=True):
#     a = np.array(a)  # First
#     b = np.array(b)  # Mid
#     c = np.array(c)  # End
    
#     if right_hand:
#         radians = np.arctan2(a[1]-b[1], a[0]-b[0]) - np.arctan2(c[1]-b[1], c[0]-b[0])
#     else:
#         radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    
#     angle = np.abs(radians * 180.0 / np.pi)
    
#     if angle > 180.0:
#         angle = 360 - angle
        
#     return angle


# def calculate_angle(a,b,c, right_hand=False):
#     a = np.array(a) # First
#     b = np.array(b) # Mid
#     c = np.array(c) # End
    
#     radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
#     angle = np.abs(radians*180.0/np.pi)
    
#     if angle >180.0:
#         angle = 360-angle
        
#     return angle 

# # Curl counter variables
# counter = 0 
# stage = None

# ## Setup mediapipe instance
# with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#     while cap.isOpened():
#         ret, frame = cap.read()
#         frame = cv2.resize(frame,(1280,720),interpolation=cv2.INTER_AREA)
        
#         # Recolor image to RGB
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         image.flags.writeable = False
      
#         # Make detection
#         results = pose.process(image)
    
#         # Recolor back to BGR
#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
#         # Extract landmarks
#         try:
#             landmarks = results.pose_landmarks.landmark
            
#             # Get coordinates
#             shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
#             elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
#             wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
#             shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
#             elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
#             wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
#             # Calculate angle
#             angle = calculate_angle(shoulder, elbow, wrist)
#             angle_right = calculate_angle_right(shoulder_right, elbow_right, wrist_right)
            
#             # Visualize angle
#             cv2.putText(image, str(angle), 
#                            tuple(np.multiply(elbow, [640, 480]).astype(int)), 
#                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
#                                 )
            
#             # Curl counter logic
#             if angle > 160:
#                 stage = "down"
#             if angle < 30 and stage =='down':
#                 stage="up"
#                 counter +=1
#                 print(counter)
                       
#         except:
#             pass
        
#         # Render curl counter
#         # Setup status box
#         cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
#         # Rep data
#         cv2.putText(image, 'REPS', (15,12), 
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
#         cv2.putText(image, str(counter), 
#                     (10,60), 
#                     cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
#         # Stage data
#         cv2.putText(image, 'STAGE', (65,12), 
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
#         cv2.putText(image, stage, 
#                     (60,60), 
#                     cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
#         # Render detections
#         mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
#                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
#                                 )               
        
#         cv2.imshow('Mediapipe Feed', image)

#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # import cv2
# # import mediapipe as mp
# # import numpy as np

# # mp_drawing = mp.solutions.drawing_utils
# # mp_pose = mp.solutions.pose

# # def calculate_angle(a, b, c):
# #     a = np.array(a)  # First
# #     b = np.array(b)  # Mid
# #     c = np.array(c)  # End

# #     radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
# #     angle = np.abs(radians * 180.0 / np.pi)

# #     if angle > 180.0:
# #         angle = 360 - angle

# #     return angle

# # # Curl counter variables
# # down_count = 0
# # up_count = 0
# # stage = None
# # is_down = False

# # # Setup mediapipe instance
# # with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
# #     cap = cv2.VideoCapture(0)
# #     while cap.isOpened():
# #         ret, frame = cap.read()
# #         frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_AREA)

# #         # Recolor image to RGB
# #         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #         image.flags.writeable = False

# #         # Make detection
# #         results = pose.process(image)

# #         # Recolor back to BGR
# #         image.flags.writeable = True
# #         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# #         # Extract landmarks
# #         try:
# #             landmarks = results.pose_landmarks.landmark

# #             # Get coordinates for left hand
# #             left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
# #             left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
# #             left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

# #             # Calculate angles
# #             angle_left = calculate_angle(left_shoulder, left_elbow, left_wrist)

# #             # Curl counter logic
# #             if angle_left > 160 and not is_down:
# #                 stage = "down"
# #                 down_count += 1
# #                 is_down = True
# #             if angle_left < 30 and is_down:
# #                 stage = "up"
# #                 up_count += 1
# #                 is_down = False

# #             # Visualize counts on the image
# #             cv2.putText(image, f"Downs: {down_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
# #             cv2.putText(image, f"Ups: {up_count}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# #         except:
# #             pass

# #         # Render detections
# #         mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
# #                                    mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
# #                                    mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
# #                                    )

# #         cv2.imshow('Mediapipe Feed', image)

# #         if cv2.waitKey(10) & 0xFF == ord('q'):
# #             break

# #     cap.release()
# #     cv2.destroyAllWindows()




import asyncio
import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import speech_recognition as sr
import time
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',170)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

def speak(text):
    def _speak(text):
        engine.say(text)
        engine.runAndWait()
    
    # Create a thread for speech output
    threading.Thread(target=_speak, args=(text,)).start()

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle, np.sign(c[0] - a[0]) # Return angle and direction (+1 for right, -1 for left)

# Curl counter variables
down_count_left = 0
up_count_left = 0
down_count_right = 0
up_count_right = 0
stage_left = None
stage_right = None
is_down_left = False
is_down_right = False

# Last counts recorded for posture evaluation
# last_down_count_left = down_count_left
# last_up_count_left = up_count_left
# last_down_count_right = down_count_right
# last_up_count_right = up_count_right
# last_check_time = time.time()
# check_interval = 2.0  # Interval to check for changes (in seconds)

# ************************** added now *****************
# last_feedback_time_left = 0
# last_feedback_time_right = 0
# feedback_delay = 2.0  # Seconds of delay before giving feedback
# ************************** added now ******************

# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    cap = cv2.VideoCapture(0)
    last_feedback_time_left = time.time()
    last_feedback_time_right = time.time()
    feedback_interval = 3.0
    while cap.isOpened():
        # speak("Hello Janvi")
        ret, frame = cap.read()
        frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_AREA)
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates for left hand
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Get coordinates for right hand
            right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            # Calculate angles for left and right hand
            angle_left, dir_left = calculate_angle(left_shoulder, left_elbow, left_wrist)
            angle_right, dir_right = calculate_angle(right_shoulder, right_elbow, right_wrist)

            # Left hand curl counter logic
            # if dir_left == 1:
            if angle_left > 160 and not is_down_left:
                stage_left = "down"
                down_count_left += 1
                is_down_left = True
            if angle_left < 30 and is_down_left:
                stage_left = "up"
                up_count_left += 1
                is_down_left = False

            if dir_left == 1:
                if(angle_left < 150):
                    last_feedback_time_left = time.time()
            if angle_right > 160 and not is_down_right:
                stage_right = "down"
                down_count_right += 1
                is_down_right = True
            if angle_right < 30 and is_down_right:
                stage_right = "up"
                up_count_right += 1
                is_down_right = False

            if dir_right == -1:
                if(angle_right < 150):
                    last_feedback_time_right = time.time()

            #  *********** Check for changes in time(New) ********************
            current_time = time.time()
            if current_time - last_feedback_time_left >= feedback_interval and down_count_left < 16:
                speak("Bend a slight more with your left arm")
                last_feedback_time_left = current_time

            if current_time - last_feedback_time_right >= feedback_interval and down_count_right < 16:
                speak("Bend a slight more with your right arm")
                last_feedback_time_right = current_time
            #  *********** Check for changes in time(New) ********************
                
            if(down_count_left == 21 or up_count_left == 21 or down_count_right == 21 or up_count_right == 21):
                speak("Good Job!, Keep it up..")
                speak("You have completed one set..")
                break

            # Visualize counts for left hand on the image
            cv2.putText(image, f"Left Downs: {down_count_left}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, f"Left Ups: {up_count_left}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Visualize counts for right hand on the image
            cv2.putText(image, f"Right Downs: {down_count_right}", (800, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, f"Right Ups: {up_count_right}", (800, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        except:
            pass

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                   mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                   mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                   )

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
