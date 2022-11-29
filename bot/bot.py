from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
nlp = spacy.load('en_core_web_sm')
bot = ChatBot(
    "Norman",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    #logic_adapters=[
    #    "chatterbot.logic.MathematicalEvaluation",
    #    "chatterbot.logic.TimeLogicAdapter"
    #],
    database_uri="sqlite:///database.sqlite3"
)

trainer = ListTrainer(bot)
trainer.train([
    'Hello',
    'Keep good work Carlos',
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'You are welcome.',
])
print('Type something to begin...')
exit_conditions = (":q", "quit", "exit")
while True:
    try:
        query = input("> ")
        if query in exit_conditions:
            break
        else:
            print(f"🪴 {bot.get_response(query)}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    