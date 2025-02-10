import lib_coasterimg as coasterimg
import time
import os
#test
#een nieuwe regel
# git commit -m "rollercoaster-check-Mo"
# Read check values
file1 = open("rules/age.txt", "r")
age_check = int(file1.read())
file1.close()

file2 = open("rules/height.txt", "r")
height_check = int(file2.read())
file2.close()  # Correcte wijziging: file2.close() in plaats van file1.close()

running = True
while running:

    # Get inputs
    os.system('cls')
    print("Rollercoaster-check™")
    age = input("Voer leeftijd in: ")
    height = input("Voer lengte in: ")
    age = int(input("Voer leeftijd in: "))
    height = int(input("Voer lengte in: "))

    # Process checks
    if(age > age_check and height > height_check):
        os.system('cls')
        print("Stap maar in!")
        print(coasterimg.get())
        time.sleep(1)  # Pauze van 1 seconde in plaats van 2

    else:
        os.system('cls')
        print("Je voldoet niet aan de voorwaarden...")
        print(coasterimg.sad())
        time.sleep(1)  # Pauze van 1 seconde in plaats van 2

    result = input("Druk op Enter om nog een keer te checken, of Q om te stoppen\n\n")
    if(result.upper() == "Q"):
        running = False

