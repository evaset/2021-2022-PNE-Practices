import Seq0
gen_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gen in gen_list:
    seq = Seq0.seq_read_fasta(gen)
    gen_dict = Seq0.seq_count(seq)
    max_val = Seq0.max_val(gen_dict)
    print("Gene", str(gen) + ": Most frequent Base:", max_val)

