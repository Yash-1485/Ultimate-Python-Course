import speech_recognition as sr, webbrowser as wb, pyttsx3 as ps, musicLibrary as ms,sys, pyautogui as pg, requests as req    
import pygame,os
from gtts import gTTS
music=ms.music
recognizer=sr.Recognizer()
engine=ps.init()
news_api="d9524a8c976943d48e9fa008c5c93cbb"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts=gTTS(text)
    tts.save('temp.mp3')
    

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load("temp.mp3")  # Replace with your file path

    # Play the audio
    pygame.mixer.music.play()

    # Wait until the music finishes playing
    while pygame.mixer.music.get_busy():  # Check if the music is still playing
        pygame.time.Clock().tick(10)      # Wait briefly to avoid high CPU usage
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove('temp.mp3')


def process_command(c:str):
    # print(c)
    if c.lower()=='open google':wb.open('https://www.google.com')
    elif c.lower()=='open youtube':wb.open('https://www.youtube.com')
    elif c.lower()=='open linkedin':wb.open('https://www.linkedin.com')

    elif c.lower().startswith('play music'):
        wb.open(music[c.lower().split(' ')[2]])
    
    # if c.lower()=='forward':pg.hotkey('ctrl','tab')
    # elif c.lower()=='backward':pg.hotkey('ctrl','shift','tab')
    # elif c.lower()=='close tab':pg.hotkey('ctrl','W')    
    # elif c.lower()=='close':pg.hotkey('alt','f4')
    # elif c.lower()=='play' or c.lower()=='pause':pg.press('space')
    # elif c.lower()=='volume down':pg.hotkey('fn','f8')
    # elif c.lower()=='volume up':pg.hotkey('fn','f7')
    # elif c.lower()=='mute':pg.hotkey('fn','f6')
    # elif c.lower()=='scroll up':pg.scroll(500)
    # elif c.lower()=='scroll down':pg.scroll(-500)
    # elif c.lower()=='press':pg.press('enter')
    
    elif 'news' in c.lower():
        try:
            response = req.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            
            articles = data.get('articles', [])
            if not articles:
                print("No news articles found.")
                return
            
            for i, article in enumerate(articles[:5], start=1):  # Limit to top 5 articles
                title = article.get('title', 'No Title')
                print(f"{i}. {title}")
                speak(title)  # Assuming `speak` is a defined function for text-to-speech
        except req.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")

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
                                sys.exit()
                        except Exception as e:pass
            elif 'switch off' in word.lower():
                speak('Have a good day sir...')
                break
        except Exception as e:print(e)

