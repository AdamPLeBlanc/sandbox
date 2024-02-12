#! /usr/bin/env python3

import sys
import re
import random

 

def get_input(message,ans_rgx=None):
    resp = None
    if ans_rgx:
        ans_rgx = re.compile(ans_rgx)
    while not resp:
        resp = input(message)
        if ans_rgx and not ans_rgx.search(resp):
            #if we're filtering responses and this response didnt match, erase response and try again
            resp = None

    return resp
 

def generate_team_numbers():
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers



def main():
    team_a = get_input("what is the name of the first team? ")
    team_b = get_input("what is the name of the second team? ")

    print("generating numbers...")
    print(f"team {team_a} numbers: {','.join([str(n) for n in generate_team_numbers()])}")
    print(f"team {team_b} numbers: {','.join([str(n) for n in generate_team_numbers()])}")

 

if "__main__" in __name__:
    main()
