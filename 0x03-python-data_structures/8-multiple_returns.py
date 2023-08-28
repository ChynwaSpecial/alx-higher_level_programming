#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    character1 = sentence[0] if length > 0 else "None"
    tup = length, character1
    return(tup)
