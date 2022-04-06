from telebot import types


class States:
    states_array = {}
    current_state = None
    current_state_name = None
    
    def __init__(self, name=None, buttons=None, parent=None, row=3):
        self.name = name
        self.buttons = buttons
        self.parent = parent
        self.row = row

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row)
        markup.add(*buttons)
        self.markup = markup

        self.__class__.states_array[name] = self

    @classmethod
    def set_state(cls, name):
        state = cls.states_array.get(name)
        cls.current_state = state
        cls.current_state_name = name
        return state


state_main = States("Главное меню", buttons=["Картинки и факты", "Игры", "Помощь"], parent=None, row=2)

state_choice = States("Картинки и факты", buttons=["Несуществующие вещи", "Факт о котах", "Помощь",
                                                   "Вернуться"], parent=state_main, row=2)
state_does_not_exist = States("Несуществующие вещи", buttons=["Котик \U0001F431",
                                                              "Человек \U0001F9D1\U0001F3FC\U0000200D\U0001F4BC",
                                                              "Вайфу \U0001F9DD\U0001F3FB\U0000200D\U00002640\U0000FE0F",
                                                              "Картина \U0001F5BC", "Город \U0001F306",
                                                              "Небо \U0001F30C", "Глаз \U0001F441", "Случайная",
                                                              "Вернуться"], parent=state_choice)

state_games = States("Игры", buttons=["Камень, ножницы, бумага", "Чёт-нечёт", "Вернуться"], parent=state_main, row=2)
state_rps = States("Камень, ножницы, бумага", buttons=["Камень \U0001FAA8", "Ножницы \U00002702", "Бумага \U0001F4C4",
                                                       "Вернуться"], parent=state_games, row=2)
