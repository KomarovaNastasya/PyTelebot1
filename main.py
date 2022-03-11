import telebot
from telebot import types
import random
import requests
import bs4
import io

bot = telebot.TeleBot('5250359342:AAE4qvngPu5RiSbjFsl1Z_pTULiA-qW5puc')


# --------------------------------------------
# Обработка команды /start
# --------------------------------------------
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_menu = types.KeyboardButton("Меню")
    btn_help = types.KeyboardButton("Помощь")
    btn_about = types.KeyboardButton("Об авторе")
    markup.add(btn_menu, btn_help, btn_about)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! "
                          "Я {1.first_name}, тестовый бот для курса программирования на языке Пайтон."
                     .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


# ---------------------------------------
# Получение сообщений
# ---------------------------------------
@bot.message_handler(func=lambda message: message.text.lower() in ("несуществующие вещи",
                                                                   "котик 🐱", "котик", "🐱",
                                                                   "человек 👱", "человек", "👱",
                                                                   "город 🌆", "город", "🌆",
                                                                   "вайфу 🧝‍♀", "вайфу", "🧝‍♀",
                                                                   "картина 🖼", "картина", "🖼",
                                                                   "случайная"))
def this_x_does_not_exist(message):
    chat_id = message.chat.id
    msg_text = message.text

    text_low = msg_text.lower()
    i = 0
    rnd = ""
    while i == 0:
        if text_low == "несуществующие вещи":
            i = 1

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_cat = types.KeyboardButton("Котик 🐱")
            btn_person = types.KeyboardButton("Человек 👱")
            btn_city = types.KeyboardButton("Город 🌆")
            btn_waifu = types.KeyboardButton("Вайфу 🧝‍♀")
            btn_artwork = types.KeyboardButton("Картина 🖼")
            btn_random = types.KeyboardButton("Случайная")
            btn_menu = types.KeyboardButton("Вернуться в меню")
            markup.add(btn_cat, btn_person, btn_city, btn_waifu, btn_artwork, btn_random, btn_menu)

            bot.send_message(chat_id, text="Вы в меню несуществующих вещей\nВыберете категорию", reply_markup=markup)

        elif text_low in ("котик 🐱", "котик", "🐱") or rnd == "Кот":
            i = 1
            req = requests.get('https://thiscatdoesnotexist.com')
            bot.send_photo(message.chat.id, io.BytesIO(req.content), caption="Несуществующий котик")

        elif text_low in ("человек 👱", "человек", "👱") or rnd == "Человек":
            i = 1
            req = requests.get('https://thispersondoesnotexist.com/image')
            bot.send_photo(message.chat.id, io.BytesIO(req.content), caption="Несуществующий человек")

        elif text_low in ("картина 🖼", "картина", "🖼") or rnd == "Картина":
            i = 1
            req = requests.get('https://thisartworkdoesnotexist.com')
            bot.send_photo(message.chat.id, io.BytesIO(req.content), caption="Несуществующая картина")

        elif text_low in ("город 🌆", "город", "🌆") or rnd == "Город":
            i = 1
            req = requests.get('http://thiscitydoesnotexist.com')
            soup = bs4.BeautifulSoup(req.text, "html.parser")
            result = f"http://thiscitydoesnotexist.com" + soup.find("img").get("src")[1:]
            city = requests.get(result)
            bot.send_photo(message.chat.id, io.BytesIO(city.content), caption="Несуществующий город")

        elif text_low in ("вайфу 🧝‍♀", "вайфу", "🧝‍♀") or rnd == "Вайфу":
            i = 1
            rnd = random.randint(1, 100000)
            rnd_vers = random.randint(2, 3)
            if rnd_vers == 3:
                req = requests.get(f'https://www.thiswaifudoesnotexist.net/example-{rnd}.jpg')
            else:
                req = requests.get(f'https://www.thiswaifudoesnotexist.net/v2/example-{rnd}.jpg')
            bot.send_photo(message.chat.id, io.BytesIO(req.content),
                           caption=f"Несуществующая вайфу\n(v{rnd_vers} id{rnd})")

        elif text_low == "случайная":
            rnd_class = ["Кот", "Человек", "Вайфу", "Картина", "Город"]
            rnd = random.choice(rnd_class)

        else:
            i = 1
            bot.send_message(chat_id, text="Пока такой функции нет")
            get_text_messages(message)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    msg_text = message.text
    text_low = msg_text.lower()

    if text_low == "меню" or text_low == "вернуться в меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_dont_exist = types.KeyboardButton("Несуществующие вещи")
        btn_start = types.KeyboardButton("/start")
        markup.add(btn_dont_exist, btn_start)
        bot.send_message(chat_id, text="Вы в меню", reply_markup=markup)

    elif text_low in ("помощь", "help"):
        print(text_low)
        bot.send_message(chat_id, text="Сгенерированные нейросетью несуществующие:\n"
                                       "Котики – thiscatdoesnotexist.com\n"
                                       "Люди – thispersondoesnotexist.com\n"
                                       "Города – thiscitydoesnotexist.com\n"
                                       "Вайфу – thiswaifudoesnotexist.net\n"
                                       # "Лошадки –\n"
                                       # "Ночные небеса –\n"
                                       "Картины – thisartworkdoesnotexist.com\n")

    elif text_low == "об авторе":
        bot.send_message(chat_id, text="Уголок автора")

    else:
        bot.send_message(chat_id, text="Ваше сообщение: " + msg_text)


# --------------------
# Запуск бота
# --------------------
bot.polling(none_stop=True, interval=0)

print()
