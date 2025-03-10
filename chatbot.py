import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Sample responses for different intents
responses = {
    "greeting": ["Hello! How can I assist you?", "Hi there! What can I do for you?"],
    "farewell": ["Goodbye! Have a great day!", "Bye! Take care."],
    "thanks": ["You're welcome!", "No problem! Glad to help."],
    "unknown": ["I'm not sure how to respond to that.", "Can you rephrase your question?"]
}

# Keywords for intent recognition
keywords = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "farewell": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you", "appreciate"]
}

# Function to determine intent
def get_intent(user_input):
    tokens =user_input.lower().split()
    for intent, words in keywords.items():
        if any(word in tokens for word in words):
            return intent
    return "unknown"

# Function to process user input and generate responses
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])

# Main chatbot loop
def chat():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    nltk.download("punkt")  # Ensure nltk tokenizer is available
    chat()
