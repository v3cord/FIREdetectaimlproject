import cv2         # For openCV
import threading   
import playsound   # For alarm sound

fire_cascade = cv2.CascadeClassifier('fire_model.xml') # To access xml file 

vid = cv2.VideoCapture(0) # start camera "0" for laptop camera and "1" for USB attahed camera 
runOnce = False 

def play_alarm_sound_function(): 
    playsound.playsound('Alarm Sound.mp3',True) # to play alarm
    print("Fire alarm end")


while(True):
    Alarm_Status = False
    ret, frame = vid.read() #
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert frame into gray color
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5) # 

   
    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        print("Fire alarm initiated")
        threading.Thread(target=play_alarm_sound_function).start()  
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
