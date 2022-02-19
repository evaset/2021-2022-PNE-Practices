class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        #we jsut return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the lenght of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
    All the objets of class Gene will inherite
    the methods from the Seq class"""
    pass

    def __init__(self, strbases, name=""):
        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

#Main program
#Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
#Create another object of the class Seq
s2 = Seq("CGTAAC")
g = Gene("CGTAAC", "FRAT1")

#printing the objects
print(f"Sequence 1: {s1}")
print(f"    Length:{s1.len()}")
print(f"Sequence 2: {s2}")
print(f"    Length: {s2.len()}")
print(f"Gene: {g}")
print(f"    Length: {g.len()}")