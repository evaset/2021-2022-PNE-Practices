from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

IP = "localhost"
PORT1 = 8000
PORT2 = 8081
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
c1 = Client(IP, PORT1)
c2 = Client(IP,PORT2)
print(c1)
print(c2)

gen = "FRAT1"
msg = Seq()
msg.read_fasta(gen)
c1.send(msg)
c2.send(msg)
print(f"Gene{gen}:{msg}")
n = 1
for frag in msg.fragment(10):
    print(f"Fragment {n}: {frag}")
    if n % 2 == 0:
        c1.talk(f"Fragment {n}: {frag}")
    else:
        c2.talk(f"Fragment {n}: {frag}")
    n += 1


