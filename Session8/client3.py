import socket

# SERVER IP, PORT
PORT = 8000
IP = "localhost"

while True:
  # -- Ask the user for the message
    msg = input("Introduce your message in the chat:")
  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(str.encode(msg))
  # -- Close the socket
    s.close()