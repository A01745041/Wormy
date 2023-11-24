# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:15:23 2023

@author: A0174
"""

import random
import re  



# Patrones de entrada y respuestas
patterns = [
    {"pattern": r"I need (.*)", "responses": ["Why do you need {0}?", "Would it really help you to get {0}?", "Are you sure you need {0}?",]},
    {"pattern": r"Why don't you (.*)", "responses": ["Do you really think I don't {0}?", "Perhaps eventually I will {0}.", "Do you really want me to {0}?",]},
    {"pattern": r"Why can't I (.*)", "responses": ["Do you think you should be able to {0}?", "If you could {0}, what would you do?", "I don't know -- why can't you {0}?",]},
    {"pattern": r"I am (.*)", "responses": ["Did you come to me because you are {0}?", "How long have you been {0}?", "How do you feel about being {0}?",]},
    {"pattern": r"I'm (.*)", "responses": ["How does being {0} make you feel?", "Do you enjoy being {0}?", "Why do you tell me you're {0}?",]},
    {"pattern": r"Are you (.*)", "responses": ["Why does it matter whether I am {0}?", "Would you prefer it if I were not {0}?", "Perhaps you believe I am {0}.", "I may be {0} -- what do you think?",]},
    {"pattern": r"What (.*)", "responses": ["Why do you ask?", "How would an answer to that help you?", "What do you think?",]},
    {"pattern": r"How (.*)", "responses": ["How do you suppose?", "Perhaps you can answer your own question.", "What is it you're really asking?",]},
    {"pattern": r"Because (.*)", "responses": ["Is that the real reason?", "What other reasons come to mind?", "Does that reason apply to anything else?", "If {0}, what else must be true?",]},
    {"pattern": r"(.*) sorry (.*)", "responses": ["There are many times when no apology is needed.", "What feelings do you have when you apologize?", "Apologies are not necessary.",]},
    {"pattern": r"Hello(.*)", "responses": ["Hello... I'm glad you could drop by today.", "Hi there... how are you today?", "Hello, how are you feeling today?",]},
    {"pattern": r"I think (.*)", "responses": ["Do you doubt {0}?", "Do you really think so?", "But you're not sure {0}?",]},
    {"pattern": r"(.*) friend (.*)", "responses": ["Tell me more about your friends.", "When you think of a friend, what comes to mind?", "Why don't you tell me about a childhood friend?",]},
    {"pattern": r"I feel (.*)", "responses": ["Why do you feel {0}?", "Can you explain why you are {0}?", "Why {0}?",]},
    {"pattern": r"My name is (.*)", "responses": ["Hi {0}, how can I help you today?", "Nice to meet you, {0}. What's on your mind?",]},
    {"pattern": r"What is your name", "responses": ["You can call me Wormy.", "I'm Wormy, your virtual assistant.",]},
    {"pattern": r"quit: (bye|goodbye|quit)", "responses": ["Goodbye. Thank you for talking to me."]},
    {"pattern": r"pre: (dont|can't|won't|recollect|dreamt|dreams|maybe|how|when|certainly|machine|computers|were|you're|i'm|same)", "responses": ["I see. Please go on."]},
    {"pattern": r"post: (am|your|me|myself|yourself|i you|you I|my your|i'm you are)", "responses": ["Why do you say that {0}?", "I'm not sure I understand. Can you elaborate?"]},
    {"pattern": r"synon: (belief|feel|think|believe|wish|family|mother|mom|father|dad|sister|brother|wife|children|child|desire|want|need|sad|unhappy|depressed|sick|happy|elated|glad|better|cannot|can't|everyone|everybody|nobody|noone|be|am|is|are|was)", "responses": ["Tell me more about {0}.", "How does {0} make you feel?", "Can you elaborate on {0}?"]},
    {"pattern": r"key: xnone\n  decomp: *\n    reasmb: I'm not sure I understand you fully.\n    reasmb: Please go on.\n    reasmb: What does that suggest to you ?\n    reasmb: Do you feel strongly about discussing such things ?", "responses": ["I'm not sure I understand you fully.", "Please go on.", "What does that suggest to you?", "Do you feel strongly about discussing such things?"]},
    {"pattern": r"key: sorry\n  decomp: *\n    reasmb: Please don't apologise.\n    reasmb: Apologies are not necessary.\n    reasmb: I've told you that apologies are not required.", "responses": ["Please don't apologize.", "Apologies are not necessary.", "I've told you that apologies are not required."]},
    {"pattern": r"initial: (.*)", "responses": ["How do you do. Please tell me your problem."]},
    {"pattern": r"final: (.*)", "responses": ["Goodbye. Thank you for talking to me."]},
    {"pattern": r"quit: (bye|goodbye|quit)", "responses": ["Goodbye. Thank you for talking to me."]},
    {"pattern": r"pre: (dont|can't|won't|recollect|dreamt|dreams|maybe|how|when|certainly|machine|computers|were|you're|i'm|same)", "responses": ["I see. Please go on."]},
    {"pattern": r"pre: (.*?) (.*?)", "responses": ["Tell me more about the relationship between {0} and {1}.", "How are {0} and {1} connected?", "What comes to mind when you think of {0} and {1} together?"]},
    {"pattern": r"post: (am|your|me|myself|yourself|i you|you I|my your|i'm you are)", "responses": ["Why do you say that {0}?", "I'm not sure I understand. Can you elaborate?"]},
    {"pattern": r"synon: (.*?) (.*?)", "responses": ["Tell me more about the connection between {0} and {1}.", "How does {0} relate to {1}?", "Can you elaborate on the similarities between {0} and {1}?"]},
    {"pattern": r"key: xnone\n  decomp: *\n    reasmb: I'm not sure I understand you fully.\n    reasmb: Please go on.\n    reasmb: What does that suggest to you ?\n    reasmb: Do you feel strongly about discussing such things ?", "responses": ["I'm not sure I understand you fully.", "Please go on.", "What does that suggest to you?", "Do you feel strongly about discussing such things?"]},
    {"pattern": r"key: (.*?)\n  decomp: *\n    reasmb: (.*?)", "responses": ["Can you tell me more about {0}?", "What do you think about {0}?", "How does {0} make you feel?"]},
]



memory = []

# Función para responder al usuario
def respond(user_input):
    global memory  # Accede a la variable global memory

    # Verificar si el usuario mencionó su nombre y almacenarlo en la memoria
    user_name_match = re.match(r"My name is (.*)", user_input)
    if user_name_match:
        user_name = user_name_match.group(1)
        memory.append(f"User's name is {user_name}")

    # Almacenar la entrada del usuario en la memoria
    memory.append(user_input)

    for pattern in patterns:
        match = re.match(pattern['pattern'], user_input)
        if match:
            response = random.choice(pattern['responses'])
            
            # Si la respuesta incluye el marcador de posición {memory}, reemplazarlo con la memoria acumulada
            if "{memory}" in response:
                response = response.replace("{memory}", "\n".join(memory))
            
            return response.format(*[match.group(i) for i in range(1, match.lastindex + 1)])

    return "Please tell me more about it."


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
        


    
