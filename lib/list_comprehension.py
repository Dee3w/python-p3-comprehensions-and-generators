#!/usr/bin/env python3

def return_evens(num_list):
      my_list = [n for n in num_list if n%2 == 0]
      return my_list

def make_exclamation(sentence_list):
      my_list = [n + '!' for n in sentence_list]
      return my_list 