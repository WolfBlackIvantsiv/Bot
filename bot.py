import os
import random

import pyowm
import telebot

bot = telebot.TeleBot('1922989323:AAHBy0wEnTgfrFYhbcZlbG6jgwsPWHk0Bos')


@bot.message_handler(content_types=['new_chat_members'])
def send_welcome(message):
    chatID = message.chat.id
    bot.reply_to(message,
                 """ Привіт! \nРаді бачити вас у нашому ламповому чатику, що об'єднює ходорівську громаду! \nЯ - Бот, що імітує всім відомого Женіка, любителя сказати "Е".Вам розв'язані руки для обговорення що до будь-які теми, та \nпам'ятайте, у кожної теми є свої межі(правила), почувайтеся як у дома,та хорошого спілкування!""")
    f = open("ezgif.com-add-text.gif.mp4", "rb")
    bot.send_animation(chatID, f)


@bot.message_handler(content_types="text")
def send_text(message):
    chatID = message.chat.id
    text = message.text.lower()

    if text == "!h" or text == "!д":
        bot.send_message(chatID,
                         """Привіт усім новим користувачам.\n\nАдміністрація чату рада вас вітати!\n\nПросимо 
                         дотримуватися усіх правил. \n\nУ випадку виявлення порушень з боку інших учасників просимо 
                         повідомити нашу командуs.\n\nПриємного спілкування!""")
    elif text == "!info" or text == "!інфо":
        bot.send_message(chatID,
                         "Привіт, я Женік!\n\nЯ створений задля покращення цього чату.\n\nЯ унікальний бот, "
                         "який з часом буде ставати лише кращим")
    elif text == "сергій" or text == "сергій":
        bot.reply_to(message, "Найкращий в світі!!!")
    elif text == "!к" and "!к" or text == "!команди" and "!команди":
        f = open("Команди.txt", "rb")
        bot.send_document(chatID, f)
    elif text == "шо робиш" and "шо робиш" or text == "шо робиш?" and "шо робиш?" or text == "що робиш" and "що робиш" or text == "що робиш?" and "що робиш?":
        f = open("ібу_і_пю.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "хуй" and "хуй" or text == "пизда" and " пизда":
        f = open("хуя_собі_свого_зніми.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "сука" and "сука" or text == "блять" and "блять" or text == "блядь":
        f = open("тикурвайобанаблять.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == " їбати" and " їбати" or text == "єбати" and "єбати" or text == "єбу" and "єбу" or text == "я єбу" and "я єбу" or text == "в'єбати" and "в'єбати" or text == "вєбати" and "вєбати":
        f = open("я_ше_можу_вебати.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "ого" and "ого":
        f = open("ніхуясобіблять.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "марічка" and "марічка":
        bot.reply_to(message, "Найкраща в світі!!!")
    elif text == "тихо" and "тихо" or text == "рот закрий" and "рот закрий":
        f = open("завалю_по_єбалу_точно.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "уєбав" and "уєбав" or text == "пішов ти" and "пішов ти":
        f = open("уебав.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "мля" and "мля" or text == "бля" and "бля":
        f = open("тваюматьблять....mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "блять" and "блять" or text == "блядь" and "блядь" or text == "соси" and "соси" and "блядь" or text == "курва" and "курва":
        f = open("зара_точно_перехуяру.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "шо" and "шо" or text == "не поняв" and "не поняв" or text == "ясно" and "ясно":
        f = open("издєуиууиуиу_непонятне_бубніння.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "закрий рот" and "закрий рот" or text == "тихо буть" and "тихо буть" or text == "тихо будь" and "тихо будь":
        f = open("завалю_по_єбалу_точно.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "е" and "е" or text == "e" and "e":
        f = open("е.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "даун?" and "даун?" or text == "дурачок?" and "дурачок?":
        f = open("бля_ти_далбайоб.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "хуйня" and "хуйня" or text == "пизда" and "пизда" or text == "не знімай" and "не знімай" or text == "зніми" and "зніми" or text == "відео" and "відео" or text == "хуя собі свого зніми" and "хуя собі свого зніми":
        f = open("хуя_собі_свого_зніми.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "ти дебіл" and "ти дебіл" or text == "ти тупий" and "ти тупий" or text == "далбайоб" and "далбайоб" or text == "ти дебіл?" and "ти дебіл?" or text == "ти тупий?" and "ти тупий?" or text == "довбойоб" and "довбойоб":
        f = open("бля_ти_далбайоб.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "йди нахуй" and "йди нахуй" or text == "йди ти" and "йди ти":
        f = open("диннахуй.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "не нервуй" and "не нервуй" or text == "пішов ти" and "пішов ти":
        f = open("йди_ннахуй_заєбав.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "куда?" and "куда?" or text == "куда" and "куда":
        f = open("куда.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "ти поганий" and "ти поганий" or text == "ти погана" and "ти погана":
        f = open("тикурвайобанаблять.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "шо сказав?" and "шо сказав?" or text == "що сказав?" and "що сказав?" or text == "шо бля?" and "шо бля":
        f = open("куда.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "жостко" and "жостко" or text == "ніхуя собі" and "ніхуя собі" or text == "ніхуя собі блять" and "ніхуя собі блять":
        f = open("ніхуясобіблять_тивєбав_е.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "міст" and "міст" or text == "моста" and "моста" or text == "кличко" and "кличко" or text == "впав" and "впав":
        f = open("який_міст_впизду_бля.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "вікна" and "вікна" or text == "йоб тваю мать з тими вікнками" and "йоб тваю мать з тими вікнками":
        f = open("йобтваюматьзтимивікнкаминахуйблять.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "ало" and "ало" or text == "альо" and "альо":
        f = open("альобля.mp3", "rb")
        bot.send_audio(chatID, f)
    elif text == "га" and "га" or text == "га?" and "га?":
        f = open("га.mp3", "rb")
        bot.send_audio(chatID, f)

    elif text == "!w" and "!w" or text == "!п" and "!п" or text == "!погода" and "!погода":
        owm = pyowm.OWM('0cee35c4d29f2fcc16a2c9ae2d965d3d')
        mgr = owm.weather_manager()
        place = "Ходорів"
        observation = mgr.weather_at_place(place)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        if temp <= 0:
            bot.send_message(chatID, "Ходорів: " + str(temp) + "❄")
        elif 0 < temp < 10:
            bot.send_message(chatID, "Ходорів: " + str(temp) + "☁")
        elif 10 < temp < 20:
            bot.send_message(chatID, "Ходорів: " + str(temp) + "⛅")
        elif temp > 20:
            bot.send_message(chatID, "Ходорів: " + str(temp) + "☀")


if __name__ == "__main__":
    bot.get_updates()
    bot.polling(none_stop=True)
