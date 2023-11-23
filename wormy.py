# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:15:23 2023

@author: A0174
"""

import random
import re  
# Patrones de entrada y respuestas
patterns = [
    {"pattern": r"I need (.*)", "responses": ["Why do you need {0}?", "Would it really help you to get {0}?", "Are you sure you need {0}?"]},
    {"pattern": r"Why don't you (.*)", "responses": ["Do you really think I don't {0}?", "Perhaps eventually I will {0}.", "Do you really want me to {0}?"]},
    {"pattern": r"Why can't I (.*)", "responses": ["Do you think you should be able to {0}?", "If you could {0}, what would you do?", "I don't know -- why can't you {0}?"]},
    {"pattern": r"I am (.*)", "responses": ["Did you come to me because you are {0}?", "How long have you been {0}?", "How do you feel about being {0}?"]},
    {"pattern": r"I'm (.*)", "responses": ["How does being {0} make you feel?", "Do you enjoy being {0}?", "Why do you tell me you're {0}?"]},
    {"pattern": r"Are you (.*)", "responses": ["Why does it matter whether I am {0}?", "Would you prefer it if I were not {0}?", "Perhaps you believe I am {0}.", "I may be {0} -- what do you think?"]},
    {"pattern": r"What (.*)", "responses": ["Why do you ask?", "How would an answer to that help you?", "What do you think?"]},
    {"pattern": r"How (.*)", "responses": ["How do you suppose?", "Perhaps you can answer your own question.", "What is it you're really asking?"]},
    {"pattern": r"Because (.*)", "responses": ["Is that the real reason?", "What other reasons come to mind?", "Does that reason apply to anything else?", "If {0}, what else must be true?"]},
    {"pattern": r"(.*) sorry (.*)", "responses": ["There are many times when no apology is needed.", "What feelings do you have when you apologize?", "Apologies are not necessary."]},
    {"pattern": r"Hello(.*)", "responses": ["Hello... I'm glad you could drop by today.", "Hi there... how are you today?", "Hello, how are you feeling today?"]},
    {"pattern": r"I think (.*)", "responses": ["Do you doubt {0}?", "Do you really think so?", "But you're not sure {0}?"]},
    {"pattern": r"(.*) friend (.*)", "responses": ["Tell me more about your friends.", "When you think of a friend, what comes to mind?", "Why don't you tell me about a childhood friend?"]},
    {"pattern": r"I feel (.*)", "responses": ["Why do you feel {0}?", "Can you explain why you are {0}?", "Why {0}?"]},
    {"pattern": r"My name is (.*)", "responses": ["Hi {0}, how can I help you today?", "Nice to meet you, {0}. What's on your mind?"]},
    {"pattern": r"What is your name", "responses": ["You can call me Wormy.", "I'm Wormy, your virtual assistant."]},
]

# Función para responder al usuario
def respond(user_input):
    # Verificar si el usuario mencionó su nombre y almacenarlo
    user_name_match = re.match(r"My name is (.*)", user_input)
    user_name = user_name_match.group(1) if user_name_match else None

    for pattern in patterns:
        match = re.match(pattern['pattern'], user_input)
        if match:
            response = random.choice(pattern['responses'])
            
            # Si el usuario mencionó su nombre, ignorar el nombre de Eliza en la respuesta
            if user_name:
                response = re.sub(r'\bWormy\b', '', response)
            
            return response.format(*[match.group(i) for i in range(1, match.lastindex + 1)])

    return "I'm not sure I understand."

# Programa principal
print("Wormy: Hello! How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Wormy: Goodbye!")
        break
    else:
        response = respond(user_input)
        print("Wormy:", response)
