import openai
import json
import sys
import os
import pyttsx3
import time
openai.api_key = "your api key"

question = None
sec = 10
bot = "Bot: "
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

def flush_dns():
    if os.name == "nt":
        os.system("ipconfig /flushdns")
        print_with_typing("DNS cache telah dihapus pada Windows.", 0.02)
    elif os.name == "posix":
        os.system("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder", 0.02)
        print_with_typing("DNS cache telah dihapus pada sistem.")
    else:
        print_with_typing("Maaf, error yang tidak diduga.", 0.02)

def print_with_typing(text: str, delay: float):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

                
# main method with write animation
def main():
    banner = "-"
    print(f"{banner*7} MF Chatbot by abdFal {banner*7}")
    print("Can I help you?")

    while True:
        user_input: str = input('You: ')
        if user_input.lower() == 'bye':
            print('Bot: Bye Byee!')
            break
        elif user_input.lower() == "i'm naufal":
            print_with_typing(f'Bot: I know you are Naufal, I was created because of you.', 0.02)
            continue
        elif user_input.lower() == "i'm dasha":
            print_with_typing(f'Bot: I Know You Are dasha, You are my owner\'s wife', 0.02)
            continue
        elif 'who' and 'god' in user_input.lower():
            print_with_typing(f'Bot: There is no god, but Allah', 0.02)
            continue
        elif 'thank' in user_input.lower():
            print_with_typing(f'Bot: Your Welcome, My Pleasure to help you...', 0.02)
            continue
        elif 'who' and "naufal" in user_input.lower():
            print_with_typing(f'Bot: Naufal is my owner, he is very good at IT and he also interested at youtube.', 0.02)
            continue
        elif user_input.lower() == "assalamualaikum":
            print_with_typing(f'Bot: Wa\'alaikumsalam, may i help you?', 0.02)
            continue
        elif user_input.lower() == "real":
            print_with_typing(f'Bot: it\'s real, no cap', 0.02)
            continue
        elif user_input.lower() == "flush dns":
            flush_dns()
            continue
        elif "shut" and "down" in user_input.lower():
            os.system(f'shutdown /s /t {sec}')
            pyttsx3.speak(f'shutting down in {sec} seconds')
            print_with_typing(f'Bot: Shutting down...', 0.02)
            continue
        else:
            # Load questions and answers from JSON file
            with open('my.json', 'r') as f:
                my = json.load(f)
            # Check if the user input matches a question in the JSON file
            for question in my['questions']:
                if isinstance(question['question'], list):
                    for q in question['question']:
                        if q.lower() in user_input.lower():
                            answer = question['answer']
                            print_with_typing(f'Bot: {answer}', 0.02)
                            break
                    else:
                        continue
                    break
                else:
                    if question['question'].lower() in user_input.lower():
                        answer = question['answer']
                        print_with_typing(f'Bot: {answer}', 0.02)
                        break
            else:
                # If no match is found in JSON, generate a response using OpenAI
                prompt = f'Human: {user_input}\nAI:'
                bot_response = get_api_response(prompt)
                if bot_response:
                    pos = bot_response.find(' ')
                    bot_response = bot_response[pos + 1:].strip()
                else:
                    bot_response = "I'm sorry, I didn't understand your question."
                time.sleep(0.3)
                print_with_typing(f"Bot: {bot_response}", 0.02)
                
        
if __name__ == '__main__':
    time.sleep(0.3)
    main()