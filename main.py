# Imports
import cv2
import face_recognition
from playsound import playsound
from random import randrange
from signal import signal, SIGINT

#Config
scale = 1 # Precision. The more the better. But then it also uses more GPU/CPU
model = 'hog' # hog makes it run on CPU and cnn makes it run on GPU. cnn is best but i have a 12 year old graphics card -_-

# Asigning varibles
has_found = False
has_lost = True
sadness = 0
lol = 0
has_found = False
has_lost = True

# Starting Video Capture
cap = cv2.VideoCapture(1)

# Shutdown function
def shutdown(signal_received, frame):
    print('Shutting down')
    cap.release()
    cv2.destroyAllWindows()
    playsound(f'sound/shutdown/{randrange(1, 6)}.wav')
    exit()

def mainLoop():
    # Asigning varibles
    has_found = False
    has_lost = True
    sadness = 0
    lol = 0
    has_found = False
    has_lost = True

    while True:
        success, img = cap.read()
        
        Current_image = cv2.resize(img,(0,0),None,scale,scale)
        Current_image = cv2.cvtColor(Current_image, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(Current_image, model=model)  
        
        sadness = randrange(0,500)
        if sadness == 75:
            print('SAD')
            playsound(f'sound/sadness/{randrange(1,6)}.wav')

        if face_locations:
            lol = 0
            if not has_found:
                print('FOUND YOU!')
                has_found = True
                has_lost = False
                playsound(f'sound/detection/{randrange(1, 5)}.wav')
        elif not face_locations and not has_lost:
            print('Maybe lost you')
            if lol == 8:
                lol = 0
                print('LOST YOU')
                has_found = False
                has_lost = True
                playsound(f'sound/noDetection/{randrange(1, 4)}.wav')
            else:
                lol += 1

        #cv2.imshow("Frame", img)

if __name__ == '__main__':
    # Asign shutdown function
    signal(SIGINT, shutdown)
    print('Running. Press CTRL-C to exit.')

    # Signaling startup
    print('Hello')
    playsound(f'sound/startup/{randrange(1,4)}.wav', block=False)

    # Run the main loop
    mainLoop()