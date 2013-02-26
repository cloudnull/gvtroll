#!/usr/bin/env python

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys
import os

# Local Import for word list
from alice import alice

def mimic_dict(filename):
    """
    Takes the Input string ans creates our markov chains
    """
    word_list = {}
    all_the_words = alice.split()
    for count, word in enumerate(all_the_words):
        word = word.strip()
        if word in word_list:
            word_list[word].append(all_the_words[count+1])
        else:
            word_list[word] = []
        try:
            word_list[word].append(all_the_words[count+1])
        except:
            pass
    return word_list


def print_mimic(mimic_dict, word):
    """
    Given mimic dict and start word, prints 200 random words.
    """
    if not word:
        word = random.choice(mimic_dict.keys())
    output = [word]

    for story in xrange(0,199):
        word = random.choice(mimic_dict[word])
        output.append(word)

    # This is for tweeting nonsense
    twitter = ' '.join(output)[:120]
    return twitter


# Provided main(), calls mimic_dict() and mimic()
def main():
    """
    Starts the mimc application
    """
    dict = mimic_dict(alice)
    twitter = print_mimic(dict, '')
    return twitter


if __name__ == '__main__':
    main()

