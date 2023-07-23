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
api_session = str("AQAUaEYAI5HsvsoLEf0t1jTms6vg3SGuQRYPGfzB5e40suYDUtM0h2r8iX4q4iqIQ-WIVAvU9XS5MBwo2PPdcJrdVyqZpF0oa7e_YOmMAOW5wXfgvZTnOwpIIHq11F14m6k2VXnLtgPuWalI5K7frwULMBhmzbfzKsOPBCw3yY8A4aiQtUlu93xoIrGbDJnkVKYJ4xZkyqGQ_W1fiA7hPvGuMhngBscARJ8AagodF4bLmsm_0dp-Wt4ao_6vZQ_VLp2Hra9XZQsh8CxSVe2JLAS38g_C5ZpFz8a-9K85hXGZ83LrobBiLdehSEtIxnwfBZ7H2LUeOydJfXswbhToiHturZNnZAAAAAAmdd42AA")

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
