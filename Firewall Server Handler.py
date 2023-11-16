# www.theforage.com - Telstra Cyber Task 3
# Firewall Server Handler


from http.server import BaseHTTPRequestHandler, HTTPServer


host = "localhost"
port = 8000


#########
# Handle the response here 


#########




class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()


    def do_POST(self):
        self.handle_request()
    
    def handle_request(self):
        if self.path == '/tomcatwar.jsp' or self.has_blocked_headers():
            self.block_request()
        else:
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
    
    def has_blocked_headers(self):
        blocked_headers = [
            "suffix=%>//",
            "c1=Runtime",
            "c2=<%",
            "DNT=1",
            "Content-Type=application/x-www-form-urlencoded"
        ]
        for header in blocked_headers:
            if header not in self.headers:
                return False
        return True 
    
    def block_request(self):
        self.send_response(403)
        self.send_header('content-type','text/plain')
        self.end_headers()
        self.wfile.write(b'Access denied: Blocked request')


if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))


    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)