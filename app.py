from prepare import detect_vehicle
import cv2


def Simulator():
    CarVideo = cv2.VideoCapture('cars/cars2.mp4')

    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        controlkey = cv2.waitKey(1)
        if ret:
            cv2.imshow('Video', frame)
            cars_frame = detect_vehicle(frame)
        else:
            cv2.imshow('False detections', frame)
        if controlkey == ord('q'):
            break

    CarVideo.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Simulator()
