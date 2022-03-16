from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

IP = "localhost"
PORT = 8080
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
c = Client(IP, PORT)
print(c)

gen = "FRAT1"
msg = Seq()
msg.read_fasta(gen)
c.send(msg)
print(f"Gene{gen}:{msg}")
n = 1
for frag in msg.fragment(5):
    c.talk(f"Fragment {n}: {frag}")
    print(f"Fragment {n}: {frag}")
    n += 1

