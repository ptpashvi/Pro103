import sys
import time
import random
import os
import shutil

#watchdog modules
from watchdog.observers import Observer
#parent class
from watchdog.events import FileSystemEventHandler

from_directory = "/Users/kalpeshpatel/Desktop/Python"
to_directory = "/Users/kalpeshpatel/Desktop/destination"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.scr_path} has been created!")
    def on_deleted(self, event):
        print(f"Oops! Someone Deleted {event.scr_path}!")
        
event_handler=FileMovementHandler()

observer=Observer()
observer.schedule(event_handler, from_directory,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()