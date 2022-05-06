from pyrogram import Client, filters
import config
from db import Database

db = Database()
app = Client('user', config.api_id, config.api_hash, 'a', 'a', 'a')

minecraft_bot_id = 5086631591
gaming_chat = -1001286994009

@app.on_message(filters=filters.new_chat_members)
def new_chat(c, m):
    print(1)
    if m.new_chat_members[0] != app.get_me().id:
        return
    app.send_message(m.chat.id, 'Для инициализации чата фракции ВМФ пропишите ".addchat имя_фракции".')

@app.on_message(filters=filters.all)
def main_handler(c, m):
    print(2)
    if m.from_user.id != minecraft_bot_id and m.chat.id != gaming_chat:
        print(3)
        if not m.text.startswith('.addchat '):
            return
        db.add_chat(m.text.split(' ', 1)[1], m.chat.id)
    print(4)
    for chat in db.get_chats():
        app.send_message(chat_id=chat['id'], text=m.text)


app.run()