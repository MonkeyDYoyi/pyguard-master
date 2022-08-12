from pickle import TRUE


class main:
    def __init__(self, api_id, api_hash, api_session, CW_ids:dict={}):
        import logging
        log = logging.getLogger()
        
        self.api_id = api_id
        self.api_hash = api_hash
        self.api_session = api_session

        # from pyrogram import Client, MessageHandler, Filters
        from pyrogram import Client#, Filters, MessageHandler
        try:
            from pyrogram import MessageHandler                  
        except ImportError:
            from pyrogram.handlers import MessageHandler
        try:
            from pyrogram import Filters                  
        except ImportError:
            from pyrogram import filters    
        #from pyrogram.api import functions
        try:
            from pyrogram.api import functions
        except ImportError:
            from pyrogram.raw import functions
        from numpy.random import randint
        
        import re
        import time
        from datetime import datetime, timedelta
        import os
        import random
        from pyrogram.errors import AuthKeyUnregistered, MessageIdInvalid, AuthKeyDuplicated

        app = Client(api_session, api_id, api_hash)
        try:
            app.start()
        except AuthKeyUnregistered:
            log.warning("Han desactivado este HASH: "+api_session)
            return
        except AuthKeyDuplicated:
            raise Exception("ERROR!! HASH DUPLICADO" + api_session)
        ids = {}
        mainIds = {}
        cousinIds = {}
       
        me=app.get_me()
        me.username = me.username if me.username else me.first_name

        """
        MAINS IDS
        """
        mainIds ["crazzy"] = 774368292
        mainIds ["yoyi"] = 645258806
        mainIds ["ines"] = 835010162
        mainIds ["imanol"] = 716287267
        mainIds ["brian"] = 705724375
        mainIds ["rodrigo"] = 609697213        
        mainIds ["barbaro"] = 918655458
        mainIds ["zoro"] = 434324721
        mainIds ["sir"] = 668189411
        mainIds ["mad"] = 732995570
        mainIds ["gaby"] = 696138098

        """
        COUSINS IDS
        """
        cousinIds ["sheik"] = 925069789
        cousinIds ["vivi"] = 721073856
        cousinIds ["pumpkin"] = 959027567
        cousinIds ["niko"] = 827072071
        cousinIds ["yuni"] = 941568573
        cousinIds ["harry"] = 896337255
        cousinIds ["UwU"] = 820726863
        cousinIds ["Shiro"] = 978699363
        cousinIds ["paulita"] = 991929844
        cousinIds ["ungrim"] = 955268100

        """
        CW CODE
        """
        ids["CW"] = 408101137 #game
        ids["CastleOrders"] = -1001155831076 #Lupus
        ids["Auction"] = -1001209424945 #Auctions
        ids["Grup"] = -1001386769293 #Coffee Break Guild Chat
        ids["Canal"] = -1001194163201 #Coffee Break Guild Channel
        ids["Caza"] = 807376493 #Botdecaza
        ids["helper"] = 1137518285 #Bot de ayuda dreadwitch
        ids["RangerSquad"] = -1001227862489
        ids["spam_CB"] = -1001155668487
        ids["grup_mm"] = -1001274004593
        ids["GrupBlanco"] = -1001192852225#Coffee Break Guild Chat clean
        ids["Suicide_Squad"] = -1001367858712 #Canal del escuadrón suicida
        ids["vivi"] = 721073856
        ids["sheik"] = 925069789
        ids["yoyi"] = 645258806
        ids["EVENT"] = -1001744603110 #EVENT GROUP
        ids["EVENT2"] = -1001249772299 #EVENT GROUP 2
        ids["Lycaon"] =  976918452#Lycaon bot

        try:
            ids.update(CW_ids)
        except:
            log.warning("CW_ids not found or is an incorrect dict")

        GC = True if (me.id == cousinIds ["pumpkin"]) else False
        GCmm = True if (me.id == 883822191) else False
        auto_quest=False
        caza = False
        quest = "🍄Swamp" if ((me.id == 645258806) or (me.id == 740687108)) else ("🌲Forest" if  (me.id == 645258856 or me.id == 1347467384) else "🍄Swamp")
        if ((me.id == cousinIds["UwU"]) or (me.id == cousinIds["paulita"])):
            quest = "⛰️Valley" 
        level=-1
        ff=True
        #collector = True if ((me.id == 802156685) or (me.id == 740687108) or (me.id == 955268100)or (me.id == 953357637)or (me.id == 925069789)) else False 
        collector = False
        #Blacksmith =True if (me.id == 645258806) else False
        Blacksmith = False 
        alch = False
        en_quest=False
        gast_stmn=True
        #sentinela = True if (me.id == mainIds ["rodrigo"] or (me.id == mainIds ["brian"]) or (me.id == mainIds ["zoro"]) or (me.id == mainIds ["gaby"])) else False
        sentinela = False
        tactics = "/tactics_eagles"
        cod_trader = "09" if (me.id == 873541475) else ("55" if (me.id == 434324721) else "41")
        trader = True if ((me.id == 609697213) or (me.id == 705724375) or (me.id == 434324721) or (me.id == mainIds ["gaby"])) else False
        ofertas = True if ((me.id == 774368292) or (me.id == 716287267)) else False
        #knight = True if ((me.id == 835010542) or (me.id == 953357637) or (mainIds ["crazzy"]) or (mainIds ["sir"]) or (mainIds ["ines"]) or (mainIds ["barbaro"]) or (mainIds ["mad"]) or (mainIds ["imanol"]) or (cousinIds ["pumpkin"]) or (cousinIds ["niko"])) else False
        knight = False
        ranger = False 
        if((me.id == 774391292) or (me.id == mainIds["rodrigo"]) or (me.id == mainIds["zoro"]) or (me.id == mainIds["brian"]) or (me.id == mainIds["barbaro"]) or (me.id == mainIds["mad"]) or (me.id == mainIds ["crazzy"])):
            ranger = True
        #ranger = False
        ambush = False if ranger else True
        if ((me.id == cousinIds ["harry"]) or (me.id == cousinIds ["yuni"])):
            ambush = False 
        ordenes = True #False if ranger else True 
        tregua = True
        rango_max = 6
        dice = False
        general = True if me.id == 835010162 else False
        general2 = True if me.id == 609697213 else False
        orden_adelantada = False
        #defensores = True if ((me.id == 983997362) or (me.id == 913237756) or (me.id == 883822191) or (me.id == 896337255)) else False  
        defensores = False  
        apuntar = False
        pet = True if me.id == 774368292 else False 
        gopher = False 
        warra = True if me.id == 835010162 else False
        pasapasa = False
        vago = True if me.id == 774368291 else False
        #added by Yoyi for testing porpouse
        vago_yoyi = True if (me.id == mainIds ["yoyi"] or me.id == 774368292) else False #Id de Kaizoku
        ratio = 0.7
        ratio_actual = 0
        # hp_regen_rate = 6
        # hunt_alredy_delayed = False
        alredy_defending = False
        target = 'none'
        FirstTime = True
        offhand_atack = 'none'
        offhand_defend = 'none'
        venom = True
        wait_time = 0
        tempbool = False
        tempID = 0
        autoOpenShop = True if (me.id == mainIds ["yoyi"] or me.id == cousinIds ["harry"]) else False
        stamina = 0
        # autoOpenShop = True if (me.id == cousinIds ["harry"]) else False

        #added by yoyi
        battle_hours = {}
        battle_hours["Batalla_7pm_-4UTC"] = 23 
        battle_hours["Batalla_3am_-4UTC"] = 7 
        battle_hours["Batalla_11am_-4UTC"] = 15 
        try:
            os.environ["YOYI_HUNT_GLOBAL"]
        except:
            os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"

        if (me.id == mainIds ["yoyi"] or me.id == cousinIds ["sheik"] or me.id == cousinIds ["vivi"] or me.id == mainIds ["zoro"]):
            ids["helper"] = 1242346205 #Bot de ayuda mugiwarabot
        if (me.id == mainIds ["yoyi"]):
            caza = True
            ratio = 0.5 
        loop_quest = False
        taberna = False
        event_flag = True
        mensaje_id = [12345]
        #end added by yoyi

        envio_rep = True if vago else False
        

        import time
        #added by Yoyi for testing porpouse
        def get_target(mensaje):
            nonlocal target
            # if re.search("⚔️Attacking 🐺", mensaje.text):
            #     target = 'wolf'
            if "⚔Attacking 🦅" in mensaje.text:
                target = 'eagle'
            elif "⚔Attacking 🦈" in mensaje.text:
                target = 'shark'
            elif "⚔Attacking 🌑" in mensaje.text:
                target = 'moon'
            elif "⚔Attacking 🥔" in mensaje.text:
                target = 'potato'
            elif "⚔Attacking 🦌" in mensaje.text:
                target = 'deer'
            elif "⚔Attacking 🐉" in mensaje.text:
                target = 'dragon'
            else:
                target = 'none'  
            # app.send_message(ids["helper"], "El target actual es "+ target)
        def check_knigth_or_senti():
            return ((me.id == 835010542) or (me.id == 953357637) or (me.id == mainIds ["crazzy"]) or (me.id == mainIds ["sir"]) or (me.id == mainIds ["ines"]) or (me.id == mainIds ["barbaro"]) or (me.id == mainIds ["mad"]) or (me.id == mainIds ["imanol"]) or (me.id == cousinIds ["pumpkin"]) or (me.id == mainIds ["zoro"]) or (me.id == mainIds ["rodrigo"]) or (me.id == mainIds ["brian"]) or (me.id == cousinIds ["niko"]) or (me.id == mainIds ["gaby"]) or (me.id == cousinIds ["ungrim"] or (me.id == cousinIds["Shiro"])))
        
        def check_alredy_got_classes():
           return (knight or sentinela or ranger or Blacksmith or collector or alch)

        def print_stored_clases():
            nonlocal knight, sentinela, ranger, Blacksmith, alch, collector
            value = ""
            if knight:
                value += "knight "
            if sentinela:
                value += "sentinel "
            if ranger:
                value += "ranger "
            if Blacksmith:
                value += "blacksmith "
            if alch:
                value += "alchemist "
            if collector:
                value += "collector "
            return value
        def send_me():
           app.send_message(ids["CW"], "🏅Me")

        def send_hero():
           app.send_message(ids["CW"], "/hero")

        #end added by Yoyi

        def cazar(mensaje):
            nonlocal level, ids, rango_max
            has_link = False
            if mensaje.edit_date: return None

            if re.search("lvl\.([0-9]+)", mensaje.text):
                mob_info = int(re.findall("lvl\.([0-9]+)", mensaje.text)[0])
                log.info (mob_info)
            else:
                mob_info = 999
                log.info ('No level encontrado en caza')
            
            if mensaje.reply_markup:
                if mensaje.reply_markup.inline_keyboard:
                    if re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url):
                        has_link=re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url).group()
            
            if int(level-10)< mob_info < int(level+rango_max):
                if re.search("an ambush\!", mensaje.text):
                    if GC or int(level)>mob_info or me.id == mainIds ["yoyi"]:
                        if has_link:
                            app.send_message(ids["CW"], str(has_link))
                        else:
                            mensaje.forward(ids["CW"])
                    else:
                        time.sleep(abs(int(level)-mob_info))
                        if has_link:
                            app.send_message(ids["CW"], str(has_link))
                        else:
                            mensaje.forward(ids["CW"])
                else:
                    if has_link:
                        app.send_message(ids["CW"], str(has_link))
                    else:
                        mensaje.forward(ids["CW"])

        def programar_ataque(mensaje, timer:int=randint(3, 7)):
            nonlocal app, ids
            try:
                orden_list=re.search("(⚔Attack) ([^\w\d\s]+)(\w+)",mensaje)
                if orden_list:
                    orden_list=orden_list.groups()
                    time.sleep(timer-2)
                    app.send_message(ids["Canal"], "#atk_"+orden_list[2].lower())
                    time.sleep(timer-2)
                    app.send_message(ids["CW"], orden_list[0])
                    time.sleep(timer-2)
                    app.send_message(ids["CW"], orden_list[1])
                else:
                    log.warning("No detecto el formato de ataque"+mensaje)
            except:
                log.warning("Alerta: El ataque no ha sido programado.")


        def orden_adelant(mensaje, timer:int=randint(3, 7)):
            nonlocal app, ids
            try:
                orden_list=re.search("(⚔Attack) ([^\w\d\s]+)(\w+)",mensaje)   
                if orden_list:
                    orden_list=orden_list.groups()
                    time.sleep(timer-2)
                    app.send_message(ids["Canal"], "#atkad_"+orden_list[2].lower())
                    time.sleep(timer-2)
                    app.send_message(ids["CW"], orden_list[0])
                    time.sleep(timer-2)
                    app.send_message(ids["CW"], orden_list[1])
                else:
                    log.warning("No detecto el formato de ataque"+mensaje)
            except:
                log.warning("Alerta: El ataque no ha sido programado.")

       
        def reporte():
            nonlocal ids, app, ordenes, auto_quest, caza, level, GC, GCmm, quest, ff, ambush, Blacksmith, en_quest, gast_stmn, sentinela, tactics, cod_trader, trader, ofertas, dice, apuntar, pet, gopher, log, loop_quest, taberna
            if loop_quest == True:
                temp = '🌲🍄⛰️loop_quest'
            else:
                temp = quest
            app.send_message(ids["helper"], "Hola, las funciones de ayuda al CW están activadas"+"\n"+
                 ("El autoquest a "+str(temp)+" está activado" if auto_quest else "El autoquest está desactivado")+"\n"+
                 ("Las órdenes automáticas están activadas" if ordenes else "Las órdenes automáticas están desactivadas")+"\n"+
                 ("Captarás las órdenes adelantadas de Ranger" if apuntar else "No captarás las órdenes adelantadas de Ranger")+"\n"+
                 ("La caza de mobs está activada" if caza else "La caza de mobs se encuentra desactivada")+"\n"+
                 "El level medio para la caza y ayuda en ambush fijado es: "+str(level)+"\n"+
                 ("La autoarena está activada" if ff else "La autoarena está desactivada")+"\n"+
                 ("La ayuda a las ambush está activada" if ambush else "La ayuda a las ambush está desactivada")+"\n"+
                 ("Se activará el loop de quest cuando se llene la stamina" if ordenes else "No se activará el loop de quest cuando se llene la stamina")+"\n"+
                 ("Las tactics fijadas son: "+tactics if sentinela else "Métele al /mem para que seas sentí con tactics 😜")+"\n"+
                 ("Las ofertas del auction se encuentran activadas" if ofertas else "Las ofertas del auction se encuentran desactivadas")+"\n"+ 
                 ("Deja el invento que tú no eres sentinela /mem 🌚 no vas a vender "+cod_trader if not sentinela else ("El trader se encuentra activado con el recurso: "+cod_trader if trader else "El trader se encuentra desactivado"))+"\n"+
                 ("El loop de los dados se encuentra activado" if dice else "El loop de los dados se encuentra desactivado")+"\n"+
                 ("El loop de taberna se encuentra activado" if taberna else "El loop de taberna se encuentra desactivado")+"\n"+
                 ("La diversión y el baño de tu mascota está en mis manos 😘"+"\n" if pet else "")+
                 ("Las funciones del GC se encuentran activadas" if GC else "Las funciones del GC se encuentran desactivadas ")+"\n"+
                 ("El tiempo de espera para cazar es de " +str(wait_time)+" segundos")+"\n"+
                 "El nivel detectado es: " + str(level)+"\n"+
                 "Las clases detectadas son: " + str(print_stored_clases())+"\n"+
                 ("/command_list")+"\n"+
                 ("/hunt_report")+"\n"+
                 ("/report")+"\n")

        def reporte_caza():
            nonlocal ratio, ratio_actual, vago_yoyi, caza
            cadena = ""
            cadena += "Reporte de variables de caza:\n"
            cadena += "Caza activada\n" if (caza == True) else "Caza desactivada\n"
            cadena += "Vago_yoyi activado\n" if (vago_yoyi == True) else "Vago_yoyi desactivado\n" 
            cadena += "Ratio umbral: " + "{:.2f}".format(ratio) + "\n" + "Ratio actual: " + "{:.2f}".format(ratio_actual) +"\n" + "\n" + "Delay en segundos: " + str(wait_time) + "\n\n"
            cadena += "Comandos de Caza:\n" + "/caza_on\n" + "/caza_off\n" + "/vago_yoyi_on\n" + "/vago_yoyi_off\n" + "/set_ratio\n" + "/set_hpRegen\n" + "/vago_yoyi\n" + "/check_delay\n"
            app.send_message(ids["helper"], cadena)  

        def mascota():
            nonlocal ids, app, pet, log
            timer = randint(1, 60) 
            while pet:
                app.send_message(ids["CW"], "/pet")
                time.sleep(2)
                app.send_message(ids["CW"], "⚽Play")
                time.sleep(2)
                app.send_message(ids["CW"], "🛁Clean")
                time.sleep(7200+timer)
                
        def selector_CW(message):
            #added by Yoyi for testing porpouse last four nonlocal variables
            nonlocal ids, app, ordenes, auto_quest, caza, level, GC, GCmm, quest, ff, ambush, Blacksmith, alch, en_quest, gast_stmn, sentinela, tactics, cod_trader, trader,ofertas, knight, collector, ranger, tregua, rango_max, dice, general, general2, orden_adelantada, defensores, apuntar, pet, warra, pasapasa, envio_rep, gopher, vago, log, vago_yoyi, ratio, ratio_actual, alredy_defending, target, offhand_atack, offhand_defend, venom, wait_time, autoOpenShop, stamina, loop_quest, taberna, tempbool, tempID, event_flag, mensaje_id
            
            mensaje = message
            timer = randint(3, 7)
            tiempo = randint(7, 60)
            open_shop = randint(600,860)
            tiempo_or = randint(5,600)
            timer_aq = randint(1, 60) 
            timer_rep = randint (1, 700)

            if (mensaje.chat.id==ids["CW"]) and (mensaje.from_user.id==ids["CW"]): #Game
                if "Congratulations! You are still alive." in mensaje.text: #Para que cuando llegue de un ambush diga con /f_report cómo fue la batalla y con /whois quién ayudo 
                    mensaje.click(0)
                    #app.send_message(ids["CW"], '/f_report')
                    time.sleep(timer)  
                    mensaje.click(1)
                    #mensaje.reply('/whois')
                    #added by Yoyi for testing porpouse
                    if vago_yoyi:
                        time.sleep(randint(3, 7)) 
                        app.send_message(ids["CW"], "🏅Me")
                    #end added by Yoyi
                elif ('You were strolling around on your horse' in mensaje.text and (check_knigth_or_senti())): # El más importante para que cuando llegue un foray de alguien más responda /go
                    auto_quest=False
                    time.sleep(tiempo)
                    mensaje.click(0)
                elif '/pledge' in mensaje.text: # Para que cuando llegue un pledge a un knight lo coja
                    mensaje.reply('/pledge')
                elif  'so you were banned.' in mensaje.text:
                    app.block_user(ids["CW"])
                elif 'Leaderboard of fighters' in mensaje.text and ff: # Loop para ir a la arena cuando da resultado de arena
                    time.sleep(timer)  
                    mensaje.reply('▶️Fast fight')
                elif 'You didn’t find an opponent. Return later.' in mensaje.text and ff:
                    time.sleep(timer)
                    mensaje.reply('▶️Fast fight')
                elif re.search("an ambush\!", mensaje.text):
                    mensaje.forward(ids["spam_CB"])
                elif 'You met some hostile creatures.' in mensaje.text:
                    #added by yoyi
                    if ((me.id == cousinIds ["UwU"]) or (me.id == cousinIds ["paulita"])):
                        mensaje.forward(mainIds ["gaby"])
                        return
                    if ((me.id == cousinIds ["vivi"]) and (os.environ["YOYI_HUNT_GLOBAL"] == "TRUE")):
                        mensaje.forward(mainIds ["yoyi"])
                        return
                    #end added by yoyi
                    mensaje.forward(ids["spam_CB"])
                    time.sleep(59+timer)
                    mensaje.forward(ids["Caza"])
                    
                elif "Class info: /class" in mensaje.text:
                    if (re.search(".+?🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹+Class info: /class", mensaje.text)):
                        ranger = True
                    else:
                        ranger = False

                    if (re.search(".+?⚔️.+?Class info: /class", mensaje.text)) or (re.search("⚔️.+?Class info: /class", mensaje.text)) or (re.search("⚔️+Class info: /class", mensaje.text)):
                        knight = True  
                    else:
                        knight = False                

                    if (re.search(".+?🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡+Class info: /class", mensaje.text)):
                        sentinela = True
                    else:
                        sentinela = False
                    
                    if (re.search(".+?⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️+Class info: /class", mensaje.text)):
                        alch = True
                    else:
                        alch = False
                    
                    if (re.search(".+?📦.+?Class info: /class", mensaje.text)) or (re.search("📦.+?Class info: /class", mensaje.text)) or (re.search("📦+Class info: /class", mensaje.text)):
                        collector = True
                    else:
                        collector = False
                    
                    if (re.search(".+?🛠.+?Class info: /class", mensaje.text)) or (re.search("🛠.+?Class info: /class", mensaje.text)) or (re.search("🛠+Class info: /class", mensaje.text)):
                        Blacksmith = True
                    else:
                        Blacksmith = False
                    
                    time.sleep(timer)
                    if(check_alredy_got_classes()):
                        app.send_message(ids["helper"], "Clase/es registrada: "+"\n"+("-Ranger"+"\n" if ranger else "")+("-Knight"+"\n" if knight else "")+("-Sentinel"+"\n" if sentinela else "")+("-Alchemist"+"\n" if alch else "")+("-Collector"+"\n" if collector else "")+("-Blacksmith"+"\n" if Blacksmith else ""))
                    else:
                        app.send_message(ids["helper"], "No cogió class")

                elif 'Invite has been sent.' in mensaje.text and GC:
                    time.sleep(timer)
                    app.send_message(ids["Grup"], 'Tómate un cafecito anda ☕️')
                elif '[invalid action]' in mensaje.text and GC:
                    time.sleep(timer)
                    app.send_message(ids["Grup"], 'No hay café pa ti ☕️')
                    
                elif 'Invite has been sent.' in mensaje.text and GCmm:
                    time.sleep(timer)
                    app.send_message(ids["grup_mm"], 'Tómate un cafecito anda ☕️')
                elif '[invalid action]' in mensaje.text and GCmm:
                    time.sleep(timer)
                    app.send_message(ids["grup_mm"], 'No hay café pa ti ☕️')
                elif "You'll be back in" in mensaje.text:
                    en_quest=True
                    time_enquest = int(re.findall("You'll be back in (\d+)", mensaje.text)[0])
                    time.sleep(15+time_enquest*60)
                    en_quest=False
                    time.sleep(timer)
                    mensaje.reply('🗺Quests')
               
                elif 'Many things can happen in the forest.' in mensaje.text and auto_quest:
                        time.sleep(timer)
                        if loop_quest == True:
                            if quest == '🌲Forest':
                                quest='🍄Swamp'
                            elif quest == '🍄Swamp':
                                quest='⛰️Valley'
                            elif quest == '⛰️Valley':
                                quest='🌲Forest'
                            elif quest == '🌲🍄⛰️loop_quest':
                                quest='🌲Forest'
                        if "🔥" in mensaje.text:
                            # app.send_message(ids["helper"], "Hay perseptive secker")
                            if (("🌲Forest 3min 🔥" in mensaje.text) or ("🌲Forest 5min 🔥" in mensaje.text)):
                                # app.send_message(ids["helper"], "Hay quest 🌲Forest")
                                quest='🌲Forest'
                            elif (("🍄Swamp 4min 🔥" in mensaje.text) or ("🍄Swamp 6min 🔥" in mensaje.text)):
                                # app.send_message(ids["helper"], "Hay quest 🍄Swamp")
                                quest='🍄Swamp'
                            elif (("🏔Mountain Valley 4min 🔥" in mensaje.text) or ("🏔Mountain Valley 6min 🔥" in mensaje.text)):
                                # app.send_message(ids["helper"], "Hay quest ⛰️Valley")
                                quest='⛰️Valley'
                        mensaje.click(quest)
                elif 'Stamina restored. You are ready for more adventures!' in mensaje.text and gast_stmn:
                    auto_quest=True
                    loop_quest = True
                    app.send_message(ids["helper"], "Autoquest activado")
                    quest='🌲🍄⛰️loop_quest'
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                    time.sleep(timer)
                    app.send_message(ids["CW"], '🗺Quests')
                elif (re.search("🏅Level: ([0-9]+)", mensaje.text)) and ('Battle of the seven castles in' in mensaje.text):
                    level = int(re.findall("🏅Level: ([0-9]+)", mensaje.text)[0])
                    if(level == -1):
                        app.send_message(ids["helper"], "No cogió level")
                    hp = int(re.findall("Hp\:.([0-9]+)", mensaje.text)[0])
                    #OJOOOOO obtener la stamina del player
                    stamina = int(re.findall("🔋Stamina: ([0-9]+)", mensaje.text)[0]) 
                    #added by Yoyi for testing porpouse
                    get_target(mensaje)
                    if re.search("🛡Defending", mensaje.text):
                        alredy_defending = True
                    else:
                        alredy_defending = False

                    hpMax = int(re.findall("Hp\:.([0-9]+)/([0-9]+)", mensaje.text)[0][1])
                    ratio_actual = float(hp)/float(hpMax)
                    if vago_yoyi:
                        if (caza or ambush):
                            #app.send_message(ids["helper"], "ratio_actual es: " + str(float(ratio_actual)))
                            if ratio_actual < ratio:
                                app.send_message(ids["helper"], "El valor del ratio actual es menor que el establecido, cuyo valor es de: " + str(float(ratio)))
                                # caza_previos_value = caza
                                # ambush_previos_value = ambush
                                caza = False
                                ambush = False
                                # if not hunt_alredy_delayed:
                                app.send_message(ids["helper"], "Caza y Ambush deshabilitados temporalmente.")
                                    # hunt_alredy_delayed = True #Para evitar otro delay en caso de que ya haya uno ejecutandose
                                
                                # time.sleep(((int(hpMax) - int(hp)) * 60 )/int(hp_regen_rate))
                                    #caza = True
                                    # caza = caza_previos_value
                                    # ambush = ambush_previos_value
                                    # hunt_alredy_delayed = False
                                # app.send_message(ids["CW"], "🏅Me")
                        elif ((stamina >= 5) and (ratio_actual >= ratio)): #OJOOO incluir condicion para comprobar estamina y activar la caza y ambush nuevamente
                            caza = True
                            if(me.id == mainIds["yoyi"]):
                                os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                                # hunt_count = 0
                            ambush = True
                            app.send_message(ids["helper"], "Detectamos vago_yoyi activado, ratio por encima del umbral y estamina superior a 5 y activamos la caza y ambush nuevamente. Desea desactivarlos? \n/vago_yoyi_off\n/caza_off\n/ambush_off")              
                    
                    #end added by Yoyi


                    #time.sleep(timer)
                    #mensaje.forward(ids["expbot"]) 
                    #if vago:
                        #if hp < 500:
                            #caza = False
                            #time.sleep(1800+timer_aq)
                            #app.send_message(ids["CW"], "🏅Me")
                        #else:
                            #caza = True
                elif ('You are ready to strike.' in mensaje.text) or ('You joined the defensive formations.' in mensaje.text):
                    if ranger:
                        caza = False
                        ambush = False
                        vago_yoyi = False
                        app.send_message(ids["helper"], "Caza automatica desactivada."+"\n"+
                        ("Ambush automatico desactivado.")+"\n"+
                        ("Vago_yoyi desactivado."))
                    if alch:
                        if('You are ready to strike.' in mensaje.text):
                            time.sleep(timer)
                            app.send_message(ids["CW"], "/on_508")
                        elif('You joined the defensive formations.' in mensaje.text):
                            time.sleep(timer)
                            app.send_message(ids["CW"], "/on_506")
                            
                elif re.search("Back in ([0-9]+)", mensaje.text):
                    quest_time = int(re.findall("Back in ([0-9]+)", mensaje.text)[0])
                elif re.search("carry ([0-9]+)", mensaje.text.lower()) and trader:
                    carry = int(re.findall("carry ([0-9]+)", mensaje.text.lower())[0])
                    app.send_message(ids["CW"], "/sc "+str(cod_trader)+" "+str(carry))
                elif ('⚜️Forbidden Champion') and ('Your attacks:') in mensaje.text:
                    time.sleep(timer)
                    mensaje.forward(ids["spam_CB"])

                elif 'won! - he takes' in mensaje.text and dice:
                    app.send_message(ids["CW"], '🎲Play some dice')

                elif 'Recipient shall send to bot:' in mensaje.text and warra and pasapasa:
                    mensaje.forward(ids["spam_CB"])
                    pasapasa = False
                elif 'Recipient shall send to bot:' in mensaje.text and GCmm and pasapasa:
                    mensaje.forward(ids["grup_mm"])
                    pasapasa = False

                elif 'Your result on the battlefield:' in mensaje.text and envio_rep and vago:
                    envio_rep = False
                    time.sleep(timer_rep)
                    mensaje.forward(ids["RangerSquad"])
                elif 'Not enough stamina. Come back after you take a rest.' in mensaje.text:
                    #desactivar la caza
                    caza = False
                    # vago_yoyi = False
                    if(me.id == mainIds["yoyi"]):
                        os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                    app.send_message(ids["helper"], "La caza de mobs se encuentra desactivada")
                    # app.send_message(ids["helper"], "Vago_yoyi desactivado")  
                elif 'You are preparing for a fight' in mensaje.text:
                    wait_time = wait_time + 1

                elif 'You took a pint of cold ale.' in mensaje.text and taberna:
                    # en_quest=True
                    temp_time = 5
                    time.sleep(15+temp_time*60)
                    # en_quest=False
                    time.sleep(timer)
                    app.send_message(ids["CW"],'🏰Castle') 
                elif '🍺The tavern opens in the evening' in mensaje.text and taberna:
                    time.sleep(timer)
                    app.send_message(ids["CW"],'🍺Tavern')
                elif 'Price of one pint: 3💰' in mensaje.text and taberna:
                    time.sleep(timer)  
                    app.send_message(ids["CW"],'🍺Have a pint')
                elif ((('Conversation complete.' in mensaje.text) or ('Who sits in a pub during daytime?' in mensaje.text) or ("You don't even have enough gold for a pint of ale. Why don't you get a job?" in mensaje.text))and taberna):
                    time.sleep(timer) 
                    taberna = False
                    app.send_message(ids["helper"], "Loop de taberna desactivado.")
                elif ('Recipient shall send to bot:' in mensaje.text) and tempbool:
                    tempbool = False
                    mensaje.forward(tempID)
                                 
            elif (mensaje.chat.id==ids["Auction"]) and ofertas:
                if "Mystery" in mensaje.text: 
                    time.sleep(timer)
                    mensaje.forward(ids["CW"])
             #   elif "stone" in mensaje.text: 
               #     time.sleep(timer)
                #    mensaje.forward(ids["CW"])

                          
                  
            # elif (mensaje.chat.id==ids["CastleOrders"]):
            #     if general:
            #         if '🛡Defenders defend the castle wall' in mensaje.text:
            #             time.sleep(timer-1)
            #             app.send_message(ids["Canal"], '#def_castillo')
            #             time.sleep(timer-1)
            #             app.send_message(ids["CW"], '🛡Defend')

            #         #elif ('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text):
            #             #programar_ataque(mensaje.text, timer)

            #         elif ('⚔BATTLE SOON!⚔' in mensaje.text):
            #             time.sleep(timer+2)
            #             app.send_message(ids["CW"], '⚽Play')
                   

            # elif (mensaje.chat.id==ids["RangerSquad"]) and (general2):
            #     #if ('⚔Attack' in mensaje.text):
            #         #if orden_adelantada:
            #             #orden_adelant(mensaje.text, timer)
            #             #orden_adelantada = False
   

            #     if ('🛡Defenders defend the castle wall' in mensaje.text):
            #         if orden_adelantada:
            #             time.sleep(timer-1)
            #             app.send_message(ids["Canal"], '#defad_castillo')
            #             time.sleep(7200)
            #             app.send_message(ids["CW"], '🛡Defend')
            #             orden_adelantada = False
                  

                
            elif caza and mensaje.chat.id==ids["CastleOrders"] and ("Be careful" in  mensaje.text):
                if vago:
                    rango_max = 7
                    cazar(mensaje)
                else:
                    rango_max = 6
                    cazar(mensaje)


            elif mensaje.chat.id==ids["spam_CB"]:
                if re.search("an ambush\!", mensaje.text):
                    if ambush:
                        if level < 36:
                            rango_max = 11
                            cazar(mensaje)
                        else:
                            if vago:
                                rango_max = 10
                                cazar(mensaje)
                            else:
                                rango_max = 9
                                cazar(mensaje)

                elif (caza) and ("Be careful" in  mensaje.text):
                    if(me.id == mainIds["yoyi"] or me.id == cousinIds ["sheik"] or me.id == cousinIds ["vivi"]):
                        if mensaje.from_user.id == cousinIds ["harry"]:
                            return None
                    else:
                        time.sleep(wait_time)
                    if vago:
                        rango_max = 10
                        cazar(mensaje)
                    else:
                        rango_max = 6
                        cazar(mensaje)

                elif ("/g_withdraw" in mensaje.text) and warra: 
                    mensaje.forward(ids["CW"])
                    pasapasa = True
                    
            elif mensaje.chat.id==ids["Grup"]:
                if re.search("an ambush\!", mensaje.text):
                    if ambush:
                        if level < 36:
                            rango_max = 11
                            cazar(mensaje)
                        else:
                            if vago:
                                rango_max = 10
                                cazar(mensaje)
                            else:
                                rango_max = 9
                                cazar(mensaje)

                elif ("/g_invite" in mensaje.text) and GC: 
                    time.sleep(timer)
                    mensaje.forward(ids["CW"])

            elif mensaje.chat.id==ids["GrupBlanco"]:
                if ("⛳️Battle results:" in mensaje.text):
                    if (autoOpenShop):
                        time.sleep(open_shop)
                        app.send_message(ids["CW"], '/myshop_open')
                    if(ranger):
                        ambush = True
                        app.send_message(ids["helper"], 'Ambush activado satisfactoriamente.')
                    if(alch):
                        if(not autoOpenShop):
                            time.sleep(open_shop)
                        time.sleep(timer)
                        app.send_message(ids["CW"], "/on_506")
 
                    
            # elif mensaje.chat.id==ids["grup_mm"]:

                    
              
            #     if ("/g_invite" in mensaje.text) and GCmm: 
            #         time.sleep(timer)
            #         mensaje.forward(ids["CW"])
                
            #     elif ("/g_withdraw" in mensaje.text) and GCmm: 
            #         mensaje.forward(ids["CW"])
            #         pasapasa = True

            #     elif ("#oa_on"==mensaje.text.lower()) and general2:
            #         orden_adelantada = True 
            #         app.send_message(ids["Grup"], "El envío de órdenes de ranger está activado" if orden_adelantada else "El envío de órdenes de ranger está desactivado")

            #     elif ("#oa_off"==mensaje.text.lower()) and general2:
            #         orden_adelantada = False
            #         app.send_message(ids["Grup"], "El envío de órdenes de ranger está activado" if orden_adelantada else "El envío de órdenes de ranger está desactivado")
               
            #     elif ("#open_shop" in mensaje.text) and Blacksmith:
            #         time.sleep(timer)
            #         app.send_message(ids["CW"], '/myshop_open')
            #     elif ("⛳️Battle results:" in mensaje.text):
            #         orden_adelantada = True
            #         envio_rep = True
            #         time.sleep(timer+420)
            #         app.send_message(ids["CW"], '/report')
            #         if Blacksmith:
            #             time.sleep(open_shop)
            #             app.send_message(ids["CW"], '/myshop_open')
            #         #elif sentinela:
            #             #time.sleep(open_shop)
            #             #app.send_message(ids["CW"], '/use_tnt')
            #         #elif knight:
            #             #time.sleep(open_shop)
            #             #app.send_message(ids["CW"], '/use_cry')
            #         #elif collector:
            #             #time.sleep(open_shop)
            #             #app.send_message(ids["CW"], '/use_crl')  
            #        #if general:
            #             #time.sleep(timer+450)
            #             #app.send_message(ids["CW"], '⚽Play')  

        
            #     elif (caza) and ("Be careful" in  mensaje.text):
            #         if vago:
            #             rango_max = 10
            #             cazar(mensaje)
            #         else:
            #             rango_max = 6
            #             cazar(mensaje)
       

            elif mensaje.chat.id==ids["Canal"]:

                #Added by Yoyi
                if '#def_castillo_forced' == mensaje.text:
                    app.send_message(ids["CW"], '🏅Me')
                    time.sleep(timer+1)
                    if not alredy_defending:
                        time.sleep(timer+1)
                        app.send_message(ids["CW"], '🛡Defend')
                #End added by Yoyi

                #if sentinela or defensores:
                # elif defensores:
                #     if ordenes:
                #         if '#def_guild' == mensaje.text:
                #             if defensores:
                #                 if sentinela:
                #                     app.send_message(ids["CW"], '🛡Defend')
                #                     time.sleep(timer+1)
                #                     app.send_message(ids["CW"], tactics)
                #                 else:
                #                     time.sleep(timer+1)
                #                     app.send_message(ids["CW"], '🛡Defend')
                #                     time.sleep(timer_aq+900)
                #                     auto_quest=True
                #                     app.send_message(ids["CW"], '🗺Quests')         
                #             else:
                #                 time.sleep(timer+1)
                #                 app.send_message(ids["CW"], '/g_def') 
                #                 time.sleep(timer+1)
                #                 app.send_message(ids["CW"], tactics) 
                elif (ranger and sentinela):
                    if ordenes:
                        if '#RSatk_dragons' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'dragon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🐉')                            
                        elif '#RSatk_sharks' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'shark':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦈') 
                        elif '#RSatk_eagles' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'eagle':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦅')
                        elif '#RSatk_deers' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'deer':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦌')
                        elif '#RSatk_potato' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'potato':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🥔')
                        elif '#RSatk_moon' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'moon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🌑')
                        elif '#RSdef_castillo' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if not alredy_defending:
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🛡Defend')
                        elif '#RSdef_guild' == mensaje.text and tregua:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def')                   
                        elif '#RSdef_total' == mensaje.text:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def')
                        elif re.search("ga_atk ([A-z0-9]+)", mensaje.text):
                            cod_atk = re.findall("ga_atk ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_atk "+cod_atk)  
                        elif re.search("ga_def ([A-z0-9]+)", mensaje.text):
                            cod_def = re.findall("ga_def ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_def "+cod_def)
                #elif not (sentinela) and not (defensores):
                elif (ranger and knight):
                    if ordenes:
                        if '#RKatk_dragons' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'dragon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🐉')                            
                        elif '#RKatk_sharks' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'shark':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦈') 
                        elif '#RKatk_eagles' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'eagle':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦅')
                        elif '#RKatk_deers' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'deer':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦌')
                        elif '#RKatk_potato' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'potato':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🥔')
                        elif '#RKatk_moon' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'moon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🌑')
                        elif '#RKdef_castillo' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if not alredy_defending:
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🛡Defend')
                        elif '#RKdef_guild' == mensaje.text and tregua:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def')                   
                        elif '#RKdef_total' == mensaje.text:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def')
                        elif re.search("ga_atk ([A-z0-9]+)", mensaje.text):
                            cod_atk = re.findall("ga_atk ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_atk "+cod_atk)  
                        elif re.search("ga_def ([A-z0-9]+)", mensaje.text):
                            cod_def = re.findall("ga_def ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_def "+cod_def)
                else:
                    if ordenes:
                        if '#atk_dragons' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'dragon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🐉')                            
                        elif '#atk_sharks' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'shark':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦈') 
                        elif '#atk_eagles' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'eagle':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦅')
                        elif '#atk_deers' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'deer':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦌')
                        elif '#atk_potato' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'potato':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🥔')
                        elif '#atk_moon' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'moon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🌑')
                        elif '#def_castillo' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if not alredy_defending:
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🛡Defend')
                        elif '#def_guild' == mensaje.text and tregua:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def')                   
                        elif '#def_total' == mensaje.text:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def')
                        elif re.search("ga_atk ([A-z0-9]+)", mensaje.text):
                            cod_atk = re.findall("ga_atk ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_atk "+cod_atk)  
                        elif re.search("ga_def ([A-z0-9]+)", mensaje.text):
                            cod_def = re.findall("ga_def ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_def "+cod_def)
                        
                    """ if apuntar:
                        if '#atkad_dragons' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'dragon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🐉')
                                if GC and orden_adelantada:
                                    orden_adelantada = False     
              
                        elif '#atkad_sharks' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'shark':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦈')
                                if GC and orden_adelantada:
                                    orden_adelantada = False      
              
                        elif '#atkad_eagles' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'eagle':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦅')
                                if GC and orden_adelantada:
                                    orden_adelantada = False 
              
                        elif '#atkad_deers' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'deer':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🦌')
                                if GC and orden_adelantada:
                                    orden_adelantada = False    
              
                        elif '#atkad_potato' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'potato':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🥔')
                                if GC and orden_adelantada:
                                    orden_adelantada = False         
              
                        elif '#atkad_moon' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if target != 'moon':
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '⚔Attack')
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🌑')
                                if GC and orden_adelantada:
                                    orden_adelantada = False    
              
                        elif '#defad_castillo' == mensaje.text:
                            app.send_message(ids["CW"], '🏅Me')
                            time.sleep(timer+1)
                            if not alredy_defending:
                                time.sleep(timer+1)
                                app.send_message(ids["CW"], '🛡Defend')
                                if GC and orden_adelantada:
                                    orden_adelantada = False  
              
                        elif '#defad_guild' == mensaje.text and tregua:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def')                   
                        elif '#defad_total' == mensaje.text:
                            time.sleep(timer+1)
                            app.send_message(ids["CW"], '/g_def C')
                        elif re.search("ga_atkad ([A-z0-9]+)", mensaje.text):
                            cod_atk = re.findall("ga_atkad ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_atk "+cod_atk)  
                        elif re.search("ga_defad ([A-z0-9]+)", mensaje.text):
                            cod_def = re.findall("ga_defad ([A-z0-9]+)", mensaje.text)[0]
                            app.send_message(ids["CW"], "/ga_def "+cod_def)  """
   
            elif mensaje.chat.id==ids["Suicide_Squad"]:
                mensaje.forward(ids["CW"])
                
            elif caza and mensaje.chat.id==ids["Caza"] and ("Prepare yourself to fight:" in  mensaje.text):
                if vago:
                    rango_max = 15
                    cazar(mensaje)
                else:
                    rango_max = 6
                    cazar(mensaje)

            #added by yoyi
            elif ((me.id == mainIds["yoyi"] or me.id == cousinIds["vivi"]) and ((mensaje.chat.id == cousinIds["vivi"]) or (mensaje.chat.id == cousinIds["sheik"]))):
                mensaje.forward(ids["CW"])
                if '/g_withdraw' in mensaje.text:
                    tempID = mensaje.chat.id
                    tempbool = True
                    
            elif ((me.id == cousinIds["vivi"] or me.id == cousinIds["sheik"]) and ((mensaje.chat.id == mainIds["yoyi"]) or (mensaje.chat.id == cousinIds["vivi"]))):
                if '/g_receive' in mensaje.text:
                    mensaje.forward(ids["CW"])
            
            elif ((mensaje.chat.id == ids["EVENT"] or mensaje.chat.id == ids["EVENT2"]) and event_flag):
                if(("fruit drinks." in mensaje.text) and ("🐺Wolfpack" in mensaje.text)):
                    mensaje.forward(ids["CW"])

            elif (mensaje.chat.id == ids["Lycaon"] and caza):
                if(("A new hunt is available:" in mensaje.text) and not(mensaje.message_id in mensaje_id)):
                    mensaje_id.append(mensaje.message_id)

                    # mensaje.click(1)

                    if mensaje.reply_markup:
                         if mensaje.reply_markup.inline_keyboard:
                            mensaje.forward(ids["CW"])
                            #  if re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url):
                    #             has_link=re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url).group()
                    
                    app.send_message(ids["helper"], "Hunt id added: " + str(mensaje.message_id))

            #end added by yoyi
    
            elif mensaje.chat.id==ids["helper"]:
                if re.search("level ([0-9]+)", mensaje.text.lower()):
                    level = int(re.findall("level ([0-9]+)", mensaje.text.lower())[0])
                    app.send_message(ids["helper"], "Level para caza registrado: "+str(level))
                elif re.search("sc ([0-9]+)", mensaje.text.lower()):
                    cod_trader = re.findall("sc ([0-9]+)", mensaje.text.lower())[0]
                    app.send_message(ids["helper"], "Recurso a vender al trader  registrado: "+cod_trader)
                elif "/trader"==mensaje.text.lower():
                    if (sentinela) or (me.id == 705724375):
                        trader = not trader
                        app.send_message(ids["helper"], "Trader activado" if trader else "Trader desactivado")
                    else:
                        app.send_message(ids["helper"], "Deja el invento que tú no eres sentinela /mem 🌚")
                elif "/aq"==mensaje.text.lower():
                    auto_quest = not auto_quest
                    app.send_message(ids["helper"], "Autoquest activado" if auto_quest else "Autoquest desactivado")
                elif 'swamp'==mensaje.text.lower():
                    quest='🍄Swamp'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                elif 'forest'==mensaje.text.lower():
                    quest='🌲Forest'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                elif 'valley'==mensaje.text.lower():
                    quest='⛰️Valley'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)

                elif 'loop_quest' == mensaje.text.lower():
                    loop_quest = True
                    quest='🌲🍄⛰️loop_quest'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)

                elif ("/gc"==mensaje.text.lower()):
                    GC = not GC
                    app.send_message(ids["helper"], "Las funciones del GC se encuentran activadas" if GC else "Las funciones del GC se encuentran desactivadas")
                elif ("/general"==mensaje.text.lower()):
                    general = not general
                    app.send_message(ids["helper"], "El envío de órdenes automáticas está activado" if general else "El envío de órdenes automáticas está desactivado")
                elif ("/captain"==mensaje.text.lower()):
                    general2 = not general2
                    app.send_message(ids["helper"], "El envío de órdenes automáticas está activado" if general2 else "El envío de órdenes automáticas está desactivado")
            
                elif "/caza"==mensaje.text.lower():
                    caza = not caza
                    if(me.id == mainIds["yoyi"]):
                        if(os.environ["YOYI_HUNT_GLOBAL"] == "TRUE"):
                            os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                        else:
                            os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                    app.send_message(ids["helper"], "La caza de mobs se encuentra activada" if caza else "La caza de mobs se encuentra desactivada")
                elif "/caza_on"==mensaje.text.lower():
                    caza = True
                    if(me.id == mainIds["yoyi"]):
                        os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                        # hunt_count = 0
                    app.send_message(ids["helper"], "La caza de mobs se encuentra activada")
                elif "/caza_off"==mensaje.text.lower():
                    caza = False
                    if(me.id == mainIds["yoyi"]):
                        os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                    app.send_message(ids["helper"], "La caza de mobs se encuentra desactivada") 
                elif "/ff"==mensaje.text.lower():
                    ff = not ff
                    app.send_message(ids["helper"], "La autoarena está activada" if ff else "La autoarena está desactivada")
                elif "/ambush"==mensaje.text.lower():
                    ambush = not ambush
                    app.send_message(ids["helper"], "La ayuda a las ambush está activada" if ambush else "La ayuda a las ambush está desactivada")
                elif "/ordenes"==mensaje.text.lower():
                    ordenes = not ordenes
                    app.send_message(ids["helper"], "Las órdenes automáticas están activadas" if ordenes else "Las órdenes automáticas están desactivadas") 
                elif "/apuntar"==mensaje.text.lower():
                    apuntar = not apuntar
                    app.send_message(ids["helper"], "Las órdenes adelantadas están activadas" if apuntar else "Las órdenes adelantadas están desactivadas")        
                elif 'moon'==mensaje.text.lower():
                    tactics='/tactics_moonlight'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)  
                elif 'potato'==mensaje.text.lower():
                    tactics='/tactics_potato'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'eagle'==mensaje.text.lower():
                    tactics='/tactics_highnest'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)  
                elif 'deer'==mensaje.text.lower():
                    tactics='/tactics_deerhorn'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'shark'==mensaje.text.lower():
                    tactics='/tactics_sharkteeth'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'dragon'==mensaje.text.lower():
                    tactics='/tactics_dragonscale'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif "/stamina"==mensaje.text.lower():
                    gast_stmn = not gast_stmn
                    app.send_message(ids["helper"], "Se activará el loop de quest cuando se llene la stamina" if ordenes else "No se activará el loop de quest cuando se llene la stamina")
                elif "/oferta"==mensaje.text.lower():
                    ofertas = not ofertas
                    app.send_message(ids["helper"], "Las ofertas del auction se encuentran activadas" if ofertas else "Las ofertas del auction se encuentran desactivadas") 
                elif "/dice"==mensaje.text.lower():
                    dice = not dice
                    app.send_message(ids["helper"], "El loop de los dados se encuentra activado" if dice else "El loop de los dados se encuentra desactivado") 

                # elif "/taberna"==mensaje.text.lower():
                #     taberna = not taberna
                #     app.send_message(ids["helper"], "El loop de taberna está activado" if taberna else "El loop de taberna se encuentra desactivado")
                elif "/mascota"==mensaje.text.lower():
                    pet = not pet
                    app.send_message(ids["helper"], "You are now the proud owner of a cute pet" if pet else "You just kill your pet I hope you feel great about it")
                    if pet:
                        mascota()
                elif "/gopher"==mensaje.text.lower():
                    gopher = not gopher
                    app.send_message(ids["helper"], "You are now the proud owner of a cute gopher" if gopher else "You just kill your gopher I hope you feel great about it")
                    #if gopher:
                        #gopher()
                
                elif "/sa"==mensaje.text.lower():
                    stamina_alt = not stamina_alt
                    app.send_message(ids["helper"], "True stamina_alt" if stamina_alt else "False stamina_alt")
                    

                elif "/report"==mensaje.text.lower():
                    reporte()
                elif "/on"==mensaje.text.lower():
                    (caza,ff,ambush,auto_quest,ordenes)=(True,True,True,True,True)
                    reporte()
                elif "/off"==mensaje.text.lower():
                    (caza,ff,ambush,auto_quest,ordenes)=(False,False,False,False,False)
                    reporte()

                #added by Yoyi for testing porpouse 
                # elif "/test"==mensaje.text.lower():
                #     app.send_message(ids["helper"], "Mensaje de prueba")                 
                elif (re.search("/set_ratio.([0-9]+)", mensaje.text)):
                    temp = int(re.findall("/set_ratio.([0-9]+)", mensaje.text)[0])
                    if temp <= 100 and temp >= 0:
                        ratio = float(temp)/100
                        app.send_message(ids["helper"], "Valor de ratio modificado correctamente, el nuevo valor es: " + str(int(ratio*100)))  
                    else:
                        app.send_message(ids["helper"], "Valor de ratio incorrecto, inserte un valor entre 0 y 100.")

                # elif (re.search("/set_hpRegen.([0-9]+)", mensaje.text)):
                #     hp_regen_rate = int(re.findall("/set_hpRegen.([0-9]+)", mensaje.text)[0])
                #     app.send_message(ids["helper"], "Valor de ratio modificado correctamente, el nuevo valor es: " + str(int(hp_regen_rate)))
                elif "/vago_yoyi" == mensaje.text.lower():
                    vago_yoyi = not vago_yoyi
                    # if(os.environ["YOYI_HUNT_GLOBAL"] == "TRUE"):
                    #     os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                    # else:
                    #     os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                    app.send_message(ids["helper"], "vago_yoyi activado" if vago_yoyi else "vago_yoyi desactivado")
                elif "/vago_yoyi_on" == mensaje.text.lower():
                    vago_yoyi = True
                    # os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                    app.send_message(ids["helper"], "Vago yoyi se encuentra activado")
                elif "/vago_yoyi_off" == mensaje.text.lower():
                    vago_yoyi = False
                    # os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                    app.send_message(ids["helper"], "Vago yoyi se encuentra desactivado")
                elif "/ambush_off" == mensaje.text.lower():
                    ambush = False
                    app.send_message(ids["helper"], "Ambush se encuentra desactivado")
                elif "/ambush_on" == mensaje.text.lower():
                    ambush = True
                    app.send_message(ids["helper"], "Ambush se encuentra activado")
                elif "/hunt_report" == mensaje.text.lower():
                    reporte_caza()
                elif "/me" == mensaje.text.lower():
                    send_me()
                elif "/hero" == mensaje.text.lower():
                    send_hero()                               
                elif "/use_peace" == mensaje.text.lower():
                    app.send_message(ids["CW"], '/use_p04')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p05')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p06')
                    time.sleep(randint(2, 6))
                elif "/use_rage" == mensaje.text.lower():
                    app.send_message(ids["CW"], '/use_p01')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p02')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p03')
                    time.sleep(randint(2, 6))
                elif "/use_morph" == mensaje.text.lower():
                    app.send_message(ids["CW"], '/use_p19')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p20')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p21')
                    time.sleep(randint(2, 6))
                elif "/use_mana" == mensaje.text.lower():
                    app.send_message(ids["CW"], '/use_p13')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p14')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p15')
                    time.sleep(randint(2, 6))
                elif "/use_greed" == mensaje.text.lower():
                    app.send_message(ids["CW"], '/use_p07')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p08')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p09')
                    time.sleep(randint(2, 6))
                elif "/use_nature" == mensaje.text.lower():
                    app.send_message(ids["CW"], '/use_p10')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p11')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p12')
                    time.sleep(randint(2, 6))
                elif "/use_duality" == mensaje.text.lower():
                    app.send_message(ids["CW"], '/use_p37')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p38')
                    time.sleep(randint(2, 6))
                    app.send_message(ids["CW"], '/use_p39')
                    time.sleep(randint(2, 6))
                elif "/loop_quest" == mensaje.text.lower():
                    auto_quest = not auto_quest
                    if auto_quest:
                        loop_quest = True
                        app.send_message(ids["helper"], "Autoquest activado")
                        quest='🌲🍄⛰️loop_quest'
                        time.sleep(2)
                        app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                    else:
                        loop_quest = False
                        app.send_message(ids["helper"], "Autoquest desactivado")
                elif "/loop_tavern" == mensaje.text.lower():
                    taberna = not taberna
                    app.send_message(ids["helper"], "El loop de taberna está activado" if taberna else "El loop de taberna se encuentra desactivado")
                elif "/event_on" == mensaje.text.lower():
                    event_flag = True
                    app.send_message(ids["helper"], "Funcionalidad del evento habilitada.")
                elif "/event_off" == mensaje.text.lower():
                    event_flag = False
                    app.send_message(ids["helper"], "Funcionalidad del evento deshabilitada.")
                elif "/event" == mensaje.text.lower():
                    event_flag = not event_flag
                    app.send_message(ids["helper"], "Funcionalidad del evento deshabilitada." if event_flag else "Funcionalidad del evento deshabilitada.")

                elif "/print" == mensaje.text.lower():
                    # app.send_message(ids["helper"], "La lista de ids de mensajes salvade es: " + str(", ".join(mensaje_id)))
                    app.send_message(ids["helper"], "La lista de ids de mensajes salvade es: " + str(mensaje_id))

                            #ONLY FOR TEST PURPOUSE
                elif ("A new hunt is available:" in mensaje.text and caza):
                    app.send_message(ids["helper"], "Ya estamos aqui.")
                    if(("A new hunt is available:" in mensaje.text) and not(mensaje.message_id in mensaje_id)):
                        app.send_message(ids["helper"], "A la pura se lo prometí.")
                        mensaje_id.append(mensaje.message_id)
                

                elif "/command_list" == mensaje.text.lower():
                    app.send_message(ids["helper"], "Added by yoyi"+"\n" + "Comandos de caza:\n" + "/caza_on\n" + "/caza_off\n" + "/vago_yoyi_on\n" + "/vago_yoyi_off\n" + "/set_ratio\n" + "/set_hpRegen\n" + "/check_delay\n" + "/hunt_report\n\n" + 
                    "Comandos de batalla:\n" + "/use_peace\n" + "/use_rage\n" + "/use_morph\n" + "/use_duality\n\n" + 
                    "Comandos de quest:\n" + "/use_greed\n" + "/use_nature\n\n" + 
                    "Comandos de programación:\n" + "/venom_on\n" + "/venom_off\n" + "/offhand_atack\n" + "/offhand_defend\n" + "/auto_open_shop_on\n" + "/auto_open_shop_off\n\n" +
                    "Otros:\n" + "/use_mana\n" + "/hero\n" + "/me\n" + "/report\n" + "/loop_quest\n" + "/loop_tavern\n" + "/event_off")
                elif "No cogió class" == mensaje.text.lower():
                    app.send_message(ids["CW"],"🏅Me")
                    time.sleep(10)
                elif "No cogió level" == mensaje.text.lower():
                    app.send_message(ids["CW"],"/hero")
                    time.sleep(10)

                elif ((re.search("/ga_atk [A-z0-9]+", mensaje.text) or re.search("/ga_atk_[A-z0-9]+", mensaje.text))):
                    temporal_time = datetime.utcnow()
                    actual_hour = int(temporal_time.hour)
                    # app.send_message(ids["helper"], "Hora actual: " + str(actual_hour))
                    if(actual_hour >= battle_hours["Batalla_3am_-4UTC"] and actual_hour < battle_hours["Batalla_11am_-4UTC"]):#próxima batalla es la de las 11am(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=((battle_hours["Batalla_11am_-4UTC"]-1) - int(temporal_time.hour)))
                    elif(actual_hour >= battle_hours["Batalla_11am_-4UTC"] and actual_hour < battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 7pm(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=((battle_hours["Batalla_7pm_-4UTC"]-1) - int(temporal_time.hour)))
                    elif(actual_hour >= battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=(battle_hours["Batalla_7pm_-4UTC"] - int(temporal_time.hour)) + battle_hours["Batalla_3am_-4UTC"] - 1)
                    elif(actual_hour < battle_hours["Batalla_3am_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=(battle_hours["Batalla_3am_-4UTC"] - 1 - int(temporal_time.hour)))
                    temporal_time = temporal_time.replace(minute= 53)
                    # app.send_message(ids["helper"], "Hora programada para rage: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                    if venom:
                        app.send_message(ids["helper"], "/use_rage", schedule_date = int(datetime.timestamp(temporal_time)))
                    if alch:
                        temporal_time = temporal_time.replace(minute= 55)
                        app.send_message(ids["CW"], "/on_508", schedule_date = int(datetime.timestamp(temporal_time)))
                    else:
                        if(offhand_atack != 'none'):
                            temporal_time = temporal_time.replace(minute= 55)
                            app.send_message(ids["CW"], offhand_atack, schedule_date = int(datetime.timestamp(temporal_time)))
                    temporal_time = temporal_time.replace(minute= 59)
                    # app.send_message(ids["helper"], "Hora programada para orden: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                    app.send_message(ids["CW"], mensaje.text, schedule_date = int(datetime.timestamp(temporal_time)))
                    app.send_message(ids["helper"], "Programada la orden y el rage satisfactoriamente")

                # elif ((me.id == mainIds["yoyi"]) and (re.search("/ga_def [A-z0-9]+", mensaje.text) or re.search("/ga_def_[A-z0-9]+", mensaje.text)  or re.search("/ga_def", mensaje.text))):
                elif ((re.search("/ga_def [A-z0-9]+", mensaje.text) or re.search("/ga_def_[A-z0-9]+", mensaje.text)  or re.search("/ga_def", mensaje.text))):
                    temporal_time = datetime.utcnow()
                    actual_hour = int(temporal_time.hour)
                    # app.send_message(ids["helper"], "Hora actual: " + str(actual_hour))
                    if(actual_hour >= battle_hours["Batalla_3am_-4UTC"] and actual_hour < battle_hours["Batalla_11am_-4UTC"]):#próxima batalla es la de las 11am(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=((battle_hours["Batalla_11am_-4UTC"]-1) - int(temporal_time.hour)))
                    elif(actual_hour >= battle_hours["Batalla_11am_-4UTC"] and actual_hour < battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 7pm(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=((battle_hours["Batalla_7pm_-4UTC"]-1) - int(temporal_time.hour)))
                    elif(actual_hour >= battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=(battle_hours["Batalla_7pm_-4UTC"] - int(temporal_time.hour)) + battle_hours["Batalla_3am_-4UTC"] - 1)
                    elif(actual_hour < battle_hours["Batalla_3am_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                        temporal_time = temporal_time + timedelta(hours=(battle_hours["Batalla_3am_-4UTC"] - 1 - int(temporal_time.hour)))
                    temporal_time = temporal_time.replace(minute= 53)
                    # app.send_message(ids["helper"], "Hora programada para peace: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                    if venom:
                        app.send_message(ids["helper"], "/use_peace", schedule_date = int(datetime.timestamp(temporal_time)))
                    if alch:
                        temporal_time = temporal_time.replace(minute= 55)
                        app.send_message(ids["CW"], "/on_506", schedule_date = int(datetime.timestamp(temporal_time)))
                    else:
                        if(offhand_defend != 'none'):
                            temporal_time = temporal_time.replace(minute= 55)
                            app.send_message(ids["CW"], offhand_defend, schedule_date = int(datetime.timestamp(temporal_time)))
                    temporal_time = temporal_time.replace(minute= 59)
                    # app.send_message(ids["helper"], "Hora programada para orden: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                    app.send_message(ids["CW"], mensaje.text, schedule_date = int(datetime.timestamp(temporal_time)))  
                    app.send_message(ids["helper"], "Programada la orden y el peace satisfactoriamente") 
                
                elif "/check_delay" == mensaje.text.lower():
                    app.send_message(ids["helper"], "El tiempo de espera para cazar es de " +str(wait_time)+" segundos")  
            
                elif "/auto_open_shop" == mensaje.text.lower():
                    autoOpenShop = not autoOpenShop
                    app.send_message(ids["helper"], "Apertura automática de shop luego de la batalla activada.\n" if autoOpenShop else "Apertura automática de shop luego de la batalla desactivada.\n")
                
                elif "/auto_open_shop_on" == mensaje.text.lower():
                    autoOpenShop = True
                    app.send_message(ids["helper"], "Apertura automática de shop luego de la batalla activada.\n")  
                
                elif "/auto_open_shop_off" == mensaje.text.lower():
                    autoOpenShop = False
                    app.send_message(ids["helper"], "Apertura automática de shop luego de la batalla desactivada.\n")  
                
                                  

                # elif "/test" == mensaje.text.lower():
                #     app.send_message(ids["helper"], str(os.environ["TEST_ENVIRONMENT_VARIABLE"]))
                #     test_time = datetime.now()
                #     test_time = test_time.replace(minute = (test_time.minute + 3))
                #     app.send_message(ids["helper"], str(test_time.minute))
                #     app.send_message(ids["helper"], "probando mensajes programados", schedule_date = int(datetime.timestamp(test_time)))
                    
                    

                # elif re.search("/write_env [A-z0-9]+", mensaje.text):
                #     os.environ["TEST_ENVIRONMENT_VARIABLE"] = str(re.findall("/write_env [A-z0-9]+", mensaje.text)[0])
                #     app.send_message(ids["helper"], str(os.environ["TEST_ENVIRONMENT_VARIABLE"]))

                elif (re.search("/offhand_atack (/on_[A-z0-9]+)", mensaje.text)):
                    temp = str(re.findall("/offhand_atack (/on_[A-z0-9]+)", mensaje.text)[0])
                    offhand_atack = temp
                    app.send_message(ids["helper"], "Offhand para ataque modificado correcatmente, el nuevo valor es: " + offhand_atack)  
                
                elif (re.search("/offhand_defend (/on_[A-z0-9]+)", mensaje.text)):
                    temp = str(re.findall("/offhand_defend (/on_[A-z0-9]+)", mensaje.text)[0])
                    offhand_defend = temp
                    app.send_message(ids["helper"], "Offhand para defensa modificado correcatmente, el nuevo valor es: " + offhand_defend) 
                
                elif "/venom_on" == mensaje.text.lower():
                     venom = True
                     app.send_message(ids["helper"], "Programación de rage y peace antes de la batalla activada.")
                elif "/venom_off" == mensaje.text.lower():
                     venom = False
                     app.send_message(ids["helper"], "Programación de rage y peace antes de la batalla desactivada.")
                elif "/venom" == mensaje.text.lower():
                    venom = not venom
                    app.send_message(ids["helper"], "Programación de rage y peace antes de la batalla activada." if venom else "Programación rage y peace antes de la batalla desactivada.")
                    

                #end added by Yoyi
                
                elif (re.search("🏅Level: ([0-9]+)", mensaje.text)) and ('Battle of the seven castles in' in mensaje.text):
                    level = int(re.findall("🏅Level: ([0-9]+)", mensaje.text)[0])
                    hp = int(re.findall("Hp\:.([0-9]+)", mensaje.text)[0])
                    if vago:
                        if hp < 500:
                            caza = False
                            time.sleep(1800+timer_aq)
                            app.send_message(ids["CW"], "🏅Me")
                        else:
                            caza = True    

                elif (GC) or (general):
                    if '🛡Defenders defend the castle wall' in mensaje.text:
                        time.sleep(timer-2)
                        app.send_message(ids["Canal"], '#def_castillo')
                        time.sleep(timer-2)
                        app.send_message(ids["CW"], '🛡Defend')
                    #elif ('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text):
                        #programar_ataque(mensaje.text, timer)
                elif general2:     
                    if '🛡Defenders defend the castle wall' in mensaje.text:
                        time.sleep(timer-1)
                        app.send_message(ids["Canal"], '#def_castillo')
                        time.sleep(timer-1)
                        app.send_message(ids["CW"], '🛡Defend')
                    #elif (('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text)) and (orden_adelantada):
                        #orden_adelant(mensaje.text, timer)
                        orden_adelantada = False
                    elif '⚔BATTLE IS OVER⚔' in mensaje.text:
                        orden_adelantada = True

                         
                            
                           

        
        """

        nonlocal FUNCTION

        """
      #Borrar aquellos que ids que no son utiles. 
        def chat_on():
            nonlocal ids
            dialogs = [i.chat.id for i in app.iter_dialogs()]
            faltan = False
            for k, v in ids.items():
                if  v not in dialogs:
                    ids[k]=1217879961
                    faltan = True
            if -1001386769293 in dialogs: #🔲 Alianza DRK EKE & no #🔰DRKyEKE alianza
                #Allies = Allies_cuadrado
                if faltan:
                    try:
                        app.send_message("@shitandtrash_bot", "/start")
                        app.send_message(1217879961,"mandaré aquí lo que deberia mandar a otros chats pero no pude."+
                                         "puedes moverlo a archivados, pero no lo borres por favor...")
                    except:
                        log.warning("No se ha podido unir al bot de Basuramia_bot")
           # if BS:
                #No_Allies = ["🌶"] + [ally for ally in Allies if ally not in ("🛹", "💍","🔍")]

     
        
        chat_on()
        #if ids["CW"] != 1217879961: #No está en la basura..
               #app.send_message(ids["CW"],"🏅Me")
               #time.sleep(10)
               #app.send_message(ids["CW"],"/hero")
               #time.sleep(10)
        if ids["helper"] != 1217879961: #No está en la basura...
               app.send_message(ids["helper"],"Bot reiniciado...!!! 😜😘")                
               reporte()
             #  mascota()
        

        #else:
            #def selector_CW(message): #borrar modulo CW
                #pass
        
        @app.on_message(Filters.chat(list(ids.values())) & Filters.text & ~Filters.scheduled)
        def cliente(client, message):
            nonlocal api_session, FirstTime
            if message.chat.id!=1217879961: #no es de Basuramia_bot
                if(FirstTime):
                    FirstTime = False
                    app.send_message(ids["CW"],"🏅Me")
                    time.sleep(3)
                    app.send_message(ids["CW"],"/hero")
                    #time.sleep(10)                    
                #try:
                    #if BS: selector_BS(message)
               # except Exception as e:
                   # log.warning(str(me.username)+" ha sufrido un error:", exc_info=True)
                try:
                    selector_CW(message)
                except Exception as e:
                    log.warning(str(me.username)+" ha sufrido un error:", exc_info=True)
            elif message.text == "ids":
                app.send_message(1217879961,str(ids))
            elif message.text == "users":
                usuarios = app.get_chat_members(-1001386769293)
                #usuarios += app.get_chat_members(-1001455157282) #🔲 Alianza DRK EKE
                app.send_message(1217879961,str([[member.user.first_name, member.user.id] for member in usuarios]))
            elif message.text == "hash":
                app.send_message(1217879961,str(api_session[0:20]))
                app.send_message(1217879961,str(api_session[-21:]))

    def stop(self):
        app.stop()
 