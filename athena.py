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


engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices)
#by default system provides us with 2 vpices which can be accessed by voices[0] or voices[1]
#print(voices[0].id) o/p-> david(male)
#print(voices[1].id) o/p-> zira(female)

engine.setProperty('voice',voices[1].id)

#for speaking 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening")
    
    speak("I am Athena, please tell me what can I do for you today?")

#makeing a take command function
#for taking icrophone input from the user and give string output
def takeCommand():
    #taking audio and converting it to string or none
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #using it as a source microphone
        print("listening...")
        #listening
        #for pausing for a second
        r.pause_threshhold=1
        audio=r.listen(source)
    try:
        #if any issue
        print("recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said:- :{query}\n")
        #creating a fstring
    except Exception as e:
        #throws exception
        #print(e) as it cant recognize
        print("say that again please...")
        return 'none'
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',586)
    server.ehlo()
    server.startls()
    server.login('999.atulsingh@gmail.com','your_password')
    #not secure
    server.sendmail('999.atulsingh@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while 2:
        query=takeCommand().lower()
        #logic for executing tasks as per query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            #how many sentences we want to parse
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open goegle' in query:
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open chatgpt' in query:
            webbrowser.open("chatgpt.com")
        elif 'play music' in query:
            music_dir='C:\\mine\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strfttime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            #os module is used to open any folder or application
            codePath="C:\\Users\\DADDY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email to harry' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to="999.atulsingh@gmail.com"
                sendEmail(to,content)
                speak("email has been seny!")
            except Exception as e:
                print(e)
                speak("sorry atul, i am not able to send the mail")



            #