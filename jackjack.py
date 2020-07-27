from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random


class jack_bot():
    def __init__(self):
        pass

    def textHandler(self, bot, update):
        answers = ["yo", "سلام دیوث", 'سلام سکسی', 'چه سلامی چه علیکی!!']
        if update.message.text == "سلام":
            rand_index = random.randint(0, 100)
            if 0 < rand_index < 26:
                index = 0
            elif 26 < rand_index < 51:
                index = 1
            elif 51 < rand_index < 76:
                index = 2
            else:
                index = 3
            str = answers[index]
            bot.send_message(text=str, chat_id=update.message.chat_id)
       # TODO: add counter for each person and send message if it is bigger than 5

    def main(self):
        token = Updater("1276393434:AAFxJyGaWuj7B2jnc_D7mJ00YG5BFN4AbBw", use_context=True)
        token.dispatcher.add_handler(MessageHandler(Filters.text, self.textHandler))

        token.start_polling()
        token.idle()

bot = jack_bot()
bot.main()