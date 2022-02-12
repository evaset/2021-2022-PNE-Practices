import Seq0
filename = Seq0.valid_filename()
print("DNA file:", str(filename)+".txt")
sequence = Seq0.seq_read_fasta(filename)
print("The first 20 bases are:", sequence[:20])


