import pyttsx3


if __name__=="__main__":
    print("Welcome to RoboSpeaker")
    while True:
        x=input("Enter what you want to say:")
        engine=pyttsx3.init()
        if x=="quit":
            y="Bye Bye Friends"
            engine.say(y)
            engine.runAndWait()
            break
        
    
        # Set Properties
        engine.setProperty("rate",150)
        engine.setProperty("Volume",100)
    
        # Speak the text
        engine.say(x)
        engine.runAndWait()



