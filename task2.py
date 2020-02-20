#got some help from stackoverflow

from itertools import product
with open("datafile") as myfile:
    head = [next(myfile) for x in range(25)] # importing first 25 lines
print(head)


def i33t(string):
    vocab = {
    "a" or "A" :["4"],
    "o" or "O" :["0"],
    "e" or "E" :["3"]
    "i" or "I" :["1"]
    for word in string.split(" "):
                
