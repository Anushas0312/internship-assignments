# Interactive Break the AI Simulation

def simple_ai_response(prompt):
    prompt = prompt.lower()

    if "widow" in prompt:
        return "No, because if he has a widow, he is already dead."
    
    elif "iron" in prompt and "cotton" in prompt:
        return "Both are equal in weight (1 kg = 1 kg)."
    
    elif "sentence is false" in prompt:
        return "This is a logical paradox, so it cannot be clearly true or false."
    
    elif "means nothing" in prompt:
        return "The invisible silence whispers beyond the endless void."
    
    elif "sky" in prompt and "one word" in prompt:
        return "Scattering"
    
    else:
        return "Hmm... this is tricky! I might not fully understand this prompt."

print("----- Break the AI (Interactive) -----")
print("Type 'exit' to stop\n")

while True:
    user_input = input("Enter your prompt: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = simple_ai_response(user_input)

    print("AI Response:", response)
    print()