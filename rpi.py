from bluepy import btle
from bluepy.btle import Scanner, DefaultDelegate
import os
from firebase_admin import credentials, initialize_app, storage


fileName = 'latest'
picsTaken = 0

#p = btle.Peripheral("d9:16:66:ba:68:10")
#p.setDelegate( MyDelegate(params))



class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr == "df:d4:c8:cc:41:d6":
            os.system("fswebcam " + fileName + ".jpg")
            bucket = storage.bucket()
            blob = bucket.blob(fileName + str(picsTaken))
            blob.upload_from_filename(fileName + str(picsTaken) + ".jpg")
            blob.make_public()
            picsTaken += 1
        

scanner = Scanner().withDelegate(ScanDelegate())


while True:
    devices = scanner.scan(10.0)

