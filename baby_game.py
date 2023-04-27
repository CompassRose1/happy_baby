
#To do: Add more care functions including feed, rock to sleep, and play peekaboo. Add check to see if player wins.

# Create Baby class.
class Baby:
    def __init__(self, name):
        self.name = name
        self.clean_diaper = False
        self.hunger = 5
        self.energy = 5
        self.amusement = 5
        
    def __repr__(self):
        if self.clean_diaper == True:
            return(self.name + " has a clean diaper, hunger level:" + str(self.hunger) + ", energy level:" + str(self.energy) + ", and amusement level:" + str(self.amusement))
        else:
            return(self.name + " has a dirty diaper, hunger level:" + str(self.hunger) + ", energy level:" + str(self.energy) + ", and amusement level:" + str(self.amusement))   
    def change_diaper(self):
        self.clean_diaper = True
        print (self.name + "'s diaper has been changed!")
    def check_happiness(self):
        if self.clean_diaper == False:
            haplevel = (self.hunger + self.energy + self.amusement) / 4
        else:
            haplevel = (self.hunger + self.energy + self.amusement + 10) / 4
        return haplevel
        
# Create Player class.
class Player:
    def __init__(self, name, title):
        self.name = name
        self.title = title

# Get initial player inputs.
baby_name = input("What is your baby's name?")
my_baby = Baby(baby_name)
player_name = input("What is your name?")
player_title = input ("What is your title? You can choose: Mother, Father, Parent, or Caregiver.")
my_player = Player(player_name, player_title)

print("Congratulations " + my_player.name + "! You have a new baby named " + my_baby.name + "!")

# Give initial baby stats.
print(my_baby)
print(my_baby.name + "'s happiness level is " + str(my_baby.check_happiness()))


# Create round in which baby stats decrease and player can perform baby care functions.
def round (choice):
    my_baby.hunger -= 1
    my_baby.energy -= 1
    my_baby.amusement -= 1
    if choice == "change diaper":
        my_baby.change_diaper()
        print(my_baby.clean_diaper)
    else:
        print("That is not one of the choices. Please try again.")
    
# Iterate through ten rounds.

for count in range (10):
    #Diaper becomes dirty every three rounds.
    if count % 3 == 0:
        my_baby.clean_diaper = False
    player_choice = input("How would you like to care for " + my_baby.name + "? You can: change diaper.")
    round(player_choice)
    print(my_baby)
    print(my_baby.name + "'s happiness level is " + str(my_baby.check_happiness()))
    if my_baby.check_happiness() <= 0:
        print("You lose")


        

