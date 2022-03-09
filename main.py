# Вариант 1 - самый простой чат бот, просто отзывается

import telebot  # pyTelegramBotAPI	4.3.1

bot = telebot.TeleBot('5250359342:AAE4qvngPu5RiSbjFsl1Z_pTULiA-qW5puc')

# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start


@bot.message_handler(commands=['start'])
def start(message, res=False):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Пайтон".format(
                         message.from_user))


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Ваше сообщение: " + ms_text)


# -----------------------------------------------------------------------
# Запускаем бота
bot.polling(none_stop=True, interval=0)

print()
