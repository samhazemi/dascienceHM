# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

	if (user_choice == "r" and computer_choice == "p"):
	   print("You chose rock. The computer chose paper.")
        print("Sorry. You lose.")
	
	elif (user_choice == "s" and computer_choice == "P"):
	   print("You chose Sisors. The computer chose paper.")
        print("You won.")	
	elif (user_choice == "s" and computer_choice == "s"):
	  print("You chose Sisors. The computer chose sisors.")
        print("Tie.")
	elif (user_choice == "p" and computer_choice == "p"):
	  print("You chose paper. The computer chose paper.")
        print("Tie.")
	elif (user_choice == "r" and computer_choice == "r"):
	  print("You chose Rock. The computer chose Rock.")
        print("Tie.")
	else:
	   (user_choice == "r" and computer_choice == "s"):
	   print("You chose rock. The computer chose Sisors.")
        print("You won.")		

# Run Conditionals
