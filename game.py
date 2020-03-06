import random

# I, Mitchell Glennie, student number 000808122, certify that all code
# subbmitted is my own work; that I have not copied it from any other source.
# I also certify that I have not allowed my work to be copied by others.

###################
#     classes     #
###################

# class for dice
class Dice:
    
    # private method for checking all equal pattern
    def __allEqual(self):
        return len(set(self.dice)) == 1
    
    # private method for checking sum prime number pattern
    def __sumPrime(self):
        s = sum(self.dice)
        if s > 1: 
            for i in range(2,s):
                if (s % i) == 0:
                    return False
        return True
    
    # private method for three of n equal pattern
    def __threeOfN(self):
        for d in self.dice:
            c = 0
            for e in self.dice:
                if d == e: c += 1
            if c == 3: return True
        return False
    
    # private method for all different values pattern
    def __allDifferent(self):
        return len(set(self.dice)) == len(self.dice)

    # constructor
    def __init__(self, count):
        self.dice = [random.randint(1,6) for x in range(count)]

    # method for checking pattern in dice
    def pattern(self):
        if self.__allEqual():
            return 100, "all dice being equal"
        elif self.__sumPrime():
            return 50, "the sum of the dice is a prime number"
        elif self.__threeOfN():
            return 30, "3 of {} dice are equal".format(len(self.dice))
        elif self.__allDifferent():
            return 25, "all dice have different values"
        else: 
            return None, False

    # method for calculating score of sum
    def sumScore(self):
        return sum(self.dice)

    # method for rerolling a specific die
    def reroll(self, index):
        self.dice[index] = random.randint(1, 6)

###################
#     methods     #
###################

# method for validating names
def validateName(name):
    if not name.isalpha(): return False
    return name[0].upper()+name[1:].lower()

# method for validating y/n choices
def choice(choice):
    y,n = ['y', 'yes'], ['n', 'no']

    # remove case sensitivity
    choice = input(choice+' [y/n] ').lower()

    while choice not in y and choice not in n:
        choice = input("Please enter a valid input [y/n]: ").lower()
    
    # return true/false (y/n)
    if choice in y: return True
    elif choice in n: return False

# method for each phase
def nextPhase(d):
    reroll, fail = False, False
    
    # loop until at least one die is rerolled
    while not reroll:
        # if no die were rerolled in last attempt print
        if fail: print("You didn't reroll any dice or score any points, please try again.")

        # if there is a pattern ask the user if they want to score points
        score, reason = d.pattern()
        if reason:
            s = choice("Would you like to score the pattern points for {} ({} points)?".format(
                reason, score
            ))
            if s: return score
        
        # ask the user if they want to score for the points of the sum
        score, reason = d.sumScore(), "the sum of the dice"
        s = choice("Would you like to score the pattern points for {} ({} points)?".format(
                reason, score
            ))
        if s: return score

        # ask user if they want to reroll any dice
        for die in range(len(d.dice)):
            r = choice("Would you like to reroll die {}? ".format(die+1))
            if r:
                d.reroll(die)
                reroll = True
        
        fail = True
    return 0

# method for each turn
def nextTurn(turn):
    # print what turn it is
    print("Turn "+str(turn)+":")

    # initialize 5 dice
    d = Dice(5)

    # initial loop print
    print("You rolled 5 dice, the values are: {}".format(
            ", ".join(str(die) for die in d.dice)
    ))
    # loop 3 phases
    for i in range(3):
        phase = nextPhase(d)
        if phase > 0: return phase
        print("You rerolled some dice, the values are: {}".format(
            ", ".join(str(die) for die in d.dice)
        ))
    
    # determine score after all rerolls are used
    score, reason = d.pattern()
    if not reason:
        score = d.sumScore()
        reason = "the sum of the dice."
    
    # print what the user will score
    print("You are out of reroll tries, you score {} points for {}.".format(score, reason))
    return score

###################
#       game      #
###################

# initialize score
score = 0

# print game information
print("Programming Fundamentals 201935, Mitchell Glennie, 000808122")
        
# get the user's first name and make sure it is valid
name = validateName(input("Welcome to my game, what is your first name? "))
while not name: 
    print("Names can only contain letters.")
    name = validateName(input("Please re-enter your name: "))

# greet the user
print("Thank you {}, you start off with {} points. let's play!".format(name, score))

# loop 10 turns
for turn in range(1, 11):
    # add score of each turn to user's score
    score += nextTurn(turn)

    # print new score
    print("Your score is now {} points. Taking points ended your turn.".format(score))
    
    # notify end of turn
    print("End of turn {}.".format(turn))

# print final score
print("Game over! Your final score is: {} points.".format(score))