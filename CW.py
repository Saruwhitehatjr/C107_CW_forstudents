import cv2



vid=cv2.VideoCapture("bb3.mp4")

#load tracker
tracker= cv2.TrackerCSRT_create()
# Select obj to track from first frame
val,first_frame= vid.read()

# create ROI - 3 parameters ,ROI name, image name, REct from left -False , from center - true
bbox=cv2.selectROI("Tracking",first_frame,False)

# initite tracker
tracker.init(first_frame,bbox)
print(bbox)

def drawBox(frame,bbox):
    x,y,w,h= int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.putText(frame,"TRACKING",(75,90),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(255,0,0),2)


while True:
    ret,frame=vid.read()
    #update tracker
    success,bbox=tracker.update(frame)
    if success:
        drawBox(frame,bbox)
    else:
        cv2.putText(frame,"OBJECT LOST",(75,90),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(255,0,0),2)    



    cv2.imshow("video",frame)
    if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows()    
