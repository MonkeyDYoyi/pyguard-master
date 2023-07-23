#!/usr/bin/python
# -*- coding: utf-8-*-

from pyrogram import Client#, Filters, MessageHandler
try:
    from pyrogram import MessageHandler                  
except ImportError:
    from pyrogram.handlers import MessageHandler 
try:
    from pyrogram import Filters                  
except ImportError:
    from pyrogram import filters                                
from numpy.random import randint
import re
import time
import os

# api_id = int(os.environ.get("APP_ID"))
# api_hash = str(os.environ.get("API_HASH"))
api_id = int(1337414)
api_hash = str("7e280b5751e5ce2c413239c412976c31")

app=Client(str(round(time.time() * 1000))+str(randint(1,10000)), api_id, api_hash)
app.start()
print(app.export_session_string())
app.stop()
