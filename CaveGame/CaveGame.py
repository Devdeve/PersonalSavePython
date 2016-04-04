print("Welcome to Fioyra, Land of magic, you are an adventurer exploring, what class do you want to be? Mage, Archer or Warrior?")
Clss=input()
print("ok you are a(n) " + Clss + " Exploring a cave and have 3 options to go, Forward to a darkly lit cave, one with a question mark over or one with a dice over the entrance and another with a sword")
cave1=input()
if cave1 == "Forward":
    print("you get a small tingle down your spine like you are being watched as you walk in to the room slowly")
    print("keep going or escape now?")
    cave11=input()
    if cave11 == "Keep going":
        print("you encounter a dragon sleeping and decide to hit it with your weapon")
        print("the dragon wakes up and you ready to fight")
        print("what type of attack do you want to do? Bash or Slash?")
        Attack1=input()
        if Attack1=="Bash":
            print("You bash the dragon on the head and hit it for 50% health, He shoots you with a fireball hitting you with 20% health damage")
            print("what do you want to do now? Run away or Slash at him")
        if Attack1=="Slash":
            print("You slash the dragon on the wing and hit it for 50% health, He shoots you with a fireball hitting you with 10% health damage")
            print("you slash at him again killing him")            
            print("you slash at the dragon and hit him for 50% of his health killing him, behind him you see 5 gold coins on the ground")
            print("you leave the cave and decide to explore a new cave, You have a choice between two caves, a cave with a dice over it or a cave with a question mark over the entrance. choose between Dice and Question")
            cave111=input()
            if cave111=="Question":
                        print("You enter the cave and feel a presense around you. you continue going in and see a wall with some words on")
                        print("the wall reads: you have to guess my number between 1 and 20, you have 10 tries")
                        print("guess my number")
                        guessesTaken = 0
                        value = random.randint(1,20)
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
                                 print("well done you guessed the number correctly")
                                 print("the wall starts to glow as it opens up revealing 10 gold coins")
                                 print("you have the choice of going forward or going back out of the cave. which one do you choose?")
                                 Cave90=input()
                                 if Cave90=="Forward":
                                     print("you go forward to the new cave")
                                     print("there is a puzzle on the wall")
                                     print("there are 3 numbers im thinking of. guess the number that they are below in 3 tries")
                                     value = random.randint(1,6)
                                     value1 = random.randint(1,6)
                                     value2 = random.randint(1,6)
                                     input(guss)
                                     gusstaken=gusstaken + 1
                                     if guss>value and guss>value1 and guss>value2:
                                          print("you guessed my number correctly. well done")
                                          print("a stone wall starts to move revealing 5 gold coins that you put in your bag")
                                     if gusstaken=="3":
                                          print("max number of tries attempted. you hear as the cave collapses as you exit")
                                 if Cave90=="Go Back":
                                     print("you decide to go back and retire to the inn with your 15 gold peices and decide to stop adventuring for today")
                                     quit
                            
                        if guessesTaken=="10":
                                      print("max number of tries attempted, the cave starts to collapse as you quickly escape")
                                      print("you decide to go to the final cave and see some words on the wall")
                                      print("there are 3 numbers im thinking of. guess the number that they are below in 3 tries")
                                      value = random.randint(1,6)
                                      value1 = random.randint(1,6)
                                      value2 = random.randint(1,6)
                                      guss=input()
                                      gusstaken=gusstaken + 1
                                      if guss>value and guss>value1 and guss>value2:
                                          print("you guessed my number correctly. well done")
                                          print("a stone wall starts to move revealing 5 gold coins that you put in your bag")
                                          print("you decide to stop adventuring for today and relax to the nearest inn")
                                          print("game over, you ended with 10 gold peices")
                                          quit
                                      if gusstaken=="3":
                                          print("max number of tries attempted. you hear as the cave collapses as you exit")
            if cave111=="Dice":
                                      print("there are 3 numbers im thinking of. guess the number that they are below in 3 tries")
                                      value = random.randint(1,6)
                                      value1 = random.randint(1,6)
                                      value2 = random.randint(1,6)
                                      guss=input()
                                      gusstaken=gusstaken + 1
                                      if guss>value and guss>value1 and guss>value2:
                                          print("you guessed my number correctly. well done")
                                          print("a stone wall starts to move revealing 5 gold coins that you put in your bag")
                                      if gusstaken=="3":
                                          print("max number of tries attempted. you hear as the cave collapses as you exit")
                                          
                                      else:
                                          print("you were wrong try again")
                                      print("You enter the final cave and feel a presense around you. you continue going in and see a wall with some words on")
                                      print("the wall reads: you have to guess my number between 1 and 20, you have 10 tries")
                                      print("guess my number")
                                      guessesTaken = 0
                                      value = random.randint(1,20)
                                      while guessesTaken < 10:
                                          print('Take a guess.') # There are four spaces in front of print.
                                          guess = input()
                                          guess = int(guess)
                                          guessesTaken = guessesTaken + 1
                                      if guess > value:
                                             print('Your guess is too low.') # There are eight spaces in front of print
                                      if guess > value:
                                             print('Your guess is too high.')
                                      if guess == value:
                                             print("well done you guessed the number correctly")
                                             print("the wall starts to glow as it opens up revealing 10 gold coins")
                                                
                                                




    if cave11=="Escape":
        print("you escape the cave and decide adventuring is not the type for you, you sit back and relax in the nearest inn")
        print("game over, you retired")
        quit
        





if cave1=="Question":
                        print("You enter the cave and feel a presense around you. you continue going in and see a wall with some words on")
                        print("the wall reads: you have to guess my number between 1 and 20, you have 10 tries")
                        print("guess my number")
                        guessesTaken = 0
                        value = random.randint(1,20)
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
                                 print("well done you guessed the number correctly")
                                 print("the wall starts to glow as it opens up revealing 4 gold coins")
                             
                             if guessesTaken=="10":
                               print("max number of tries attempted, the cave starts to collapse as you quickly escape")
if cave1=="Dice":
                                  print("there are 3 numbers im thinking of. guess the number that they are below in 3 tries")
                                  value = random.randint(1,6)
                                  value1 = random.randint(1,6)
                                  value2 = random.randint(1,6)
                                  input(guss)
                                  gusstaken=gusstaken + 1
                                  if guss>value and guss>value1 and guss>value2:
                                          print("you guessed my number correctly. well done")
                                          print("a stone wall starts to move revealing 5 gold coins that you put in your bag")
                                          print("you see a sword lying on the ground and put it into your holster")
                                          print("do you want to go to the cave with the dice above or the one with a sword above?")
                                          cave211=input()
                                          if cave211=="Dice":
                                                    print("You enter the cave and feel a presense around you. you continue going in and see a wall with some words on")
                                                    print("the wall reads: you have to guess my number between 1 and 20, you have 10 tries")
                                                    print("guess my number")
                                                    guessesTaken = 0
                                                    value = random.randint(1,20)
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
                                                             print("well done you guessed the number correctly")
                                                             print("the wall starts to glow as it opens up revealing 4 gold coins")
                                                     if gusstaken=="3":
                                                             print("max number of tries attempted. you hear as the cave collapses as you exit")
                                              
                                  else:
                                          print("you were wrong try again")

if cave1!="Question" and cave1!="Dice" and cave1!="Forward":
    print("you decide questing is not for you and retire to the closest inn")
    print("game over you scores 0 gold peices")
    quit
                                  
        
