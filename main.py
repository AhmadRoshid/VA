import speech_recognition as AR
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import calendar

listener = AR.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.say('Hello , im your assistant')
engine.say('What can I do for you ? ')
print('Hello , im your assistant')
print('What can I do for you ? ')
engine.runAndWait()

def talk(text1):
    try:
        engine.say(text1)
        engine.runAndWait()
    except:
        pass

def take_command():
    try:
        with AR.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='id-ID')
            command = command.lower()
            if 'calypso' in command:
                command = command.replace('calypso', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        now = datetime.datetime.now()
        my_date = datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()]
        monthNum = now.month
        dayNum = now.day
        month_name = ['January, ', 'February, ', 'March, ', 'April, ', 'May, ', ' June, ',
                      'July, ', 'August, ', 'September, ', 'October, ', 'November, ', 'December, ']
        ordinalNumbers = [' 1st, ', ' 2nd ', ' 3rd, ', ' 4th, ', ' 5th, ', ' 6th, ', ' 7th, ', ' 8th, ', ' 9th, ',
                          ' 10th, ', ' 11th, ', ' 12th, ', ' 13th, ', ' 14th, ', ' 15th, ', ' 16th, ', ' 17th, ',
                          ' 18th, ', ' 19th, ', ' 20th, ', ' 21th, ', ' 22th, ', ' 23th, ', ' 24th, ', ' 25th, ',
                          ' 26th, ', ' 27th, ', ' 28th, ', ' 29th, ', ' 30th, ', ' 31th, ']
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(month_name[monthNum - 1] + weekday + ordinalNumbers[dayNum - 1] + time)
        talk('Current time is ' + month_name[monthNum-1] + weekday + ordinalNumbers[dayNum -1] + time)
    elif 'what' in command:
        what = command.replace('what ', '')
        info = wikipedia.summary(what, 1)
        pywhatkit.search(info)
        print(info)
        talk(info)
    elif 'weather' in command:
        info_weather = command
        pywhatkit.search(info_weather)
        print(info_weather)
        talk(info_weather)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'help' in command:
        print('yes sir!')
        talk('yes sir!')
    elif 'who is' in command:
        who = command.replace('who is', '')
        whois = wikipedia.summary(who, 1)
        pywhatkit.search(whois)
        print(whois)
        talk(whois)
    elif 'thank you' in command:
        print('Your welcome sir')
        talk('your welcome sir')
        quit()
    else:
        talk('say the command again...')

while True:
    run_alexa()
    print('\n' * 20)
    ask = 'anything else sir ?'
    print(ask)
    talk(ask)
