import pygame
from gtts import gTTS
import time

def speak(text):
    print(f"Jarvis: {text}")
    tts = gTTS(text=text, lang='en')
    tts.save("reply.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("reply.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.quit()

# मुख्य प्रोग्राम
speak("Hello sir! I am ready. Please type your command below.")

try:
    while True:
        # Pydroid च्या खालच्या पट्टीतील 'Console' मध्ये टाईप करा
        query = input("You: ").lower().strip()
        
        if "hello" in query:
            speak("Hello sir! You are a coding warrior.")
        elif "exit" in query:
            speak("Goodbye sir, take some rest now.")
            break
        elif query == "":
            continue
        else:
            speak("I am listening, but still learning.")
except EOFError:
    print("In-put मध्ये अडचण आली, कृपया पुन्हा रन करा.")
