'''TODO: Reflect on what you learned this week and what is still unclear.

continue restarts the loop, break breaks

python ../course/week3/tests.py

control backtick
control /
f'give me a number between {low}, and {high}' ''' sub method

Binary search
    - splits answers into a binary e.g higher lower

within lists:
lista = []

retrun will break wile loops, good for doing loops where you want an input to cause the break 
'''
'''1. Determine what you need for the algorithm'''
2. Determine how to express a certain step
3. See step 2.
4. Run algorithm
5. If not working, see step 6. otherwise, finish
6. diagnose the problem
7. see step 2 if neccesary.

54 min onwards

range(10) returns a range object.
range(9999999999) would be very power intensive as its giving a list of o to x

need to cast list
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> list(range(3, 15, 3))
[3, 6, 9, 12]


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
    pass
    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    
    try:
        high = input("Enter an upper bound: ")
        high = int(high)
    except ValueError:
        print("thats not a number")

    try:
        low = input("Enter an lower bound: ")
        low = int(low)
    except ValueError:
        print("thats not a number")
    
    print("OK then, a number between {} and {} ?".format(low, high))
'''




ex 1 onwrads:

# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    chungus = []
    y = start
    while y < stop:
        chungus.append(y)
        y = y + step

    return chungus


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    return loop_ranger(start, stop, step)


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    lista = []
    for i in range(start, stop, 2):
        lista.append(i)
        print(lista)

    return lista


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    message = 'give me a number between {}, and {}'.format(low, high)
    
    while True: 
        input_numb = int(input(message))
        if high > input_numb > low:
            print ('nice 1')
            return input_numb 
        else:
            print ('nope')

        
    return None



def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    mes = 'give a chungus numbgus: '
    
    while True:
        input_attempt = input(mes)
        try:
            val = int(input_attempt)
            return val
        except:
            print("No.. input is not a number.")
    


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    message = f'give me a number between {low}, and {high}'
    while True:
        testing = input(message)
        try:
            testing = int(testing)
        except:
            print('Nope')
            continue
        if low <= testing <= high:
            return testing
        else:
            print('nope')
    return None





if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    # print("\nloop_ranger", loop_ranger(1, 10, 2))
    # print("\nlone_ranger", lone_ranger(1, 10, 3))
    # print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)

END DONT COPY THIS EX 4 BELOW

# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0
    while (low <= high and guess != actual_number):
        guess = (low + high) // 2
        print(guess)
        if (guess < actual_number):
            low = guess + 1
        elif (guess > actual_number):
            high = guess - 1
        elif (guess == actual_number):
            return {"guess": guess, "tries": tries}
        tries += 1
    


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))

