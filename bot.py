from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤖",
])
trainer.train([
    "Are you from earth?",
    "We came from outer space"
])
trainer.train([
    "Who won the super bowl in February 2022?",
    "The Los Angeles Rams"
])
trainer.train([
    "Who won the 2022 world cup?",
    "Argentina, led by Lionel Messi"
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"👽 {chatbot.get_response(query)}")