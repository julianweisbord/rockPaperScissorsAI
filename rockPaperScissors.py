import sys
from tool import Tool, Rock, Paper, Scissors
from RPSGame import RPSGame

answer = 'y'
play = RPSGame()
while(answer == 'y'):
	#function call
	play.bring_together()
	answer = raw_input("Would you like to play again(y or n)?")
	
	if(answer!='y'):
		print("exited")
		sys.exit(0)