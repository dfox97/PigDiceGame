from random import randint
class dice:
    def __init__(self):
        self.sides=6
        self.dice_roll=0
    def __str__(self):
        return str(self.dice_roll)
    def roll(self):
        self.dice_roll = randint(1,self.sides)
        return self.dice_roll


class player:
    def __init__(self,playername):
        self.playername=playername
        self.bank=0

    def bank_it(self,add_it):
        self.bank=self.bank+add_it
    
    def get_bank(self):
        return str(self.bank)
    
    def get_name(self):
        return str(self.playername)

def playerMove():
    tmp_total=0
    choice = "Y"
    d=dice()
    while choice == "Y":
        roll_value=d.roll()
        # print(f"\nPlayer, {player1.get_name()} has rolled a {roll_value}")
        if roll_value == 1: 
            print("\nYou have lost your turn because you rolled a 1\n")
            tmp_total = 0
            again='N'
        else:
             print(f"\nPlayer, {player1.get_name()} has rolled a {roll_value}")
             tmp_total +=roll_value
             print(f"Your temporary total is {tmp_total}")
             print(f"Your banked total is {player1.get_bank()}")
             choice=input("Roll again? Y or N: ")
             if choice == 'N':
                 player1.bank_it(tmp_total)
                 print(f"Your banked total is {player1.get_bank()}")
                 
        print('Your turn is over')
    return player1.get_bank()

def computerMove():
    tmp_total=0
    choice = "Y"
    d2=dice()
    while choice == "Y":
        roll_value=d2.roll()
        print(f"\Computer  has rolled a {roll_value}")
        tmp_total +=roll_value

        if roll_value == 1: 
            print("\nComputer lost because it rolled a 1\n")
            tmp_total = 0
            again='N'
        
        if tmp_total < 15:
            print("Comptuer will roll again")
        else:
            print(f"Computer temporary total is {tmp_total}")
            print(f"Computer banked total is {Computer.get_bank()}")
            Computer.bank_it(tmp_total)
            print(f"Computer banked total is {Computer.get_bank()}")
            choice = "N"
    return Computer.get_bank()



    

player1 = player("Dan")
Computer = player("Computer")
p_win = False
c_win = False
d=dice()
roll_value=d.roll()
goal = "20"

while (player1.get_bank()<goal and Computer.get_bank()<goal):
    print("Player banked score is: ",player1.get_bank())
    print("Computer banked score is: ",Computer.get_bank())
    playerMove()
    print("Player banked score is now: ",player1.get_bank())
    if (player1.get_bank()<goal):
        computerMove()
        print("Computer banked score is now: ",Computer.get_bank())
if (player1.get_bank()>Computer.get_bank()):
    print("Player wins!")
else:
    print("Computer wins!")
   

# while (not p_win and not c_win):
#     p_turn=True
#     tmp_total=0

#     roll_value=d.roll()
#     print(f"\nPlayer, {player1.get_name()} has rolled a {roll_value}")
#     if(p_turn==True and roll_value > 1):
#         tmp_total +=roll_value
#         print(f"Your temporary total is {tmp_total}")
#         print(f"Your banked total is {player1.get_bank()}")

#         choice=input("Do you want to roll again? Y or N: \n")
#         if (choice == "Y"):
#             print("\nYou selected to roll again")
#             p_turn = True
#             if (player1.get_bank() >= goal):
#                 print(player1.get_bank())
#                 p_win=True
#         else:
#             #computers turn
#             player1.bank_it(tmp_total)
#             tmp_total = 0
#             p_turn = False

#     else:
#         print("\nYou have lost your turn because you rolled a 1\n")
#         tmp_total=0
#     if (p_turn == False):
#         tmp_total = 0
#         roll_value=d.roll()
#         print("\nComputer rolled ",roll_value)
#         tmp_total = roll_value

#         if(roll_value > 1):
#             Computer.bank_it(tmp_total)
#             tmp_total=0
#             if(Computer.get_bank()>=goal):
#                 print(Computer.get_bank(Y))
#                 c_win = True
#             else:
#                 p_turn = True
#         else:
#             print("\nComputer lost because it rolled a 1\n")

# if(p_win):
#     print(f"Player {player1.get_name()}, you won!")
# if(c_win):
#     print(f"Player {Computer.get_name()}, you won!")