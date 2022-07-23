import random

# snake water gun game
def game(comp, you):
    #If two values are equal, declare a tie!
    if comp == you:
        return None

    #check for all possibilaties when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
            
     #check for all possibilaties when computer chose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True 

     #check for all possibilaties when computer chose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True 

randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn: Snake(1) Water(2) or Gun(3)?")
a = game(comp, you)

print(f"Computer chose{comp}")
print(f"you chose{you}")

if a == None:
    print("The game is a Tie!")
elif a:
    print("You win!")
else:
    print("You lose!")