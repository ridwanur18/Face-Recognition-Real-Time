import cv2
import face_recognition
import pickle
import os
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtimefacerecog-d270c-default-rtdb.firebaseio.com/',
    'storageBucket': 'realtimefacerecog-d270c.firebasestorage.app'
})


# importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    if (path == '.DS_Store'):
        print('continuing')
        continue  # skip macOS system file
    fileName = os.path.join(folderPath, path)
    img = cv2.imread(fileName)
    
    imgList.append(img)    
    studentIds.append(os.path.splitext(path)[0])
    
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
            
    return encodeList


print('Encoding started...')
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print('Encoding complete')

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print('file saved')

