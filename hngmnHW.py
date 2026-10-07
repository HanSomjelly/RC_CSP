# RC, Hangman Homework, CSP 6th
import random

# Read the list of possible words from words.txt
with open("words.txt", "r") as file:
    words = file.read().splitlines()

    # Read the win/loss totals from stats.txt
    