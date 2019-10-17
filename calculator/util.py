#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
