#importing modules and dependencies
import cv2
import mediapipe as mp
import time
mpDraw = mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose= mpPose.Pose()

#initalizing some values
up=False
count=0  #for rep count
t=0      #for kneebend timer



#Video feed
cap=cv2.VideoCapture("KneeBendVideo.mp4")

while True:
    success,img=cap.read()
    img= cv2.resize(img,(1080,720))
    RGB_img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=pose.process(RGB_img)
    #print(result.pose_landmarks)

    mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
    points={} #dictionary to hold all the points of detection
    for id, lm in enumerate(result.pose_landmarks.landmark,start=0):
        h,w,c= img.shape
        cx,cy= int(lm.x*w),int(lm.y*h)
        #print(id,lm,cx,cy)
        points[id]=(cx,cy)

    cv2.circle(img,points[25],10, (255,0,0),cv2.FILLED)
    #cv2.circle(img, points[26], 10, (255, 0, 0), cv2.FILLED)
    cv2.circle(img,points[23],10, (255,0,0),cv2.FILLED)


    if points[25][1] < points[13][1]:
        t = t + 1
        time.sleep(0.01)   #setting up a timmer
        #print(t)
        up=True
        #count+=1
    sec = round((t/15),2)


    if points[25][1] > points[23][1]:
        t=0
        print("DOWN")
        up=False

    if sec==8.0:
        count=count+1  #increasing the count by one as soon as the timer hits 8 seconds

    cv2.rectangle(img,(0,0),(220,73),(255,0,0),-1)
    cv2.putText(img,"KNEE BEND TIMER:",(15,12),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    cv2.putText(img,str(sec),(10,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)
    cv2.putText(img, "REP COUNT:", (800, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)
    cv2.putText(img, str(count),(1000,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0, 0), 5)
    if sec<8.0:
        cv2.putText(img, "Keep your knee bent", (380, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,255 ), 5)


    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break



