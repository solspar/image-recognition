# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 08:19:25 2020

@author: alw
"""
import logging
import cloudstorage as gcs

from google.appengine.api import app_identity
import cv2
import os
import numpy as np
from PIL import Image
# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
from google.cloud import storage

# Instantiates a client


# The name for the new bucket




def get(self):
  bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())

  self.response.headers['Content-Type'] = 'text/plain'
  self.response.write('Demo GCS Application running from Version: '
                      + os.environ['CURRENT_VERSION_ID'] + '\n')
  self.response.write('Using bucket name: ' + bucket_name + '\n\n')

def create_file(self, filename,x,y,h,w):
  """Create a file.

  The retry_params specified in the open call will override the default
  retry params for this particular file handle.

  Args:
    filename: filename.
  """
  self.response.write(filename)

  write_retry_params = gcs.RetryParams(backoff_factor=1.1)
  gcs_file = gcs.open(filename,
                      'w',
                      content_type='text/plain',
                      options={'x-goog-meta-foo': 'foo',
                               'x-goog-meta-bar': 'bar'},
                      retry_params=write_retry_params)
  gcs_file.write(gray[y: y + h, x: x + w])
  
  gcs_file.close()
  self.tmp_filenames_to_clean_up.append(filename)



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
        count += 1

        # save picture/change the place to save from facedata to cloud
        
        create_file("Facedata/User." + str(face_id)+ '.'+str(face_name) + '.' + str(count) +'.jpg',x,y,h,w)
        cv2.imshow('image', img)

    # 保持画面的持续。

    k = cv2.waitKey(1)

    if k == 27:   # 通过esc键退出摄像
        break

    elif count >= 200:  # 得到1000个样本后退出摄像
        break

# 关闭摄像头
cap.release()
cv2.destroyAllWindows()
