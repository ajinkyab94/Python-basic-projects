from gtts import gTTS
import os

# १. शब्दांचा साठा (Dictionary)
dictionary = {
    "success": "यश",
    "hardwork": "कष्ट",
    "coding": "संगणक प्रणाली लेखन",
    "dream": "स्वप्न",
    "goal": "ध्येय",
    "education": "शिक्षण"
}

def translate_and_speak():
    print("🤖 जार्विस: मी तुम्हाला शब्दांचे अर्थ सांगू शकतो.")
    print("उपलब्ध शब्द: success, hardwork, coding, dream, goal, education")
    
    word = input("इंग्रजी शब्द टाईप करा: ").lower()

    if word in dictionary:
        martha_meaning = dictionary[word]
        result = f"{word} चा मराठीत अर्थ होतो, {martha_meaning}"
        print(f"✅ {result}")
        
        # आवाज तयार करणे
        tts = gTTS(text=result, lang='mr')
        tts.save("translator.mp3")
        print("📢 'translator.mp3' तयार झाली आहे, ऐकून पहा!")
    else:
        print("❌ क्षमस्व, हा शब्द माझ्या शब्दकोशात नाही.")

# रन करा
translate_and_speak()
