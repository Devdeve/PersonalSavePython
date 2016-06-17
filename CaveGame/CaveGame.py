def Questi():
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
		if guessesTaken=="10":
		   print("max number of tries attempted, the cave starts to collapse as you quickly escape")
def Dice():
	print("there are 3 numbers im thinking of. guess the number that they are below in 3 tries")
	value = random.randint(1,6)
	value1 = random.randint(1,6)
	value2 = random.randint(1,6)
	input(guss)
	gusstaken=gusstaken + 1
	if guss>value and guss>value1 and guss>value2:
		print("you guessed my number correctly. well done")

print("Welcome to Fioyra, Land of magic, you are an adventurer exploring, what class do you want to be? Mage, Archer or Warrior?")
Clss=input()
print("ok you are a(n) " + Clss + " Exploring a cave and have 2 options to go, Dice or Question")
cave1=input()
if cave1 == "Dice":
	Dice()
	print("You decide to go into the cave with a question wall in")
	Questi()
	quit
if cave1=="Question":
	Questi()
	print("You decide to go into the cave with dice in")
	Dice()
	quit
else:
    print("you decide questing is not for you and retire to the closest inn")
    quit