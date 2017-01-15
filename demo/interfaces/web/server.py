from http import server
import os


webdir = '.'
port = 8888

os.chdir(webdir)
srvaddr = ('', port)
srv = server.HTTPServer(srvaddr, server.CGIHTTPRequestHandler)
srv.serve_forever()
