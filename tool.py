
class Tool:
	def get_type(self):
		return type

	def set_type(self, human_choice):
		type = human_choice

class Rock(Tool):
	
	def fight(self,user_input):

		if(user_input== 's')
			return 1	
		
		if(user_input== 'p'):
			return 2
		if(user_input=='r'):
			return 3
		else:
			return 0
class Scissors(Tool):
	
	def fight(self,user_input):

		if(user_input== 'p')
			return 1	
		
		if(user_input== 'r'):
			return 2
		if(user_input=='s'):
			return 3
		else:
			return 0	
class Paper(Tool):
	
	def fight(self,user_input):

		if(user_input== 'r')
			return 1	
		
		if(user_input== 's'):
			return 2
		if(user_input=='p'):
			return 3
		else:
			return 0												