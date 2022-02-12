import Seq0
filename = "U5"
sequence = Seq0.seq_read_fasta(filename)
print("Gene", str(filename) + ":")
print("Frag:", sequence[:20])
reverse = Seq0.seq_reverse(sequence[:20])
print("Rev:", reverse)