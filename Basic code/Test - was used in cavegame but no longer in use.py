import random
print("choose between 'Guess the number', 'Hello World' and 'Dice Thrower'")
Choice=input()
if Choice=="Hello World": 
    print("What is your name")
    name=input()
    print("hello "+ name +" this is a test program")
    print(name+",what is your favourite colour?")
    colour=input()
    print("and your age?")
    age=input()
    print("Hello "+name+" you are "+age+ " years old and your favourite colour is "+ colour+" this is my first program written in python")
quit
if Choice=="Dice Thrower":
    print("roll the dice, choose how many dices you want thrown betweeen 1-3")
    value = random.randint(1,6)
    value1 = random.randint(1,6)
    value2 = random.randint(1,6)
    Dicethrown=input()
    if Dicethrown=="1":    
        print(value)
    if Dicethrown=="2":
        print(value)
        print(value1)
    if Dicethrown=="3":
        print(value)
        print(value1)
        print(value2)
if Choice=="Guess the number":
    print("Guess the number game, Choose your difficulty, Easy, Medium or Hard")
    Diff=input()
    if Diff=="Easy":
            guessesTaken = 0
            value = random.randint(1,10)
            print("I am thinking of a number between 1 and 10, you have 5 tries")
            while guessesTaken < 5:
                     print('Take a guess.') # There are four spaces in front of print.
                     guess = input()
                     guess = int(guess)
                     guessesTaken = guessesTaken + 1
                     if value + 5 > guess and value - 5 < guess and value != guess:
                         print("wrong but close")
                     if guess < value:
                         print('Your guess is too low.') # There are eight spaces in front of print.
                     if guess > value:
                         print('Your guess is too high.')
                     if guess == value:
                         print("well done you guessed my number")
                         break
            else:
                 print("max number of tries attempted")            
    if Diff=="Medium":
            guessesTaken = 0
            value = random.randint(1,15)
            print("I am thinking of a number between 1 and 10, you have 15 tries")
            while guessesTaken < 10:
                     print('Take a guess.') # There are four spaces in front of print.
                     guess = input()
                     guess = int(guess)
                     guessesTaken = guessesTaken + 1
                     if guess < value:
                         print('Your guess is too low.') # There are eight spaces in front of print.
                     if guess > value:
                         print('Your guess is too high.')
                     if guess == value:
                         print("well done you guessed my number")
                         break
            else:
                 print("max number of tries attempted")
    if Diff=="Hard":
            guessesTaken = 0
            value = random.randint(1,20)
            print("I am thinking of a number between 1 and 20, you have 10 tries")
            while guessesTaken < 10:
                     print('Take a guess.') # There are four spaces in front of print.
                     guess = input()
                     guess = int(guess)
                     guessesTaken = guessesTaken + 1
                     if guess < value:
                         print('Your guess is too low.') # There are eight spaces in front of print.
                     if guess > value:
                         print('Your guess is too high.')
                     if guess == value:
                         print("well done you guessed my number")
                         break
            else:
                 print("max number of tries attempted")
    quit
