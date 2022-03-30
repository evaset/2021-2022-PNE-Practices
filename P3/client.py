from Client0 import Client

PRACTICE = 3
EXERCISE = 7

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 6123

# -- Create a client object
c = Client(IP, PORT)
print(c)
...
# -- Send a message to the server
print(" * Testing PING...")
msg = c.talk("PING")
print(msg[0])

print(" * Testing GET...")
msg = c.talk("GET 0")
print("GET 0:", msg[0])
seq = msg[0]
msg = c.talk("GET 1")
print("GET 1:", msg[0])
msg = c.talk("GET 2")
print("GET 2:", msg[0])
msg = c.talk("GET 3")
print("GET 3:", msg[0])
msg = c.talk("GET 4")
print("GET 4:", msg[0],"\n")

print(" * Testing INFO...")
msg = c.talk(f"INFO {seq}")
print(msg[0])

print(" * Testing COMP...")
msg = c.talk(f"COMP {seq}")
print("COMP:", msg[0],"\n")

print(" * Testing REV...")
msg = c.talk(f"REV {seq}")
print("REV:", msg[0],"\n")

print(" * Testing GENE...")
for gene in gene_list:
    msg = c.talk(f"GENE {gene}")
    print(f"GENE {gene}","\n", msg[0], "\n")

print(" * Testing OPE...")
msg = c.talk(f"OPE ACGTACGt")
print(msg[0])
