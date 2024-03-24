import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your Assistant')
engine.say('What can I do for you')
engine.runAndWait()


#talk function speak the command
def talk(text):
    engine.say(text)   
    engine.runAndWait()


#take_command function takes command make it useful
def take_command():
    try:
       with sr.Microphone() as source:
         print("Listening...")
         voice = listener.listen(source)
         command = listener.recognize_google(voice)
         command = command.lower()
         if 'alexa' in command:
            command = command.replace('alexa', '')
            talk(command)
         print(command)

    except:
        pass
    return command

#plays the song provided by user
def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        print(time)
        talk('Current time is '+time)
    
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'jokes' or 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'are you single' in command:
        talk('I am in relationship with wifi')

    elif 'Thank you' or 'ok bye' in command:
        talk('welcome, see you again')
        return False
        
    else:
        print("I can't understand, please say again")
        talk("I can't understand, please say again")
        

#calling the function run_alexa

while True:
   if run_alexa():
    break