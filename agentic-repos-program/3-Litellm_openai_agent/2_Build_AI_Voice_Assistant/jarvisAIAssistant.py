# Import required libraries

import speech_recognition as sr        # For converting voice input to text
import pyttsx3                         # For converting text to speech
from litellm import completion         # LiteLLM library to call LLMs like Gemini, GPT etc.
import os                              # For environment variable access
from dotenv import load_dotenv         # For loading API keys securely from .env file

# Step 1: Load environment variables from .env file
# This lets you access your Gemini API key without hardcoding it into your Python file
load_dotenv()  # Ye function .env file se environment variables ko load karta hai

# Step 2: Set Gemini API key for LiteLLM to use
# os.getenv reads the variable from .env, and os.environ sets it for the runtime
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Step 3: Initialize Text-to-Speech engine using pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Set speech rate/speed (lower = slower, higher = faster)

# Step 4: Function to speak a given text aloud using text-to-speech
def speak(text):
    engine.say(text)         # Load the text into the voice engine
    engine.runAndWait()      # Speak the text aloud

# Step 5: Function to listen for user’s voice and convert it into text
def take_command():
    r = sr.Recognizer()      # Initialize recognizer
    with sr.Microphone() as source:    # Use microphone as input source
        print("Listening...")          # Show listening prompt
        audio = r.listen(source)       # Listen to the audio from user
    
    try:
        print("Recognizing...")        # Attempting to convert audio to text
        query = r.recognize_google(audio)  # Use Google’s speech recognition API
        print(f"You said: {query}")         # Show what user said
        return query
    except sr.UnknownValueError:       # If speech is not recognized
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:            # If Google API is not reachable
        print("Could not request results from Google.")
        return ""

# Step 6: Function to get AI response using LiteLLM and Gemini
def ai_reply(prompt):
    response = completion(
        model="gemini/gemini-1.5-flash",         # Using Gemini 1.5 Flash model
        messages=[{"role": "user", "content": prompt}]  # Send the prompt as user message
    )
    # Return only the content part of the AI's response
    return response["choices"][0]["message"]["content"]

# Step 7: Main assistant loop - keeps listening and responding
def run_jarvis():
    while True:
        query = take_command()  # Listen to user's voice and convert to text
        
        # If user says "exit", "quit" or "stop" then break the loop
        if query.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye! Have a nice day!")
            break
        
        # If query was successfully recognized
        if query:
            reply = ai_reply(query)  # Get AI's response using Gemini
            print(f"Jarvis: {reply}")  # Print it on screen
            speak(reply)              # Speak it aloud

# Step 8: Start the assistant
run_jarvis()  # Run the assistant by calling the function


#In terminal:
# python jarvisAIAssistant.py