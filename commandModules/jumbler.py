'''
Created on 13 Mar 2021

@author: Rus

This python module takes text as input and returns a jumbled version.
For example, I input "Forks have minecraft accounts."
It will output a randomly jumbled version, such as: "Frkos hvae mnciferat atcnconus."
'''

print("Preparing Jumbler Module [ALPHA]...")

def jumble(words):
    toJumble = []
    jumbleStc = str()
    jumbleWord = str()
    holdWord = str()
    
    return "Command is not yet operational."
    for c in words:
        if c != " ":
            holdWord += str(c)
        elif c == " ":
            toJumble.append(holdWord)
            holdWord = str()
        print("holdWord: " + str(holdWord))
        print("toJumble: " + str(toJumble))
    
    for w in toJumble:
        for c in w:
            pass