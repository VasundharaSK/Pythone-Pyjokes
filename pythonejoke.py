# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:29:07 2020

@author: VK
"""

import time
import pyjokes
Name = input("Enter your name: ")
time.sleep(2)

print("Hi {} How can i help you!!".format(Name))
time.sleep(2)

print("Hey Python can you tell me a joke ")
time.sleep(2)

print("Sure here is your joke hope it makes you feel better")
time.sleep(2)

print(pyjokes.get_joke('en','all'))