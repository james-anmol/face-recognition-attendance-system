import face_recognition
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture= cv2.VideoCapture(0)

my_image = face_recognition.load_image_file("D:\\work (mca)\\pythonProject6\\faces\\a.jpg")
my_image_encoding=face_recognition.face_encodings(my_image)[0]

f1_image = face_recognition.load_image_file("D:\\work (mca)\\pythonProject6\\faces\\f1.jpg")
f1_image_encoding=face_recognition.face_encodings(f1_image)[0]

known_face_encodings=[my_image_encoding,f1_image_encoding]
known_face_names=["anmol","nct"]


students=known_face_names

face_locations=[]
face_encodengs=[]

now=datetime.now()
current_date =now.strftime("%Y-%m-%d")

f=open(f"{current_date}.csv","w+",newline="")
lnwriter =csv.writer(f)

while True:
    _, frame =video_capture.read()
    small_frame =cv2.resize(frame, (0,0), fx=0.25 ,fy=0.25)
    rgb_small_frame =cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    face_locations =face_recognition.face_locations(rgb_small_frame)
    face_encodengs=face_recognition.face_encodings(rgb_small_frame,face_locations)

    for face_encodeng in face_encodengs:
        matches= face_recognition.compare_faces(known_face_encodings,face_encodeng)
        face_distance =face_recognition.face_distance(known_face_encodings,face_encodeng)
        best_match_index=np.argmax(face_distance)

        if(matches[best_match_index]):
            name= known_face_names[best_match_index]

            cv2.imshow("Attendence",frame)
            if cv2.waitKey(1) & 0xFF ==ord("q"):
                break
            if name in known_face_names:
                font =cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText =(10,100)
                fontScale =1.5
                fontColor =(255, 0, 0)
                thickness =3
                lineType=2
                cv2.putText(frame,name + "present", bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)

                if name in students :
                    students.remove(name)
                    current_time=now.strftime(" %H-%M-%S")
                    lnwriter.writerow([name,current_time])




video_capture.release()
cv2.destroyAllWindows()
f.colse()