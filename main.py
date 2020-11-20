import pyttsx3
engine = pyttsx3.init()
engine.say("Hello !")
engine.runAndWait()

num = input("Please enter a number: ")
num2 = input("Please enter another number: ")
total = int(num) + int(num2)
total = str(total)

engine = pyttsx3.init()
engine.say("The total is: " + total)
engine.runAndWait()

