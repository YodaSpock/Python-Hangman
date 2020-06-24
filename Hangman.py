#This is my Python Hangman Game
from numpy import random;
#Initialize words for the hangman game
#Potentially add web scrapping or difficulty levels based on user input 
words = ["diagram", "computer", "zoo", "penguin", "lobster", "ground", "racecar"];

x = random.randint(len(words));

#position of the word in the array 
#print(x);
#the word in the array
print(words[x]);

#print the number of blanks in the word
guess_word = words[x];
word_length = len(guess_word);

#breakup word into letters to be guessed 
letters = list(guess_word)
print(letters);

for i in range (0, word_length):
    print ("_", end = " ");
    
print("(" , word_length, "Letters to guess )");

#TODO - add while game is playing loop
validGuess = False;
while not validGuess: 
    char = input("Please enter a guess: ")
    #Enter a letter checking
    #TODO - Add checking for previous guessed letters
    if char.isalpha():
        if len(char) == 1: 
            validGuess = True;
        else:
            print("Please only enter a single character");
    else: 
        print("Please enter a valid character");
                 