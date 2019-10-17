#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Calculator: 
    """
    A static Calculator class, not meant to be instantiated.
    """

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


# Helper functions, esp. for printing
def list_to_string(l):
    """
    Takes a list, returns a formatted version of each element
    in the list as a string. Generally, each one will be indented
    by *. 
    """
    s = ""
    for i in l:
        s += "   * " + i + "\n"
    return s

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
