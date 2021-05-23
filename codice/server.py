import socket
import sys

server = ("localhost", 8000) 

try:
    gatewayInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    gatewayInterface.bind(server)
    
    print("Server in attesa del gateway...")
    gatewayInterface.listen(1)
    connSocket, addr = gatewayInterface.accept() 
    print("Connessione con gateway stabilita.\n")
except Exception as e:
    print("Errore durante configurazione socket server.")
    print("Err: ",e)
    sys.exit(1)
    
def main():	
    while True:
        try:
            message = connSocket.recv(4096)
        except Exception as e:
            print("Errore ricezione messaggio dal gateway.")
            print("Err: "+e)
            sys.exit(1)
        print(message.decode("utf-8"))

if __name__ == "__main__":
    main()
