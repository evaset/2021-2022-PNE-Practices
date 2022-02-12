def seq_ping():
    print("Testing the seq_ping() funcion")
    print("OK")

def valid_filename():
    exit = False
    while not exit:
        filename = input("What file do you want to open?: ")
        try:
            folder = "../Session4/"
            file = filename
            f = open(folder + file + ".txt", "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File does not exist. Provide another file")

def seq_read_fasta(filename):
    folder = "../Session4/"
    file = filename
    text = open(folder + file + ".txt", "r").read()
    text = text[text.find("\n"):].replace("\n", "")
    return text

def seq_len(seq):
    count = 0
    for e in seq:
        count += 1
    return count

def seq_count_base(seq, base):
    base_count = seq.count(base)
    return base_count

def seq_count(seq):
    d = {"A": 0, "T": 0, "C": 0, "G": 0}
    for c in seq:
        d[c] += 1
    return d

def seq_reverse(seq):
    seq = seq[::-1]
    return seq

def seq_complement(seq):
    d = {"A": "T", "T":"A", "C":"G", "G":"C"}
    comp_list = []
    for c in seq:
        comp_list.append(d[c])
    return comp_list

def max_val(gen_dict):
    for key, value in gen_dict.items():
        max_val = max(gen_dict.values())
        if value == max_val:
            return key