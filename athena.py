#installing pyttsx3 
#install speach recognition module
#pyttsx3 is for 
import pyttsx3 
#microsoft has launched this Speech Api for taking voices and use them
import datetime
#importing date time module for the Greetings :)
import speech_recognition as sr
#importing speech recognition library for take command function
import wikipedia
# importing wikipedia for searching the queries
import webbrowser
#for opening any website if needed
import os
#for playing music and opening folders
import smtplib
#smtplib package used to send emails from gmail
import random
import getpass



engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)
#by default system provides us with 2 vpices which can be accessed by voices[0] or voices[1]
#print(voices[0].id) o/p-> david(male)
#print(voices[1].id) o/p-> zira(female)



#for speaking 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    # hour=int(datetime.datetime.now().hour)
    # if hour>=0 and hour<12:
    #     speak("good morning!")
    # elif hour>=12 and hour<18:
    #     speak("good afternoon!")
    # else:
    #     speak("good evening")
    name=getpass.getuser()
    speak(f"HI {name}, I am Athena, how are you?")

#makeing a take command function
#for taking icrophone input from the user and give string output
def takeCommand():
    #taking audio and converting it to string or none
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #using it as a source microphone
        speak("How can I help you today")
        #for pausing for a second
        r.pause_threshhold=1
        audio=r.listen(source)
    try:
        #if any issue
        # print("recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said:- :{query}\n")
        return query
        #creating a fstring
    except sr.UnknownValueError:
        speak("Sorry, I did'nt get that. Could you please repeat that again?")
        return takeCommand()
        #throws exception
        #print(e) as it cant recognize
        # print("say that again please...")
        # return 'none'
    except sr.RequestError:
        speak("Sorry, My speech service is down please try again later")
        return ""
    return query

def searchWiki(query):
    speak("Searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=1)
    speak("According to wikipedia")
    speak(results)

def sendEmail(to,content):
    # server=smtplib.SMTP('smtp.gmail.com',586)
    # server.ehlo()
    # server.startls()
    # server.login('999.atulsingh@gmail.com','your_password')
    # #not secure
    # server.sendmail('999.atulsingh@gmail.com',to,content)
    # server.close()
    try:
        speak("What should I say?")
        content = takeCommand()
        if content != "":
            to = "example@gmail.com"  # replace with a valid email address
            speak("Sending email")
            os.system(f"echo {content} | mail -s 'Subject' {to}")
            speak("Email has been sent!")
    except:
        speak("Sorry, I am not able to complete this request at the moment.")

def openWeb(website):
    speak(f"opening {website}")
    webbrowser.open(website)

def playMusic():
    speak("Playing some music")
    music_dir = 'C:\\mine\\songs'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, random.choice(songs)))


def getTime():
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"It's currently {strTime}, {getpass.getuser()}")

def openCode():
    speak("Opening Visual Studio Code")
    codePath = "C:\\Users\\DADDY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

def tellJoke():
    jokes = ["Why was the math book sad? Because it had too many problems.",
             "Why don't scientists trust atoms? Because they make up everything.",
             "What did one toilet say to the other toilet? You look a bit flushed.",
             "I told my wife she was drawing her eyebrows too high. She looked surprised.",
             "Why don’t skeletons fight each other? They don’t have the guts.",
             "Why did the tomato turn red? Because it saw the salad dressing!",
             "I would tell you a chemistry joke, but I know I wouldn't get a reaction."]
    speak(random.choice(jokes))

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing tasks as per query
        if 'wikipedia' in query:
            searchWiki(query)
            # speak("searching wikipedia...")
            # query=query.replace("wikipedia","")
            # results=wikipedia.summary(query,sentences=1)
            #how many sentences we want to parse
            # speak("according to wikipedia")
            # print(results)
            # speak(results)
        elif 'open youtube' in query:
            openWeb("https://youtube.com")
        elif ' open goegle' in query:
            openWeb("https://google.com")
        elif ' open gmail' in query:
            openWeb("https://gmail.com")
        elif 'athena open chatgpt' in query:
            openWeb("https://chatgpt.com")
        elif 'play music' in query:
            playMusic()
            # music_dir='C:\\mine\\songs'
            # songs=os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))
        elif ' time' in query:
            # strTime=datetime.datetime.now().strftime("%H:%M:%S")
            # speak(f"the time is {strftime}")
            getTime()
        elif 'open code' in query:
            #os module is used to open any folder or application
            openCode()
            # codePath="C:\\Users\\DADDY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            # os.startfile(codePath)
        elif 'send email ' in query:
            sendEmail()
        elif 'stop' in query or 'exit' in query:
            speak("GOODBYE!")
            break
            # try:
            #     speak("what should i say")
            #     content=takeCommand()
            #     to="999.atulsingh@gmail.com"
            #     sendEmail(to,content)
            #     speak("email has been seny!")
            # except Exception as e:
            #     print(e)
            #     speak("sorry atul, i am not able to send the mail")