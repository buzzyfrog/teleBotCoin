import config
import telebot
import chance


bot = telebot.TeleBot(config.TELEGRAM_API_TOKEN)
markup = telebot.types.ReplyKeyboardMarkup(True, True)
btn = telebot.types.InlineKeyboardButton(text='flip', callback_data='flip')
markup.add(btn)


@bot.message_handler(commands=['start'])
def command_message(message):
    bot.send_message(message.chat.id, 'Hey, how are you?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello:)')
    elif message.text.lower() == 'goodbye':
        bot.send_message(message.chat.id, 'Bye')
    elif message.text.lower() == 'flip':
        if(chance.Chance.probabilityCalculate() >= 5):
            gifdoc = open('./src/coin-flip-45.gif', 'rb')
            bot.send_message(message.chat.id, 'Орел!', reply_markup=markup)
            bot.send_document(message.chat.id, gifdoc)
        else:
            gifdoc = open('./src/coin-flip-45.gif', 'rb')
            bot.send_message(message.chat.id, 'Решка!', reply_markup=markup)
            bot.send_document(message.chat.id, gifdoc)


if __name__ == '__main__':
    bot.polling()
