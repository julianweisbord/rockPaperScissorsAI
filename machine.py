import random, sys
from tool import Tool, Rock, Paper, Scissors
#from rpsgame import RPSGame

class AI():
    def __init__(self):
        print "I am the robot, I am all powerfull."
        self.next_value = 0

    player_array = []
    between_pattern = []
    def set_next_value(self, val):
        self.next_value = val
    def get_next_value(self):
        return self.next_value

    def set_between_pattern(self, pattern):
        self.between_pattern = pattern
    def get_between_pattern(self):
        return self.between_pattern

    def set_array(self,my_list):
        self.player_array = my_list

    def get_array(self):
        return self.player_array

    def random(self):
        rand= random.randint(0,10000)
        return rand

    def data(self,populate):
        self.player_array.append(populate)
        print "Here are your past moves: ", self.player_array

    def algorithm(self):
        match = self.match_algorithm()
        favorite = self.percent_algorithm()
        print "match : ", match, " len(self.get_array()) ", len(self.get_array())
        if(match>=3 and len(self.get_array()) >=7):
            patterns = self.get_between_pattern()
            print "PATTERNS ARRAY: ", patterns
            self.set_next_value(patterns[0])
            print "we will play the opposite of what they threw!!!!!!!!!!!!!!!!"
            if(self.get_next_value() == 'r'):
                print "We will throw paper "
                return 'p'
            elif(self.get_next_value() =='p'):
                print "We will throw scissors "
                return 's'
            elif(self.get_next_value() == 's'):
                print "We will throw rock "
                return 'r'
            # return opposite of what they threw after pattern
#COMPUTER NEEDS TO BE TRICKIER ABOUT THROWING THE FAVORITE
        if (favorite == False):
            print "favorite was false maybe we will try a different algorithm"
        elif (favorite !=False):
            print "we will play the opposite of their favorite."
            if (favorite == 'r'):
                print "They tend to favor rock"
                return 'p'
            elif (favorite == 'p'):
                print "They tend to favor paper"
                return 's'
            elif (favorite == 's'):
                print "They tend to favor scissors"
                return 'r'
        suggestion = False
        return suggestion

#only return length_counter if beginning and ending arrays are equal
    def match_algorithm(self):
        print "AI IS PRINTING ARRAY", self.get_array()
        length_counter = 0
        prev_counter = 1
        stop_index = 0
        index = 0
        index_counter = 0
        prev_pattern = []
        pattern = []
        in_between_counter = 0
        in_between = []
        # pattern_repeat_counter = 1
        # pattern_repeat= [[]]

#there could definately be more than one pattern.
        for item in self.get_array():

            # if(self.get_array()[length_counter +1] == None):
            # # & length_counter <3):
            #     break
            if(len(self.get_array()) >=3):
                if(self.get_array()[-prev_counter] ==self.get_array()[len(self.get_array())-1]):
                    if(self.get_array()[length_counter] == self.get_array()[-prev_counter]):
                        pattern.append(item)
                        print "prev counter: ",prev_counter
                        prev_pattern.append(self.get_array()[-prev_counter])
                        length_counter+=1
                        prev_counter+=1
                        print "prev_counter, length_counter: ", prev_counter, ", ", length_counter
                #if value is not equal to last item in array
                elif(self.get_array()[-prev_counter] != self.get_array()[len(self.get_array())-1]):
                    stop_index = len(self.get_array()) - prev_counter +2

                    #if arrays are equal then create an in betwen array
                    if(pattern == prev_pattern):
                        if(length_counter >=3):

                            #problem with in_between only works if in_between has one value
                            print "length_counter, ", "stop_index ", length_counter, " ", stop_index
                            for x in xrange(length_counter, stop_index):
                                in_between.append(self.get_array()[x])
                            print "in_between array: ", in_between
                            self.set_between_pattern(in_between)
                            #delete first value of in_between corresponding to private array so that the same value doesn't keep getting put into set_next_val.

                            # score =self.get_array()
                            # self.set_array(score.pop(length_counter))

                            return length_counter
                #might never go in here fix something
                    if(self.get_array()[-prev_counter] !=self.get_array()[length_counter]):
                        #pattern needs to restart if the values aren't equal
                        while len(pattern) > 0:
                            pattern.pop(0)
                        print "pattern should be empty: ", pattern

            index+=1
            if(index == stop_index):
                break

    def percent_algorithm(self):

        rock_counter = 0.0
        paper_counter = 0.0
        scissors_counter = 0.0
        rock_percent = 0.0
        paper_percent = 0.0
        scissors_percent =0.0

        counter = 0
        for length in self.get_array():

            print "list length is: ", (counter+1)
            if(self.get_array()[counter]=='r'):
                rock_counter +=1
            elif(self.get_array()[counter]=='p'):
                paper_counter +=1
            elif(self.get_array()[counter]=='s'):
                scissors_counter +=1
            counter +=1

        total_counter = rock_counter + paper_counter + scissors_counter

        if(rock_counter != 0.0):
            rock_percent = (100 * rock_counter)/(total_counter)
            print "Rock Percent: ", rock_percent

        if(scissors_counter != 0.0):
            scissors_percent =  (100*scissors_counter)/ (total_counter)
            print "Scissors Percent: ", scissors_percent

        if(paper_counter != 0.0):
            paper_percent =  (100*paper_counter)/ (total_counter)
            print "Paper Percent: ", paper_percent


        if(total_counter >=8):
            if((rock_percent-10.0>=paper_percent) & (rock_percent-10.0>= scissors_percent)):
                rock_time = 'r'
                print "ITS ROCK TIME! "
                return rock_time
            elif((paper_percent-10.0>=rock_percent) & (paper_percent-10.0>= scissors_percent)):
                paper_time = 'p'
                print "ITS PAPER TIME! "
                return paper_time
            elif((scissors_percent-10.0>=paper_percent) & (scissors_percent-10.0>= rock_percent)):
                scissors_time = 's'
                print "ITS SCISSORS TIME! "
                return scissors_time

        percent_suggestion = False
        return percent_suggestion



    #def ai_choice(self):

    #    algorithmDesicion = False
    #    return algorithmDesicion
        #or returns r, p, or s


    def comp_answer(self):
        ai = self.algorithm()
        #ai_bool = self.ai_choice()
        print "THIS IS AI: ", ai
        if(ai==False):
            random =self.random()
            print("here is random number generated: " + str(random))
            if(random <=3333):
                print "rock"
                computer_answer = 'r'
                return computer_answer
                #call function that adds r to array
            elif (3334<=random<=6666):
                print "paper"
                computer_answer = 'p'
                return computer_answer
                #call function that adds p to array
            elif(6667<=random<=10000):
                print "scissors"
                computer_answer = 's'
                return computer_answer
                #call function that adds s to array
            else:
                print "error in computer answer"
            return ai

        else:
            print "This is ai: ", ai
            return ai
