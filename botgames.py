import random


def rps(bot, chat_id, msg):
    comp_choice = {
        1: "Камень \U0001FAA8",
        2: "Ножницы \U00002702",
        3: "Бумага \U0001F4C4"
    }
    comp = random.choice(list(comp_choice.keys()))
    if msg in ("камень \U0001FAA8", "камень", "\U0001FAA8"):
        user = 1
        
    elif msg in ("ножницы \U00002702", "ножницы", "\U00002702"):
        user = 2
    
    elif msg in ("бумага \U0001F4C4", "бумага", "\U0001F4C4"):
        user = 3

    else:
        user = 0
        bot.send_message(chat_id, text="Что-то пошло не так")
        
    bot.send_message(chat_id, text=comp_choice[comp])
    
    win = ["Никто не выиграл!", "Я выиграл!", "Вы выиграли!"]
    res = ["Ничья", "Бумага покрывает камень!", "Ножницы разрезают бумагу!", "Камень ломает ножницы!"]
    
    if user == comp:
        result = res[0]
        winner = win[0]
        
    else:
        value = f"{user}{comp}"
        res_array = {
            "31": [win[2], res[1]],
            "23": [win[2], res[2]],
            "12": [win[2], res[3]],
            "13": [win[1], res[1]],
            "32": [win[1], res[2]],
            "21": [win[1], res[3]],
            }
        winner = res_array[value][0]
        result = res_array[value][1]
    bot.send_message(chat_id, text=f"{result}\n{winner}")
