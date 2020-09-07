# CIS41A: Summer 2020: Lab4 Dictionaries: Nandhini Pandurangan
# This program reads a txt file to create a Morse Code dictionary. It translates the the string,
# "THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES", into Morse Code

"""
Lab 4 - Dictionaries

 Write a UDT (class) to contain MorseCode data, as read from the MorseCode.csv file.
 Read each line from the MorseCode.csv file and convert it to a MorseCode object.
 After constructing the MorseCode object, insert it into a MorseCode Container class containing
    a Dictionary to hold MorseCode objects.

 Convert this sentence to MorseCode by looking up each character in the dictionary and printing the MorseCode:

"THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES"

"""

import csv


class MorseCode:
    def __init__(self, char, symbol):
        self.char = char
        self.symbol = symbol

    def __str__(self):
        return self.symbol + " "


class MorseContainer:
    def __init__(self):
        self.morse_code_dict = {}  # dictionary to hold Morse Code

    def reader(self, csvfile):
        for line in csv.reader(open(csvfile)):  # read the txt file
            k = line[0]  # set the key to a character
            self.morse_code_dict[k] = MorseCode(line[0], line[1])  # create MorseCode object & insert into dictionary

    # translate() looks up each character in a string and converts it to Morse Code
    def translate(self, sentence):
        sentence_list = sentence.split(" ")  # make a list of all the words in the sentence

        for i in range(len(sentence_list)):  # per word in the sentence
            for letter in sentence_list[i]:  # per letter in the word
                print(self.morse_code_dict.get(letter), end=" ")  # retrieve the matching value for the character


            if i != len(sentence_list) - 1:  # insert forward slash between each word
                print("/", end= " ")


# main() creates MorseContainer Class Object and calls appropriate functions to translate a string into Morse Code
def main():
    mc = MorseContainer()
    mc.reader("MorseCode.txt")
    mc.translate("THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES")


# calling main()
main()

''' 
 my output:         -  ....  .  / --.-  ..-  ..  -.-.  -.-  / -...  .-.  ---  .--  -.  / .--.  ---  ---  -..  .-..  .  / .---  ..-  --  .--.  .  -..  / ---  ...-  .  .-.  / -  ....  .  / .-..  .-  --..  -.--  / ..-.  ---  -..-  / .----  ..---  ...--  / -  ..  --  .  ...
 online translator: -  ....  .  / --.-  ..-  ..  -.-.  -.- / -...   .-.  ---  .--  -.  / .--.  --- ---   -..  .-..  .  / .---  ..-  --  .--.  .  -..  / ---  ...-  .  .-.  / -  ....  .  / .-..  .-  --..  -.--  / ..-.  ---  -..-  / .----  ..---  ...--  / -  ..  --  .  ... 
'''