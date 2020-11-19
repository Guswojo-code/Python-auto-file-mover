from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time
from fileinput import filename

class MyHandler(FileSystemEventHandler):
    print ("1")
    def on_modified(self, event):
        
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)
           

folder_to_track = "C:\\Users\\Gustav\\Downloads\\AltSomSkalFlyttesOverPåTranscend"
folder_destination = "C:\\Users\\Gustav\\Documents\\Overførsler"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
print ("2")

try:
        while True:
            time.sleep(10)

except KeyboardInterrupt:
    print ("DONE!")
    observer.stop()
observer.join()

