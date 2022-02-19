from Seq1 import Seq

gen_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for gen in gen_list:
    s = Seq()
    s.read_fasta(gen)
    gen_dict = s.count()
    max_val = s.max_val(gen_dict)
    print("Gene", str(gen) + ": Most frequent Base:", max_val)

