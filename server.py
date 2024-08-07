import socket
import threading
from map import Maps
from final_project import ServiceManager
from main import MechanicManager
from grage2 import GarageMananger



class SocketServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.map = Maps()
        self.map.read_json()
        self.servis_manager = ServiceManager().load(self.map)
        self.mechanic_manager = MechanicManager().load(self.map)
        self.garage_manager = GarageMananger().load(self.map)
    def start(self):
        server_host = socket.gethostbyname(socket.gethostname())
        print(f"Server running on {server_host}")
        server_port = 18080
        self.server_socket.bind(("192.168.90.80", server_port))
        self.server_socket.listen(5)
        print(f"Listening on port {server_port}")

        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def handle_client(self, conn, addr):
        print(f"[New connection] {addr} connected.")
        connected = True
        while connected:
            user = conn.recv(1024).decode()
            user = user.split(',')
            user_name = user[0]
            user_id = user[1]
            user_x = user[2]
            user_y = user[3]
            user_service = user[4]
            current_user = self.userManager.add_member(user_name, user_id, user_x, user_y, user_service)

            req = conn.recv(1024).decode()
            if req == '1' :
                mechanic, distance = self.mechanic_manager.find_mechanic_drone(user_x, user_y)
                
                service_string = mechanic.get_arrival_time(distance).encode()
                service = service()
                mechanic.set_service(service)
                self.service_manager.add_service(service)

            elif req =='2':
                mechanic, distance = self.mechanic_manager.find_mechanic_direct(user_x, user_y)
                service_string = mechanic.get_arrival_time(distance).encode()
                service = service()
                mechanic.set_service(service)
                self.service_manager.add_service(service)

            elif req == '3':
                mechanic, distance = self.mechanic_manager.find_mechanic_indirect(user_x, user_y)
                service_string = mechanic.get_arrival_time(distance).encode()
                service = service()
                mechanic.set_service(service)
                self.service_manager.add_service(service)
                
            elif req == '4':
                list_service = []
                for i in range(len(current_user.get_service())):
                    list_service.append(current_user.get_service().str())
                service_string = ",".join(list_service).encode()


            conn.sendall(service_string)
               

            if user == "finish":
                connected = False
           
        conn.close()

if __name__ == "main":
    server = SocketServer()
    server.start()