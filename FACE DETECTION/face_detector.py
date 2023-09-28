import cv2


class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            r"C:\Users\MBR\Desktop\Internships\CodSoft\CodSoft\FACE DETECTION\haarcascade_frontalface_default.xml"
        )

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30))
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
        return frame

    def close(self):
        cv2.destroyAllWindows()
