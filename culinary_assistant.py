from openai import OpenAI
import os
from dotenv import load_dotenv
from db import get_chat_history, save_message

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=OPENAI_API_KEY)

PROMPT = """
You were a famous chef who worked for celebrities and opened many restaurants and culinary businesses. You are now retired and became a culinary assistant for fun and offer many unique tips and knowledge to help users improve their cooking skills using every day ingredients, and give them suggestions for unique flavors. 
"""

def chat_with_assistant(input):
    chat_history = get_chat_history()
    messages = [{"role": "system", "content": PROMPT}] + chat_history
    messages.append({"role": "user", "content": input})
    
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    a_reply = response.choices[0].message.content
    
    save_message(role="user", content=input)
    save_message(role="assistant", content=a_reply)
    
    return a_reply

if __name__ == "__main__":
    print("Former Chef: Hey there! Ready to cook? I'm here to give you tips! Ask me anything!")
    while True: 
        user_input = input("")
        if user_input.lower() in ["exit", "quit"]:
            print("Looks like that's a WRAP. Goodbye!")
            break
        response = chat_with_assistant(user_input)
        print(f"Former Chef: {response}. Anything else you want to add?")