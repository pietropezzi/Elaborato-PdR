import socket

deviceInterface = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
deviceInterface.bind(("", 8200))

serverInterface = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverInterface.bind(("", 8100))
while True:
	print("listening...")
	message = deviceInterface.recv(1024)
	print(message.decode("UTF-8"))