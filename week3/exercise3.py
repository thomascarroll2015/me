"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    return
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    
    while True:
      lwrBound = input("Enter an lwr bound: ")
      try:
          lwrval = int(lwrBound)
          print('Thanks, that is a number')
          break
      except ValueError:
          try:
              lwrval = float(lwrBound)
              print("nope. Input is a float number, try again")
          except ValueError:
              print("No.. input is not a number. It's a string, try again")
    while True:
      upperBound = input("Enter an upper bound: ")
      try:
          uppval = int(upperBound)
          print('Thanks')
          break
      except ValueError:
          try:
              uppval = float(upperBound)
              print("nope. Input is a float  number")
          except ValueError:
              print("No.. input is not a number. It's a string")



    print("OK then, a number between {} and {} ?".format(lwrval , uppval))
    actualNumber = random.randint(0, uppval)

    input_validation = False

    while not input_validation:
        guessedNumber = (input("Guess a number: "))
        try:
                  gval = int(guessedNumber)
                  print('Thanks for the integer')
                  break
        except ValueError:
            try:
                gval = float(guessedNumber)
                print("nope. Input is a float  number")
            except ValueError:
                print("No.. input is not a number. It's a string")

    while not input_validation: 
        if uppval > gval > lwrval:
            print ('Guess is in range')
            input_validation = True
        else:
            print ('not in range doggy')
            input_validation = True
    
    guessed = False
    while not guessed:
        print("You guessed {},".format(gval),)
        if gval == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif gval < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
