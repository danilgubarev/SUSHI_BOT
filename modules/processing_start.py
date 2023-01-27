import modules.create_bot as c_bot
import modules.creating_keyboard as c_keyboard
import modules.sending_picture as s_pictures
@c_bot.bot.message_handler(commands = ["start"])
def start_bot(message):
    c_bot.bot.send_message(
        message.chat.id,
        "Hi User",
        reply_markup= c_keyboard.keyboard
    )
    c_bot.bot.register_next_step_handler(message, s_pictures.send_message_user)