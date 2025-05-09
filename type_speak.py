import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set speech rate (normal human-like is around 150-175)
engine.setProperty('rate', 160)  # You can tweak this value

print("Type something and press Enter. Type 'exit' to quit.")

while True:
    text = input("You: ")
    if text.lower() == 'exit':
        break
    engine.say(text)
    engine.runAndWait()
