import random
from art import logo
from random import randint

print(logo)
num = randint(1, 100)
mode = input("Welcome to Guessing game, type 'e' for easy mode, and, 'h' for hard mode: ")

#easy mode
if mode == "e":
    print("You have 10 attempts to guess a number from 1 to 100")
    chosen_num = int(input("Pick a number between 1 and 100: "))
    attempts = 9
    while attempts != 0:
        if chosen_num == num:
            print("Perfect! You got it")
            break
        elif chosen_num > num:
            chosen_num = int(input(f"{chosen_num} is too high, pick again: "))
        else:
            chosen_num = int(input(f"{chosen_num} is too low, pick again: "))
        attempts -= 1

#hard mode
elif mode == "h":
    print("You have 5 attempts to guess a number from 1 to 100")
    chosen_num = int(input("Pick a number between 1 and 100: "))
    attempts = 4
    while attempts != 0:
        if chosen_num == num:
            print("Perfect! You got it")
            break
        elif chosen_num > num:
            chosen_num = int(input(f"{chosen_num} is too high, pick again: "))
        else:
            chosen_num = int(input(f"{chosen_num} is too low, pick again: "))
        attempts -= 1
