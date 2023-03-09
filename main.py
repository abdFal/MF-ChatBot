import openai
import json
import sys

openai.api_key = "your api key"

question = None

def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' Human:', ' AI:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(user_input: str, prompt_list: list[str]) -> str:
    if 'i\'m naufal' in user_input.lower():
        return "I know you are Naufal, I was created because of you."
    elif 'i\'m dasha' in user_input.lower():
        return "I Know You Are dasha, You are my owner's wife"
    elif 'who' and 'naufal' in user_input.lower():
        return "Naufal is my owner, he is very good at IT and he also interested at youtube"
    elif 'thank' in user_input.lower():
        return "Your Welcome, My Pleasure to help you..."
    else:
        # Load questions and answers from JSON file
        with open('my.json', 'r') as f:
            my = json.load(f)
        # Check if the user input matches a question in the JSON file
        for question, answer in my.items():
            if question.lower() in user_input.lower():
                return answer
        # If no match is found, generate a response using OpenAI
        prompt = f'Human: {user_input}\nAI:'
        bot_response = get_api_response(prompt)
        if bot_response:
            pos = bot_response.find(' ')
            bot_response = bot_response[pos + 1:].strip()
        else:
            bot_response = "I'm sorry, I didn't understand your question."
        return bot_response

def main():
    prompt_list: list[str] = ['']

    print("Can I help you?")

    while True:
        user_input: str = input('You: ')
        if user_input.lower() == 'bye':
            print('Bot: Bye Human!')
            break
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')

if __name__ == '__main__':
    main()
