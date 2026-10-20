#Rule Based AI chatbot 

import datetime

name = input("Swagat hai, please enter your name : ")
presentHour = datetime.datetime.now().hour

if(5 <= presentHour < 12):
    print(f"Good morning! {name}, Welcome to Your Chatbot😊")
elif(12 <= presentHour < 17):
    print(f"Good afternoon! {name}, Welcome to Your Chatbot😊")
elif(17 <= presentHour < 21):
    print(f"Good evening! {name}, Welcome to Your Chatbot😊")
else:
    print(f"Good night! {name}, Welcome to Your Chatbot😊")
    
print("You can ask me basic questions. Type 'bye' to exit from the bot.\n")

#Chatbot Memory Creation
responses={
    "hello chatbot": "Hello, how can I assist you?",
    "how are you": "I'm very well! Thanks for asking. What about you?",
    "how have you been": "I'm very well! Thanks for asking. What about you?",
    "i am also very well": "That's Great to hear!😊",
    "i am fine": "That's Great to hear!😊",
    "who are you": "I am a smart AI chatbot, YourBuddy🤖",
    "who created you": "I was created by Krish Gaur, on 5 September 2026.",
    "what can you do": "I can answer common questions.",
    "can you help me": "Of course! I can help you.",
    "are you a human": "No, I'm an AI chatbot.",
    "motivate me": "Keep going. Every bug of your project makes you a better developer.",
    "i am happy": "That's Great to hear!😊",
    "i am sad": "I'm sorry you're feeling this way🙁",
    "good morning": "Good morning! How have you been?",
    "good afternoon": "Good afternoon! How have you been?",
    "good evening": "Good evening! How have you been?",
    "good night": "Good night! Have a great sleep!"
}


def getResponseOfBot(yourQuestion):
    yourQuestion = yourQuestion.lower()
    for eachKey in responses:
        # if eachKey in yourQuestion:
        if yourQuestion in eachKey:
            return responses[eachKey]

    return "I am not able to tell that yet. Mai jald hi isko seekh lunga"

while True:
    userInput=input("You: ")
    if "bye" in userInput.lower():
        print("Bye, See you later👋. Take care!\n")
        break
    reply=getResponseOfBot(userInput)
    print("Bot: ",reply)


