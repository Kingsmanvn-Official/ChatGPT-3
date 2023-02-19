import sys
import os
import openai_secret_manager

def send_message(message, token, chat_id):
    import telegram

    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message)

    return "Message sent"

if __name__ == "__main__":
    secrets = openai_secret_manager.get_secret("telegram_chatbot")
    chat_id = secrets["chat_id"]
    token = secrets["access_token"]
    message = sys.argv[1]
    print(send_message(message, token, chat_id))
