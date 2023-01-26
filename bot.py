import telebot

bot = telebot.TeleBot('5738333587:AAEaonLV6VfHmZaAw6_Vt4vpPbouECw2_Rs')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.chat.id, sti)
    str = f'Шалом, <b>{message.from_user.first_name}{message.from_user.last_name}</b>'\nНапиши /button'
    bot.send_message(message.chat.id, str, parse_mode='html')


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('1')
    start = types.KeyboardButton('2')
    help = types.KeyboardButton('3')
    bio = types.KeyboardButton('4')
    off = types.KeyboardButton('5')
    markup.add(website, start, help, bio, off)
    bot.send_message(message.chat.id, 'Клавиатура активирована✅', reply_markup=markup)
@bot.message_handler(commands=['start'])


bot.polling(none_stop=True)
