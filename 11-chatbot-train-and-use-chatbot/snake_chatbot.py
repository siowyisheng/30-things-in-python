from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer
# chatterbot.set_trainer(ListTrainer)

# chatterbot.train([
#     "Hi there!",
#     "Hello",
# ])

# # or train it with twitter data!

chatbot = ChatBot('Scaley Snake')

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")

while True:
    my_input = input()
    print(chatbot.get_response(my_input))