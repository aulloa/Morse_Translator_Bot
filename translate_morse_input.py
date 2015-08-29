#!/usr/bin/env python
#
# This is the script-wide docstring:
"""
morse code translator takes user input and turns it into morse
code
"""
import urllib2


def underscore (morse_input):
    "finds indexes of underscores in string which speperate words of morse "
    x = 0
    i_arry = []
    while True:
        i = morse_input.find ('_', x)
#        print (i)
        x = i+1
        i_arry.append (i)
        if i == -1:
            break
    return i_arry


def wordparse (morse_input):
    "parses morse input into morse strings"
    w         = underscore(morse_input)
    if w[0] == -1:
        morse_strings = [morse_input]
        print ("single word")
    else:
        n_letters = len (w)
        s         = 0
        e         = w [0]
        morse_strings = []
        for x in range(0,n_letters):
            morse_string  = morse_input [s:e]
            morse_strings.append (morse_string)
        #    print (morse_strings)
            if e == len (morse_input):
                break
            if w [x + 1] == -1:
                    e = len (morse_input)
            else:
                 e = w [x + 1]
            s = w [x] + 1
    return morse_strings


def whitespace(morse_string):
    "finds indexes of spaces in string of morse letters"
    x = 0
    i_arry = []
    while True:
        i = morse_string.find (' ', x)
        x = i+1
        i_arry.append (i)
        if i == -1:
            break
    return i_arry


def parser(morse_string):
    "uses whitespace to parse atring into list"
    w         = whitespace(morse_string)
    if w[0] == -1:
        morse_letters = [morse_string]
        print ("single letter")
    else:
        n_letters = len (w)
        s         = 0
        e         = w [0]
        morse_letters = []
        for x in range(0,n_letters):
            morse_letter  = morse_string [s:e]
            morse_letters.append (morse_letter)
            if e == len (morse_string):
                break
            if w [x + 1] == -1:
                    e = len (morse_string)
            else:
                e = w [x + 1]
            s = w [x] + 1
    return morse_letters


def morse_tree (morse):
    """
    morse tree function runs a morse letter, string of dots and dashes
    through the tree
    """
    Lmorse = len(morse)
    if morse[0] == ".":
        if Lmorse == 1:
            i = "E"
        elif morse[1] == "-":
            if Lmorse == 2:
                i = "A"
            elif morse[2] == ".":
                if Lmorse == 3:
                        i = "R"
                elif morse[3] == "-":
                     i = "A"
                else:
                     i = "L"
            elif morse[2] == "-":
                if Lmorse == 3:
                        i = "W"
                elif morse[3] == "-":
                     i = "J"
                else:
                     i = "P"
        elif morse[1] == ".":
            if Lmorse == 2:
                i = "I"
            elif morse[2] == ".":
                if Lmorse == 3:
                    i = "S"
                elif morse[3] == ".":
                      i = "H"
                else:
                     i = "V"
            else:
                 if Lmorse == 3:
                     i = "U"
                 elif morse[3] == ".":
                       i = "F"
                 else:
                      i = "u"
    if morse[0] == "-":
        if Lmorse == 1:
            i = "T"
        elif morse[1] == "-":
            if Lmorse == 2:
                i = "M"
            elif morse[2] == ".":
                if Lmorse == 3:
                        i = "G"
                elif morse[3] == "-":
                     i = "Q"
                else:
                     i = "Z"
            elif morse[2] == "-":
                if Lmorse == 3:
                        i = "O"
                elif morse[3] == "-":
                     i = "S"
                else:
                     i = "O"
        elif morse[1] == ".":
            if Lmorse == 2:
                i = "N"
            elif morse[2] == ".":
                if Lmorse == 3:
                    i = "D"
                elif morse[3] == ".":
                      i = "B"
                else:
                     i = "X"
            else:
                 if Lmorse == 3:
                     i = "K"
                 elif morse[3] == ".":
                       i = "C"
                 else:
                      i = "Y"
    return i
def translate_letters (morse_string):
    morse_letters = parser (morse_string)
    #print (morse_letters ) 
    n_letters = len (morse_letters)
    transletter_arry = []
    for x in range (0,n_letters):
        transletter = morse_tree (morse_letters [x])
        transletter_arry.append (transletter)
    return (transletter_arry)
def translate_morse_input(user_input):
    word_strings = wordparse (user_input)
    n_word_strings = len (word_strings)
    transwords = []
    for x in range (0,n_word_strings):
        transletter_array = translate_letters (word_strings [x])
        transletter_array_j = ''.join(transletter_array)
        transwords.append (transletter_array_j)
        transwords_j = ' '.join(transwords)
    return transwords_j

# this will only run if this file is executed as a script
if __name__ == '__main__':
    print("Welcome to Morse Interpreter")
    user_input = input(' Enter Morse Code: ')
    translated = translate_morse_input(user_input)
    print(translated)
    Close = input('Close?')
  


