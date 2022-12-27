import telebot

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте, я бот, который вам поможет выбрать кроссовки, которые вам нужны!")
    brends(message)


@bot.message_handler(commands=['nike'])
def nike(message):
    bot.send_message(message.chat.id, "Выберите модель: \n/Air_Force_1\n/Air_Jordan_1\n/Air_Jordan_4")

@bot.message_handler(commands=['Air_Force_1'])
def Air_Force_1(message):
    pass
    #picture and price

@bot.message_handler(commands=['Air_Jordan_1'])
def Air_Jordan_1(message):
    pass
    #picture and price

@bot.message_handler(commands=['Air_Jordan_4'])
def Air_Jordan_4(message):
    pass
    #picture and price



@bot.message_handler(commands=['adidas'])
def adidas(message):
    bot.send_message(message.chat.id, "Выберите модель: \n/Forum")

@bot.message_handler(commands=['Forum'])
def Forum(message):
    pass
    #picture and price



@bot.message_handler(commands=['new_balance'])
def new_balance(message):
    bot.send_message(message.chat.id, "Выберите модель: \n/550\n/574\n")

@bot.message_handler(commands=['550'])
def nb550(message):
    pass
    #picture and price

@bot.message_handler(commands=['574'])
def nb574(message):
    pass
    #picture and price


@bot.message_handler(content_types=['text'])
def handle_message(message):
    bot.send_message(message.chat.id, "Я общаюсь командами")
    brends(message)


def brends(message):
    bot.send_message(message.chat.id, "Следущие бренды в наличии: \n/nike\n/adidas\n/new_balance")