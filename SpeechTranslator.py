import speech_recognition as sp
import pyttsx3 as tts
import googletrans as gt
import pyaudio
def speak(s):
    engine=tts.init()
    engine.setProperty("rate",150)
    voices=engine.getProperty("voices")
    engine.setProperty("volume",0.8)# setting up volume level  between 0 and 1
    #print(engine.getProperty("volume"))
    engine.setProperty("voice",voices[1].id)
    engine.say(s)
    engine.runAndWait()
    engine.stop()
def getlang():
    s= input("Enter the language to Translate : ")
    c= gt.LANGUAGES  #Dictionary of languages
    for i,j in c.items():
        if j==s.lower():
            return i

def translate(s,lang):
    translator= gt.Translator()
    translation=translator.translate(s,dest=lang)
    return translation.text


def speaktext():
    recog= sp.Recognizer()
    mic=sp.Microphone()
    ##Speak to Text
    t=0
    while True:  #Infinite loop so that user can say easily
        #Exception Handlind
        try:
             #Use Micropohone as input
             with mic as source:
                 #Wait for a sec and ajust noice error
                 recog.adjust_for_ambient_noise(source,duration=0.2)
                 print("Say RL to start")
                 print("~~~~~~~~~~~~~~~~~~~~~~")
                 audio= recog.listen(source)
                 text=recog.recognize_google(audio)
             if text.lower()=="rl":
                speak("HI THATS ME R.L. 1.0 TELL ME ASENTENCE TO TRANSLATE")
                while True:
                    print("~~~~~~~~~~~~~~~~~~~~~~ Say Sentence")
                    try:
                        with mic as source1:
                            recog.adjust_for_ambient_noise(source1,duration=0.2)
                            audio1=recog.listen(source1)
                            getsentence=recog.recognize_google(audio1)  #Sentence to tramslate
                            print(getsentence)
                            s=getlang()
                            translation=translate(getsentence,s)
                            print("Translation",translation)
                            speak(translation)
                            print("Want to say more Press 1 or for exit Press 2 : ")
                            ch=int(input())
                            if ch==2:
                                t=111
                                break

                    except sp.RequestError as e:
                        print("Can't Send the request {} 1.1".format(e))
                    except sp.UnknownValueError:
                        print("Unknwon error occur say again 1.1")




        except sp.RequestError as e:
            print("Can't Send the request {}".format(e))
            t=1
        except sp.UnknownValueError:
            print("Unknwon error occur say again ")
            t=1
        if t==111:
            return 0


speaktext()