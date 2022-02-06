from bluepy import btle
import os
from firebase_admin import credentials, initialize_app, storage


fileName = 'latest'
picsTaken = 0

#p = btle.Peripheral("d9:16:66:ba:68:10")
#p.setDelegate( MyDelegate(params))


scanner = Scanner().withDelegate(ScanDelegate())


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr == "d9:16:66:ba:68:10":
            os.system("raspistill -o " + filename + str(picsTaken) + ".jpg")
            bucket = storage.bucket()
            blob = bucket.blog(fileName + str(picsTaken))
            blob.upload_from_filename(fileName + str(picsTaken) + ".jpg")
            blob.make_public()
            picsTaken += 1
        

scanner = Scanner().withDelegate(ScanDelegate())


while True:
    devices = scanner.scan(10.0)

