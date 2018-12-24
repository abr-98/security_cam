from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-p","--prototxt",required=True,help="./MobileNetSSD_deploy.prototxt.txt")
ap.add_argument("-m", "--model", required=True,help="./MobileNetSSD_deploy.caffemodel")
ap.add_argument("-c", "--confidence", type=float, default=0.2,help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

CLASSES=["background","aeroplane","bicycle","bird","bus","car","cat","cow","dog","horse","motorbike","person","sofa","train","tvmonitor","sofa"]
COLORS=np.random.uniform(0,255,size=(len(CLASSES),3))

print("loading model...")
net=cv2.dnn.readNetFromCaffe(args["prototxt"],args["model"])

print("starting video ")
vs=VideoStream(src=0).start()
time.sleep(2.0)
fps=FPS().start()

while True:
  frame=vs.read()
  frame=imutils.resize(frame,width=400)

  (h,w)=frame.shape[:2]
  blob=cv2.dnn.blobFromImage(cv2.resize(frame,(300,300)),0.007843,(300,300),127.5)

  net.setInput(blob)
  detection=net.forward()
  for i in np.arange(0, detections.shape[2]):
    confidence=detection[0,0,i,2]

    if confidence>args["confidence"]:

      idx=int(detections[0,0,i,1])
      box=detections[0,0,i,3:7]*np.array([w,h,w,h])
      (startX,startY,endX,endY)=box.astype("int")

      label="{}: {:.2f}%".format(CLASSES[idx],confidence * 100)
      cv2.rectangle(frame,(startX,startY),(endX,endY),COLORS[idx],2)
      y = startY - 15 if startY - 15 > 15 else startY + 15
      cv2.putText(frame, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
  cv2.imshow("Frame", frame)
  key = cv2.waitKey(1) & 0xFF

  	# if the `q` key was pressed, break from the loop
  if key == ord("q"):
     break

  	# update the FPS counter
  fps.update()
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
