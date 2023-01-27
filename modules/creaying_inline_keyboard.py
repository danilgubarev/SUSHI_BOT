import telebot
import modules.creating_inline_button as inline_button
inline_keyboard1 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard1.add(inline_button.inline_button1, inline_button.inline_button_processing1)

inline_keyboard2 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard2.add(inline_button.inline_button2, inline_button.inline_button_processing2)

inline_keyboard3 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard3.add(inline_button.inline_button3, inline_button.inline_button_processing3)

inline_keyboard4 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard4.add(inline_button.inline_button4, inline_button.inline_button_processing4)

inline_keyboard5 = telebot.types.InlineKeyboardMarkup(row_width= 2)
inline_keyboard5.add(inline_button.inline_button5, inline_button.inline_button_processing5)


