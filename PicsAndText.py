import requests
import random
import bs4
import io


# -----------------------
# This CAT Does Not Exist
# -----------------------
def cat(bot, chat_id):
    req = requests.get('https://thiscatdoesnotexist.com')
    bot.send_photo(chat_id, io.BytesIO(req.content), caption="Несуществующий котик")


# --------------------------
# This PERSON Does Not Exist
# --------------------------
def person(bot, chat_id):
    req = requests.get('https://thispersondoesnotexist.com/image')
    bot.send_photo(chat_id, io.BytesIO(req.content), caption="Несуществующий человек")


# -------------------------
# This WAIFU Does Not Exist
# -------------------------
def waifu(bot, chat_id):
    rnd = random.randint(1, 100000)
    rnd_vers = random.randint(2, 3)
    if rnd_vers == 3:
        req = requests.get(f'https://www.thiswaifudoesnotexist.net/example-{rnd}.jpg')
    else:
        req = requests.get(f'https://www.thiswaifudoesnotexist.net/v2/example-{rnd}.jpg')
    bot.send_photo(chat_id, io.BytesIO(req.content),
                   caption=f"Несуществующая вайфу\n(v{rnd_vers} id{rnd})")


# ----------------------------
# This ART WORK Does Not Exist
# ----------------------------
def art(bot, chat_id):
    req = requests.get('https://thisartworkdoesnotexist.com')
    bot.send_photo(chat_id, io.BytesIO(req.content), caption="Несуществующая картина")


# ------------------------
# This CITY Does Not Exist
# ------------------------  
def city(bot, chat_id):
    req = requests.get('http://thiscitydoesnotexist.com')
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    result = "http://thiscitydoesnotexist.com" + soup.find("img").get("src")[1:]
    res = requests.get(result)
    bot.send_photo(chat_id, io.BytesIO(res.content), caption="Несуществующий город")


# -----------------------
# This SKY Does Not Exist
# -----------------------    
def sky(bot, chat_id):
    rnd = random.randint(1, 5000)
    if 1 <= rnd <= 9:
        res = f"000{rnd}"
    elif 10 <= rnd <= 99:
        res = f"00{rnd}"
    elif 100 <= rnd <= 999:
        res = f"0{rnd}"
    else:
        res = f"{rnd}"
    req = requests.get(
        f"https://firebasestorage.googleapis.com/v0/b/thisnightskydoesnotexist.appspot.com/o"
        f"/images%2Fseed{res}.jpg?alt=media")
    bot.send_photo(chat_id, io.BytesIO(req.content), caption=f"Несуществующее ночное небо\n(seed{res})")


# -----------------------
# This EYE Does Not Exist
# -----------------------    
def eye(bot, chat_id):
    req = requests.get('https://thiseyedoesnotexist.com/random/')
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    result = "https://thiseyedoesnotexist.com/" + soup.find("img").get("src")
    res = requests.get(result)
    bot.send_photo(chat_id, io.BytesIO(res.content), caption="Несуществующий глаз")
    

# -------------------
# Случайная категория
# -------------------
def random_txdne(bot, chat_id):
    rnd_class = {
        "Кот": cat, 
        "Человек": person,
        "Вайфу": waifu,
        "Картина": art,
        "Город": city,
        "Небо": sky,
        "Глаз": eye
    }
    rnd_choice = random.choice(list(rnd_class.keys()))
    rnd = rnd_class[rnd_choice]
    return rnd(bot, chat_id)


# -------------
# Факты о котах
# -------------
def meow_fact(bot, chat_id):
    meow = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1').json()
    bot.send_message(chat_id, text=f'Факт о котах:\n{meow["text"]}')
    

# --------------------
# ******** ***** совет
# --------------------
def advice(bot, chat_id):
    ad = requests.get('http://fucking-great-advice.ru/api/random').json()
    bot.send_message(chat_id, text=f'Совет:\n{ad["text"]}')


# -----------------------------------
# Цитаты на испанском с Викицитатника
# -----------------------------------
def cita(bot, chat_id):
    req = requests.get("https://es.wikiquote.org/wiki/Especial:Aleatoria")
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    res = soup.find("div", class_="mw-parser-output").find("ul", recursive=False).find_all("li")[0].get_text()
    res = res.replace('[1]', '').replace('[2]', '').replace('[3]', '')
    bot.send_message(chat_id, text=f'Цитата:\n{res}')
