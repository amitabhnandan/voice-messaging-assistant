# WRITE YOUR CODE HERE
from datetime import datetime

def format_date(date):
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    if 10 <= date.day <= 20 or date.day % 10 not in suffixes:
        suffix = 'th'
    else:
        suffix = suffixes[date.day % 10]
    return date.strftime(f"%B {date.day}{suffix}, %Y")

# Example usage
date = datetime(2024, 6, 21)
print(format_date(date))  # Output: June 21st, 2024

from datetime import datetime
from main_helper.date_utils import format_date

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

import random
from main_helper.greetings import get_greetings
from main_helper.date_utils import format_date

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