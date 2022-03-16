class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases
        if self.strbases == "NULL":
            print("NULL Seq created")
        if not self.valid_sequence() and not self.strbases == "NULL":
            self.strbases = "ERROR"
            print("INVALID Seq!")
        if self.valid_sequence() and self.strbases != "NULL":
            print("New sequence created!")

    @staticmethod
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence(self):
        valid = True
        i = 0
        while len(self.strbases) > 0 and i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        if self.valid_sequence():
            return len(self.strbases)
        else:
            return "0"

    def count_base(self, base):
        base_count = self.strbases.count(base)
        return base_count

    def count(self):
        d = {"A": 0, "T": 0, "C": 0, "G": 0}
        base = self.strbases
        for c in base:
            try:
                d[c] += 1
            except KeyError:
                pass
        return d

    def reverse(self):
        if self.valid_sequence():
            reverse = self.strbases[::-1]
        else:
            reverse = self.strbases
        return reverse

    def complement(self):
        d = {"A": "T", "T": "A", "C": "G", "G": "C"}
        comp_list = ""
        if self.valid_sequence():
            for c in self.strbases:
                comp_list += d[c]
        else:
            comp_list = self.strbases
        return comp_list

    def read_fasta(self, filename):
        folder = "../Session4/"
        file = filename
        text = open(folder + file + ".txt", "r").read()
        self.strbases = text[text.find("\n"):].replace("\n", "")


    def max_val(self, gen_dict):
        for key, value in gen_dict.items():
            max_val = max(gen_dict.values())
            if value == max_val:
                return key

    def fragment(self, num_base):
        n = 0
        b = num_base
        fragment_list = []
        while len(fragment_list) < b:
            fragment = self.strbases[n:n+10]
            fragment_list.append(fragment)
            n += 10
        return fragment_list

    def percent(self, dict_count):
        total = self.len()
        p = {"A": 0, "T": 0, "C": 0, "G": 0}
        for key,value in dict_count.items():
            p[key] = (int(value) * 100) / int(total)
        return p





