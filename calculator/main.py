#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Calculator: 

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a - b

    @staticmethod
    def div(a, b):
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b;


# Helper for printing
def list_to_string(l):
    s = ""
    for i in l:
        s += "   *" + i + "\n"
    return s

# Settings
FUNCTIONS_SUPPORTED = ["add", "sub", "mul", "div", "power"]

# Loop for input
def main(): 
    print("Hello! Welcome~")
    print("Please enter the kind of function you would like to use.")
    print("Currently supported functions are: \n" + list_to_string(FUNCTIONS_SUPPORTED))
    
    sel = input("Select an option: ")
    if(sel == "add"):
        print("Specify two numbers, a and b")
        a = input("a: ")
        b = input("b: ")
        # Cast numbers to float via function, then add
        res = Calculator.add(float(a), float(b))
        print("Result: " + str(res))
    else: 
        print("Function \"" + sel + "\" not implemented.")

# Execute our program
main()
