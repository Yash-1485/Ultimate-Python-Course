import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def listen_until_speech():
    with sr.Microphone() as source:
        print("Listening for audio input...")

        while True:
            # Listen for audio
            audio = recognizer.listen(source)
            try:
                # Recognize speech using Google's API
                text = recognizer.recognize_google(audio)
                
                # Check if text is not empty
                if text:
                    print("You said:", text)
                    return text  # Exit function if speech is detected

            except sr.UnknownValueError:
                # Speech not recognized, continue listening
                print("Waiting for valid speech...")

            except sr.RequestError as e:
                # Error in the request, possibly connectivity issues
                print(f"Could not request results; {e}")
                break  # Optionally break or handle the error

# Call the function
listen_until_speech()
