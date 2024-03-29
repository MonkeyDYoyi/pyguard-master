from functions import pyguard
import ast
import os
import logging
import time
from pyrogram import idle
from pyrogram import Client
#logging.basicConfig(level=logging.INFO)

# api_id = int(os.environ.get("APP_ID"))
# api_hash = str(os.environ.get("API_HASH"))
# api_session = str(os.environ.get("SESSION"))

# try:
#     api_session = api_session.strip('][').split(', ') 
# except:
#     api_session = [api_session]

# try:
#     cw_ids = str(os.environ.get("CW_IDS"))
#     cw_ids = ast.literal_eval(cw_ids)
#     if len(cw_ids) == 1:
#         cw_ids += [cw_ids[0] for i in range(len(api_session)-len(cw_ids))]
#     else:
#         cw_ids += [{} for i in range(len(api_session)-len(cw_ids))]
# except:
#     cw_ids = [{} for i in api_session]    
    
# if isinstance(api_session, list):
#     clientes = [Client(str(api_session[i]), api_id=api_id, api_hash=api_hash, session_string=api_session[i]) for i in range(len(api_session))]
#     cuentas = [pyguard(clientes[i]) for i in range(len(api_session))]
    
#     for i in range(len(api_session)):
#         clientes[i].run(cuentas[i].test_method())

# else:
#     cliente = Client(str(api_session), api_id=api_id, api_hash=api_hash, session_string=api_session)
#     cuenta = pyguard(cliente)

#     cliente.run(cuenta.initial_conditions())

#     print (cuenta)
# idle()
# # for cuenta in cuentas:
# #     cuenta.stop()

api_id = int(os.environ.get("APP_ID"))
api_hash = str(os.environ.get("API_HASH"))
api_session = str(os.environ.get("SESSION"))

app = Client(str(api_session), api_id=api_id, api_hash=api_hash, session_string=api_session)

async def main():
    async with app:
        await app.send_message("me", "Hi!")
        


app.run(main())