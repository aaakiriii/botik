import os

os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["ALL_PROXY"] = ""
os.environ["NO_PROXY"] = "*"

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaVideo

# ====================================
# ВСТАВЬ СВОЙ ТОКЕН
# ====================================
TOKEN = "8905152911:AAGiu2NXxWcjD9EJGx9HdwwD67Rkb5XRteI"

bot = telebot.TeleBot(TOKEN)


# ====================================
# ФУНКЦИЯ ГЛАВНОГО МЕНЮ
# ====================================
def send_main_menu(chat_id):

    # Создаём кнопки
    keyboard = InlineKeyboardMarkup(row_width=2)

    button1 = InlineKeyboardButton("первое мяу❤️", callback_data="btn1")
    button2 = InlineKeyboardButton("второе мяу❤️", callback_data="btn2")
    button3 = InlineKeyboardButton("третье мяу❤️", callback_data="btn3")
    button4 = InlineKeyboardButton("последнее мяу❤️", callback_data="btn4")

    keyboard.add(button1, button2, button3, button4)

    # Открываем изображение
    photo = open("др картинка.jpg", "rb")

    # Отправляем фото + текст + кнопки
    bot.send_photo(
        chat_id,
        photo,
        caption="""Выбирай кнопочку (желательно по порядку)
Некоторые могут долго грузить, чут чут подожди :3""",
        reply_markup=keyboard
    )


# ====================================
# КОМАНДА START
# ====================================
@bot.message_handler(commands=['start'])
def start(message):

    send_main_menu(message.chat.id)


# ====================================
# ОБРАБОТКА КНОПОК
# ====================================
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    bot.answer_callback_query(call.id)

    # -------------------
    # КНОПКА 1
    # -------------------
    if call.data == "btn1":

        keyboard = InlineKeyboardMarkup()

        back_button = InlineKeyboardButton(
            "Назад в меню",
            callback_data="back"
        )

        keyboard.add(back_button)

        # ОТПРАВЛЯЕМ ФОТО
        with open("козлек.jpg", "rb") as photo:
            bot.send_photo(
                call.message.chat.id,
                photo
            )

        # ЧИТАЕМ ТЕКСТ ИЗ ФАЙЛА
        with open("знакомство.txt", "r", encoding="utf-8") as file:
            text = file.read()

        # ОТПРАВЛЯЕМ ТЕКСТ + КНОПКИ
        bot.send_message(
            call.message.chat.id,
            text,
            reply_markup=keyboard
        )
    # -------------------
    # КНОПКА 2
    # -------------------
    elif call.data == "btn2":

        keyboard = InlineKeyboardMarkup()

        back_button = InlineKeyboardButton(
            "Назад в меню",
            callback_data="back"
        )

        keyboard.add(back_button)

        # -------------------
        # ОТПРАВЛЯЕМ ФОТО
        # -------------------
        with open("окси и гнойный.jpg", "rb") as photo:

            bot.send_photo(
                call.message.chat.id,
                photo
            )

        # -------------------
        # ЧИТАЕМ ТЕКСТ ИЗ ФАЙЛА
        # -------------------
        with open("подарочки.txt", "r", encoding="utf-8") as file:
            text = file.read()

        # -------------------
        # ОТПРАВЛЯЕМ ТЕКСТ + КНОПКИ
        # -------------------
        bot.send_message(
            call.message.chat.id,
            text,
            reply_markup=keyboard
        )

    # -------------------
    # КНОПКА 3
    # -------------------
    elif call.data == "btn3":

        keyboard = InlineKeyboardMarkup()

        back_button = InlineKeyboardButton(
            "Назад в меню",
            callback_data="back"
        )

        keyboard.add(back_button)

        # -------------------
        # ОТПРАВЛЯЕМ ФОТО
        # -------------------
        with open("с друнчиком не геи.jpg", "rb") as photo:

            bot.send_photo(
                call.message.chat.id,
                photo
            )

        # -------------------
        # ЧИТАЕМ ТЕКСТ ИЗ ФАЙЛА
        # -------------------
        with open("питер.txt", "r", encoding="utf-8") as file:
            text = file.read()

        # -------------------
        # ОТПРАВЛЯЕМ ТЕКСТ + КНОПКИ
        # -------------------
        bot.send_message(
            call.message.chat.id,
            text,
            reply_markup=keyboard
        )


    # -------------------
    # КНОПКА 4
    # -------------------
    elif call.data == "btn4":

        # -----------------------------
        # СОЗДАЁМ КНОПКИ
        # -----------------------------
        keyboard = InlineKeyboardMarkup()

        back_button = InlineKeyboardButton(
            "Назад в меню",
            callback_data="back"
        )

        keyboard.add(back_button)

        # -----------------------------
        # ОТПРАВЛЯЕМ 2 ВИДЕО
        # -----------------------------

        try:
            VIDEO1 = "BAACAgIAAxkBAAOkahuD0HIy3xxKNpkg7IrnkdiNMyYAAiKgAAIX0dlIC_asCJf32447BA"
            VIDEO2 = "BAACAgIAAxkBAAOmahuD_G5n1ciw4CC-etp_IWhE1ioAAiOgAAIX0dlIZ0OF6AqI9KE7BA"

            bot.send_video(call.message.chat.id, VIDEO1)
            bot.send_video(call.message.chat.id, VIDEO2)

            with open("люблю.txt", "r", encoding="utf-8") as file:
                text = file.read()

            bot.send_message(
                call.message.chat.id,
                text,
                reply_markup=keyboard
            )

        except Exception as e:
            print("BTN4 ERROR:")
            print(repr(e))
        # -------------------
        # ОТПРАВЛЯЕМ ТЕКСТ + КНОПКИ
        # -------------------
        bot.send_message(
            call.message.chat.id,
            text,
            reply_markup=keyboard
        )
    # -------------------
    # НАЗАД В МЕНЮ
    # -------------------
    elif call.data == "back":

        # Удаляем сообщение с кнопкой
        bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )

        # Показываем главное меню
        send_main_menu(call.message.chat.id)


# ====================================
# ЗАПУСК БОТА
# ====================================
print("Бот запущен...")

bot.infinity_polling(skip_pending=True)