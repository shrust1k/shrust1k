import telebot
import mcsv

bot = telebot.TeleBot("2006280214:AAGWMTOt2HNNbnqBm6-GdZhdU0MQ31B1Ddo", parse_mode=None)


@bot.message_handler(commands=['expense', '-', "spend", "waste"])
def main_func(message):

	if message.content_type == 'text':

		try:
			a = message.text.split(" ")
			msg = float(a[1])


			try:
				if msg != 0:
					category = a[2]
					category = category.lower()
					if category not in ["food", "drink", "lego", "clothing", "transport", "party", "other"]:
						bot.send_message(message.chat.id, "Chosen category doesnt exist")

					else:

						mcsv.append(msg, category)
						bot.send_message(message.chat.id,
										 f"Succesfully added expense: *{msg} €* in a category: *{category}*",
										 parse_mode="Markdown")

				else:
					bot.send_message(message.chat.id, "Expense cannot be 0")

			except IndexError as r:
				print(r)
				bot.send_message(message.chat.id, "Didnt mention the expense or didnt split up ")

		except ValueError and IndexError as r:
			bot.send_message(message.chat.id, "Write numbers only/ write an expense")
			print(r)


@bot.message_handler(commands=["remove"])
def remove(message):
	mcsv.remove_last_row(mcsv.flist("mtable.csv"))
	bot.send_message(message.chat.id, "Removed")


@bot.message_handler(commands=["plan"])
def statistics(message):
	bot.send_message(message.chat.id, mcsv.plan( mcsv.flist("mtable.csv")))


@bot.message_handler(commands=["categories"])
def statistics(message):
	bot.send_message(message.chat.id, mcsv.categories(mcsv.flist("mtable.csv")))





@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}! \nI'm bot made by shrust1k.\nI can manage your expenses, here'ŗe my commmands:"
									  " \n/expense _amount_ _category_ - write down expense \n/remove - removes last added expense"
									  " \n/plan - gives you all expenses \n/help - shows you all categorries\n"
									  "/categories - shows you how mnuch did u spent in every category "
					 ,parse_mode="Markdown")

@bot.message_handler(commands=["help"])
def send_welcome(message):
	bot.send_message(message.chat.id, "Food🥨 \nDrink🥤 \nLego🧱 \nClothing👖 \nTransport🚎 \nParty🍻 \nOther👽 \n"
									  "You *should't put emojis*, it is only for visibility"
					 , parse_mode="Markdown")


bot.polling()


