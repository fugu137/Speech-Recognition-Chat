import speech_recognition as sr

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    print("Hi, what should I call you?")
    audio = r.listen(source)
    
try:
    name = r.recognize_google(audio, language='en')
    print("Hi {}, how are you?".format(name))

    with mic as source:
        audio2 = r.listen(source)

    response = r.recognize_google(audio2)
    
    if "how are you" in response:
        print("I'm well, thanks!")
    else:
        print("Nice to meet you!")

except Exception as e:
    print("Error" + e)

