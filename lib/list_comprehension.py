#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [n for n in num_list if n%2 == 0]
    return evens_list
    pass

def make_exclamation(sentence_list):
    if len(sentence_list) > 0:
     exclamation_list = [s + "!" for s in sentence_list]
     return exclamation_list
    else :
     return sentence_list
     pass