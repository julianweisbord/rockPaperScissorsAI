import sys
import tool
import RPSGame

answer = 'y'

while(answer == 'y'):
	#function call

	answer = raw_input("Would you like to play again(y or n)?")
	if(answer!='y'):
		print("exited")
		sys.exit(0)