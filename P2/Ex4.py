from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

IP = "localhost"
PORT = 8080
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
c = Client(IP, PORT)
print(c)

gen_list = ["U5", "ADA", "FRAT1"]
for gen in gen_list:
    msg = Seq()
    msg.read_fasta(gen)
    # -- Send a message to the server
    c.send(msg)
    c.debug_talk(f"Sending {gen} Gene to the server...")
    
    ...


