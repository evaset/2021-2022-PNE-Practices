from Seq1 import Seq

FILENAME = "U5"
s = Seq()
s.read_fasta(FILENAME)

print(f"Sequence: (Length:{s.len()})", end=" ")
print(f"{s}")
print(f"Bases: {s.count()}")
print(f"Rev: {s.reverse()}")
print(f"Comp: ",end="")
complement_list = s.complement()
for c in complement_list:
    print(c, end="")