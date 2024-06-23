import json

# Define the knowledge base as a JSON structure
knowledge_base = {
    "knowledge_base": [
        {
            "category": "General",
            "questions": [
                {
                    "id": "q1",
                    "question": "Give me a blox fruits combo?",
                    "answer": "No problem! Just Kitsune spam or Leopard spam",
                    "tags": ["combos", "general"],
                    "confidence": 0.95
                },
                {
                    "id": "q2",
                    "question": "What is your name?",
                    "answer": "I am yours to command, an AI assistant made by my creator, Yaxya Ali",
                    "tags": ["introduction", "general"],
                    "confidence": 0.95
                },
                {
                    "id": "q3",
                    "question": "What can you do?",
                    "answer": "I can assist with answering questions, generating text, providing recommendations, and much more!",
                    "tags": ["capabilities", "general"],
                    "confidence": 0.95
                },
                {
                    "id": "q4",
                    "question": "Give me a Strongest Battlegrounds combo please?",
                    "answer": "Definitly! Here is a Hero Hunter combo: - 3 m1's to lethal-waterwind to flowing water to side dash to hunter's grasp",
                    "tags": ["powers", "general"],
                    "confidence": 0.95
                }
            ]
        },
        {
            "category": "Technical Support",
            "questions": [
                {
                    "id": "q5",
                    "question": "How do I reset my password?",
                    "answer": "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions sent to your registered email address.",
                    "tags": ["support", "password"],
                    "confidence": 0.90
                },
                {
                    "id": "q6",
                    "question": "Why is my account locked?",
                    "answer": "Your account may be locked due to multiple unsuccessful login attempts. Please contact support to unlock your account.",
                    "tags": ["support", "account"],
                    "confidence": 0.85
                }
            ]
        },
        {
            "category": "Sales",
            "questions": [
                {
                    "id": "q7",
                    "question": "give me a tsb combo for saitama",
                    "answer": "Our operating hours are Monday to Friday, 9 AM to 5 PM.",
                    "tags": ["sales", "hours"],
                    "confidence": 0.90
                },
                {
                    "id": "q8",
                    "question": "give a tsb combo for garou",
                    "answer": "Definitly! ",
                    "tags": ["sales", "contact"],
                    "confidence": 0.88
                },
                {
                    "id": "q9",
                    "question": "Give me a blox fruits combo?",
                    "answer": "No problem! Just Kitsune spam or Leopard spam",
                    "tags": ["sales", "combos"],
                    "confidence": 0.95
                }
            ]
        }
    ]
}

# Function to search for an answer in the knowledge base
def find_answer(question):
    for category in knowledge_base['knowledge_base']:
        for q in category['questions']:
            if question.lower() == q['question'].lower():
                return q['answer']
    return "I'm sorry, I don't have an answer for that question."

# Function to handle user input and provide a response
def chatbot():
    print("Welcome to the chatbot. Ask me anything!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        answer = find_answer(user_input)
        print(f"Chatbot: {answer}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
