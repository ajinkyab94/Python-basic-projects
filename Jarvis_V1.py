import requests
import datetime

def get_weather():
    # तुझा Level 10 चा कोड
    city = "Alibag"
    url = f"https://wttr.in/{city}?format=3"
    res = requests.get(url)
    return res.text

def get_joke():
    # तुझा Level 9 का कोड
    url = "https://official-joke-api.appspot.com/random_joke"
    res = requests.get(url).json()
    return f"{res['setup']} - {res['punchline']}"

def jarvis_brain():
    print("--- 🤖 अजिंक्यचा जार्विस सक्रिय झाला आहे ---")
    
    while True: # हा लूप जार्विसला जिवंत ठेवेल
        query = input("\nमी तुमची काय मदत करू शकतो? (type 'exit' to stop): ").lower()
        
        if "weather" in query or "हवामान" in query:
            print("☁️ तपासत आहे...")
            print(get_weather())
            
        elif "joke" in query or "जोक" in query:
            print("🤣 हा घ्या जोक:")
            print(get_joke())
            
        elif "time" in query or "वेळ" in query:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🕒 सध्याची वेळ: {now}")
            
        elif "exit" in query or "थांब" in query:
            print("👋 निरोप घेतो, अजिंक्य सर! तुमची रात्र शुभ असो.")
            break # लूपमधून बाहेर पडण्यासाठी
            
        else:
            print("क्षमा करा, मला हे अजून समजले नाही. मी अजून शिकतोय!")

# जार्विस सुरू करा
jarvis_brain()
