import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

try:
    webcam = cv2.VideoCapture(0)  # Attempt to access the camera
    if not webcam.isOpened():
        raise ValueError("Camera index out of range or not accessible.")
except Exception as e:
    print(f"Error initializing webcam: {e}")
    webcam = None

smile_counter = 0
SMILE_THRESHOLD = 10

def detect_smile():
    global smile_counter
    if webcam is None:
        print("Webcam is not initialized.")
        return False
    success, frame = webcam.read()
    if not success:
        print("Failed to read from webcam.")
        return False
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(face_gray, 1.7, 20)
        if len(smiles) > 0:
            smile_counter += 1
            if smile_counter >= SMILE_THRESHOLD:
                return True
        else:
            smile_counter = 0
    return False

def release_camera():
    if webcam:
        webcam.release()
    cv2.destroyAllWindows()

try:
    print(detect_smile())
except Exception as e:
    print(f"An error occurred during smile detection: {e}")
finally:
    release_camera()
#is this even working? i only got false after trying for a whole 5m