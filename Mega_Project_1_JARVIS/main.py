import speech_recognition as sr, webbrowser as wb, pyttsx3 as ps, musicLibrary as ms
music=ms.music
recognizer=sr.Recognizer()
engine=ps.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c:str):
    # print(c)
    if c.lower()=='open google':wb.open('https://www.google.com')
    elif c.lower()=='open youtube':wb.open('https://www.youtube.com')
    elif c.lower()=='open linkedin':wb.open('https://www.linkedin.com')

    elif c.lower().startswith('play music'):
        wb.open(music[c.lower().split(' ')[2]])

if __name__=="__main__":
    speak("Initializing JARVIS...")
    r=sr.Recognizer()
    while True:
        #Listen for the wake word 'JARVIS'        
        try:
            #obtaining audio from microphone
            with sr.Microphone() as source:
                print('Listening...')
                while True:
                    try:
                        audio=r.listen(source,timeout=None,phrase_time_limit=5)
                        word=r.recognize_google(audio)                        
                        if word:
                            # print(word)
                            break
                    except Exception as e:pass
            # print(word)
            print('Recognizing...')
            if 'jarvis' in word.lower() or 'switch on' in word.lower():
                speak('Sir...')
                with sr.Microphone() as source:
                    print('JARVIS Activated...')
                    while True:
                        try:
                            print('JARVIS IS LISTENING...')
                            audio=r.listen(source,timeout=None,phrase_time_limit=5)
                            command=r.recognize_google(audio)
                            if command:
                                print('JARVIS is recognizing...')
                                # print(command)
                                process_command(command)
                            if 'switch off' in command.lower():
                                speak('Have a good day sir...')
                                break
                        except Exception as e:pass
            elif 'switch off' in word.lower() or 'switch off' in command.lower():
                speak('Have a good day sir...')
                break
        except Exception as e:print(e)

