import numpy as np
import cv2
import os

plate_cascade = cv2.CascadeClassifier('cascade/haarcascade_car_plate.xml')
vehicle_cascade = cv2.CascadeClassifier('cascade/haarcascade_car.xml')


def detect_vehicle(frame):
    vehicle = vehicle_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in vehicle:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      color=(255, 0, 0), thickness=2)
        crop_img = frame[y:y+h, x:x+w]
        dst = cv2.detailEnhance(crop_img, 10, 1.5)
        cv2.imshow('vehicle', dst)
        if cv2.waitKey(0) & 0xff == ord('q'):
            pass
        # detect_plate(dst)


def detect_plate(frame):
    plate = plate_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in plate:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      color=(0, 255, 0), thickness=2)
        crop_img = frame[y:y+h, x:x+w]
        # cv2.imwrite('samples/img.png', crop_img)
        super_resolution(crop_img)


def super_resolution(frame):
    # sr = cv2.dnn_superres.DnnSuperResImpl_create()
    # path = "samples/img.png"
    # sr.readModel(path)
    # sr.setModel("edsr", 4)
    # print(sr)
    # result = sr.upsample(frame)
    # resized = cv2.resize(result, dsize=None, fx=4, fy=4)

    cv2.imshow('vehicle plate', frame)
    if cv2.waitKey(0) & 0xff == ord('q'):
        pass
