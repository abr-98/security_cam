import cv2
from twilio.rest import Client
account_sid = 'user_sid'
auth_token = 'user_token_twilio'
client = Client(account_sid, auth_token)
cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()
while True:
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<900:
            continue
        message = client.messages \
            .create(
            body="Someone is looking in your laptop",
            from_='<Number given by twilio >',
            to="<Client's number>"
        )
    cv2.imshow("Motion Status",frame1)
    frame1=frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()