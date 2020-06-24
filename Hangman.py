#This is my Python Hangman Game
from numpy import random;

#Initialize words for the hangman game
#Potentially add web scrapping or difficulty levels based on user input 
words = ["diagram", "computer", "zoo", "penguin", "lobster", "ground", "racecar"];

#Randomly choose a word
x = random.randint(len(words));

#position of the word in the array 
#print(x);

#the word in the array
#print(words[x]);

#print the number of blanks in the word
guess_word = words[x];

#breakup word into letters to be guessed 
letters = list(guess_word);

#print all letters in the word
#print(letters);

cur_word = "";
for j in range (0, len(guess_word)):
    cur_word = cur_word + "_"
#print("current", cur_word)

#Guesses 
guesses = 6; 
#Letters Left 
letters_left = len(guess_word);
#Guessed Letters
guessed_letters = [];


for i in range (0, len(cur_word)):
    print (cur_word[i], end = " ");
    
print("")
print("(" , letters_left, "Letters to guess - ", guesses, "wrong guesses left )");

 
#Checks previous guesses to see if current char is valid to guess
def previousGuess(letter):
    for i in range (0, len(guessed_letters)):
        if guessed_letters[i] == letter:
            return True;
    return False;

#creates a new word and maps the guesses over.
def updateWord(letter, index):
    updated = "";
    for i in range(0, len(cur_word)):
        if(i == index):
            updated = updated + letter;
        else:
            updated = updated + cur_word[i];
    return updated;

#Checks the correct word and fills in any correct letters
def checkCorrect(letter):
    found = False; 
    for i in range (0, len(guess_word)):
        if guess_word[i] == letter:
            #define cur as a global variable -> thanks stack overflow
            global cur_word

            cur_word = updateWord(letter, i);
            
            #define ll as a global variable -> thanks stack overflow
            global letters_left;
            letters_left = letters_left - 1;
            print("Index", i)
            found = True
            
    return found;
    

#TODO - make sure all checks are handled 
while guesses > 0 and letters_left > 0:
    validGuess = False;
    while not validGuess: 
        char = input("Please enter a guess: ")
        
        #Enter a letter checking
        if char.isalpha():
            if len(char) == 1: 
                if(not previousGuess(char)):
                    #print(previousGuess(char))
                    if(not checkCorrect(char)):
                        guesses = guesses - 1;
                    guessed_letters.append(char);
                    #print("letters guessed:", guessed_letters)
                    validGuess = True;
                    
                else:
                    print("Please guess a letter you haven't guessed yet");
            else:
                print("Please only enter a single character");
        else: 
            print("Please enter a valid character");
    
    for i in range (0, len(cur_word)):
        print (cur_word[i], end = " ");
    print("")
    print("(" , letters_left, "Letters to guess - ", guesses, "wrong guesses left )");
                 
    
