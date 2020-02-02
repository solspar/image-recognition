# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 03:30:57 2020

@author: alw
"""

import cv2
import os
from websocket import create_connection
import json
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
from google.cloud import storage


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_trainer/trainer.yml')

faceCascade = cv2.CascadeClassifier(r'C:\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

# The name for the new bucket
bucket_name = "swamp-ml-1580531853344.appspot.com"
# Instantiates a client
def make_blob_public(bucket_name, blob_name):
    """Makes a blob publicly accessible."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.make_public()

    return blob.public_url
        
    






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
sendtime=0
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
        
        if confidence <80:
            count+=1
            idnum = names[idnum]
            confidence = "{0}%".format(round(100 - confidence))
            
            if count>30:
                sendtime+=1
                if sendtime==1:
                    appdict={
                            'name': idnum,
                            'photo': make_blob_public('swamp-ml-1580531853344.appspot.com', "Facedata/User." +str(idnum) +'.jpg')}
                    ws=create_connection("ws://35.193.149.149/")
                    app_json=json.dumps(appdict)
                    ws.send(app_json)
                    sendtime+=1
                
            
                #send imformation
        else:
            sendtime=0
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