# Import necessary libraries
import openai
import speech_recognition as sr
import pyttsx3

# Assign OpenAI API key
openai.api_key = "YOUR OPENAI KEY"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Loop to listen for audio input
while True:
    # Create speech recognizer object
    r = sr.Recognizer()

    # Listen for input
    with sr.Microphone() as source:
        print("Speak now:")
        audio = r.listen(source)

    # Try to recognize the audio
    try:
        prompt = r.recognize_google(audio, language="en-EN", show_all=False)
        print("You asked:", prompt)

        # Use OpenAI to create a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300
        )

        # Get the response text
        response_text = str(response['choices'][0]['text']).strip('\n\n')
        print(response_text)

        # Speak the response
        engine.say(response_text)
        engine.runAndWait()
        print()

    # Catch if recognition fails
    except:
        response_text = "Sorry, I didn't get that!"
        print(response_text)
        engine.say(response_text)
        engine.runAndWait()
        print()
