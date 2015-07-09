import sys

class Tool(object):
	user_array = []
	def __str__(self):
		return self.type

	def get_type(self):
		return self.type

	def set_type(self, human_choice):
		self.type = human_choice

	def get_comp_type(self):
		return self.comp_type

	def set_comp_type(self, comp_choice):
		self.comp_type = comp_choice

	def fight(self, computer):
			super(Tool, self).__init__()

class Rock(Tool):
	def __init__(self):
		super(Rock, self).__init__()
		self.type = 'r'

	def fight(self,computer):
		#rObj = Tool()
		if(computer.comp_type =='s'):
			print ("You Win!!!")
			return 1
		elif(computer.comp_type =='p'):
			print("You Lost")
			return 2
		elif(computer.comp_type =='r'):
			print("You Tied")
			return 3
		else:
			return 0

class Scissors(Tool):
	def __init__(self):
		super(Scissors, self).__init__()
		self.type = 's'

	def fight(self, computer):
		#sObj = Tool()
		if(computer.comp_type =='p'):
			print ("You Win!!!\n")
			return 1
		elif(computer.comp_type =='r'):
			print("You Lost\n")
			return 2
		elif(computer.comp_type =='s'):
			print("You Tied\n")
			return 3
		else:
			return 0

class Paper(Tool):
	def __init__(self):
		super(Paper, self).__init__()
		self.type = 'p'

	def fight(self, computer):
		#pObj = Tool()
		if(computer.comp_type =='r'):
			print ("You Win!!!\n")
			return 1
		elif(computer.comp_type =='s'):
			print("You Lost\n")
			return 2
		elif(computer.comp_type =='p'):
			print("You Tied\n")
			return 3
		else:
			return 0
