from telegram.ext import Updater, CommandHandler

def start_bot(bot, updater):
 print("Hello")

def main():
  updtr = Updater('5405166187:AAE_k-11QwwaWadIYp1aKcrpCVLDFkcMJFg')

  updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

  updtr.start_polling()
  updtr.idle()

if __name__ == "__main__":
 main()
