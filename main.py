import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak():
    text = input("Enter the text you want to hear: ")
    say(text)

if __name__ == '__main__':
    print('PyCharm')
    say("Enter the text you want to hear: ")
    speak()
