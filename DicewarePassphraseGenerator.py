#This is a passphrase generator based on the Diceware method of passphrase generation https://diceware.dmuth.org/.

#Import random module and the Diceware Word list dictionary
import random
from DiceDictionary import DiceDict as DD
from DiceDictionary import SymbolList as SL
print("This is a passphrase generator based on the Diceware method of passphrase generation, "
      "\nyou will be asked how long you want your passphrase, and after generation, "
      "\nyou will be asked if you want to add a symbol, and after that if you want to add a number.")

#Ask user how long they want the passphrase to be
lengthInvalid = True
while lengthInvalid:

    Length = input("\nPlease enter how many words long you would like your passphrase \n(between 5-10, Recommended:7): ")
    try:
        if int(Length) >= 5 and int(Length) <= 10:
            lengthInvalid = False
        else:
            print("That is not a valid number.")
    except ValueError:
        print("That is not a number.")
        continue


#Roll 5 dice, add their values to a list (Passwords)
Passwords = []
P = 1
while P <= int(Length): #Stop when there are X words (Defined by user) from the dictionary in the passphrase
    TotalRoll = []
    i = 1
    TR = 0
    TotalRollConcat = ""
    while i <= 5:
        Diceroll = random.randint(1,6)
        TotalRoll.append(Diceroll)
        i += 1
    #Concatenate the Dice rolls
    while TR != 5:
        TotalRollConcat += str(TotalRoll[TR])
        TR += 1
    #Grab the value with your generated key from the dictionary
    Word = DD[int(TotalRollConcat)]
    Passwords.append(Word.capitalize())
    P += 1
#Concatenate the words in the password list
Passphrase = ""
pp = 0
while pp < int(Length):
    Passphrase += str(Passwords[pp])
    pp += 1
print("")
print(Passphrase)

#Check if user wants to add a random symbol/number/caps etc. into the passphrase, or if they want to save it to a text file.
range = len(Passphrase) - 1
char = None
inputInvalid = True
while inputInvalid:
        Symbol = input("\nHere is your passphrase. If you want to make it extra secure, \n"
                       "you can replace a random character with a random symbol \n"
                       "(You may wish to skip this if your generated password already has a symbol). (Y/N): ").lower()

        if Symbol == "y":
           char = random.randint(0, range)
           sym = random.choice(SL)
           Passphrase_list = list(Passphrase)
           Passphrase_list[char] = sym
           Passphrase = "".join(Passphrase_list)
           inputInvalid = False
        elif Symbol == "n":
            inputInvalid = False
        else:
            print("That is not a valid answer")
            continue


print("")
print(Passphrase)

inputInvalid = True
while inputInvalid:
    number = input("\nWould you like to replace a random character with a random number? \n"
                   "(You may wish to skip this if your generated password already has a number). (Y/N): ").lower()
    if number == "y":
        char2 = char
        while char2 == char:
            char2 = random.randint(1, range)
        num = random.randint(0, 9)
        Passphrase_list = list(Passphrase)
        Passphrase_list[char2] = str(num)
        Passphrase = "".join(Passphrase_list)
        inputInvalid = False
    elif number == "n":
        inputInvalid = False
    else:
        print("That is not a valid answer")
        continue

print("""
Here is your passphrase, please write it down and keep it somewhere safe until 
you've memorised it, at which point you should dispose of the written version in a secure manner.\n""")
print(Passphrase)



