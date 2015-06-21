import random
from tool import Tool, Rock, Paper, Scissors
class RPSGame():
	def random(self):
		rand= random.randint(0,10000)
		return rand

	def player_choice(self):
		pChoice= raw_input("Would you like to play rock, paper, or scissors (r,p,s)?: ")
		return pChoice

	def comp_answer(self):
		random =random()
		print("here is random number generated: "+random)

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
	def choices(self, theInput):
		if(theInput== 'r'):	
			rocky = Tool()
			#rocky.set_type('r')	
			print ("created a new rock "+ rocky.get_type() + "\n")
			return rocky
		if(theInput== 'p'):	
			papery = Tool()
			#papery.set_type('p')	
			print ("created a new paper  "+ papery.get_type() + "\n")
			return papery
		if(theInput== 's'):	
			scissorsy = Tool()
			#scissorsy.set_type('s')	
			print ("created a new scissors "+ scissorsy.get_type() + "\n")
			return scissorsy

	def bring_together(self):
		print("in bring together!")
		playerChoice = player_choice()
		computerChoice = comp_answer()
		player = choices(playerChoice)
		computer = choices(computerChoice)

		winLoss = player.fight(computer)
		if(winLoss ==1):
			human_wins+=1
		elif(winLoss == 2):
			computer_wins +=1
		elif(winLoss == 3):
			ties +=1	
		else:
			print("comparison failed")	
		data()	 	
	def data(self):
		print("Human Wins: "+ human_wins+ "\n")
		print("Computer Wins: "+ computer_wins+ "\n")
		print("Ties: "+ ties + "\n")
		#need function that takes number of wins, losses, ties and adds them based on fight function

					
			
