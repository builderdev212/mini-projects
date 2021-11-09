from random import randint

class ask:
	def __init__(self):
		self.good = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."] # 1 2 3 5 4 3 6 3 4 1 2
		self.maybe = ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."] # 5 5 3 10 1
		self.no = ["My reply is no.", "My sources say no.", "Outlook not so good.", "Don't count on it.", "Very doubtful."] # 2 2 4 5 7
	def choose(self):
		choice = randint(0, 2)
		if choice == 0:
			option = randint(0, 34)
			if option == 0:
				return(self.good[0])
			elif option >= 1 and option <= 2:
				return(self.good[1])
			elif option >= 3 and option <= 5:
				return(self.good[2])
			elif option >= 6 and option <= 9:
				return(self.good[3])
			elif option >= 10 and option <= 14:
				return(self.good[4])
			elif option >= 15 and option <= 18:
				return(self.good[5])
			elif option >= 19 and option <= 21:
				return(self.good[6])
			elif option >= 22 and option <= 27:
				return(self.good[7])
			elif option >= 28 and option <= 30:
				return(self.good[8])
			elif option >= 31 and option <= 34:
				return(self.good[9])
			else:
				print("Error. 8 Ball is out of service.")
				exit()
		elif choice == 1:
			option = randint(0, 23)
			if option >= 0 and option <= 4:
				return(self.maybe[0])
			elif option >= 5 and option <= 9:
				return(self.maybe[1])
			elif option >= 10 and option <= 12:
				return(self.maybe[2])
			elif option >= 13 and option <= 22:
				return(self.maybe[3])
			elif option == 23:
				return(self.maybe[4])
			else:
				print("Error. 8 Ball is out of service.")
				exit()
		elif choice == 2:
			option = randint(0, 19)
			if option >= 0 and option <= 1:
				return(self.no[0])
			elif option >= 2 and option <= 3:
				return(self.no[1])
			elif option >= 4 and option <= 7:
				return(self.no[2])
			elif option >= 8 and option <= 12:
				return(self.no[3])
			elif option >= 13 and option <= 19:
				return(self.no[4])
			else:
				print("Error. 8 Ball is out of service.")
				exit()

if __name__ == "__main__":
	from time import sleep
	running = True
	ask = ask()
	while running == True:
		question = input("What is your question?\n")
		if question != None:
			print(ask.choose())
		else:
			pass
		sleep(0.5)
		repeat = input("Would you like to ask another question? (yes/no)\n")
		if (repeat[0] == "y" or repeat[0] == "Y") and (repeat[1] == "e" or repeat[1] == "E") and (repeat[2] == "s" or repeat[2] == "S"):
			pass
		elif (repeat[0] == "n" or repeat[0] == "N") and (repeat[1] == "o" or repeat[1] == "O"):
			running = False
		else:
			running = False
