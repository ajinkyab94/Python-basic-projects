def unit_converter():
    print("--- ⚖️ युनिट कन्व्हर्टर (Unit Converter) ---")
    print("1. किलोमीटर चे मीटर (km to m)")
    print("2. सेल्सिअस चे फॅरेनहाइट (C to F)")
    print("3. किलो चे ग्राम (kg to g)")
    
    choice = input("\nपर्याय निवडा (1-3): ")
    
    if choice == '1':
        km = float(input("किलोमीटर टाका: "))
        meter = km * 1000
        print(f"✅ {km} km म्हणजे {meter} मीटर.")
        
    elif choice == '2':
        celsius = float(input("सेल्सिअस तापमान टाका: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"✅ {celsius}°C म्हणजे {fahrenheit}°F.")
        
    elif choice == '3':
        kg = float(input("किलो टाका: "))
        gram = kg * 1000
        print(f"✅ {kg} किलो म्हणजे {gram} ग्राम.")
        
    else:
        print("❌ चुकीचा पर्याय!")

unit_converter()
