import os
import subprocess
import time
import threading
from watchdog.observers import Observer

from models.plugin_handler import PluginHandler

def watch_plugins():
    observer = Observer()
    event_handler = PluginHandler()
    observer.schedule(
        event_handler,
        os.environ.get("PLUGIN_FOLDER"),
        recursive=True
    )
    observer.start()
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    watch_plugins()