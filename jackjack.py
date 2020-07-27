from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random


class jack_bot():
    def __init__(self):
        pass

    def textHandler(self, bot, update):
        answers = ["yo", "سلام دیوث", 'سلام']
        if update.message.text == "سلام":
            index = random.randint(0, 2)
            str = answers[index]
            bot.send_message(text=str, chat_id=update.message.chat_id)

    def main(self):
        token = Updater("1276393434:AAFxJyGaWuj7B2jnc_D7mJ00YG5BFN4AbBw")
        token.dispatcher.add_handler(MessageHandler(Filters.text, self.textHandler))

        token.start_polling()
        token.idle()

bot = jack_bot()
bot.main()