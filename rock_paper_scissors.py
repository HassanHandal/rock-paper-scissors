#start the game
user = input("Hello, What's your name? : ")
print(f"Please select your move {user} as shown in choieces : \n1- r for rock \n2- p for paper \n3- s for scissors")
#ask the player to select his move
user_move = input("enter your move : ")
#make the pc choose random move
import random
pc_move = random.choice(["r", "p", "s"])
print(f"You chose {user_move} and I chose {pc_move} so :")
#if user = r pc = s or user = p pc = r user = s pc = p
# player win
#if else player lose
if user_move == pc_move :
    print("it's a tie!")
elif (user_move == "r" and pc_move == "s") or (user_move == "p" and pc_move == "r") or (user_move == "s" and pc_move == "p"):
    print("You are a Winner, Congratulations")
else:
    print("You are a looser, good luck")