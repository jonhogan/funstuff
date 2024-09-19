"""Generate silly names chosen at random from two lists"""

import random
from colorama import Fore
from colorama import Style



fName = ("Baby Oil", "Bad News", "Big Burps", "Beenie-Weenie",
         "Lady Bug", "Jumbo Jim", "Little John", "Slurmy Slurm",
           "Schlomo", "Red Five", "Gold Leader")
lName = ("Appleyard", "Jones", "Jefferson", "Mugglesworth","Clovenhoof", "Porkins", "Pennywise")

repeat = True
cAnswer =" "

while repeat:

    firstName = random.choice(fName)
    lastName = random.choice(lName)

    print(f"{Fore.RED}{firstName} {lastName}{Style.RESET_ALL}")

    cAnswer = input("Would you like a new name? ").lower()

    if cAnswer in ["no", "n"]:
        repeat = False
