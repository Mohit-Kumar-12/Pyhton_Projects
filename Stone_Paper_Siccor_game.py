import random

def game_winner(comp,you):
    if comp==you:
        return None
    elif comp=='stone':
        if you=='siccor':
            return False
        elif you=='paper':
            return True     
    elif comp=='paper':
        if you=='stone':
            return False
        elif you=='siccor':
            return True     
    elif comp=='siccor':
        if you=='paper':
            return False
        elif you=='stone':
            return True     

comp=("comp Turn: Stone, Paper or Siccor ?\n")
automatic=random.randint(1,3)
if automatic==1:
    comp='stone'
elif automatic==2:
    comp='paper'
elif automatic==3:
    comp='siccor'


you=input("your Turn: stone, paper or siccor ?\n")

a=game_winner(comp,you)

print(f"Computer selected {comp}")
print(f"Player selected {you}")

if a==None:
    print("The gsme is tie !")
elif a:
    print("You won the game.")
else:
    print("You loss the game.")
