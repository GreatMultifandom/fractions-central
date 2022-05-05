from pyrogram import Client
import config
from db import Database

db = Database()
app = Client('user', config.api_id, api.hash, 'a', 'a', 'a')

app.run()