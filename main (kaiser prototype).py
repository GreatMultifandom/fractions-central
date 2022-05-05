from pyrogram import Client
import db

app = Client("my_account")


@app.on_message()
def log(client, message):
    if (message.from_user == botID):
        for (x in db):
            app.send_message(chat_id=x, text=message.text)


app.run()