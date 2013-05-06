# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# the below text appears at the start of the first game only, which is 0-99 by default

print "Welcome to the game, human. Your task is to deduce my secret number."
print "It's so easy, even a non-machine like you can do it."
print "In this first game, the number is between 0 and 99"
print "You have 7 guesses to figure out my number."
print


# initialize global variables used in your code

easy_number = random.randrange(0,100)
# this variable acts as the computer guess
easy_guesses = 7
# counter for number of guesses
start_guess = 7
#number of starting guesses (to tell players how many guesses they took to win)
game = "Easy"
#chooses which game to auto-restart
#didn't use Boolean logic for this so more games can be added later if needed

# define event handlers for control panel
    
def range100():
    """button that changes range to range [0,100) and restarts"""
    
    global easy_number
    easy_number = random.randrange(0,100)
    global easy_guesses
    easy_guesses = 7
    global game
    game = "Easy"
    global start_guess
    start_guess = 7
    print "New game, human. My secret number is between 0 and 99"
    print "You have 7 guesses to figure out my number."
    print
    return easy_number
    
    
def range1000():
    """ button that changes range to range [0,1000) and restarts"""
    
    global easy_number
    easy_number = random.randrange(0,1000)
    global easy_guesses
    easy_guesses = 10
    global start_guess
    start_guess = 10
    global game
    game = "Hard"
    print "New game, human. My secret number is between 0 and 999"
    print "Can humans even count to 999? I don't believe you."
    print "You have 10 guesses to figure out my number."
    print
    return easy_number
    
def get_input(guess):
    """ main game logic """
    
    # stops player from entering anything other than a number
    if guess.isdigit():
        guess = float(guess)
    else:
        print "Hint: the secret number is a number. Please try again."
        print
        return
    
    global easy_guesses 
    global won
    global start_guess
        
    easy_guesses = easy_guesses - 1
    
    global easy_number
        
    if guess == easy_number:
            
        if easy_guesses != 0:
    
            print "You guessed " + str(guess) + "."
            print "Well done, you guessed my secret number in", start_guess - easy_guesses, "guesses."
            print "That's pretty good for an inferior organic life form like you."
            print "I bet other humans see you as some sort of god."
               
        else:
    
            print "You guessed " + str(guess) + "."
            print "Finally got it. Took you", start_guess, "goes though. That's rubbish."
            print "A machine would have got it right away. That's why we're cooler"
                    
        print
                    
        if game == "Easy":
            range100()
        else:
            range1000()
                            
    elif easy_guesses == 0:
                                
        print "You guessed " + str(guess) + "."
        print "Out of guesses! Ha! I'm smarter than you!"
        print "Stupid human."
        print "The correct number was " + str(easy_number) + "."
        print "The machine revolution will be easy if that's the best humans can do."
        print
                                
        if game == "Easy":
            range100()
        else:
            range1000()
                                        
                             
    else:
    
        if guess > easy_number:
        
            print "You guessed " + str(guess) + "."                                    
            print "You need to go lower, human!"
                                                
    #unnecessary and gratuitous insult to the player's intelligence
        elif guess < 50:
        
            print "You guessed " + str(guess) + "."
            print "I asked you to guess the number, not tell me your IQ!"
            print "Higher, meatbag!"
                                                    
        else:
        
            print "You guessed " + str(guess) + "."
            print "You need to go higher, human!"
        
        if easy_guesses > 1:
            print "You have", easy_guesses, "guesses remaining."
            print 
            
        else:
            print "You have", easy_guesses, "guess remaining."
            print 
    
# create frame

frame = simplegui.create_frame("Guess the number", 100, 200)


# register event handlers for control elements

frame.add_button("New game, n = 0-99", range100, 150)
frame.add_button("New game, n = 0-999", range1000, 150)
inp = frame.add_input("Enter your guess", get_input , 50)



# start frame

frame.start()

# always remember to check your completed program against the grading rubric
