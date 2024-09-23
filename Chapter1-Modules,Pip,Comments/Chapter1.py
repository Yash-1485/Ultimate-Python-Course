# print("Hello World!")

# import pyjokes as pj
# joke=pj.get_joke()
# print(joke)#Why do Java programmers have to wear glasses? Because they don't C#.

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello sir, what i can do for you?")
# engine.runAndWait()

import os
files=os.listdir('D:/')
# print(files)
print(type(files))
for file in files:print(file)