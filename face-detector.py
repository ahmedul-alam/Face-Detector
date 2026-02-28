# import cv2
# video_capture = cv2.VideoCapture(0)
# while True:
#     ret , video = video_capture.read()
#     cv2.imshow("video_live",video)
#     if cv2.waitKey(10) ==ord('s'):
#         break

# video_capture.release()


import cv2
face_cap = cv2.CascadeClassifier("c:\\Users\\AHMED\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
while True:
     ret , video = video_capture.read()
     gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
     faces = face_cap.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
     for (x,y,w,h) in faces:
         cv2.rectangle(video, (x,y), (x+w,y+h), (0,255,0), 2)
     cv2.imshow("video_live",video)
     if cv2.waitKey(10) ==ord('s'):
         break

video_capture.release()

