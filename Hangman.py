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

#breakup word into letters to be guessed 
letters = list(guess_word)

#print all letters in the word
print(letters);

#Guesses left
guesses = 6; 
letters_left = len(guess_word);

for i in range (0, letters_left):
    print ("_", end = " ");
    
print("")
print("(" , letters_left, "Letters to guess - ", guesses, "wrong guesses left )");

 
def checkWord(letter):
    print(letter)
    for i in range (0, len(guess_word)):
        if guess_word[i] == letter:
            print("Index", i)
    

#TODO - add while game is playing loop
while guesses > 0:
    validGuess = False;
    while not validGuess: 
        char = input("Please enter a guess: ")
        #Enter a letter checking
        #TODO - Add checking for previous guessed letters
        if char.isalpha():
            if len(char) == 1: 
                checkWord(char);
                validGuess = True;
            else:
                print("Please only enter a single character");
        else: 
            print("Please enter a valid character");
    guesses = guesses - 1;
    for i in range (0, len(guess_word)):
        print ("_", end = " ");
    print("")
    print("(" , letters_left, "Letters to guess - ", guesses, "wrong guesses left )");
                 
    
