from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(name='PaBot', read_only=True, 
logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool',
              'fantastic big dawg',
              'i\'m ok',
              'glad to hear that',
              'i\'m fine',
              'glad to hear that',
              'i feel awesome',
              'excellent, glad to hear that',
              'not so good',
              'sorry to hear that',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']

math_talk_1 = ['pythagorean theorem',
             'a squared plus b squared equals c squared.']

math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(bot)

for item in (small_talk, math_talk_1, math_talk_2):
    list_trainer.train(item)