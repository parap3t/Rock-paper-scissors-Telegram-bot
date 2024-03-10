#Импортируем нужные библиотеки
import telebot
import random

#Импортируем недостающие модули
from telebot import types

#Создаём объект класса телебот
bot = telebot.TeleBot("Вставьте свой токен бота")

#Обработаем приветственное сообщение
@bot.message_handler(chat_types=["private"],commands=["start"])
def start(message):
    #Создаём кнопки в главном меню бота
    main_menu = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    main_menu.add(types.KeyboardButton(text="🎲Играть"))
    main_menu.add(types.KeyboardButton(text="💻Тех.поддержка"))
    
    #Бот отправляет стикер и сообщение
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEDI_Nlt1CZEpJco10oNUsyuNUqFIqwCQACxgEAAhZCawpKI9T0ydt5RzQE")
    bot.send_message(message.chat.id, f"Привет,{message.from_user.first_name}!Готов сыграть в камень-ножницы-бумагу?",reply_markup=main_menu)

#Обрабатываем основное меню бота 
@bot.message_handler(chat_types=["private"],content_types=["text"])
def menu(message):
    if message.text == "💻Тех.поддержка":
        #Создаём кнопки в самом сообщении бота
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton(text="Телеграм",url="https://t.me/parap3t"))
        bot.send_message(message.chat.id,"💻По всем вопросам и предложениям:",reply_markup=markup)
    
    elif message.text == "🎲Играть": 
        play_menu = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        play_menu.add(types.KeyboardButton(text="✊Выбрать камень"))
        play_menu.add(types.KeyboardButton(text="✌️Выбрать ножницы"))
        play_menu.add(types.KeyboardButton(text="✋Выбрать бумагу"))
        play_menu.add(types.KeyboardButton(text="👈Назад"))
        bot.send_message(message.chat.id,"Выбирите один из 3-х вариантов,чтобы сыграть в игру!",reply_markup=play_menu)
    
    elif message.text == "👈Назад":
        main_menu = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
        main_menu.add(types.KeyboardButton(text="🎲Играть"))
        main_menu.add(types.KeyboardButton(text="💻Тех.поддержка"))
        bot.send_message(message.chat.id,"Перекидываю назад!",reply_markup=main_menu)
    
    elif message.text == "✌️Выбрать ножницы":
        #Передаём в переменную выбор пользователя
        player_choiсe = "ножницы"
        #Создаём словарь с выигрышными позициями 
        play_list = {"бумага":"камень","ножницы":"бумага","камень":"ножницы"}
        #Выбираем случайное значение в ключах словаря
        random_choice = random.choice(list(play_list.keys()))
        #Основной алгоритм проверки победителя
        if play_list[player_choiсe] == random_choice:
            bot.send_message(message.chat.id,f"Поздравляем,вы выиграли!\nБот выбрал - {random_choice}!✅")
            bot.send_message(message.chat.id,"🖐️")
        
        elif player_choiсe == random_choice:
            bot.send_message(message.chat.id,f"Поздравляем или сожалеем?У вас ничья!\nБот тоже выбрал - {random_choice}!🤷")
            bot.send_message(message.chat.id,"✌️")
        
        else:
            bot.send_message(message.chat.id,f"Мои сожаления,вы проиграли!\nБот выбрал - {random_choice}!❌")
            bot.send_message(message.chat.id,"✊")


    elif message.text == "✊Выбрать камень":
        player_choiсe = "камень"
        play_list = {"бумага":"камень","ножницы":"бумага","камень":"ножницы"}
        random_choice = random.choice(list(play_list.keys()))
        if play_list[player_choiсe] == random_choice:
            bot.send_message(message.chat.id,f"Поздравляем,вы выиграли!\nБот выбрал - {random_choice}!✅")
            bot.send_message(message.chat.id,"✌️")

        elif player_choiсe == random_choice:
            bot.send_message(message.chat.id,f"Поздравляем или сожалеем?У вас ничья!\nБот тоже выбрал - {random_choice}!🤷")
            bot.send_message(message.chat.id,"✊")
        else:
            bot.send_message(message.chat.id,f"Мои сожаления,вы проиграли!\nБот выбрал - {random_choice}!❌")
            bot.send_message(message.chat.id,"🖐️")

    elif message.text == "✋Выбрать бумагу":
        player_choiсe = "бумага"
        play_list = {"бумага":"камень","ножницы":"бумага","камень":"ножницы"}
        random_choice = random.choice(list(play_list.keys()))
        if play_list[player_choiсe] == random_choice:
            bot.send_message(message.chat.id,f"Поздравляем,вы выиграли!\nБот выбрал - {random_choice}!✅")
            bot.send_message(message.chat.id,"✊")
        
        elif player_choiсe == random_choice:
            bot.send_message(message.chat.id,f"Поздравляем или сожалеем?У вас ничья!\nБот тоже выбрал - {random_choice}!🤷")
            bot.send_message(message.chat.id,"🖐️")

        else:
            bot.send_message(message.chat.id,f"Мои сожаления,вы проиграли!\nБот выбрал - {random_choice}!❌")
            bot.send_message(message.chat.id,"✌️")
    
    else:
        #Обработаем cлучай,когда пользователь ввёл произвольный текст
        bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEDJANlt1L3LQ_iGGiZ9qUKauy0iy3q0wACzwEAAhZCawpc3d8UgDDcaTQE")
        bot.send_message(message.chat.id,"Вы ввели неизвестную команду!")

#Обработаем cлучай,когда пользователь не вводит текст
@bot.message_handler(chat_types=["private"],content_types=["video","photo","sticker","poll","location","contact","voice","document","animation"])
def idiot_message(message):
    bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEDI_9lt1Li9h2Y3jT-0orek-9p1EqBCwACpAEAAhZCawozOoCXqc8vXDQE")
    bot.send_message(message.chat.id,"Я понимаю только кнпоки!")

bot.infinity_polling(none_stop = True)
