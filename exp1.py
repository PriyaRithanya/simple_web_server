from http.server import HTTPServer,BaseHTTPRequestHandler
content = '''<!DOCTYPE html>
<html>
<head>
  <title>TCP/IP Protocol Suite</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 30px;
    }
    table {
      border-collapse: collapse;
      width: 70%;
      margin: auto;
    }
    th, td {
      border: 1px solid #333;
      padding: 10px;
      text-align: center;
    }
    th {
      background-color: #4CAF50;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h2 style="text-align:center;">TCP/IP Protocol Suite</h2>
  <table>
    <tr>
      <th>Layer</th>
      <th>Example Protocols</th>
    </tr>
    <tr>
      <td>Application Layer</td>
      <td>HTTP, FTP, DNS, SMTP, DHCP, Telnet</td>
    </tr>
    <tr>
      <td>Transport Layer</td>
      <td>TCP, UDP</td>
    </tr>
    <tr>
      <td>Internet Layer</td>
      <td>IP, ICMP, ARP</td>
    </tr>
    <tr>
      <td>Network Access Layer</td>
      <td>Ethernet, Wi-Fi, Frame Relay, ATM</td>
    </tr>
  </table>
</body>
</html>'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type","text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
httpd = HTTPServer(server_address,MyServer) 
httpd.serve_forever()       