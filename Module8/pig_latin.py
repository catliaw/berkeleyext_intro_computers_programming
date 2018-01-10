#!/usr/bin/python3
#This program converts a sentence typed in by the user to Pig Latin
#Pig Latin Rules:
#(1) If a word begins with a consonant all consonants before the first vowel 
#are moved to the end of the word and the letters "ay" are then added to the end.
#e.g. "coin" becomes "oincay" and "flute" becomes "uteflay".
#(2) If a word begins with a vowel then "yay" is added to the end.
#e.g."egg" becomes "eggyay" and "oak" becomes "oakyay".

punctuation = [",", ".", ";", "!", "?"]

original_sentence = input("Please input a sentence to translate into Pig Latin: ")
original_words = original_sentence.split(" ")
pig_latin_sentence = ""
all_caps = True

def word_to_pig_latin(string):
    cap_vowels = ["A", "E", "I", "O", "U"]
    low_vowels = ["a", "e", "i", "o", "u"]
    cap_consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", \
                      "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    low_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", \
                      "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    punctuation = [",", ".", ";", "!", "?"]

    all_caps = True

    #if first letter in string is a lowercase vowel
    if string[0] in low_vowels:
        return string + "yay"
    #if first letter in string is a uppercase vowel
    elif string[0] in cap_vowels:
        for letter in string:
            #if letter is lowercase 
            if letter not in cap_vowels and letter not in cap_consonants:
                all_caps = False
                break
        if all_caps is True:
            return string + "YAY"
        else:
            all_caps = True
            return string + "yay"
    #if first letter in string is a lowercase consonant
    elif string[0] in low_consonants:
        return string[1:] + string[0] + "ay"
    #if first letter in string is a uppercase consonant
    elif string[0] in cap_consonants:
        for letter in string:
            #if letter is lowercase 
            if letter not in cap_vowels and letter not in cap_consonants:
                all_caps = False
                break
        if all_caps is True:
            return string[1:] + string[0] + "AY"
        else:
            all_caps = True
            return string[1].upper() + string[2:] + string[0].lower() + "ay"
    
    #in case anything else
    else:
        return string

for i, word in enumerate(original_words):
    #in case of floating chunks of punctuation
    #does NOT work for punctuation followed directly by letters
    #assuming some proper grammar will be used 
    if word[0] in punctuation:
        pig_latin_sentence += word
    #words followed by punctuation
    elif word[-1] in punctuation:
        #in case more than one punctuation mark following word
        for n, letter in enumerate(word):
            if letter in punctuation:
                pig_latin_sentence += word_to_pig_latin(word[:n]) + word[n:]
                break
    else:
        #words without punctuation
        pig_latin_sentence += word_to_pig_latin(word)
    #add space after words that aren't the last word.
    if i != (len(original_sentence) - 1):
        pig_latin_sentence += " "

print("\n" + pig_latin_sentence)