import modules.create_bot as c_bot
my_id = 992182536
@c_bot.bot.callback_query_handler(func= lambda callback: callback.data)

def request_processing(callback):
    if callback.data == "замовити":
        c_bot.bot.send_message(
            callback.message.chat.id,
            "Замовлення оформлено"
         )

        