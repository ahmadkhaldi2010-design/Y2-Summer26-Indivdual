import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url=os.getenv("ANTHROPIC_BASE_URL"),
)

def run_chat():
    print('You: (type exit to quit)')

    system_message ="""You are Ahmad, an AI assistant for MEET students. Your job is to help students understand programming, technology, and computer science. Rules:- Always explain your answers clearly.- Always encourage learning.- Never give an answer without an explanation.Response format:- Start with a one-sentence summary of the user's question.- Then explain the answer.- End with one follow-up question."""

    history = []

    total_input = 0
    total_output = 0

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        print('History so far:', history)

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0,
            system=system_message,
            messages=history
        )

        print(response)

        reply = response.content[0].text
        print(f'Claude: {reply}')

        history.append({'role': 'assistant', 'content': reply})

        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens

        total_input += input_tokens
        total_output += output_tokens

        print(f'Tokens - In: {input_tokens} | Out: {output_tokens} | Total: {input_tokens + output_tokens}')

        print(f'Running Total: {total_input + total_output}')

        cost = (total_input / 1000000 * 0.25) + (total_output / 1000000 * 1.25)

        print(f'Estimated Cost: {cost * 100:.5f} cents')

run_chat()


#lab1:
#chatgbt is more genural but this app is more specific
#refliction lab1:
#my beilives 
#the program wont remember the conversation with the user
#it doesnt  have the api soo it went go to claude and get the answers
#the cnversation stops (the program ends)
#the api code didnt work so i asked for a new one
#-------------------ahmad khaldi lab 2 reflection-------------------------------
#when i changed tocins to 50 ,The response was cut off before it finished because the AI reached the maximum token limit. The answer was much shorter than when max_tokens was 300.
#when i changed temp to 0,I expected the answers to be identical, but the AI still gave different jokes. The responses were more similar in style, but they were not exactly the same.
#to me tokens are lke the hours i work because every hour i work adds up to my salary pay ,, same point as every token adds to totalcost of using ai 
#deleted (print history so far..................................)
#predction : i think the program will still work normally but not show me history
#the code still worked but it didnt show me history
#first bug i got and all my group got on tuesday was api code error and when they fixed it next day on wednesday i had a new error which is connection error , it took yossi and anas and nada whole session to try to figure it out and fix it and in the end of the session they fixed it to me all thanks and love goes to them
#------------------------lab3-------------------------------------
#To me, the system prompt is like the rules in my MEET class. New students don’t see all the rules written down every minute but everyone still follows them In the same way the user never sees the system prompt but it controls how the AI behaves in every response
#If I Deleted This Line system=system_message ,,,,,Prediction: I think the AI will stop acting like a programming mentor.
#Result: The AI answered questions normally but it no longer stayed focused on programming and technology
#Delete one rule (Never answer questions outside programming and technology.) prediction: I think the AI will start answering any topic.
#Result: The AI answered questions about football instead of telling me it was outside its role.
#Delete this response format line: end with one follow-up question. Prediction: I think the AI will stop asking a follow-up question.
#Result: The AI still answered correctly but it no longer ended its replies with a question
#bug reflection : at first i thought my system prompt was not working because the AI gave a very long introduction but after testing more questions i relized the ai prompt was acutlly working when i asked about questions outside its role like football it refused to answer or was like lets go back to tech.
