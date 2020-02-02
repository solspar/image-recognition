# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 03:30:57 2020

@author: alw
"""

import cv2
import os
import time
"""
import logging
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity

def get(self):
  bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())

  self.response.headers['Content-Type'] = 'text/plain'
  self.response.write('Demo GCS Application running from Version: '
                      + os.environ['CURRENT_VERSION_ID'] + '\n')
  self.response.write('Using bucket name: ' + bucket_name + '\n\n')
def create_file(self, filename):
   
  Create a file.

  The retry_params specified in the open call will override the default
  retry params for this particular file handle.

  Args:
    filename: filename.
  
  self.response.write('Creating file %s\n' % filename)

  write_retry_params = gcs.RetryParams(backoff_factor=1.1)
  gcs_file = gcs.open(filename,
                      'w',
                      content_type='text/plain',
                      options={'x-goog-meta-foo': 'foo',
                               'x-goog-meta-bar': 'bar'},
                      retry_params=write_retry_params)
  gcs_file.write('abcde\n')
  gcs_file.write('f'*1024*4 + '\n')
  gcs_file.close()
  self.tmp_filenames_to_clean_up.append(filename)

"""

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier(r'C:\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX


idnum=0
path = 'Facedata'
names=[]
imagePaths = [os.path.join(path, f) for f in os.listdir(path)] 
for imagepath in imagePaths:
    id = str(os.path.split(imagepath)[-1].split(".")[2])
    if (id not in names):
        names.append(id)

cam = cv2.VideoCapture(0)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

count =0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        idnum, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence <60:
            count+=1
            idnum = names[idnum]
            confidence = "{0}%".format(round(100 - confidence))
            if count>20:
                cam.release()
                cv2.destroyAllWindows()
                #send imformation
        else:
            count=0
            idnum = "unknown"
            confidence = "{0}%".format(round(100 - confidence))

        cv2.putText(img, str(idnum), (x+5, y-5), font, 1, (0, 0, 255), 1)
        cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (0, 0, 0), 1)

    cv2.imshow('camera', img)
    k = cv2.waitKey(10)
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()