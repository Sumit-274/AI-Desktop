import speech_recognition as sr
import pyttsx3 as pt3
import webbrowser as brower
import os

def Login(password):
    exact_password = 789
    if password == exact_password:
        print("Your Password is correct")
        while True:
            pass
    else:
        return "Your Parpssword is incorrect"
        exit()

if __name__ == "__main__": 
    inp = int(input())
    Login(inp)
