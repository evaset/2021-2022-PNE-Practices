import Seq0
gen_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list = ["A", "C", "T", "G"]
for gen in gen_list:
    seq = Seq0.seq_read_fasta(gen)
    print("Gene" + str(gen) + ":")
    for base in base_list:
        count_base = Seq0.seq_count_base(seq, base)
        print(str(base) + ":", count_base)
