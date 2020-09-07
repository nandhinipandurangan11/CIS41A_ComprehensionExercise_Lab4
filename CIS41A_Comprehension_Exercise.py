# CIS41A: Summer 2020: Comprehension Exercise: Nandhini Pandurangan
# This program reads a txt file to create a Morse Code dictionary. It translates the the string,
# "THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES", into Morse Code
# This program uses comprehensions to do Lab 4 Dictionaries


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

    # line_assign() creates a MorseCode object and adds it to the dictionary
    def line_assign(self, key, value):
        self.morse_code_dict[key] = MorseCode(key, value)

    # reader() calls line_assign() per line of the csv file
    def reader(self, csvfile):
        [self.line_assign(line[0], line[1]) for line in csv.reader(open(csvfile))]

    # return_morse_code() returns "/" if the character is a space,
    # else retrieve the correct value from the dictionary
    def return_morse_code(self, letter):
        if letter == " ":
            print("/", end=" ")
        else:
            code = str(self.morse_code_dict.get(letter))
            print(code, end=" ")

    # translate() looks up each character in a string and converts it to Morse Code
    def translate(self, sentence):
        # call the function return_morse_code for each letter of the sentence
        [self.return_morse_code(letter) for letter in sentence]


# main() creates MorseContainer Class Object and calls appropriate functions to translate a string into Morse Code
def main():
    mc = MorseContainer()
    mc.reader("MorseCode.txt")
    mc.translate("THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES")


# calling main()
main()

