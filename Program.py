import speech_recognition as sr
import pyttsx3 as pt3
import webbrowser as brower
import wikipedia

def Login(password):
    exact_password = 789
    if password == exact_password:
        print("Your Password is correct")
    else:
        return "Your Parpssword is incorrect"
        exit()

def Speak(string):
    engine = pt3.init()
    engine.say(string)
    engine.runAndWait()

def Search(Name):
    return wikipedia.summary(Name)
    
if __name__ == "__main__": 
    inp = int(input())
    Login(inp)
    Speak("My name is sumit")
