#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:32:11 2019

@author: luiserebii
"""

class Meme: 
     def __init__(self, name, tag, value):
         self.name = name;
         self.tag = tag;
         self.value = value;
     def getName(self):
         return self.name;
     def getTag(self):
         return self.tag;
     def getValue(self):
         return self.value;
     def toString(self):
         string = self.name + " " + self.tag + " " + str(self.value);
         return string;
    
    
m = Meme("uguu", "gog", 100);
print(m.toString());