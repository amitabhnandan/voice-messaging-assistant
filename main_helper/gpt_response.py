# WRITE YOUR CODE HERE
from openai import OpenAI

from pathlib import Path

# Initialize OpenAI client with your API key
client = OpenAI()

# Function to generate spoken audio using OpenAI API
def generate_spoken_audio(text, voice, file_name='response.mp3'):
    # Path to save the audio file
    speech_file_path = Path(__file__).parent / file_name
    
    # Generate the spoken audio
    response = client.audio.speech.create(
        model='tts-1',
        voice=voice.lower(),  # Lowercase the user input for voice
        input=text
    )
    
    # Save the audio file
    with open(speech_file_path, 'wb') as f:
        for chunk in response.iter_bytes():
            f.write(chunk)
    
    print(f"Audio saved to {speech_file_path}")
    return speech_file_path

# Function to interact with GPT-4 and get a response
def get_gpt_response(user_input, user_name, ai_name):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant to {user_name}. Name {ai_name}. You like to keep your messages short but friendly."},
            {"role": "user", "content": user_input},
        ]
    )
    return response.choices[0].message['content']

# Continuous interaction loop
def interaction_loop(user_preferences):
    user_name = user_preferences['user_name']
    ai_name = user_preferences['ai_name']
    chosen_voice = user_preferences['voice']

    print(f"{ai_name}: Ready to get started! What can I help you with?")

    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() == "bye":
            print(f"{ai_name}: Goodbye, {user_name}!")
            break
        
        ai_response = get_gpt_response(user_input, user_name, ai_name)
        generate_spoken_audio(ai_response, chosen_voice, file_name='response.mp3')
        
        print(f"{ai_name}: {ai_response}")
        print(f"{ai_name}: Anything else I can do for you?")

# Assuming user_preferences is already set from the setup function
interaction_loop(user_preferences)