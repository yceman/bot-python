import chatterbot
import chatterbot_corpus
chatbot = ChatBot("My bot")

bot_trainer = ChatterBotCorpusTrainer(chatbot)
bot_trainer.train("chatterbot.corpus.english")

print("enter 'quit' to stop")
while True:
    user_input = input("You: ")
    if user_input == 'quit':
       break
print("Bot: ", chatbot.get_response(user_input))