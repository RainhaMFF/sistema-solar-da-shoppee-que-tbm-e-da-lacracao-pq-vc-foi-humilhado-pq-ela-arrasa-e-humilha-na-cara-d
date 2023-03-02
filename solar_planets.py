import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Stop",
             (100,80),
             cv2.FONT_HERSHEY_COMPLEX,
             2,
             (0,0,255)
             )

cv2.putText(img,
            "reading",
             (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,0,0)
             )

cv2.putText(img,
            "this",
             (190,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "its",
             (300,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "just",
             (400,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "a",
             (500,90),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )            
            
cv2.putText(img,
            "pure",
             (720,110),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             ) 

cv2.putText(img,
            "waste o-",
             (950,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "-f time.",
             (1080,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.imshow("wut r u looking at bro 🧐 ur just wasting your own time...... u could be doing anything but i warned you ur just wasting time.",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)
