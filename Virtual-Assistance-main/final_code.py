import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import pyautogui

from email.message import EmailMessage
import ssl
import smtplib

from googlesearch import search

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jack, your virtual assistant.")

def username():
    speak("What should i call you")
    uname = takeCommand()
    print("Welcome ", uname)
    speak(f"welcome {uname}")
     
    speak("How can I help you")

def tellDay():
	
	day = datetime.datetime.today().weekday() + 1
	
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print("The day is ",day_of_the_week)
		speak("The day is " + day_of_the_week)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say it again")
        return "None"
    return query 


def sendEmail(content):
    email_sender = 'talkwithfayaz@gmail.com'
    email_password = 'zelplqchdsckowoi'

    email_receiver='uyyalaajay811@gmail.com'

    subject = "Sample"
    body = content

    em=EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['subject']=subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

if __name__ == "__main__":
    wishMe()
    # username()
    # while True:
    if 1:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'google' in query:
            speak('Searching in Google...')
            query=query.replace("google", "")
 
        elif 'open youtube' in query:
            print("Opening YouTube\n")
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            print("Opening Google\n")
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open vs code' in query:
            print("Opening VS Code\n")
            speak("Opening VS Code")
            codePath = "C:\\Users\\Ajay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query: 
            print("Opening Chrome\n")
            speak("Opening Chrome")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)    

        elif 'play music' in query or 'play song' in query:
            music_dir = 'C:\\Users\\Ajay\\OneDrive\\Desktop\\Fayaz\\Songs'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 7)]))

        elif 'day' in query or 'today' in query:
            tellDay()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Time is ",strTime) 
            speak(f"The time is {strTime}")

        elif 'bye' in query:
            print("See you later. Have a nice day.\n")
            speak("See you later. Have a nice day.")
            exit()

        elif 'how are you' in query:
            print("I am fine Thank you\n")
            speak("I am fine Thank you")
            print("How are you, Sir\n")
            speak("How are you, Sir")

        elif 'fine' in query or 'good'   in query:
            print("It's good to know that your fine\n")
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            print("I have been created by team of software engineers\n")
            speak("I have been created by team of software engineers")
        
        elif "will you be my gf" in query or "will you be my bf" in query:
            print("I'm not sure about, may be you should give me some time\n")
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            print("It's hard to understand\n")
            speak("It's hard to understand")

        elif 'email' in query or 'send mail' in query:
            try:
                print("What should I send?\n")
                speak("What should I send?")
                content=takeCommand()
                sendEmail(content)
                print("Email has been sent!\n")
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry, I'm not able to send this email\n")

        elif 'note' in query:
            print("What should I note?\n")
            speak("What should I note?")
            text=takeCommand()
            fh=open('text.txt','w')
            fh.write(text)
            fh.close()
            print("Notes have been taken!\n")
            speak("Notes have been taken!")
        elif 'news' in query:
            print("Displaying News\n")
            speak("Displaying News")
            webbrowser.open("https://news.google.com/home?gl=IN&hl=en-IN&ceid=IN:en")

        elif 'screenshot' in query:
            img=pyautogui.screenshot()
            img.save(r"C:\\Users\\Ajay\\OneDrive\\Desktop\\Fayaz\\Project Jack\\image1.png")
            print("Screenshot Taken!\n")
            speak("Screenshot Taken!")

        elif 'joke' in query:
            jk = random.randint(0, 5)
            if jk == 0:
                print("What do you call a boomerang that won’t come back?")
                speak("What do you call a boomerang that won’t come back?")
                print("stick")
                speak("stick")

            elif jk == 1:
                print("What time is it when the clock strikes 13?")
                speak("What time is it when the clock strikes 13?")
                print("Time to get a new clock.")
                speak("Time to get a new clock.")

            elif jk == 2:
                print("What is a computer's favorite snack?")
                speak("What is a computer's favorite snack?")
                print("Computer chips.")
                speak("Computer chips.")

            elif jk == 3:
                print(" What kind of tree fits in your hand?")
                speak(" What kind of tree fits in your hand?")
                print("Palm tree")
                speak("Palm tree")

            elif jk == 4:
                print("What's red and smells like blue paint?")
                speak("What's red and smells like blue paint?")
                print("Red paint!")
                speak("Red paint!")

            elif jk == 5:
                print("I'm so good at sleeping I can do it with my eyes closed!")
                speak("I'm so good at sleeping I can do it with my eyes closed!")

            speak("hahhahaha")
        elif 'set timer' in query or 'timer' in query or ' countdown ' in query:
            print("For How Many Seconds ")
            speak("For How Many Seconds ")
            sec =int(takeCommand())
            while sec>0:
                print(sec)
                speak(sec)
                sec -= 1
                time.sleep(1)
            print("Time's Up\n")
            speak("Time's Up")
        else:
            print("Oops! My Team forgot to add this function in me ,please try another \n")
            speak("Oops! My Team forgot to add this function in me ,please try another ")
