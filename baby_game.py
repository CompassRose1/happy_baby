class Baby:
    def __init__(self, name):
        self.name = name
        self.haplevel = 5
        self.clean_diaper = False
        self.hunger = 5
        self.energy = 5
        self.amusement = 5
    def change_diaper(self):
        self.clean_diaper = True
        print (self.name + "'s diaper has been changed!")

baby_name = input("What is your baby's name?")
my_baby = Baby(baby_name) 
    
