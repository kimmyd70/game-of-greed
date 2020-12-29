import random

class GameLogic:
    
    @staticmethod
    def calculate_score(roll:tuple):
        # calculate the roll's score using rules of the game
        pass
        return score_from_roll
    
# Single fives are worth 50 points
# Single ones are worth 100 points
# Three of a kind are worth 100 points times the number rolled, except for three ones which are worth 1000 points
# If four, five, or six of a kind are rolled, each additional die is worth as much again as the three of a kind score
# This makes the highest possible score in a single roll 4000 for six ones (1000 for three ones, after that player gains 1000 points for each additional one in that series of rolling.) The ONE is the only die you ever count in the thousands.
# A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
# Three pairs are worth 1500 points. For instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
# If a player fails to roll a three pairs, they may make one attempt to complete the three of a kind. If the desired number(s) does not turn up on the next roll, that round is a "crap out", even if there are scoring dice on the table; i.e. 1's or 5's.
    
    @staticmethod
    def roll_dice(die_num:int):
        # create tuple with random int 1-6
        # The length of tuple must match the argument given 
        
        roll_result = tuple(())
        # loop through rolling single die for die_num number of times
        # add to tuple and return 
        for die in range(1,die_num+1):
            roll_result = roll_result + (random.randint(0,6),)
        return roll_result   

class Banker:
    def shelf(add_to_shelf:int):
        #temp store unbanked points
        pass
        
    def bank():
        #add points on shelf to total
        #reset shelf to 0
        pass
        
    def clear_shelf():
        #remove all unbanked points
        pass