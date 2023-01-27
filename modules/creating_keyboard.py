import modules.creating_buttons as c_buttons
import telebot

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.add(c_buttons.button_add_catalog1, c_buttons.button_add_catalog2, c_buttons.button_add_catalog3)