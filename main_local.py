from functions_local import main
import ast
import os
import logging
import time
from pyrogram import idle
#logging.basicConfig(level=logging.INFO)

# api_id = int(os.environ.get("APP_ID"))
# api_hash = str(os.environ.get("API_HASH"))
# api_session = str(os.environ.get("SESSION"))
api_id = int(1337414)
api_hash = str("7e280b5751e5ce2c413239c412976c31")
api_session = str("[AQAUaEYAACeHXf46UtKs6vhBehukHNdbmv2vNz9MZkiojr-5tvC0qQYpTDfq3LoyjtrGaGZ6z7f1O11s-xl17ye6hYo-j1ijk1dPd-JYdltBgBeSMI_fxR358H-FE3XvtrpmBGXOzHlQVASO4HWP_-IkbLIL_SE60_UmriPrMUwTYszlA9eQ5wnzC70nC5xZVc-Xlx2Sg_Wqe-M2Z0fXqFuTvHZCMKeeJmGEcWx8whddckg8cBkZH0aKxTiBjrRD10_N37rjkY4dViWMXKkm_60heJfuJatU3EWXRoETr5hX9t9cM-trr08gT_p4oSc8XojNlVngm0eoCKEkS79Ma6cFbqtujAAAAAAmdd42AA]")

try:
    api_session = api_session.strip('][').split(', ') 
except:
    api_session = [api_session]

try:
    # cw_ids = str(os.environ.get("CW_IDS"))
    cw_ids = str("[{}]")
    cw_ids = ast.literal_eval(cw_ids)
    if len(cw_ids) == 1:
        cw_ids += [cw_ids[0] for i in range(len(api_session)-len(cw_ids))]
    else:
        cw_ids += [{} for i in range(len(api_session)-len(cw_ids))]
except:
    cw_ids = [{} for i in api_session]    
    
if isinstance(api_session, list):
    cuentas = [
        main(api_id,api_hash,str(api_session[i]),cw_ids[i]) for i in range(len(api_session))]
else:
    cuenta = main(api_id, api_hash, api_session, cw_ids)
    print (cuenta)
idle()
for cuenta in cuentas:
    cuenta.stop()
