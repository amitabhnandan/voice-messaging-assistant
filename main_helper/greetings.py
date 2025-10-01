# WRITE YOUR CODE HERE
import datetime

#Prepopulated greetings
from datetime import datetime
from main_helper.date_utils import format_date
import random

def get_greetings(user_name, ai_name):
    today_date = format_date(datetime.now())
    greetings = [
        f"Good morning, {user_name}! I'm {ai_name}. Today is {today_date}. Let's have a productive day!",
        f"Hello, {user_name}! This is {ai_name}. The date is {today_date}. How can I assist you today?",
        f"Hi, {user_name}! I'm {ai_name}, your messaging assistant. Today is {today_date}. Ready to get started?",
        f"Hey, {user_name}! {ai_name} here. Today is {today_date}. What can I do for you?",
        f"Good day, {user_name}! I'm {ai_name}. It's {today_date} today. Let's achieve great things together!"
    ]
    return greetings

# List of follow-up questions
follow_up_questions = [
    "Anything else I can do for you?",
    "Is there anything more I can assist you with?",
    "Do you need help with anything else?",
    "Can I help you with something else?",
    "What else can I do for you?"
]

# Function to get a random follow-up question
def get_random_follow_up():
    return random.choice(follow_up_questions)

# List of goodbyes
goodbyes = [
    "Goodbye!",
    "See you later!",
    "Take care!",
    "Bye for now!",
    "Catch you later!"
]

# Function to get a random goodbye
def get_random_goodbye():
    return random.choice(goodbyes)

import random
from main_helper.greetings import get_greetings

# Function to generate a random greeting and convert it to speech
def generate_greeting_audio(user_name, ai_name):
    greetings = get_greetings(user_name, ai_name)
    greeting = random.choice(greetings)
    
    # Generate the spoken audio for the greeting
    audio_path = generate_spoken_audio(greeting, user_preferences['voice'], file_name='greeting.mp3')
    
    # Code to play audio from audio_path (implementation depends on the environment)
    # For example, you can use the playsound library: playsound(str(audio_path))
    
    print(f"Greeting played: {greeting}")

# Assuming user_preferences is already set from the setup function
generate_greeting_audio(user_preferences['user_name'], user_preferences['ai_name'])