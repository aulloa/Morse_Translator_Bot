#!/usr/bin/env python
#
# This is the script-wide docstring:
"""
Translate English Input takes user input and turns it into morse
"""
import urllib2

# Translate Dictionary
eng = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    " " : "_",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "," : ",",
    "." : ".",
    "!" : "!",
    "?" : "?",
}

def eng_to_morse(text):
    out = ""
    for char in text:
        c = eng[char] # type: str
        out += "{} ".format(c)
        #print (out)
    return("".join(out))

# this will only run if this file is executed as a script
if __name__ == '__main__':
    print("Welcome to English to Morse")
    user_input = input(' Enter English String: ')
    translated = eng_to_morse(user_input)
    print(translated)
    Close = input('Close?')


