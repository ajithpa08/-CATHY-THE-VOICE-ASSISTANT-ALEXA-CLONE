import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('I am your Cathy')
engine.say('What can I do for you')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone(device_index=0, sample_rate=44100, chunk_size=1024) as source:
            listener.adjust_for_ambient_noise(source)
            print('Listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'cathy' in command:
                command = command.replace('cathy', '')
            else:
                if 'stop' in command:
                    talk("Listening stopped")
                    print("Listening stopped.")
                    return "stop"  # Signal to stop the assistant loop
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        talk("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("There was an error with the speech recognition service.")
        talk("There was an error with the speech recognition service.")
    return command

def run_cathy():
    while True:
        command = take_command()
        if command == "stop":
            break  # Exit the loop when the user says "stop"
        elif 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
            print("Command:", command)
        elif 'what is the time' in command:
            time = datetime.datetime.now().strftime('%H:%M %p')
            talk('Current time is ' + time)
            print('Time is:', time)
        elif 'information about' in command:
            person = command.replace('information about', '')
            info = wikipedia.summary(person,2)
            print(info)
            talk(info)
        else:
            print('please say the command again')
if __name__ == "__main__":
    run_cathy()
