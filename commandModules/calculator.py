'''
Created on 10 Mar 2021

@author: Rus

This sub-program simulates a basic calculator.
It takes string as input and outputs a numerical answer.
The operations that it supports are: Addition, Subtraction, Multiplication, Division, Modulo, Factorials*, Exponents*, and Roots*.
This calculator also does not support paretheses. We will work on that some other time.

*These operations will be worked on in a different session.
'''
import random#,math
from commandModules import listlist

print("Preparing Calculator Module...")

numericalList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
operatorList1 = ["+", "-", "x", "*", "/", "%"]
operatorList2a = ["^", "s", "q", "r", "t", "c", "u"]        #Unused for now
operatorList2b = ["^", "sq", "sqrt", "cu", "curt"]          #Unused for now
opMD = ["x", "*", "/", "%"]
opAS = ["+", "-"]
operatorList3 = operatorList1 + operatorList2b
numberHolder = []
numHoldPointer = 0
ptr = 0

def rmvEmpty(list2Mod):
    global ptr
    moddedList = []
    print(f"Clearing: {list2Mod}; Ptr: {ptr}")
    for i in list2Mod:
        if i == "":
            ptr -= 1
        else:
            moddedList.append(i)
    print(f"Cleared: {moddedList}; Ptr {ptr}")
    return moddedList
    
def doExponents(num1, op, num2):
    print(f"{num1} {op} {num2}")
    pass    #To-do

def doMulDiv(num1, op, num2):
    print(f"{num1} {op} {num2}")
    if op == "mul":
        return num1 * num2
    elif op == "div":
        return num1 / num2
    elif op == "mod":
        return num1 % num2

def doAddSub(num1, op, num2):
    print(f"{num1} {op} {num2}")
    if op == "add":
        return num1 + num2
    elif op == "sub":
        return num1 - num2

def doMoreMath(operation):
    global numericalList, operatorList1, operatorList2a, operatorList2b, numberHolder, numHoldPointer, ptr
    ctr = 0
    
    print("\n---------------\n\nPhase 2: Operation Checks & Runs\n")
    
    #print("\n---------------\n\nPhase 2.1: Parentheses* and Exponents\n")
    #ptr = 0
    
    print("\n---------------\n\nPhase 2.2: Multiplication and Division\n")
    ptr = 0
    for i in operation:
        if i in opMD:
            print(f"OpMD: MulDivMod <{i}>, Ptr: {ptr}, Eq: {operation}\n")
            if i == "*" or i == "x":
                operation[ptr] = doMulDiv(float(operation[ptr-1]),"mul",float(operation[ptr+1]))
            elif i == "/":
                operation[ptr] = doMulDiv(float(operation[ptr-1]),"div",float(operation[ptr+1]))
            elif i == "%":
                operation[ptr] = doMulDiv(float(operation[ptr-1]),"mod",float(operation[ptr+1]))
            
            #Old clearing code.
            #if operation[ptr-1] != operation[-1]:
            #    operation[ptr-1] = ""
            #if operation[ptr+1] != operation[0]:
            #    operation[ptr+1] = ""
            
            ctr = 0
            if ptr != 0:
                operation[ptr-1] = ""
            for i in operation:
                ctr += 1
            if ptr != ctr:
                operation[ptr+1] = ""
            operation = rmvEmpty(operation)
        ptr += 1
    
    print("\n---------------\n\nPhase 2.3: Addition and Subtraction\n")
    ptr = 0
    for i in operation:
        if i in opAS:
            print(f"OpAS: AddSub <{i}>, Ptr: {ptr}, Eq: {operation}\n")
            if i == "+":
                operation[ptr] = doAddSub(float(operation[ptr-1]),"add",float(operation[ptr+1]))
            elif i == "-":
                operation[ptr] = doAddSub(float(operation[ptr-1]),"sub",float(operation[ptr+1]))
            
            ctr = 0
            if ptr != 0:
                operation[ptr-1] = ""
            for i in operation:
                ctr += 1
            if ptr != ctr:
                operation[ptr+1] = ""
            
            #Old clearing code.
            #if operation[ptr-1] != operation[-1]:
            #    operation[ptr-1] = ""
            #if operation[ptr+1] != operation[0]:
            #    operation[ptr+1] = ""
            
            operation = rmvEmpty(operation)
        ptr += 1
    
    ptr = 0
    return float(operation[0])
    
def doMath(eqString, toRoast):
    global numericalList, operatorList1, operatorList2a, operatorList2b, numberHolder, numHoldPointer
    output = 0
    
    print("\n\n---------------\n\nPhase 1: String to list\n")
    for ch in eqString:
        if ch in numericalList:
            try:
                numberHolder[numHoldPointer] += ch
            except IndexError:                      #This will run on every new number, ignoring indexErrors.
                numberHolder.append(ch)
            except Exception as e:
                print(f"\n\n---------------\n\nException encountered:\n{e}\n\n---------------\n\n")
                break
        elif ch in operatorList1:
            numberHolder.append(ch)
            numHoldPointer += 2
        elif ch in operatorList2a:
            pass
        
        print(f"numberHolder: {numberHolder}")
    
    if numberHolder == []:
        print("Resetting variables...")
        numberHolder = []
        numHoldPointer = 0
        ptr = 0
        output = f"`{eqString}`: Syntax Error"
        print(f"{output}")
        return f"{output}"
    else:
        output = round(doMoreMath(numberHolder), 2)
        print(f"{eqString} = {output}")
        if toRoast == True:
            print("Resetting variables...")
            numberHolder = []
            numHoldPointer = 0
            ptr = 0
            print("Sending output with suffix...\nDone!")
            return f"{eqString} = {output}{random.choice(listlist.suffixInsult)}"
        else:
            print("Resetting variables...")
            numberHolder = []
            numHoldPointer = 0
            ptr = 0
            print("Sending output without suffix...\nDone!")
            return f"{eqString} = {output}"
    

#doMath(input())                        #For testing purposes

"""
Known Issues:
- Starting an equation with an operator causes the program to use the last number in the equation.
    (Index moving to -1 position, the last item in a list.)
- Consecutive operators. An equation having 2 operators after another will result in an unknown error.
"""