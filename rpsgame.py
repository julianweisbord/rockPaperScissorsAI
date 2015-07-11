import random, sys
from tool import Tool, Rock, Paper, Scissors
from machine import AI

class RPSGame():

	def __init__(self):
		self.computer_wins = 0
		self.ties = 0
		self.human_wins = 0

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
			#print "created a new rock object ", rocky
			return rocky
		if(theInput== 'p'):
			papery = Paper()
			papery.set_comp_type('p')
			#print "created a new paper object", papery
			return papery
		if(theInput== 's'):
			scissorsy = Scissors()
			scissorsy.set_comp_type('s')
			#print "created a new scissors object", scissorsy
			return scissorsy

	def altChoices(self, theInput):
		if(theInput== 'r'):
			rocky = Rock()
			rocky.set_type('r')
			#print "created a new rock object ", rocky
			return rocky
		if(theInput== 'p'):
			papery = Paper()
			papery.set_type('p')
			#print "created a new paper object", papery
			return papery
		if(theInput== 's'):
			scissorsy = Scissors()
			scissorsy.set_type('s')
			#print "created a new scissors object", scissorsy
			return scissorsy
	def winning(self):
		print "Human Wins: ", self.human_wins
		print "Computer Wins: ", self.computer_wins
		print "Ties: ", self.ties

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
			self.winning()
			robot.data(player.get_type())
		elif(winLoss == 2):
			self.computer_wins +=1
			self.winning()
			robot.data(player.get_type())
		elif(winLoss == 3):
			self.ties +=1
			self.winning()
			robot.data(player.get_type())
		else:
			print("comparison failed")
