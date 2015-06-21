import sys

class Tool:
	def get_type(self):
		return type

	def set_type(self, human_choice):
		type = human_choice

class Rock(Tool):
	def __init__(self):
		type = 'r'

	def fight(self):
		rObj = Tool()
		if(rObj.get_type =='s'):
			print ("You Win!!!")
			return 1
		elif(rObj.get_type =='p'):
			print("You Lost")
			return 2
		elif(rObj.get_type =='r'):
			print("You Tied")
			return 3
		else:
			return 0		
	
class Scissors(Tool):
	def __init__(self):
		type = 's'

	def fight(self):
		sObj = Tool()
		if(sObj.get_type =='p'):
			print ("You Win!!!\n")
			return 1
		elif(sObj.get_type =='r'):
			print("You Lost\n")
			return 2
		elif(sObj.get_type =='s'):
			print("You Tied\n")
			return 3
		else:
			return 0		
	
class Paper(Tool):
	def __init__(self):
		type = 'p'

	def fight(self):
		pObj = Tool()
		if(sObj.get_type =='r'):
			print ("You Win!!!\n")
			return 1
		elif(sObj.get_type =='s'):
			print("You Lost\n")
			return 2
		elif(sObj.get_type =='p'):
			print("You Tied\n")
			return 3
		else:
			return 0		