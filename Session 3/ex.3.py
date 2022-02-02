def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for c in seq:
        d[c] += 1
    return d

with open("seq.txt", "r") as f:
    seq = f.readlines()
    for s in seq:
        new_seq = s.replace("\n", "")
        print("Total length", len(new_seq))
        for k, v in count_bases(new_seq).items():
            print(k + ":", v)

