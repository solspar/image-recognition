# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 01:59:38 2020

@author: alw
"""

"""
import numpy as np
import argparse
import imutils
from imutils import paths
import pickle
import cv2
import os

#parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--dataset", required=True,
                help="path to input directory of faces + images")
ap.add_argument("-e","--embeddings", required=True,
                help="path to output facial embeddings")
ap.add_argument("-d","--detector", required=True,
                help="path to opencv deep learning detector")
ap.add_argument("-m","--confidence", type=float, default =0.5,
                help="probability to filter weak detections")
args = vars(ap.parse_args())
#source code https://www.jianshu.com/p/cb6e846804bb
# load detector from disk
print("detector loading")
proPath = os.path.sep.join([args["detector"],"deploy.prototxt"])
modPath = os.path.sep.join([args["detector"], "res10_300x300_ssd_iter_14000.caffemodel"])
detector = cv2.dnn.readNetFromCaffe(proPath,modPath)

# load embedding model
embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

print("face quantify")
imagePaths = list(paths.list_images(args["dataset"]))


knownEmbeddings = []
knownNames = []

#initialize
total=0

#loop image path
for (i,imagePath) in enumerate(imagePaths):
    print(format(i+1,len(imagePaths)))
    name = imagePath.split(os.path.sep)[-2]
    image = cv2.imread(imagePath)
    image = imutils.resize(image,width=600)
    (h,w) = image.shape[:2]
    
    imageBlob = cv2.dnn.blobFromImage(
            cv2.resize(image,(320,320)),1.0,(320,320),(104.0,175.0,125.0),swapRB=False,crop=False)
    
    detector.setInput(imageBlob)
    detections = detector.forward()
    #at least one face should be found
    if len(detections) > 0:
        #make a bounding box
        i = np.argmax(detections[0,0,:,2])
        confidence = detections[0,0,i,2]
        
        if confidence>args["confidence"]:
            #find x,y coordinate
            box = detections[0,0,i,3:7] * np.array([w,h,w,h])
            (startX,startY,endX,endY) = box.astype("int")
            
            # grab ROI dimentions
            face = image[startY:endY, startX:endX]
            (FH,FW) = face.shape[:2]
            
            #ensure the face are large enough
            if FW < 18 or FH < 18:
                continue
            
            
            faceBolb = cv2.dnn.blobFromImage(face,1.0/255,
                (98,98),(0,0,0),swapRB=True,crop=False)
            embedder.setInput(imageBlob)
            vec = embedder.forward()
            
            #add name and face
            knownNames.append(name)
            knownEmbeddings.append(vec.flatten())
            total+=1
            
            data = {"embeddings": knownEmbeddings, "names" : knownNames}
            f = open(args["embeddings"],"wb")
            f.write(pickle.dumps(data))
            f.close()
            """
import numpy as np
import cv2

# 人脸识别分类器
faceCascade = cv2.CascadeClassifier(r'C:\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

# 识别眼睛的分类
eyeCascade = cv2.CascadeClassifier(r'C:\python38\Lib\site-packages\cv2\data\haarcascade_eye.xml')

# 开启摄像头
cap = cv2.VideoCapture(0)
ok = True

while ok:
    # 读取摄像头中的图像，ok为是否读取成功的判断参数
    ok, img = cap.read()
    # 转换成灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 人脸检测
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(32, 32)
    )

    # 在检测人脸的基础上检测眼睛
    for (x, y, w, h) in faces:
        fac_gray = gray[y: (y+h), x: (x+w)]
        result = []
        eyes = eyeCascade.detectMultiScale(fac_gray, 1.3, 2)

        # 眼睛坐标的换算，将相对位置换成绝对位置
        for (ex, ey, ew, eh) in eyes:
            result.append((x+ex, y+ey, ew, eh))

    # 画矩形
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    for (ex, ey, ew, eh) in result:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
 
    cv2.imshow('video', img)

    k = cv2.waitKey(1)
    if k == 27:    # press 'ESC' to quit
        break
 
cap.release()
cv2.destroyAllWindows()
            
            


