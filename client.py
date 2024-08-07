import socket  

class Client:   
    def __init__(self) -> None:  
        self.server_game = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

    def connect(self, ip, port):    
        self.server_game.connect((ip, port))  

        user = input('Username: ')  
        user_code = input('Code Meli: ')  
        X = input('X: ')   
        Y = input('Y: ')  
        request = input('Chi Mikay: ')          
        requests = f"{user},{user_code},{X},{Y},{request}"  
        
        self.server_game.sendall(requests.encode())  
        
        response1 = self.server_game.recv(1024).decode()  
        print(response1)  

        choes = input("""  
        1 - Benzin  
        2 - Thamir  
        3 - Ghatat  
        4 - List Request  
        """).strip()  
        
        self.server_game.sendall(choes.encode())  
        response2 = self.server_game.recv(1024).decode()  
        print(response2)  

        self.server_game.close()   

if __name__ == "__main__":  
    client = Client()   
    client.connect('172.17.48.1', 12345)