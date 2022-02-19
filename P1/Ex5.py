from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
base_list = ["A", "C", "T", "G"]


print(f"Sequence 1: (Length:{s1.len()})", end=" ")
print(f"{s1}")
for base in base_list:
    print(str(base) + ":" + f"{s1.count_base(base)}", end=", ")
print(f"\nSequence 2: (Length:{s2.len()})", end=" ")
print(f"{s2}")
for base in base_list:
    print(str(base) + ":" + f"{s2.count_base(base)}", end=", ")
print(f"\nSequence 3: (Length:{s3.len()})", end=" ")
print(f"{s3}")
for base in base_list:
    print(str(base) + ":" + f"{s3.count_base(base)}", end=", ")
