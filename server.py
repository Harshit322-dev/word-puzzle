import http.server
import socketserver

PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"सर्वर पोर्ट {PORT} पर चल रहा है")
    print(f"वेबसाइट देखने के लिए इस लिंक पर जाएं: http://localhost:{PORT}")
    httpd.serve_forever()
