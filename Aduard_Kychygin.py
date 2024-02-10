import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6535543696:AAERcmRampwQVEswyoWqE5Bc9O1eK7_-kkM')

class Database:
    def init(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_user(self, user_id):
        self.cursor.execute(f"SELECT username FROM users WHERE id={user_id}")
        return self.cursor.fetchone()[0]

    def register(self, user_id, name):
        self.cursor.execute(f"INSERT INTO users VALUES (?, ?)", [user_id, name])
        self.conn.commit()
    
db = Database()
    
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
        btn2 = types.InlineKeyboardButton("Цитаты", callback_data="Filosof", url= "https://t.me/chekhov_life")
        btn3 = types.InlineKeyboardButton("🤖Неиросеть", callback_data="GPT", url= "https://t.me/chatsgpts_bot")
        btn4 = types.InlineKeyboardButton("📰Новости", callback_data='Vesty', url= "https://t.me/naebnet")
        btn5 = types.InlineKeyboardButton("🥇Спорт", callback_data='Sport')
        btn6 = types.InlineKeyboardButton("💸Бизнес и стартапы", callback_data='buzinez', url= "https://t.me/ikniga")
        btn7 = types.InlineKeyboardButton("🎤ВК Музыка 2024", callback_data='Muzik', url= "https://t.me/pesni_treky")
        btn7 = types.InlineKeyboardButton("Одежда", callback_data='lavse', url= "https://t.me/pinkmoon2000")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "stop":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🟩Play", callback_data="play"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "Sport":
        markup = types.InlineKeyboardMarkup()
        bt1 = types.InlineKeyboardButton("🟥Stop", callback_data="stop")
        bt2 = types.InlineKeyboardButton("💪SJBODY", url= "https://t.me/sjbodyfit")
        bt3 = types.InlineKeyboardButton("⚽️Матч ТВ", url= "https://t.me/Match_TV")
        markup.add(bt1, bt2, bt3)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
        
bot.polling(none_stop=True)