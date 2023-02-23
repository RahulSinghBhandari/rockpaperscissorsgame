import random

player = input("Enter name : ")
print(f"Welcome {player} !!, to the game of Rock, Paper and Scissors !")
print ("Please go through the Rules & Instructions : \n R= Rock \n P = Paper \n S = Scissors \n ROCK smashes SCISSOR \n SCISSOR cuts PAPER \n PAPER covers ROCK")

ua = input("Enter a choice (R,P,S) : ")
pa = ["R", "P", "S"]
ca = random.choice(pa)
print(f"You chose {ua} \n Computer chose {ca}")

if ua == ca :
    print (f"Both players selected {ua}. It's a tie!")
elif ua == "R" :
     if ca == "S" :
        print("Rock smashes Scissors. Conratulations, You win !!")
     else :
        print("Paper covers Rock. You lose, Better luck next time !")
elif ua == "P" :
    if ca == "R" :
        print("Paper covers Rock. Conratulations, You win !!")
    else :
        print ("Scissor cuts Paper. You lose, Better luck next time ! ")
elif ua == "S" :
    if ca == "P" :
        print("Scissor cuts Paper. Conratulations, You win !!")
    else :
        print("Rock smashes Scissors. You lose, Better luck next time ! ")

