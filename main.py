import telebot
from telebot import types
# import requests
# import bs4
# import io
# import random
from states import States
import PicsAndText
import botgames

# --------------------------------------------
#
# - Сделать проверку на ввод "Главное меню", "Меню" и других глобальных команд с других состояний в strange_msg
# - Сделать проверку на другие инлайн клавиатуры в inline_keyboard, если в будущем такие будут
# - 
# --------------------------------------------

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)


# ------------------------
# Обработка команды /start
# ------------------------
@bot.message_handler(commands=['start'])
def start(message):
    change_state(message)


# -----------------------------------
# Получение сообщения от пользователя
# -----------------------------------
@bot.message_handler(content_types=['text'])
def main(message):
    chat_id = message.chat.id
    msg_text = message.text
    msg_low = msg_text.lower()

    # --------------------
    # Отсутствие состояния
    # --------------------
    if States.current_state_name is None:
        # message.text = "Главное меню"
        # change_state(message)
        chat_id = message.chat.id
        bot.send_message(chat_id, "Для начала работы со мной отправьте команду /start")

    # -----------------------------------------
    # Обработка возврата в предыдущее состояние
    # -----------------------------------------
    elif msg_low == "вернуться":
        change_state(message, back=True)

    # -----------------------
    # Состояние главного меню
    # -----------------------
    elif States.current_state_name == "Главное меню":

        if msg_low == "/start":
            bot.send_message(chat_id,
                             text="Привет, {0.first_name}!\n"
                                  "Я бот для курса программирования на языке Пайтон.\n "
                                  "Я умею присылать сгенерированные нейросетью картинки из различных категорий, "
                                  "факты о котиках (на английском), цитаты (на испанском), советы (на матерном).\n"
                                  "А также мы можем сыграть в камень-ножницы-бумагу.\n\n"
                                  "Для подробностей отправьте слово «Помощь» или тапните на соответствующий пункт меню."
                             .format(message.from_user), reply_markup=States.current_state.markup)

        elif msg_low in ("главное меню", "меню"):
            bot.send_message(chat_id, text="Вы в главном меню", reply_markup=States.current_state.markup)

        elif msg_low in ("картинки и факты", "камень, ножницы, бумага"):
            change_state(message)

        elif msg_low in ("помощь", "help", "/help"):
            help_msg(chat_id)

        else:
            strange_msg(message)

    # --------------------------------------------
    # Состояние выбора категории Картинок и фактов
    # --------------------------------------------
    elif States.current_state_name == "Картинки и факты":

        if msg_low in ("картинки и факты",):
            bot.send_message(chat_id, text="Вы в меню картинок и фактов", reply_markup=States.current_state.markup)

        elif msg_low == "несуществующие вещи":
            change_state(message)

# ! Для работы в pythonanywhere
# !       elif msg_low == "несуществующее небо":
# !           PicsAndText.sky(bot, chat_id)

        elif msg_low == "факт о котах":
            PicsAndText.meow_fact(bot, chat_id)
            
        elif msg_low == "совет":
            PicsAndText.advice(bot, chat_id)
            
        elif msg_low == "цитата":
            PicsAndText.cita(bot, chat_id)
            
        elif msg_low in ("помощь", "help", "/help"):
            help_msg(chat_id)

        else:
            strange_msg(message)

    # --------------------------
    # Состояние This X Does Not Exist
    # --------------------------
    elif States.current_state_name == "Несуществующие вещи":
        if msg_low == "несуществующие вещи":
            bot.send_message(chat_id, text="Выберете категорию несуществующего",
                             reply_markup=States.current_state.markup)

        elif msg_low in ("котик \U0001F431", "котик", "кот", "\U0001F431"):
            PicsAndText.cat(bot, chat_id)

        elif msg_low in ("человек \U0001F9D1\U0001F3FC\U0000200D\U0001F4BC",
                         "человек", "\U0001F9D1\U0001F3FC\U0000200D\U0001F4BC"):
            PicsAndText.person(bot, chat_id)

        elif msg_low in ("вайфу \U0001F9DD\U0001F3FB\U0000200D\U00002640\U0000FE0F", "вайфу",
                         "\U0001F9DD\U0001F3FB\U0000200D\U00002640\U0000FE0F"):
            PicsAndText.waifu(bot, chat_id)

        elif msg_low in ("картина \U0001F5BC", "картина", "\U0001F5BC"):
            PicsAndText.art(bot, chat_id)

        elif msg_low in ("город \U0001F306", "город", "\U0001F306"):
            PicsAndText.city(bot, chat_id)

        elif msg_low in ("небо \U0001F30C", "небо", "\U0001F30C"):
            PicsAndText.sky(bot, chat_id)

        elif msg_low in ("глаз \U0001F441", "глаз", "\U0001F441"):
            PicsAndText.eye(bot, chat_id)

        elif msg_low == "случайная":
            PicsAndText.random_txdne(bot, chat_id)

        else:
            strange_msg(message)

    # ---------------------------------
    # Состояние игры Камень, ножницы, бумага
    # ---------------------------------
    elif States.current_state_name == "Камень, ножницы, бумага":

        if msg_low in ("камень, ножницы, бумага", "rps"):
            bot.send_message(chat_id, text="Сыграем в «Камень, ножницы, бумагу»!",
                             reply_markup=States.current_state.markup)

        elif msg_low in ("камень \U0001FAA8", "ножницы \U00002702", "бумага \U0001F4C4",
                         "камень", "\U0001FAA8", "ножницы", "\U00002702", "бумага", "\U0001F4C4"):
            botgames.rps(bot, chat_id, msg_low)

        else:
            strange_msg(message)


def help_msg(chat_id):
    bot.send_message(chat_id, "Использованные сайты:", reply_markup=inline_keyboard())


# --------------------------------------------------
# Обработка смены состояния и перехода к предыдущему
# --------------------------------------------------
def change_state(message, back=False):
    if back is True:
        if States.current_state.parent.name is not None:
            States.set_state(States.current_state.parent.name)
            message.text = States.current_state_name
        else:
            return strange_msg(message)
    else:
        States.set_state(message.text)
        if message.text.lower() in ("/start", "меню"):
            States.set_state("Главное меню")
    return main(message)


# ------------------------------------------
# Обработка сoобщений, неопределённых в меню
# ------------------------------------------
def strange_msg(message):
    chat_id = message.chat.id
    msg_text = message.text
    msg_low = msg_text.lower()
    if msg_low == "меню":
        change_state(message)
    else:
        bot.send_message(chat_id, "К сожалению, я не понимаю ваше сообщение: " + msg_text +
                         "\nЧтобы вернуться в главное меню отправьте «Меню»")


def inline_keyboard():
    # Сделать проверку на разные клавиатуры, если такие будут
    buttons = [
        types.InlineKeyboardButton(text="This Cat Does Not Exist \U0001F431", url="https://thiscatdoesnotexist.com"),
        types.InlineKeyboardButton(text="This Person Does Not Exist \U0001F9D1\U0001F3FC\U0000200D\U0001F4BC",
                                   url="https://thispersondoesnotexist.com"),
        types.InlineKeyboardButton(text="This Waifu Does Not Exist  \U0001F9DD\U0001F3FB\U0000200D\U00002640\U0000FE0F",
                                   url="https://thiswaifudoesnotexist.net"),
        types.InlineKeyboardButton(text="This Art Work Does Not Exist  \U0001F5BC",
                                   url="https://thisartworkdoesnotexist.com"),
        types.InlineKeyboardButton(text="This City Does Not Exist  \U0001F306", url="https://thiscitydoesnotexist.com"),
        types.InlineKeyboardButton(text="This Night Sky Does Not Exist  \U0001F30C",
                                   url="https://arthurfindelair.com/thisnightskydoesnotexist"),
        types.InlineKeyboardButton(text="This Eye Does Not Exist  \U0001F441", url="https://thiseyedoesnotexist.com/"),
        types.InlineKeyboardButton(text="Факты о котах", url="https://github.com/alexwohlbruck/cat-facts"),
        types.InlineKeyboardButton(text="Цитаты из Викицитатника", url="https://es.wikiquote.org/wiki"),
        types.InlineKeyboardButton(text="Чертовски великолепный совет", url="https://fucking-great-advice.ru")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


# -----------
# Запуск бота
# -----------
bot.polling(none_stop=True, interval=0)

print()
