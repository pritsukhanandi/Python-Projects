import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

computer = random.choice([-1, 0, 1])

yourStr = input("Enter your choice (s/w/g): ").lower()

yourDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# Input validation
if yourStr not in yourDict:
    print("Invalid choice!")
    exit()

you = yourDict[yourStr]

print(f"\nYou chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}\n")

# Game logic
if computer == you:
    print("It's a Draw!")

elif (
    (you == 1 and computer == -1) or
    (you == 0 and computer == 1) or
    (you == -1 and computer == 0)
):
    print("You Win!")

else:
    print("You Lose!")
