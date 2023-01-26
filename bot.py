import telebot

bot = telebot.TeleBot('5738333587:AAEaonLV6VfHmZaAw6_Vt4vpPbouECw2_Rs')


@bot.message_handler(commands=['start'])
def start(message):
    srt = f'Шалом, <b>{message.from_user.first_name}{message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, srt, parse_mode='html')


bot.polling(none_stop=True)