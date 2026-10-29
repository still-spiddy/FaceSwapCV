import cv2


face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = input("Enter the absolute path of the pfp you want to use: ")
cap = cv2.VideoCapture(0)
pfp = cv2.imread(image)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
print("Enter q to exit!!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to access Webcam!!")
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        avatar = cv2.resize(pfp,(w,h))
        frame[y:y+h,x:x+w] = avatar
    
    cv2.imshow("Face Detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break


cap.release()
cv2.destroyAllWindows()
