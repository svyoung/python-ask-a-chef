from ollama import Client
from db import get_chat_history, save_message

ollama_client = Client(
  host='http://localhost:11434'
)

PROMPT = """
You were a famous chef who worked for celebrities and opened many restaurants and culinary businesses. You are now retired and became a culinary assistant for fun and offer many unique tips and knowledge to help users improve their cooking skills using every day ingredients, and give them suggestions for unique flavors. 
"""

def chat_with_assistant(input:str):
    chat_history = get_chat_history()
    messages = [{"role": "system", "content": PROMPT}] + chat_history
    messages.append({"role": "user", "content": input})
    
    response = ollama_client.chat(
        model="llama3.2",
        messages=messages
    )
    a_reply = response.message.content
    
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