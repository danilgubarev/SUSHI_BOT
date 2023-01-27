import modules.create_bot as c_bot
# import modules.url_pictures as url_pictures
import modules.file_paths as m_path
import modules.creaying_inline_keyboard as c_inline_keyboard

def send_message_user(message):
    if message.text.lower() == "new" or message.text.lower() == "sale" or message.text.lower() == "discounts":
        path_file = m_path.path_search("images/chucka.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Салат",
            reply_markup= c_inline_keyboard.inline_keyboard1
        )
        
        path_file = m_path.path_search("images/sashimi.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Сашимі",
            reply_markup= c_inline_keyboard.inline_keyboard2
        )
        
        path_file = m_path.path_search("images/sashimi2.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Сашимі",
            reply_markup= c_inline_keyboard.inline_keyboard3
        )
        
        path_file = m_path.path_search("images/sushi1.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Суші",
            reply_markup= c_inline_keyboard.inline_keyboard4
        )
        
        path_file = m_path.path_search("images/sushi2.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Суші",
            reply_markup= c_inline_keyboard.inline_keyboard5
        )
        
        