from bluepy import btle
import os
from firebase_admin import credentials, initialize_app, storage


fileName = 'latest'
picsTaken = 0
class MyDelegate(btle.DefaultDelegate):
    
    def __init__(self, params):
        btle.DefaultDelegate.__init__(self)
        cred = credentials.Certificate("hacksc2022-4d22b-firebase-adminsdk-pymt0-852e6c81ac.json")
        initalize_app(cred, {'storageBucket': 'hacksck2022-4d22b.appspot.com'})
        
        
    def handleNotification(self, chandle, data):
        os.system("raspistill -o " + filename + str(picsTaken) + ".jpg")
        bucket = storage.bucket()
        blob = bucket.blog(fileName + str(picsTaken))
        blob.upload_from_filename(fileName + str(picsTaken) + ".jpg")
        blob.make_public()
        picsTaken += 1
        #process

p = btle.Peripheral("d9:16:66:ba:68:10")
p.setDelegate( MyDelegate(params))

while True:
    if p.WaitForNotifications(1.0):
        continue;
    print("waiting")

