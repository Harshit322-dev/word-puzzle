import http.server
import socketserver
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import webbrowser

PORT = 3000

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, server):
        self.server = server

    def on_modified(self, event):
        if not event.is_directory:
            print(f"\nफ़ाइल में बदलाव: {event.src_path}")
            print("सर्वर को रीस्टार्ट किया जा रहा है...")
            self.server.shutdown()
            self.server.server_close()
            start_server()

def start_server():
    global server
    Handler = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer(("", PORT), Handler)
    
    # फ़ाइल चेंज ऑब्जर्वर सेटअप
    event_handler = FileChangeHandler(server)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    
    print(f"\nसर्वर पोर्ट {PORT} पर चल रहा है")
    print(f"वेबसाइट देखने के लिए इस लिंक पर जाएं: http://localhost:{PORT}")
    print("\nफ़ाइलों में बदलाव की निगरानी की जा रही है...")
    print("सर्वर को बंद करने के लिए Ctrl+C दबाएं")
    
    # ब्राउज़र में वेबसाइट खोलें
    webbrowser.open(f'http://localhost:{PORT}')
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        observer.stop()
        server.shutdown()
        server.server_close()
        print("\nसर्वर बंद हो गया है")

if __name__ == "__main__":
    start_server() 