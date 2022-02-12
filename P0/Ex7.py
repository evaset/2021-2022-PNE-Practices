import Seq0
filename = "U5"
sequence = Seq0.seq_read_fasta(filename)
print("Gene", str(filename) + ":")
print("Frag:", sequence[:20])
complement = Seq0.seq_complement(sequence[:20])
print("Comp: ", end="")
for c in complement:
    print(c, end="")