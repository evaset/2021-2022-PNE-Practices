from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

gen_list = ["U5", "ADA", "FRAT1"]
for gen in gen_list:
    msg = Seq()
    msg.read_fasta(gen)

    # -- Parameters of the server to talk to
    IP = "10.3.36.225"
    PORT = 8080

    # -- Create a client object
    c = Client(IP, PORT)
    print(c)
    ...
    # -- Send a message to the server
    send = msg.str(str(msg))
    print(f"To server: {send}")
    response = c.talk("Testing!!!")
    print(f"From server: {response}")
    ...


