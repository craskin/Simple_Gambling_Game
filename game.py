"""
author: Carly Raskin
DU ID: 873185794
The purpose of this program is to play a simple betting game using dice. The program runs
mainly by using classes and the magic methods python has
"""

import random

class Dice:

    def __init__(self, numside):
        """ initiating the dice rolls """
        self.numside = numside
        self.diceroll = random.randint(1, numside)
        list1 = []
        list1.append(self.diceroll)
        """ I want each individual roll to print out just for visualization sake,
        and I like the way it looks when formatted as a list """
        print("Rolled: ", list1)

    def __str__(self):
        string1 = "Rolled a ", self.diceroll
        return string1

    def __add__(self, other):
        self.diceroll += other.diceroll
        return self.diceroll

    def __eq__(self, other):
        if type(self) == type(other):
            return (self.diceroll) == (other.diceroll)

    def __gt__(self, other):
        if type(self) == type(other):
            return (self.diceroll) > (other.diceroll)

    def __lt__(self, other):
        if type(self) == type(other):
            return (self.diceroll) < (other.diceroll)

    def __ge__(self, other):
        if type(self) == type(other):
            return (self.diceroll) >= (other.diceroll)

    def __le__(self, other):
        if type(self) == type(other):
            return (self.diceroll) <= (other.diceroll)

    def __ne__(self, other):
        if type(self) == type(other):
            return (self.diceroll) != (other.diceroll)

class CupOfDice:

    def __init__(self, numdice, numside):
        self.score = 0
        self.numside = numside
        self.numdice = numdice

        """ instantiate rolling all the dice the user inputs from class Dice, adding
         each roll to score to get a total """
        for i in range(0, numdice):
            roll = Dice(numside)
            self.score += roll.diceroll

    def __str__(self):
        return str(self.score)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.score == other.score

    def __gt__(self, other):
        if type(self) == type(other):
            return self.score > other.score

    def __lt__(self, other):
        if type(self) == type(other):
            return self.score < other.score

    def __ge__(self, other):
        if type(self) == type(other):
            return self.score >= other.score

    def __le__(self, other):
        if type(self) == type(other):
            return self.score <= other.score

    def __ne__(self, other):
        if type(self) == type(other):
            return self.score != other.score


def main():
    """ how much money are the user and computer starting with? """
    money_start = int(input("Set how much money you want to start with: "))
    computer_start = money_start

    """ need two while loops to loop through the game, one to end the game and one to repeat 
       entered bet if it is lower than player's remaining money """
    bet_good = True
    game = True

    while bet_good:
        while game:
            """ how much is the user and computer betting? """
            user_bet = int(input("How much money are you betting this round? "))
            if user_bet > money_start:
                """ making sure the user cannot bet more money than they have
                (but it's okay if they bet more than the computer has)"""
                print('You cannot bet more money than you have, try again')
                bet_good = False
            else:
                numdice = int(input("Enter the number of dice you would like to roll: "))
                numside = int(input("Enter the number of sides you would like each die to have: "))
                """ Running CupOfDice twice, once to simulate user rolls and once
                to simulate computer rolls """
                user_play = CupOfDice(numdice, numside)
                print("You Scored", user_play)
                computer_play = CupOfDice(numdice, numside)
                print("Computer scored", computer_play)
                print("Your Score: ", user_play)
                """ What happens if it's a win, lose, or tie: """
                if user_play.__eq__(computer_play) == True:
                    """ in gambling, a tie means the house (computer) wins """
                    print("Even though you tied, house rules say you lose! Too bad")
                    money_start -= user_bet
                    computer_start += user_bet
                    print("Your remaining money: ", money_start)
                    print("The computer's remaining money: ", computer_start)
                elif user_play.__gt__(computer_play) == True:
                    print("Congratulations! You've won this round")
                    money_start += user_bet
                    computer_start -= user_bet
                    print("Your remaining money: ", money_start)
                    print("The computer's remaining money: ", computer_start)
                elif user_play.__lt__(computer_play) == True:
                    print("Too bad! You lose!")
                    money_start -= user_bet
                    computer_start += user_bet
                    print("Your remaining money: ", money_start)
                    print("The computer's remaining money: ", computer_start)
                if money_start <= 0:
                    bet_good = False
                    game = False
                    print("You've lost all your money! You lose the game!")
                elif computer_start <= 0:
                    bet_good = False
                    game = False
                    print("The computer ran out of money! You win!")


main()



