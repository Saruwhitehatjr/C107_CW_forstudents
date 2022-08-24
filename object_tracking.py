import cv2
import math
p1=530
p2=300
xs=[]
ys=[]

vid=cv2.VideoCapture("bb3.mp4")

tracker= cv2.TrackerCSRT_create()
ret,img= vid.read()
bbox= cv2.selectROI("Tracking",img,False)
tracker.init(img,bbox)
print(bbox)

def drawBox(frame,bbox):
    x,y,w,h = bbox[0],bbox[1],bbox[2],bbox[3]
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(frame,"Tracking",(75,90),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(0,255,0),2)
def goal_track(frame,bbox):
    x,y,w,h = bbox[0],bbox[1],bbox[2],bbox[3]
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(frame,(c1,c2),2,(0,0,255),3)
    cv2.circle(frame,(int(p1),int(p2)),2,(0,255,0),3)

    xs.append(c1)
    ys.append(c2)
    for i in range(len(xs)-1):
        cv2.circle(frame,(xs[i],ys[i]),2,(0,0,255),5)

    dist= math.sqrt((c1-p1)**2)+((c2-p2)**2)
    print(dist)
    if (dist<=20):
        cv2.putText(frame,"GOAL",(300,90),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(0,0,255),2)




while(True):
    check,frame= vid.read()
    success,bbox=tracker.update(frame)
    if(success):
        drawBox(frame,bbox)
    else:
        cv2.putText(frame,"Lost",(75,90),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(0,0,255),2)
    goal_track(frame,bbox)
    cv2.imshow("video",frame)

    if(cv2.waitKey(25)==32):
        break

vid.release()
cv2.destroyAllWindows()