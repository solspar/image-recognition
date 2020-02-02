# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 08:19:25 2020

@author: alw
"""



import cv2
import os
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(r'C:\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

face_id = input('\n enter user id:')
face_name = input('\n enter name:')
idnum = 0

names = []
names.append(face_name)

print('\n Initializing face capture. Look at the camera and wait ...')
count = 0
while True:

    # 从摄像头读取图片

    sucess, img = cap.read()
    
    # 转为灰度图片

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 检测人脸

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+w), (255, 0, 0))
        if count == 0:     
            cv2.imwrite("Namedata/User." +str(face_name) + '.jpg',img[y: y + h, x: x + w])
            upload_blob('swamp-ml-1580531853344.appspot.com',"Namedata/User." +str(face_name) +'.jpg', "Facedata/User." +str(face_name)  +'.jpg')

             
        count += 1

        # save picture/change the place to save from facedata to cloud
        
        cv2.imwrite("Facedata/User." + str(face_id)+ '.'+str(face_name) + '.' + str(count) +'.jpg',gray[y: y + h, x: x + w])
        cv2.imshow('image', img)

    # 保持画面的持续。

    k = cv2.waitKey(1)

    if k == 27:   # 通过esc键退出摄像
        break

    elif count >= 100:  # 得到1000个样本后退出摄像
        break

# 关闭摄像头
cap.release()
cv2.destroyAllWindows()
