from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler

)
from cred import TOKEN
from menu import (
    main_menu_keybord,
    courses_menu_keybord
    
)
from key_button import tele_button, courses

ABOUT = tele_button[0]
COURSES = tele_button[1]
BACK = courses[4]
LOCATION = tele_button[2]

#надо добавить этот коментарий
def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nэтот бот поможет вам с игформацией курсов. ',
        reply_markup=main_menu_keybord()
    )


def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Преимущества обучения в Codify · Обучение с нуля до Junior. Пройди обучение по авторской программе Codify и стань Junior специалистом.\n site: https://www.codifylab.com/',
    )

def reply_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose course',
        reply_markup=courses_menu_keybord()
    )

def main_menu(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Main Menu',
        reply_markup=main_menu_keybord()
    )

def location(update:Update, context:CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'location of Codify'
    )
    update.message.reply_location(
        #42.82909025000069, 74.61687279022618
        longitude=74.61687279022618,
        latitude=42.82909025000069,
        reply_to_message_id=msg.message_id
    )


updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    main_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))

updater.start_polling()
updater.idle()

