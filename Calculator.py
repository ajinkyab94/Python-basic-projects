while True:
    print("\n--- ॲडव्हान्स कॅल्क्युलेटर ---")
    print("1. बेरीज (+)")
    print("2. वजाबाकी (-)")
    print("3. गुणाकार (*)")
    print("4. भागाकार (/)")
    print("5. प्रोग्राम बंद करा (Exit)")

    paryay = input("\nतुमचा पर्याय निवडा (1-5): ")

    if paryay == '5':
        print("कॅल्क्युलेटर वापरल्याबद्दल धन्यवाद! बाय बाय!")
        break  # यामुळे लूप थांबेल आणि प्रोग्राम बंद होईल

    a = int(input(" 7 : "))
    b = int(input(" 9 : "))

    if paryay == '1':
        print("निकाल (बेरीज):", a + b)
    elif paryay == '2':
        print("निकाल (वजाबाकी):", a - b)
    elif paryay == '3':
        print("निकाल (गुणाकार):", a * b)
    elif paryay == '4':
        print("निकाल (भागाकार):", a / b)
    else:
        print("क्षमस्व! चुकीचा पर्याय.")
