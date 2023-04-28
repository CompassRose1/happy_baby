
title = '''

 .----------------. .----------------. .----------------. .----------------. .----------------.   .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | | .--------------. | .--------------. | .--------------. | .--------------. |
| |  ____  ____  | | |      __      | | |   ______     | | |   ______     | | |  ____  ____  | | | |   ______     | | |      __      | | |   ______     | | |  ____  ____  | |
| | |_   ||   _| | | |     /  \     | | |  |_   __ \   | | |  |_   __ \   | | | |_  _||_  _| | | | |  |_   _ \    | | |     /  \     | | |  |_   _ \    | | | |_  _||_  _| | |
| |   | |__| |   | | |    / /\ \    | | |    | |__) |  | | |    | |__) |  | | |   \ \  / /   | | | |    | |_) |   | | |    / /\ \    | | |    | |_) |   | | |   \ \  / /   | |
| |   |  __  |   | | |   / ____ \   | | |    |  ___/   | | |    |  ___/   | | |    \ \/ /    | | | |    |  __'.   | | |   / ____ \   | | |    |  __'.   | | |    \ \/ /    | |
| |  _| |  | |_  | | | _/ /    \ \_ | | |   _| |_      | | |   _| |_      | | |    _|  |_    | | | |   _| |__) |  | | | _/ /    \ \_ | | |   _| |__) |  | | |    _|  |_    | |
| | |____||____| | | ||____|  |____|| | |  |_____|     | | |  |_____|     | | |   |______|   | | | |  |_______/   | | ||____|  |____|| | |  |_______/   | | |   |______|   | |
| |              | | |              | | |              | | |              | | |              | | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------'   '----------------' '----------------' '----------------' '----------------'

 '''

print(title)

welcome = ('''
    Welcome to 'Happy Baby'!
    ..........................................................................................
    In this game, your goal will be to care for a baby and make the baby as happy as possible.
    The baby's happiness level will be based on its diaper status, hunger, energy, and amusement.
    You will have 10 rounds to care for the baby.
    The baby's diaper will become dirty every three rounds (even if you just changed it), and its other attibutes will gradually decrease over time.
    If at any point, the baby's hunger, energy, or amusement levels reach zero, the game will end and you will lose. Good luck!
    ''')
print(welcome)

# Create Baby class.
class Baby:
    def __init__(self, name):
        self.name = name
        self.clean_diaper = True
        self.full = 6
        self.energy = 6
        self.amusement = 6
        
    def __repr__(self):
        if self.clean_diaper == True:
            return(self.name + " has a clean diaper, fullness level:" + str(self.full) + ", energy level:" + str(self.energy) + ", and amusement level:" + str(self.amusement))
        else:
            return(self.name + " has a dirty diaper, fullness level:" + str(self.full) + ", energy level:" + str(self.energy) + ", and amusement level:" + str(self.amusement))   
    def change_diaper(self):
        self.clean_diaper = True
        print (self.name + "'s diaper has been changed!")
    def feed(self):
        self.full = 11
        print (self.name + " drank the whole bottle!")
    def sleep(self):
        # The baby will only go to sleep if they have a clean diaper, full belly, and low energy.
        if self.clean_diaper and self.full >= 5 and self.energy <=4:
            self.energy = 11
            print(self.name + " had a good nap!")
        # Explain why baby will not got to sleep.
        else:
            problem_string = self.name + " refuses to fall asleep. This is due to: "
            if self.clean_diaper == False:
                problem_string += "dirty diaper, "
            if self.full <5:
                problem_string += "hunger, "
            if self.energy >4:
                problem_string += "too much energy, "
            problem_string = problem_string.strip()
            problem_string = problem_string.strip(",")
            print (problem_string)
    def peekaboo(self):
        self.amusement = 11
        print (self.name + " giggled at your silly antics.")
    # Use baby attibutes to check overall happiness level.
    def check_happiness(self):
        if self.clean_diaper == False:
            haplevel = (self.full + self.energy + self.amusement) / 4
        else:
            haplevel = (self.full + self.energy + self.amusement + 10) / 4
        return haplevel
        
# Create Player class. Goal for future version is for player to have stats that require it to eat, sleep, etc. Additionally, could create a cooperative multiplayer mode.
class Player:
    def __init__(self, name, title):
        self.name = name
        self.title = title

# Get initial player inputs.
baby_name = input("What is your baby's name?")
my_baby = Baby(baby_name)
player_name = input("What is your name?")
player_title = input ("What is your title? You can choose: mother, father, parent, or caregiver.")
my_player = Player(player_name, player_title)

print("Congratulations " + my_player.name + "! You have a new baby named " + my_baby.name + "!")



# Create function for turning player choices into actions that perform care on the baby instance.
def action (choice):
    action_success = False
    while action_success == False:
        # Game can handle inputs with spaces and different cases.
        if choice.strip().lower() == "change diaper":
            my_baby.change_diaper()
            action_success = True
        elif choice.strip().lower() == "give bottle":
            my_baby.feed()
            action_success = True
        elif choice.strip().lower() == "rock to sleep":
            my_baby.sleep()
            action_success = True
        elif choice.strip().lower() == "play peekaboo":
            my_baby.peekaboo()
            action_success = True
        else:
            print("That is not one of the choices. Please try again.")
            choice = input("How would you like to care for " + my_baby.name + "? You can type: 'change diaper', 'give bottle','rock to sleep', or 'play peekaboo'.")
            
        

# Create tracker for highest happiness achieved.
highest_happiness = 0
# Create boolean for losing condition.
lose = False
    
# Iterate through ten rounds.

for count in range (10):
    round_string = "."*20 + "\n" + "Round Number: " + str(count+1) + "\n" + "."*20
    print (round_string)
    # Baby stats decrease over time.
    my_baby.full -= 1
    my_baby.energy -= 1
    my_baby.amusement -= 1
    #Diaper becomes dirty every three rounds.
    if (count+1) % 3 == 0:
        my_baby.clean_diaper = False
    # Give baby stats.
    print(my_baby)
    print(my_baby.name + "'s happiness level is " + str(my_baby.check_happiness()))
    #Check for losing condition
    if my_baby.full <= 0 or my_baby.energy <= 0 or my_baby.amusement <= 0:
        lose=True
        break
    #Collect highest happiness level
    if my_baby.check_happiness() > highest_happiness:
        highest_happiness = my_baby.check_happiness()
    # Get player choice for baby care action each round.
    player_choice = input("How would you like to care for " + my_baby.name + "? You can type: 'change diaper', 'give bottle','rock to sleep', or 'play peekaboo'.")
    # Perform action until the action is successful.
    action(player_choice)

# Give results based on happiness level
if lose == False:
    if highest_happiness >= 7: 
        print("Congratulations! " + my_baby.name + "'s highest happiness was " + str(highest_happiness) + ". You are an excellent " + player_title + ".")
    elif highest_happiness >= 5 and highest_happiness < 7:
        print("Congratulations! " + my_baby.name + "'s highest happiness was " + str(highest_happiness) + ". You are a good " + player_title + ".")
    else:
        print("Congratulations! " + my_baby.name + "'s highest happiness was " + str(highest_happiness) + ". You are an okay " + player_title + ".")
else:
    print("GAME OVER. YOU LOSE.")
    


        

