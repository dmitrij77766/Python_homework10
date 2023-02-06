

import random
import telebot
bot = telebot.TeleBot('6138448452:AAHgQYS96o4GtGqn4aQgSOUBpVY5v6oKLUA')
from telebot import types




with open("first.txt", "r") as f1:
    first = f1.readlines()
with open("second.txt", "r") as f2:
    second = f2.readlines()
with open("second_add.txt", "r") as f2_add:
    second_add = f2_add.readlines()
with open("third.txt", "r") as f3:
    third = f3.readlines()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
   
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, {0.first_name}! \n Cейчас я расскажу тебе гороскоп на сегодня.".format(message.from_user))
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='♈️ Овен ♈️', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='♉️ Телец ♉️', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='♊️ Близнецы ♊️', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='♋️ Рак ♋️', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='♌️ Лев ♌️', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='♍️ Дева ♍️', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='♎️ Весы ♎️', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='♏️ Скорпион ♏️', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='♐️ Стрелец ♐️', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='♑️ Козерог ♑️', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='♒️ Водолей ♒️', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='♓️ Рыбы ♓️', callback_data='zodiac')
        keyboard.add(key_ryby)
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac": 
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        msg = msg.replace("\n","")
        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)