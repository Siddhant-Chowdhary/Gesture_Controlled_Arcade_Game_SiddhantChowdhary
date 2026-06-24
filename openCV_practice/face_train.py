import os
import cv2 as cv
import numpy as np 

people = ('Roger' , 'Rafa' , 'Andy' , 'Djoko')
DIR = r'E:\SIDDHANT\SOC\train'

#p = []
#for i in os.listdir(r'E:\SIDDHANT\SOC\train'):
#    p.append(i)
#print(p)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path , img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array , cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.05 , minNeighbors = 3)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray [y:y+h , x:x+w]
                features.append(faces_roi)
                labels.append(label)
    
create_train()
print('Training Done ----------')

features = np.array(features , dtype = 'object')
labels = np.array(labels)

#print(f'Number of features are = {len(features)}')
#print(f'Number of labels are = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features , labels)

face_recognizer.save('face_trained.yml')

np.save('labels.npy' , labels)
np.save('features.npy' , features)
