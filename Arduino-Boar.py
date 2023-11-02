from ultralytics import YOLO
model=YOLO("Boar-Hunt.pt")
import cv2
import serial
# Replace 'COMX' with the actual COM port of your Arduino
ser = serial.Serial('COM1', 9600, timeout=1)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    results=model.predict(source=frame,conf=0.8,show=True)
    try :
        x=results[0]
        box = x.boxes[0]
        command='1'
        ser.write(command.encode('utf-8'))
    except:
        pass
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()