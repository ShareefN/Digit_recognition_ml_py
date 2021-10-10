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
        detect_plate(dst)


def detect_plate(frame):
    plate = plate_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in plate:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
                      color=(0, 255, 0), thickness=2)
        crop_img = frame[y:y+h, x:x+w]
        super_resolution(crop_img)


def super_resolution(frame):
    # https://www.pyimagesearch.com/2020/11/09/opencv-super-resolution-with-deep-learning/
    # modelName = frame.split(os.path.sep)[-1].split("_")[0].lower()
    modelName = frame.split(os.path.sep)
    modelScale = frame.split("_x")[-1]
    modelScale = int(modelScale[:modelScale.find(".")])
    print("[INFO] model name: {}".format(modelName))
    print("[INFO] model scale: {}".format(modelScale))

    cv2.imshow('vehicle plate', frame)
    if cv2.waitKey(0) & 0xff == ord('q'):
        pass
