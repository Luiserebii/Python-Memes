#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from calc import Calculator
from util import list_to_string

# Settings
FUNCTIONS_SUPPORTED = ["add", "sub", "mul", "div", "power"]

# Loop for input
def main(): 
    print("Hello! Welcome~")
    print("Please enter the kind of function you would like to use.")
    print("Currently supported functions are: \n" + list_to_string(FUNCTIONS_SUPPORTED))
    
    sel = input("Select an option: ")

    # Apply logic based on selection
    if(sel == "add"):
        print("Specify two numbers, a and b")
        a = input("a: ")
        b = input("b: ")
        # Cast numbers to float via function, then add
        res = Calculator.add(float(a), float(b))
        print("Result: " + str(res))

    elif(sel == "sub"):
        print("Specify two numbers, a and b");
        a = input("a: ")
        b = input("b: ")
        res = Calculator.sub(float(a), float(b))
        print("Result " + str(res))

    elif(sel == "mul"):
        print("Specify two numbers, a and b");
        a = input("a: ")
        b = input("b: ")
        res = Calculator.mul(float(a), float(b))
        print("Result " + str(res))

    elif(sel == "div"):
        print("Specify two numbers, a and b");
        a = input("a: ")
        b = input("b: ")
        res = Calculator.div(float(a), float(b))
        print("Result " + str(res))

    elif(sel == "power"):
        print("Specify two numbers, a and b");
        a = input("a: ")
        b = input("b: ")
        res = Calculator.power(float(a), float(b))
        print("Result " + str(res))
        
    else: 
        print("Function \"" + sel + "\" not implemented.")

# Execute our program
main()
