import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Ahmad. You are a good and friendly  and a smart assistant who helps students learn about technology and math. You explain things clearly and always encourage curiosity."
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()
#lab1:
#chatgbt is more genural but this app is more specific
#refliction lab1:
#my beilives 
#the program wont remember the conversation with the user
#it doesnt  have the api soo it went go to claude and get the answers
#the cnversation stops (the program ends)
#the api code didnt work so i asked for a new one
