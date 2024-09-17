import sys, random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

fName = ("Baby Oil", "Bad News", "Big Burps", "Beenie-Weenie",
         "Lady Bug", "Jumbo Jim", "Little John", "Slurmy Slurm", "Schlomo", "Red Five", "Gold Leader")
lName = ("Appleyard", "Jones", "Jefferson", "Mugglesworth","Clovenhoof", "Porkins", "Pennywise")

repeat = True
continueAnswer =" "

while(repeat):

    firstName = random.choice(fName)
    lastName = random.choice(lName)

    print(f"{Fore.RED}{firstName} {lastName}{Style.RESET_ALL}")

    continueAnswer = input("Would you like a new name? ").lower()

    if continueAnswer in ["no", "n"]:
        repeat = False




