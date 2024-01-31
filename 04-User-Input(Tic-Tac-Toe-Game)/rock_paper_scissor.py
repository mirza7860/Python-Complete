import sys
import random
from enum import Enum


class Rock_Paper_Scissor(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# sys.exit()
playerchoice = input("Enter...\n1 for Rock,\n2 for paper,\n3 for scissor\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")


computerchoice = random.choice("123")

computer = int(computerchoice)


print("you choose " + str(Rock_Paper_Scissor(player)
                          ).replace("Rock_Paper_Scissor.", "") + ".")


print("Python chooses " + str(Rock_Paper_Scissor(computer)
                              ).replace("Rock_Paper_Scissor.", "") + ".")


if player == 1 and computer == 3:
    print(" 🎉 You win !")
elif player == 2 and computer == 1:
    print(" 🎉 You win !")
elif player == 3 and computer == 2:
    print(" 🎉 You win !")
elif player == computer:
    print(" 😴 Tie game !")
else:
    print(" 😁 Python wins !")
