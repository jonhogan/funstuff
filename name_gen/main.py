import sys, random

fName = ("Baby Oil", "Bad News", "Big Burps", "Beenie-Weenie",
         "Lady Bug", "Jumbo Jim", "Little John", "Slurmy Slurm", "Schlomo", "Red Five", "Gold Leader")
lName = ("Appleyard", "Jones", "Jefferson", "Mugglesworth","Clovenhoof", "Porkins", "Pennywise")


firstName = random.choice(fName)
lastName = random.choice(lName)

print(firstName + " " + lastName)
