
def Questi():
    print("You enter the cave and feel a presense around you.")
    print("you continue going in and see a wall with some words on")
    print("the wall reads: you have to guess my number between 1 and 20")
    print("you have 10 tries")
    print("guess my number")
    guessesTaken = 0
    value = random.randint(1, 20)
    while guessesTaken < 10:
        print('Take a guess.')
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < value:
            print('Your guess is too low.')
        if guess > value:
            print('Your guess is too high.')
        if guess == value:
            print("well done you guessed the number correctly")
        if guessesTaken == "10":
            print ("max number of tries attempted")
            print ("the cave starts to collapse as you quickly escape")


def Dice():
    print ("there are 3 numbers im thinking of.")
    print ("guess a number that they are below in 3 tries")
    diceroll1 = random.randint(1, 6)
    diceroll2 = random.randint(1, 6)
    diceroll3 = random.randint(1, 6)
    diceguesstaken = 0
    while diceguesstaken < 3:
        diceguess = input()
        diceguess = int(diceguess)
        diceguesstaken = diceguesstaken + 1
        if diceguess > diceroll1 and diceguess > diceroll2 and diceguess > diceroll3:
            print ("you guessed my number correctly. well done")
        else:
            print("Try again.")
        if diceguesstaken == "3":
            print("Too many guesses taken")
            print ("the cave starts to collapse as you quickly escape")
        
        
print ("Welcome to Fioyra, Land of magic.")
print ("you are an adventurer exploring, what class do you want to be?")
print ("Mage, Archer or Warrior?")
Clss = input()
print("ok you are a(n) " + Clss + " Exploring a cave and have 2 options to go")
print("The two choices you have are Dice or Question")
cave1 = input()
if cave1 == "Dice":
    Dice()
    print("You decide to go into the cave with a question wall")
    Questi()
    quit
if cave1 == "Question":
    Questi()
    print("You decide to go into the cave with dice in")
    Dice()
    quit
else:
    print("you decide questing is not for you and retire to the closest inn")
    quit
