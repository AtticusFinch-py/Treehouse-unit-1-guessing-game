import random

def start_game():
	name = input("What is your name? ")
	print("Welcome to the guessing game, {}!".format(name))

	correct_answer = random.randrange(1, 11)

	attempts = 0
	


	while True:
		try:
			user_guess = int(input("Please pick a number between 1 and 10: "))

			if user_guess <=0 or user_guess >10:
				print("Sorry, the number must be between 1 and 10. Try again...")

		except ValueError:
			print("Please enter an integer")

		else:
			attempts += 1

			if user_guess == correct_answer:
				print("You got it! It only took you {} attempts".format(attempts))
				play_again = input("Would you like to play again? [y/n]: ".lower())
				

				while play_again == "y":
					correct_answer = random.randrange(1, 11)		
				
				
			elif user_guess > correct_answer:
				print("Guess lower")
				continue

			elif user_guess < correct_answer:
				print("Guess higher")
				continue

	return attempts
	
start_game()

