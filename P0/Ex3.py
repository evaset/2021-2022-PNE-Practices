import Seq0
gen_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gen in gen_list:
    seq = Seq0.seq_read_fasta(gen)
    length = Seq0.seq_len(seq)
    print("Gene", gen, "--> Length:", length)
