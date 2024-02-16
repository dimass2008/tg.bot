import telebot
from telebot import types
import main

bot = telebot.TeleBot('6535543696:AAERcmRampwQVEswyoWqE5Bc9O1eK7_-kkM')
    
db = main.Database()
    
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    name = message.from_user.username
    db.register(user_id, name)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("🟩Play", callback_data="play"))
    bot.send_message(message.chat.id, f'Меню программы::', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "play":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("🟥Stop", callback_data="stop")
        btn2 = types.InlineKeyboardButton("Гонки", callback_data="speed")
        btn3 = types.InlineKeyboardButton("Открытый мир", callback_data="world")
        btn4 = types.InlineKeyboardButton("Выживание", callback_data='survival')
        btn5 = types.InlineKeyboardButton("Шутер", callback_data='shooter')
        btn6 = types.InlineKeyboardButton("Экшен", callback_data='action')
        btn7 = types.InlineKeyboardButton("🎤ВК Музыка 2024", callback_data='Muzik', url= "https://t.me/pesni_treky")
        btn7 = types.InlineKeyboardButton("Одежда", callback_data='lavse', url= "https://t.me/pinkmoon2000")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "stop":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🟩Play", callback_data="play"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

 

    elif call.data == "speed":
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("🟥Stop", callback_data="stop")
        b2 = types.InlineKeyboardButton("ASSETTO CORSA")
        b3 = types.InlineKeyboardButton("forza horizon 6")
        b4 = types.InlineKeyboardButton('CARX DRIFT RACING ONLINE')
        b5 = types.InlineKeyboardButton('Need for speed 2024 ')
        markup.add(b1, b2, b3, b4, b5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "world":
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("🟥Stop", callback_data="stop")
        b2 = types.InlineKeyboardButton("Grand Theft Auto VI")
        b3 = types.InlineKeyboardButton("Red Dead Redemption")
        b4 = types.InlineKeyboardButton('FALLOUT 5')
        b5 = types.InlineKeyboardButton('MAFIA IV')
        markup.add(b1, b2, b3, b4, b5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "survival":
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("🟥Stop", callback_data="stop")
        b2 = types.InlineKeyboardButton("Minecraft")
        b3 = types.InlineKeyboardButton("Terraria")
        b4 = types.InlineKeyboardButton('The Forest')
        markup.add(b1, b2, b3, b4, b5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
     
    elif call.data == "shooter":
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("🟥Stop", callback_data="stop")
        b2 = types.InlineKeyboardButton("Battlefield 2")
        b3 = types.InlineKeyboardButton("Counter-Strike 3")
        b4 = types.InlineKeyboardButton('far cry 3')
        b5 = types.InlineKeyboardButton('Atomic Heart')
        markup.add(b1, b2, b3, b4, b5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == "action":
            markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton("🟥Stop", callback_data="stop")
            b2 = types.InlineKeyboardButton("Rust")
            b3 = types.InlineKeyboardButton("DAYZ")
            b4 = types.InlineKeyboardButton('Metro 2044')
            b5 = types.InlineKeyboardButton('Max Payne')
            markup.add(b1, b2, b3, b4, b5)
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)



bot.polling(none_stop=True)