#!/usr/bin/env python3

def return_evens(sequence):
    return [num for num in sequence if num % 2 == 0]

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]

# Testing the function using;
print(return_evens([0, 1, 3, 5, 7, 8, 9]))
# [0, 8]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
# ["Hello!", "I'm doing great!", "Python is fun!"]
