# Simple NLP Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great!"
    
    elif "your name" in user_input:
        return "I am a simple NLP Chatbot."
    
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    
    elif "study" in user_input:
        return "Studying regularly is the key to success."
    
    else:
        return "Sorry, I didn't understand that."

print("----- NLP Mini Chatbot -----")
print("Type 'exit' to stop\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)