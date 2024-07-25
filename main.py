import random

comp = random.choice([1, 0, -1])

youstr = input("Enter the choice (S for Snake, G for Gun, W for Water): ")
youDict = {"S": 1, "G": 0, "W": -1}
reverseDict = {1: "S", 0: "G", -1: "W"}

# Convert the user's choice to the corresponding value
you = youDict[youstr]


print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[comp]}")

if comp == you:
    print("It's a draw")
else:
    if (comp == 1 and you == -1) or (comp == 0 and you == 1) or (comp == -1 and you == 0):
        print("You lose")
    else:
        print("You win")
