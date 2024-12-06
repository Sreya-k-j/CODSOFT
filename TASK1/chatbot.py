import spacy

# Load the spaCy model (English)
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": "Hello! How can I help you?",
    "Bye": "Goodbye!  Adieu!",
    "thanks": "You're welcome! Happy to assist.",
    "default": "I'm sorry, I didn't quite catch that. Could you rephrase?",
}

# Function to generate a response based on NLP
def generate_response(user_input):
    doc = nlp(user_input.lower())

    # Check for greetings
    if any(token.text in ["hello", "hi", "hey"] for token in doc):
        return responses["greeting"]
    # Check for farewells
    elif any(token.text in ["bye", "Farewell", "goodbye", "quit", "exit"] for token in doc):
        return responses["Bye"]
    # Check for gratitude
    elif any(token.text in ["thank", "thanks","Thank you"] for token in doc):
        return responses["thanks"]
    # Check for "time" keyword
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    else:
        return responses["default"]

# Main chatbot function
def chatbot():
    print("Chatbot: Hi! I'm your NLP-based assistant. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")

        # Exit condition
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Generate response
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
