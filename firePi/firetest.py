from firebase_admin import credentials, initialize_app, storage
import socket
from PIL import Image
import time


cred = credentials.Certificate("hacksc2022-4d22b-firebase-adminsdk-pymt0-852e6c81ac.json")
initialize_app(cred, {'storageBucket': 'hacksc2022-4d22b.appspot.com'})
fileName = 'latest.jpg'


uploadImage = False

#To be defined

if (uploadImage):
    timestamp = time.time()
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
