import socketserver
import threading
from multiprocessing import Pool
# import bpy

class renderServer(socketserver.BaseRequestHandler):
    def setup(self):
        return super().setup()

    def handle(self):
            self.recvData = str()
            try:
                print("Success conncetion")
                # To-Do: Write Rendering Code
                # bpy.context.scene.render.filepath = "C:/Project/aaaadaaaaa" + ".png"
                # bpy.ops.render.render(use_viewport = True, write_still=True)

                self.recvData = "completed".encode()

            except NameError as e:
                print("{0} got an error: {1}".format(self.client_address[0], e))

            finally:
                print("{} wrote".format(self.client_address[0])),
                print(self.recvData)

                self.request.sendall(self.recvData.upper())


    def finish(self):
        return super().finish()

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST,PORT), renderServer)
    print("waiting for connection....")

    # threading.Thread Use

    # serverThread = threading.Thread(target=server.serve_forever())
    # serverThread.daemon = True
    # serverThread.start()
    #
    # server.shutdown()
    # server.server_close()

    # Multiprocessing Use

    pool = Pool(processes=3)
    pool.map(server.serve_forever(), range(10))
    pool.close()
    pool.join()
