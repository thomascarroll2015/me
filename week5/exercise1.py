# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    tri = {"base": 3, "height": 4}
    tri["hypotenuse"] = tri["base"] ** 2 + tri["height"] ** 2
    print("area = " + str((tri["base"] * tri["height"]) / 2))
    print("side lengths:")
    print("base: {}".format(tri["base"]))
    print("height: {}".format(tri["height"]))
    print("hypotenuse: {}".format(tri["hypotenuse"]))

    hyp2 = 5 ** 2 + 6 ** 2
    print(hyp2)

    hyp3 = 40 ** 2 + 30 ** 2
    print(hyp3)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    for i in range(start, stop - 1, -1):
        unit = message + " {}"
        print(unit.format(i))
    print(completion_message)
    pass


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = (base ** 2 + height ** 2) ** 0.5
    return hypotenuse


def calculate_area(base, height):
    area = (base * height) / 2
    return area


def calculate_perimeter(base, height):
    perimeter = base + height + calculate_hypotenuse(base, height)
    return perimeter


def calculate_aspect(base, height):
    if height > base:
        aspect = "tall"
    elif height  < base:
        aspect = "wide"
    else:
        aspect = "equal"
    return aspect


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    triangle = {
    "tall" : """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}""",
    "wide" : """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}""",
    "equal" : """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""
    }
    order = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    facts = order.format(**facts_dictionary)
    diagram = triangle[facts_dictionary["aspect"]] + "\n" + facts
    return diagram
    

#function which controls the child functions of get_triangle_facts and tell_me_about_this_right_triangle.
#It can display both functions, or one of either depending on the input
def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    facts_dictionary = get_triangle_facts(base, height)
    diagram = tell_me_about_this_right_triangle(facts_dictionary)

    if return_diagram and return_dictionary:
        return {"diagram": diagram, "facts_dictionary": facts_dictionary}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return facts_dictionary
    else:
        print("You're an odd one, you don't want anything!")

#Function which produces a pyramid of words which ascends and descends by 2 characters
def wordy_pyramid():
    import requests
    import json
    lengths_list = []
    lengths_list.extend(range(3, 21, 2))
    lengths_list.extend(range(20, 3, -2))
    return list_of_words_with_lengths(lengths_list)


def get_a_word_of_length_n(length):
    import requests
    raw = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={}"
    URL = raw.format(length)
    r = requests.get(URL)
    if r.status_code is 200: 
        word = r.text
        print(word)
        return word
    else:
        print("failed a request", r.status_code, length)



def list_of_words_with_lengths(list_of_lengths):
    test = map(get_a_word_of_length_n, list_of_lengths)
    print(test)
    return test


if __name__ == "__main__":
    do_bunch_of_bad_things()
    wordy_pyramid()
