from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a test'}
# host = ('localhost', 8888)
host = ('0.0.0.0', 8888)


class Resquest(BaseHTTPRequestHandler):

    # def handler(self):
    #     print("data:", self.rfile.readline().decode())
    #     self.wfile.write(self.rfile.readline())
    # 捕捉get请求 并返回响应

    def do_GET(self):
        # print("data:", self.rfile.readline().decode())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
        # 获取请求头长度 带入请求头
        # 重点在此步!
        # req_datas = self.rfile.read(int(self.headers['content-length']))
        # print(req_datas.decode())
        print(self.headers)
        # self.headers['content-length']
        # print(111,   self.rfile.readline())


if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
