import random, sys
from tool import Tool, Rock, Paper, Scissors

class AI():
	def __init__(self):
		#self.game = RPSGame()
		print "I am the robot, I am all powerfull."

	def random(self):
		rand= random.randint(0,10000)
		return rand

	def algorithm(self):
		whatever = self.percent_algorithm()
		suggestion = True
		return suggestion

	def percent_algorithm(self):
		game = RPSGame()
		rock_counter = 0.0
		paper_counter = 0.0
		scissors_counter = 0.0
		rock_percent = 0.0
		paper_percent = 0.0
		scissors_percent =0.0
		print "AI IS PRINTING ARRAY", game.get_array()

		counter = 0
		for length in game.get_array():

			print "list length is: ", (counter+1)
			if(game.get_array()[counter]=='r'):
				rock_counter +=1
			elif(game.get_array()[counter]=='p'):
				paper_counter +=1
			elif(game.get_array()[counter]=='s'):
				scissors_counter +=1
			counter +=1

		total_counter = rock_counter + paper_counter + scissors_counter
		if(rock_counter != 0.0):
			rock_percent = (100 * rock_counter)/(total_counter)
			print "Rock Percent: ", rock_percent
		if(paper_counter != 0.0):
			paper_percent = (100* paper_counter)/(total_counter)
			print "Paper Percent: ", paper_percent
		if(scissors_counter != 0.0):
			scissors_percent =  (100* total_counter)
			print "Scissors Percent: ", scissors_percent
		######################PICk Up Where We Left Off #################################### ########################################################################################################################################################################
		if(total_counter >=8):
			if((rock_percent-10.0>=paper_percent) & (rock_percent-10.0>= scissors_percent)):
				rock_time = True
				print "ITS ROCK TIME! "
			else:
				rock_time = false
		percent_suggestion = True
		return percent_suggestion


	def ai_choice(self):
		algorithmDesicion = False
		return algorithmDesicion

	def comp_answer(self):
		no_ai = self.algorithm()
		ai_answer = self.ai_choice()
		if(no_ai==True):
			random =self.random()
			print("here is random number generated: " + str(random))
			if(random <=3333):
				print "rock"
				computer_answer = 'r'
				#call function that adds r to array
			elif (3334<=random<=6666):
				print "paper"
				computer_answer = 'p'
				#call function that adds p to array
			elif(6667<=random<=10000):
				print "scissors"
				computer_answer = 's'
				#call function that adds s to array
			else:
				print "error in computer answer"
			return computer_answer

		else:
			return ai_answer

class RPSGame():
	player_array = []
	def __init__(self):
		self.computer_wins = 0
		self.ties = 0
		self.human_wins = 0
	def	set_array(self,my_list):
		self.player_array = my_list
	def get_array(self):
		return self.player_array


	def player_choice(self):
		valid = False
		while(valid==False):
			pChoice= raw_input("Would you like to play rock, paper, or scissors (r,p,s,e)?: \n")
			if (pChoice == 'r' or pChoice == 'p' or pChoice == 's' or pChoice =='e') :
				if(pChoice =='e'):
					sys.exit(0)
				valid = True

		return pChoice


	def choices(self, theInput):
		if(theInput== 'r'):
			rocky = Rock()
			rocky.set_comp_type('r')
			print "created a new rock object ", rocky
			return rocky
		if(theInput== 'p'):
			papery = Paper()
			papery.set_comp_type('p')
			print "created a new paper object", papery
			return papery
		if(theInput== 's'):
			scissorsy = Scissors()
			scissorsy.set_comp_type('s')
			print "created a new scissors object", scissorsy
			return scissorsy

	def altChoices(self, theInput):
		if(theInput== 'r'):
			rocky = Rock()
			rocky.set_type('r')
			print "created a new rock object ", rocky
			return rocky
		if(theInput== 'p'):
			papery = Paper()
			papery.set_type('p')
			print "created a new paper object", papery
			return papery
		if(theInput== 's'):
			scissorsy = Scissors()
			scissorsy.set_type('s')
			print "created a new scissors object", scissorsy
			return scissorsy

	def data(self,populate):
		print "Human Wins: ", self.human_wins
		print "Computer Wins: ", self.computer_wins
		print "Ties: ", self.ties
		self.player_array.append(populate)
		print "Here are your past moves: ", self.player_array

	def bring_together(self):
		robot = AI()
		playerChoice = self.player_choice()
		computerChoice = robot.comp_answer()
		player = self.altChoices(playerChoice)
		print ("This is player: ", player.get_type())

		computer = self.choices(computerChoice)
		print ("This is computer: ", computer.get_comp_type())

		winLoss = player.fight(computer)
		if(winLoss ==1):
			self.human_wins+=1
			self.data(player.get_type())
		elif(winLoss == 2):
			self.computer_wins +=1
			self.data(player.get_type())
		elif(winLoss == 3):
			self.ties +=1
			self.data(player.get_type())
		else:
			print("comparison failed")
