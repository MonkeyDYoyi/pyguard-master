from pickle import TRUE
from pyrogram import Client, filters
from pyrogram.types import Message, User
from pyrogram.raw import functions
import logging
from numpy.random import randint
import re
import time
from datetime import datetime, timedelta
import os
import random
from pyrogram.errors import AuthKeyUnregistered, MessageIdInvalid, AuthKeyDuplicated

log = logging.getLogger()

class pyguard:
    def __init__(self, cliente):
        # self.api_id = api_id
        # self.api_hash = api_hash
        # self.api_session = api_session 
        # self.app = Client(api_session, api_id=self.api_id, api_hash=self.api_hash, session_string=api_session) 
        self.app = cliente       
        
    async def initial_conditions(self, CW_ids:dict={}):
        async with self.app:
            # self.start()

            self.ids = {}
            self.mainIds = {}
            self.cousinIds = {}
        
            self.me = await self.app.get_me()
            self.me.username = self.me.username if self.me.username else self.me.first_name

            """
            MAINS IDS
            """
            self.mainIds ["yoyi"] = 645258806
            self.mainIds ["ines"] = 835010162
            self.mainIds ["imanol"] = 716287267
            """
            COUSINS IDS
            """
            self.cousinIds ["sheik"] = 925069789
            self.cousinIds ["vivi"] = 721073856
            self.cousinIds ["pumpkin"] = 959027567
            self.cousinIds ["harry"] = 896337255

            """
            CW CODE
            """
            self.ids["CW"] = 408101137 #game
            self.ids["CastleOrders"] = -1001155831076 #Lupus
            self.ids["Auction"] = -1001209424945 #Auctions
            self.ids["Grup"] = -1001386769293 #Coffee Break Guild Chat
            self.ids["Canal"] = -1001194163201 #Coffee Break Guild Channel
            self.ids["Caza"] = 807376493 #Botdecaza
            self.ids["helper"] = 1137518285 #Bot de ayuda dreadwitch
            self.ids["RangerSquad"] = -1001227862489
            self.ids["spam_CB"] = -1001155668487
            self.ids["GrupBlanco"] = -1001192852225#Coffee Break Guild Chat clean
            self.ids["Suicide_Squad"] = -1001367858712 #Canal del escuadrón suicida
            self.ids["EVENT"] = -1001744603110 #EVENT GROUP
            self.ids["EVENT2"] = -1001249772299 #EVENT GROUP 2
            self.ids["Lycaon"] =  976918452#Lycaon bot
            
            try:
                self.ids.update(CW_ids)
            except:
                log.warning("CW_ids not found or is an incorrect dict")

            self.GC = True if (self.me.id == self.cousinIds ["pumpkin"]) else False
            self.auto_quest=False
            self.caza = False
            self.quest = "🍄Swamp" #if ((self.me.id == 645258806) or (me.id == 740687108)) else ("🌲Forest" if  (me.id == 645258856 or me.id == 1347467384) else "🍄Swamp") 
            self.level=-1
            self.ff=True
            self.collector = False
            self.Blacksmith = False 
            self.alch = False
            self.knight = False
            self.ranger = False
            self.sentinela = False 
            self.en_quest=False
            self.gast_stmn=True        
            self.tactics = "/tactics_eagles"
            self.cod_trader = "09"
            self.trader = False 
            self.ofertas = False 
            self.ambush = False if self.ranger else True 
            self.ordenes = True #False if ranger else True 
            self.tregua = False
            self.rango_max = 6
            self.dice = False
            self.general = True if self.me.id == self.mainIds["ines"] else False
            self.general2 = False
            self.orden_adelantada = False
            self.defensores = False  
            self.apuntar = False
            self.pet = False 
            self.gopher = False 
            self.warra = False
            self.pasapasa = False
            self.vago = False
            #added by Yoyi for testing porpouse
            self.vago_yoyi = True if (self.me.id == self.mainIds ["yoyi"]) else False 
            self.ratio = 0.7
            self.ratio_actual = 0
            # hp_regen_rate = 6
            # hunt_alredy_delayed = False
            self.alredy_defending = False
            self.target = 'none'
            self.FirstTime = False
            self.offhand_atack = 'none'
            self.offhand_defend = 'none'
            self.venom = True
            self.wait_time = 0
            self.tempbool = False
            self.tempID = 0
            self.autoOpenShop = False #True if (self.me.id == self.mainIds ["yoyi"]) else False
            self.stamina = 0

            #added by yoyi
            self.battle_hours = {}
            self.battle_hours["Batalla_7pm_-4UTC"] = 23 
            self.battle_hours["Batalla_3am_-4UTC"] = 7 
            self.battle_hours["Batalla_11am_-4UTC"] = 15 
            try:
                os.environ["YOYI_HUNT_GLOBAL"]
            except:
                os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"

            if (self.me.id == self.mainIds ["yoyi"] or self.me.id == self.cousinIds ["sheik"] or self.me.id == self.cousinIds ["vivi"]):
                self.ids["helper"] = 1242346205 #Bot de ayuda mugiwarabot
            if (self.me.id == self.mainIds ["yoyi"]):
                self.caza = True
                self.ratio = 0.5 
            self.loop_quest = False
            self.taberna = False
            self.event_flag = True
            self.mensaje_id = [12345]
            #end added by yoyi

            self.envio_rep = True if self.vago else False

            # self.chat_on()
            # #if ids["CW"] != 1217879961: #No está en la basura..
            #        #self.app.send_message(ids["CW"],"🏅Me")
            #        #time.sleep(10)
            #        #self.app.send_message(ids["CW"],"/hero")
            #        #time.sleep(10)
            # if self.ids["helper"] != 1217879961: #No está en la basura...
            #        self.app.send_message(self.ids["helper"],"Bot reiniciado...!!! 😜😘")                
            #        self.reporte()
            #      #  mascota()
            # @self.app.on_message(filters.chat(list(self.ids.values())) & filters.text & ~filters.scheduled)
            # def cliente(client: Client, message: Message):
            #     if message.chat.id!=1217879961: #no es de Basuramia_bot
            #         if(self.FirstTime):
            #             self.FirstTime = False
            #             self.app.send_message(self.ids["CW"],"🏅Me")
            #             time.sleep(3)
            #             self.app.send_message(self.ids["CW"],"/hero")
            #             #time.sleep(10)                    
            #         #try:
            #             #if BS: selector_BS(message)
            #         # except Exception as e:
            #             # log.warning(str(me.username)+" ha sufrido un error:", exc_info=True)
            #         try:
            #             self.selector_CW(message)
            #         except Exception as e:
            #             log.warning(str(self.me.username)+" ha sufrido un error:", exc_info=True)
            #     elif message.text == "ids":
            #         self.app.send_message(1217879961,str(self.ids))
            #     elif message.text == "users":
            #         usuarios = self.app.get_chat_members(-1001386769293)
            #         #usuarios += self.app.get_chat_members(-1001455157282) #🔲 Alianza DRK EKE
            #         self.app.send_message(1217879961,str([[member.user.first_name, member.user.id] for member in usuarios]))
            #     elif message.text == "hash":
            #         self.app.send_message(1217879961,str(api_session[0:20]))
            #         self.app.send_message(1217879961,str(api_session[-21:]))
        
        #added by Yoyi for testing porpouse
    def get_target(self, mensaje: Message):
        # if re.search("⚔️Attacking 🐺", mensaje.text):
        #     target = 'wolf'
        if "⚔Attacking 🦅" in mensaje.text:
            self.target = 'eagle'
        elif "⚔Attacking 🦈" in mensaje.text:
            self.target = 'shark'
        elif "⚔Attacking 🌑" in mensaje.text:
            self.target = 'moon'
        elif "⚔Attacking 🥔" in mensaje.text:
            self.target = 'potato'
        elif "⚔Attacking 🦌" in mensaje.text:
            self.target = 'deer'
        elif "⚔Attacking 🐉" in mensaje.text:
            self.target = 'dragon'
        else:
            self.target = 'none'  

    def check_knigth_or_senti(self):
        return ((self.me.id == self.mainIds ["ines"]) or (self.me.id == self.mainIds ["imanol"]) or (self.me.id == self.cousinIds ["pumpkin"]) or (self.me.id == self.cousinIds ["vivi"]))
        
    def check_alredy_got_classes(self):
       return (self.knight or self.sentinela or self.ranger or self.Blacksmith or self.collector or self.alch)

    def print_stored_clases(self):
        value = ""
        if self.knight:
            value += "knight "
        if self.sentinela:
            value += "sentinel "
        if self.ranger:
            value += "ranger "
        if self.Blacksmith:
            value += "blacksmith "
        if self.alch:
            value += "alchemist "
        if self.collector:
            value += "collector "
        return value

    def send_me(self):
        self.app.send_message(self.ids["CW"], "🏅Me")

    def send_hero(self):
        self.app.send_message(self.ids["CW"], "/hero")

        #end added by Yoyi

    def cazar(self, mensaje: Message):
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
        if int(self.level-10)< mob_info < int(self.level+self.rango_max):
            if re.search("an ambush\!", mensaje.text):
                if self.GC or int(self.level)>mob_info or self.me.id == self.mainIds["yoyi"]:
                    if has_link:
                        self.app.send_message(self.ids["CW"], str(has_link))
                    else:
                        mensaje.forward(self.ids["CW"])
                else:
                    time.sleep(abs(int(self.level)-mob_info))
                    if has_link:
                        self.app.send_message(self.ids["CW"], str(has_link))
                    else:
                        mensaje.forward(self.ids["CW"])
            else:
                if has_link:
                    self.app.send_message(self.ids["CW"], str(has_link))
                else:
                    mensaje.forward(self.ids["CW"])

    def programar_ataque(self, mensaje: Message, timer:int=randint(3, 7)):
        try:
            orden_list=re.search("(⚔Attack) ([^\w\d\s]+)(\w+)",mensaje)
            if orden_list:
                orden_list=orden_list.groups()
                time.sleep(timer-2)
                self.app.send_message(self.ids["Canal"], "#atk_"+orden_list[2].lower())
                time.sleep(timer-2)
                self.app.send_message(self.ids["CW"], orden_list[0])
                time.sleep(timer-2)
                self.app.send_message(self.ids["CW"], orden_list[1])
            else:
                log.warning("No detecto el formato de ataque"+mensaje)
        except:
            log.warning("Alerta: El ataque no ha sido programado.")

    def orden_adelant(self, mensaje: Message, timer:int=randint(3, 7)):
        try:
            orden_list=re.search("(⚔Attack) ([^\w\d\s]+)(\w+)",mensaje)   
            if orden_list:
                orden_list=orden_list.groups()
                time.sleep(timer-2)
                self.app.send_message(self.ids["Canal"], "#atkad_"+orden_list[2].lower())
                time.sleep(timer-2)
                self.app.send_message(self.ids["CW"], orden_list[0])
                time.sleep(timer-2)
                self.app.send_message(self.ids["CW"], orden_list[1])
            else:
                log.warning("No detecto el formato de ataque"+mensaje)
        except:
            log.warning("Alerta: El ataque no ha sido programado.")

    def reporte(self):
        if self.loop_quest == True:
            temp = '🌲🍄⛰️loop_quest'
        else:
            temp = self.quest
        self.app.send_message(self.ids["helper"], "Hola, las funciones de ayuda al CW están activadas"+"\n"+
                ("El autoquest a "+str(temp)+" está activado" if self.auto_quest else "El autoquest está desactivado")+"\n"+
                ("Las órdenes automáticas están activadas" if self.ordenes else "Las órdenes automáticas están desactivadas")+"\n"+
                ("Captarás las órdenes adelantadas de Ranger" if self.apuntar else "No captarás las órdenes adelantadas de Ranger")+"\n"+
                ("La caza de mobs está activada" if self.caza else "La caza de mobs se encuentra desactivada")+"\n"+
                "El level medio para la caza y ayuda en ambush fijado es: "+str(self.level)+"\n"+
                ("La autoarena está activada" if self.ff else "La autoarena está desactivada")+"\n"+
                ("La ayuda a las ambush está activada" if self.ambush else "La ayuda a las ambush está desactivada")+"\n"+
                ("Se activará el loop de quest cuando se llene la stamina" if self.ordenes else "No se activará el loop de quest cuando se llene la stamina")+"\n"+
                ("Las tactics fijadas son: "+self.tactics if self.sentinela else "Métele al /mem para que seas sentí con tactics 😜")+"\n"+
                ("Las ofertas del auction se encuentran activadas" if self.ofertas else "Las ofertas del auction se encuentran desactivadas")+"\n"+ 
                ("Deja el invento que tú no eres sentinela /mem 🌚 no vas a vender "+self.cod_trader if not self.sentinela else ("El trader se encuentra activado con el recurso: "+self.cod_trader if self.trader else "El trader se encuentra desactivado"))+"\n"+
                ("El loop de los dados se encuentra activado" if self.dice else "El loop de los dados se encuentra desactivado")+"\n"+
                ("El loop de taberna se encuentra activado" if self.taberna else "El loop de taberna se encuentra desactivado")+"\n"+
                ("La diversión y el baño de tu mascota está en mis manos 😘"+"\n" if self.pet else "")+
                ("Las funciones del GC se encuentran activadas" if self.GC else "Las funciones del GC se encuentran desactivadas ")+"\n"+
                ("El tiempo de espera para cazar es de " +str(self.wait_time)+" segundos")+"\n"+
                "El nivel detectado es: " + str(self.level)+"\n"+
                "Las clases detectadas son: " + str(self.print_stored_clases())+"\n"+
                ("/command_list")+"\n"+
                ("/hunt_report")+"\n"+
                ("/report")+"\n")

    def reporte_caza(self):
        cadena = ""
        cadena += "Reporte de variables de caza:\n"
        cadena += "Caza activada\n" if (self.caza == True) else "Caza desactivada\n"
        cadena += "Vago_yoyi activado\n" if (self.vago_yoyi == True) else "Vago_yoyi desactivado\n" 
        cadena += "Ratio umbral: " + "{:.2f}".format(self.ratio) + "\n" + "Ratio actual: " + "{:.2f}".format(self.ratio_actual) +"\n" + "\n" + "Delay en segundos: " + str(self.wait_time) + "\n\n"
        cadena += "Comandos de Caza:\n" + "/caza_on\n" + "/caza_off\n" + "/vago_yoyi_on\n" + "/vago_yoyi_off\n" + "/set_ratio\n" + "/set_hpRegen\n" + "/vago_yoyi\n" + "/check_delay\n"
        self.app.send_message(self.ids["helper"], cadena)  

    def mascota(self):
        timer = randint(1, 60) 
        while self.pet:
            self.app.send_message(self.ids["CW"], "/pet")
            time.sleep(2)
            self.app.send_message(self.ids["CW"], "⚽Play")
            time.sleep(2)
            self.app.send_message(self.ids["CW"], "🛁Clean")
            time.sleep(7200+timer)
                
    def selector_CW(self, message: Message):        
        mensaje = message
        timer = randint(3, 7)
        tiempo = randint(7, 60)
        open_shop = randint(600,860)
        tiempo_or = randint(5,600)
        timer_aq = randint(1, 60) 
        timer_rep = randint (1, 700)

        if (mensaje.chat.id==self.ids["CW"]) and (mensaje.from_user.id==self.ids["CW"]): #Game
            if "Congratulations! You are still alive." in mensaje.text: #Para que cuando llegue de un ambush diga con /f_report cómo fue la batalla y con /whois quién ayudo 
                mensaje.click(0)
                #self.app.send_message(ids["CW"], '/f_report')
                time.sleep(timer)  
                mensaje.click(1)
                #mensaje.reply('/whois')
                #added by Yoyi for testing porpouse
                if self.vago_yoyi:
                    time.sleep(randint(3, 7)) 
                    self.app.send_message(self.ids["CW"], "🏅Me")
                #end added by Yoyi
            elif ('You were strolling around on your horse' in mensaje.text and (self.check_knigth_or_senti())): # El más importante para que cuando llegue un foray de alguien más responda /go
                self.auto_quest=False
                time.sleep(tiempo)
                mensaje.click(0)
            elif '/pledge' in mensaje.text: # Para que cuando llegue un pledge a un knight lo coja
                mensaje.reply('/pledge')
            elif  'so you were banned.' in mensaje.text:
                self.app.block_user(self.ids["CW"])
            elif 'Leaderboard of fighters' in mensaje.text and self.ff: # Loop para ir a la arena cuando da resultado de arena
                time.sleep(timer)  
                mensaje.reply('▶️Fast fight')
            elif 'You didn’t find an opponent. Return later.' in mensaje.text and self.ff:
                time.sleep(timer)
                mensaje.reply('▶️Fast fight')
            elif re.search("an ambush\!", mensaje.text):
                mensaje.forward(self.ids["spam_CB"])
            elif 'You met some hostile creatures.' in mensaje.text:
                #added by yoyi
                if ((self.me.id == self.cousinIds["vivi"]) and (os.environ["YOYI_HUNT_GLOBAL"] == "TRUE")):
                    mensaje.forward(self.mainIds ["yoyi"])
                    return
                #end added by yoyi
                mensaje.forward(self.ids["spam_CB"])
                time.sleep(59+timer)
                mensaje.forward(self.ids["Caza"])                    
            elif "Class info: /class" in mensaje.text:
                if (re.search(".+?🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹+Class info: /class", mensaje.text)):
                    self.ranger = True
                else:
                    self.ranger = False
                if (re.search(".+?⚔️.+?Class info: /class", mensaje.text)) or (re.search("⚔️.+?Class info: /class", mensaje.text)) or (re.search("⚔️+Class info: /class", mensaje.text)):
                    self.knight = True  
                else:
                    self.knight = False                
                if (re.search(".+?🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡+Class info: /class", mensaje.text)):
                    self.sentinela = True
                else:
                    self.sentinela = False                    
                if (re.search(".+?⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️+Class info: /class", mensaje.text)):
                    self.alch = True
                else:
                    self.alch = False                    
                if (re.search(".+?📦.+?Class info: /class", mensaje.text)) or (re.search("📦.+?Class info: /class", mensaje.text)) or (re.search("📦+Class info: /class", mensaje.text)):
                    self.collector = True
                else:
                    self.collector = False                    
                if (re.search(".+?🛠.+?Class info: /class", mensaje.text)) or (re.search("🛠.+?Class info: /class", mensaje.text)) or (re.search("🛠+Class info: /class", mensaje.text)):
                    self.Blacksmith = True
                else:
                    self.Blacksmith = False                    
                time.sleep(timer)
                if(self.check_alredy_got_classes()):
                    self.app.send_message(self.ids["helper"], "Clase/es registrada: "+"\n"+("-Ranger"+"\n" if self.ranger else "")+("-Knight"+"\n" if self.knight else "")+("-Sentinel"+"\n" if self.sentinela else "")+("-Alchemist"+"\n" if self.alch else "")+("-Collector"+"\n" if self.collector else "")+("-Blacksmith"+"\n" if self.Blacksmith else ""))
                else:
                    self.app.send_message(self.ids["helper"], "No cogió class")
            elif 'Invite has been sent.' in mensaje.text and self.GC:
                time.sleep(timer)
                self.app.send_message(self.ids["Grup"], 'Tómate un cafecito anda ☕️')
            elif '[invalid action]' in mensaje.text and self.GC:
                time.sleep(timer)
                self.app.send_message(self.ids["Grup"], 'No hay café pa ti ☕️')                    
            elif "You'll be back in" in mensaje.text:
                self.en_quest=True
                time_enquest = int(re.findall("You'll be back in (\d+)", mensaje.text)[0])
                time.sleep(15+time_enquest*60)
                self.en_quest=False
                time.sleep(timer)
                mensaje.reply('🗺Quests')               
            elif 'Many things can happen in the forest.' in mensaje.text and self.auto_quest:
                    time.sleep(timer)
                    if self.loop_quest == True:
                        if self.quest == '🌲Forest':
                            self.quest='🍄Swamp'
                        elif self.quest == '🍄Swamp':
                            self.quest ='⛰️Valley'
                        elif self.quest == '⛰️Valley':
                            self.quest ='🌲Forest'
                        elif self.quest == '🌲🍄⛰️loop_quest':
                            self.quest ='🌲Forest'
                    if "🔥" in mensaje.text:
                        if (("🌲Forest 3min 🔥" in mensaje.text) or ("🌲Forest 5min 🔥" in mensaje.text)):
                            self.quest='🌲Forest'
                        elif (("🍄Swamp 4min 🔥" in mensaje.text) or ("🍄Swamp 6min 🔥" in mensaje.text)):
                            self.quest='🍄Swamp'
                        elif (("🏔Mountain Valley 4min 🔥" in mensaje.text) or ("🏔Mountain Valley 6min 🔥" in mensaje.text)):
                            self.quest='⛰️Valley'
                    mensaje.click(self.quest)
            elif 'Stamina restored. You are ready for more adventures!' in mensaje.text and self.gast_stmn:
                self.auto_quest=True
                self.loop_quest = True
                self.app.send_message(self.ids["helper"], "Autoquest activado")
                self.quest='🌲🍄⛰️loop_quest'
                self.app.send_message(self.ids["helper"], "Información de quest actualizada: "+ self.quest)
                time.sleep(timer)
                self.app.send_message(self.ids["CW"], '🗺Quests')
            elif (re.search("🏅Level: ([0-9]+)", mensaje.text)) and ('Battle of the seven castles in' in mensaje.text):
                self.level = int(re.findall("🏅Level: ([0-9]+)", mensaje.text)[0])
                if(self.level == -1):
                    self.app.send_message(self.ids["helper"], "No cogió level")
                hp = int(re.findall("Hp\:.([0-9]+)", mensaje.text)[0])
                #OJOOOOO obtener la stamina del player
                self.stamina = int(re.findall("🔋Stamina: ([0-9]+)", mensaje.text)[0]) 
                #added by Yoyi for testing porpouse
                self.get_target(mensaje)
                if re.search("🛡Defending", mensaje.text):
                    self.alredy_defending = True
                else:
                    self.alredy_defending = False
                hpMax = int(re.findall("Hp\:.([0-9]+)/([0-9]+)", mensaje.text)[0][1])
                self.ratio_actual = float(hp)/float(hpMax)
                if self.vago_yoyi:
                    if (self.caza or self.ambush):
                        if self.ratio_actual < self.ratio:
                            self.app.send_message(self.ids["helper"], "El valor del ratio actual es menor que el establecido, cuyo valor es de: " + str(float(self.ratio)))
                            self.caza = False
                            self.ambush = False
                            self.app.send_message(self.ids["helper"], "Caza y Ambush deshabilitados temporalmente.")

                    elif ((self.stamina >= 5) and (self.ratio_actual >= self.ratio)): #OJOOO incluir condicion para comprobar estamina y activar la caza y ambush nuevamente
                        self.caza = True
                        if(self.me.id == self.mainIds["yoyi"]):
                            os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                            # hunt_count = 0
                        self.ambush = True
                        self.app.send_message(self.ids["helper"], "Detectamos vago_yoyi activado, ratio por encima del umbral y estamina superior a 5 y activamos la caza y ambush nuevamente. Desea desactivarlos? \n/vago_yoyi_off\n/caza_off\n/ambush_off")                                  

            elif ('You are ready to strike.' in mensaje.text) or ('You joined the defensive formations.' in mensaje.text):
                if self.ranger:
                    self.caza = False
                    self.ambush = False
                    self.vago_yoyi = False
                    self.app.send_message(self.ids["helper"], "Caza automatica desactivada."+"\n"+
                    ("Ambush automatico desactivado.")+"\n"+
                    ("Vago_yoyi desactivado."))
                if self.alch:
                    if('You are ready to strike.' in mensaje.text):
                        time.sleep(timer)
                        self.app.send_message(self.ids["CW"], "/on_508")
                    elif('You joined the defensive formations.' in mensaje.text):
                        time.sleep(timer)
                        self.app.send_message(self.ids["CW"], "/on_506")                            
            elif re.search("Back in ([0-9]+)", mensaje.text):
                self.quest_time = int(re.findall("Back in ([0-9]+)", mensaje.text)[0])
            elif re.search("carry ([0-9]+)", mensaje.text.lower()) and self.trader:
                self.carry = int(re.findall("carry ([0-9]+)", mensaje.text.lower())[0])
                self.app.send_message(self.ids["CW"], "/sc "+str(self.cod_trader)+" "+str(self.carry))
            elif ('⚜️Forbidden Champion') and ('Your attacks:') in mensaje.text:
                time.sleep(timer)
                mensaje.forward(self.ids["spam_CB"])
            elif 'won! - he takes' in mensaje.text and self.dice:
                self.app.send_message(self.ids["CW"], '🎲Play some dice')
            elif 'Recipient shall send to bot:' in mensaje.text and self.warra and self.pasapasa:
                mensaje.forward(self.ids["spam_CB"])
                self.pasapasa = False
            elif 'Your result on the battlefield:' in mensaje.text and self.envio_rep and self.vago:
                self.envio_rep = False
                time.sleep(timer_rep)
                mensaje.forward(self.ids["RangerSquad"])
            elif 'Not enough stamina. Come back after you take a rest.' in mensaje.text:
                #desactivar la caza
                self.caza = False
                # vago_yoyi = False
                if(self.me.id == self.mainIds["yoyi"]):
                    os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                self.app.send_message(self.ids["helper"], "La caza de mobs se encuentra desactivada")
                # self.app.send_message(ids["helper"], "Vago_yoyi desactivado")  
            elif 'You are preparing for a fight' in mensaje.text:
                self.wait_time = self.wait_time + 1
            elif 'You took a pint of cold ale.' in mensaje.text and self.taberna:
                # en_quest=True
                temp_time = 5
                time.sleep(15+temp_time*60)
                # en_quest=False
                time.sleep(timer)
                self.app.send_message(self.ids["CW"],'🏰Castle') 
            elif '🍺The tavern opens in the evening' in mensaje.text and self.taberna:
                time.sleep(timer)
                self.app.send_message(self.ids["CW"],'🍺Tavern')
            elif 'Price of one pint: 3💰' in mensaje.text and self.taberna:
                time.sleep(timer)  
                self.app.send_message(self.ids["CW"],'🍺Have a pint')
            elif ((('Conversation complete.' in mensaje.text) or ('Who sits in a pub during daytime?' in mensaje.text) or ("You don't even have enough gold for a pint of ale. Why don't you get a job?" in mensaje.text)) and self.taberna):
                time.sleep(timer) 
                self.taberna = False
                self.app.send_message(self.ids["helper"], "Loop de taberna desactivado.")
            elif ('Recipient shall send to bot:' in mensaje.text) and self.tempbool:
                self.tempbool = False
                mensaje.forward(self.tempID)
            # if mensaje.reply_markup:
            #     self.app.send_message(ids["helper"], "A la pura se lo prometí.")
            #     if mensaje.reply_markup.inline_keyboard:
            #         self.app.send_message(ids["helper"], "A la pura se lo prometí 2.")
            #         self.app.send_message(ids["helper"],str(mensaje.reply_markup.inline_keyboard[0][0].switch_inline_query)) 
                    # self.app.send_message(ids["CW"],str(mensaje.reply_markup.inline_keyboard[0][0].switch_inline_query))
        elif (mensaje.chat.id==self.ids["CW"]) and (mensaje.from_user.id == self.ids["Lycaon"]):
            self.app.send_message(self.ids["helper"], "Ya estamos aquí.")
            if mensaje.reply_markup:
                self.app.send_message(self.ids["helper"], "A la pura se lo prometí.")
                if mensaje.reply_markup.ForceReply:
                    self.app.send_message(self.ids["helper"], "A la pura se lo prometí 2.")
                    self.app.send_message(self.ids["helper"],str(mensaje.reply_markup.ForceReply[0][0].switch_inline_query)) 
                    self.app.send_message(self.ids["CW"],str(mensaje.reply_markup.ForceReply[0][0].switch_inline_query)) 
        elif (mensaje.chat.id==self.ids["Auction"]) and self.ofertas:
            if "Mystery" in mensaje.text: 
                time.sleep(timer)
                mensaje.forward(self.ids["CW"])
            #   elif "stone" in mensaje.text: 
            #     time.sleep(timer)
            #    mensaje.forward(ids["CW"])                                            
            #                                 
        elif self.caza and mensaje.chat.id==self.ids["CastleOrders"] and ("Be careful" in  mensaje.text):
            if self.vago:
                self.rango_max = 7
                self.cazar(mensaje)
            else:
                self.rango_max = 6
                self.cazar(mensaje)
        elif mensaje.chat.id==self.ids["spam_CB"]:
            if re.search("an ambush\!", mensaje.text):
                if self.ambush:
                    if self.level < 36:
                        self.rango_max = 11
                        self.cazar(mensaje)
                    else:
                        if self.vago:
                            self.rango_max = 10
                            self.cazar(mensaje)
                        else:
                            self.rango_max = 9
                            self.cazar(mensaje)
            elif (self.caza) and ("Be careful" in  mensaje.text):
                if(self.me.id == self.mainIds["yoyi"] or self.me.id == self.cousinIds["sheik"] or self.me.id == self.cousinIds["vivi"]):
                    if mensaje.from_user.id == self.cousinIds["harry"]:
                        return None
                else:
                    time.sleep(self.wait_time)
                if self.vago:
                    self.rango_max = 10
                    self.cazar(mensaje)
                else:
                    self.rango_max = 6
                    self.cazar(mensaje)
            elif ("/g_withdraw" in mensaje.text) and self.warra: 
                mensaje.forward(self.ids["CW"])
                self.pasapasa = True                    
        elif mensaje.chat.id==self.ids["Grup"]:
            if re.search("an ambush\!", mensaje.text):
                if self.ambush:
                    if self.level < 36:
                        self.rango_max = 11
                        self.cazar(mensaje)
                    else:
                        if self.vago:
                            self.rango_max = 10
                            self.cazar(mensaje)
                        else:
                            self.rango_max = 9
                            self.cazar(mensaje)
            elif ("/g_invite" in mensaje.text) and self.GC: 
                time.sleep(timer)
                mensaje.forward(self.ids["CW"])
        elif mensaje.chat.id==self.ids["GrupBlanco"]:
            if ("⛳️Battle results:" in mensaje.text):
                if (self.autoOpenShop):
                    time.sleep(open_shop)
                    self.app.send_message(self.ids["CW"], '/myshop_open')
                if(self.ranger):
                    self.ambush = True
                    self.app.send_message(self.ids["helper"], 'Ambush activado satisfactoriamente.')
                if(self.alch):
                    if(not self.autoOpenShop):
                        time.sleep(open_shop)
                    time.sleep(timer)
                    self.app.send_message(self.ids["CW"], "/on_506")                     
              
        elif mensaje.chat.id==self.ids["Canal"]:
            #Added by Yoyi
            if '#def_castillo_forced' == mensaje.text:
                self.app.send_message(self.ids["CW"], '🏅Me')
                time.sleep(timer+1)
                if not self.alredy_defending:
                    time.sleep(timer+1)
                    self.app.send_message(self.ids["CW"], '🛡Defend')
            #End added by Yoyi
            elif (self.ranger and self.sentinela):
                if self.ordenes:
                    if '#RSatk_dragons' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'dragon':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🐉')                            
                    elif '#RSatk_sharks' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'shark':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦈') 
                    elif '#RSatk_eagles' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'eagle':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦅')
                    elif '#RSatk_deers' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'deer':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦌')
                    elif '#RSatk_potato' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'potato':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🥔')
                    elif '#RSatk_moon' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'moon':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🌑')
                    elif '#RSdef_castillo' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if not self.alredy_defending:
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🛡Defend')
                    elif '#RSdef_guild' == mensaje.text and self.tregua:
                        time.sleep(timer+1)
                        self.app.send_message(self.ids["CW"], '/g_def')                   
                    elif '#RSdef_total' == mensaje.text:
                        time.sleep(timer+1)
                        self.app.send_message(self.ids["CW"], '/g_def')
                    elif re.search("ga_atk ([A-z0-9]+)", mensaje.text):
                        cod_atk = re.findall("ga_atk ([A-z0-9]+)", mensaje.text)[0]
                        self.app.send_message(self.ids["CW"], "/ga_atk "+cod_atk)  
                    elif re.search("ga_def ([A-z0-9]+)", mensaje.text):
                        cod_def = re.findall("ga_def ([A-z0-9]+)", mensaje.text)[0]
                        self.app.send_message(self.ids["CW"], "/ga_def "+cod_def)
            #elif not (sentinela) and not (defensores):
            elif (self.ranger and self.knight):
                if self.ordenes:
                    if '#RKatk_dragons' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'dragon':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🐉')                            
                    elif '#RKatk_sharks' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'shark':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦈') 
                    elif '#RKatk_eagles' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'eagle':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦅')
                    elif '#RKatk_deers' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'deer':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦌')
                    elif '#RKatk_potato' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'potato':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🥔')
                    elif '#RKatk_moon' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'moon':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🌑')
                    elif '#RKdef_castillo' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if not self.alredy_defending:
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🛡Defend')
                    elif '#RKdef_guild' == mensaje.text and self.tregua:
                        time.sleep(timer+1)
                        self.app.send_message(self.ids["CW"], '/g_def')                   
                    elif '#RKdef_total' == mensaje.text:
                        time.sleep(timer+1)
                        self.app.send_message(self.ids["CW"], '/g_def')
                    elif re.search("ga_atk ([A-z0-9]+)", mensaje.text):
                        cod_atk = re.findall("ga_atk ([A-z0-9]+)", mensaje.text)[0]
                        self.app.send_message(self.ids["CW"], "/ga_atk "+cod_atk)  
                    elif re.search("ga_def ([A-z0-9]+)", mensaje.text):
                        cod_def = re.findall("ga_def ([A-z0-9]+)", mensaje.text)[0]
                        self.app.send_message(self.ids["CW"], "/ga_def "+cod_def)
            else:
                if self.ordenes:
                    if '#atk_dragons' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'dragon':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🐉')                            
                    elif '#atk_sharks' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'shark':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦈') 
                    elif '#atk_eagles' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'eagle':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦅')
                    elif '#atk_deers' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'deer':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🦌')
                    elif '#atk_potato' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'potato':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🥔')
                    elif '#atk_moon' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if self.target != 'moon':
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '⚔Attack')
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🌑')
                    elif '#def_castillo' == mensaje.text:
                        self.app.send_message(self.ids["CW"], '🏅Me')
                        time.sleep(timer+1)
                        if not self.alredy_defending:
                            time.sleep(timer+1)
                            self.app.send_message(self.ids["CW"], '🛡Defend')
                    elif '#def_guild' == mensaje.text and self.tregua:
                        time.sleep(timer+1)
                        self.app.send_message(self.ids["CW"], '/g_def')                   
                    elif '#def_total' == mensaje.text:
                        time.sleep(timer+1)
                        self.app.send_message(self.ids["CW"], '/g_def')
                    elif re.search("ga_atk ([A-z0-9]+)", mensaje.text):
                        cod_atk = re.findall("ga_atk ([A-z0-9]+)", mensaje.text)[0]
                        self.app.send_message(self.ids["CW"], "/ga_atk "+cod_atk)  
                    elif re.search("ga_def ([A-z0-9]+)", mensaje.text):
                        cod_def = re.findall("ga_def ([A-z0-9]+)", mensaje.text)[0]
                        self.app.send_message(self.ids["CW"], "/ga_def "+cod_def)                        
                  
        elif mensaje.chat.id==self.ids["Suicide_Squad"]:
            mensaje.forward(self.ids["CW"])                
        elif self.caza and mensaje.chat.id==self.ids["Caza"] and ("Prepare yourself to fight:" in  mensaje.text):
            if self.vago:
                self.rango_max = 15
                self.cazar(mensaje)
            else:
                self.rango_max = 6
                self.cazar(mensaje)
        #added by yoyi
        elif ((self.me.id == self.mainIds["yoyi"] or self.me.id == self.cousinIds["vivi"]) and ((mensaje.chat.id == self.cousinIds["vivi"]) or (mensaje.chat.id == self.cousinIds["sheik"]))):
            mensaje.forward(self.ids["CW"])
            if '/g_withdraw' in mensaje.text:
                self.tempID = mensaje.chat.id
                self.tempbool = True                    
        elif ((self.me.id == self.cousinIds["vivi"] or self.me.id == self.cousinIds["sheik"]) and ((mensaje.chat.id == self.mainIds["yoyi"]) or (mensaje.chat.id == self.cousinIds["vivi"]))):
            if '/g_receive' in mensaje.text:
                mensaje.forward(self.ids["CW"])            
        elif ((mensaje.chat.id == self.ids["EVENT"] or mensaje.chat.id == self.ids["EVENT2"]) and self.event_flag):
            if(("fruit drinks." in mensaje.text) and ("🐺Wolfpack" in mensaje.text)):
                mensaje.forward(self.ids["CW"])
        elif (mensaje.chat.id == self.ids["Lycaon"] and self.caza):
            if(("A new hunt is available:" in mensaje.text) and not(mensaje.message_id in self.mensaje_id)):
                self.mensaje_id.append(mensaje.message_id)
                # mensaje.click(1)
                if mensaje.reply_markup:
                    if mensaje.reply_markup.inline_keyboard:
                        # self.app.send_message(ids["helper"], str(mensaje.reply_markup.inline_keyboard[0][0]))
                        # self.app.send_message(ids["helper"], str(mensaje.reply_markup.inline_keyboard[0][0].switch_inline_query))
                        mypeer = self.app.resolve_peer(peer_id=self.ids["CW"])
                        time.sleep(1)
                        self.app.send(data = functions.messages.SaveDraft(peer=mypeer, message="@LycaonBot " + str(mensaje.reply_markup.inline_keyboard[0][0].switch_inline_query)))
                        # time.sleep(1)
                        # self.app.send(data = functions.messages.SetTyping(peer=mypeer, action=types.SendMessageTypingAction))
                        # self.app.send_message(ids["CW"], "@LycaonBot " + str(mensaje.reply_markup.inline_keyboard[0][0].switch_inline_query))
                        # functions.messages.SaveDraft(ids["CW"], "@LycaonBot " + str(mensaje.reply_markup.inline_keyboard[0][0].switch_inline_query))
                        # mensaje.forward(ids["CW"])
                        #  if re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url):
                #             has_link=re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url).group()                    
                # self.app.send_message(ids["helper"], "Hunt id added: " + str(mensaje.message_id))
        #end added by yoyi    
        elif mensaje.chat.id==self.ids["helper"]:
            if re.search("level ([0-9]+)", mensaje.text.lower()):
                level = int(re.findall("level ([0-9]+)", mensaje.text.lower())[0])
                self.app.send_message(self.ids["helper"], "Level para caza registrado: "+str(self.level))
            elif re.search("sc ([0-9]+)", mensaje.text.lower()):
                self.cod_trader = re.findall("sc ([0-9]+)", mensaje.text.lower())[0]
                self.app.send_message(self.ids["helper"], "Recurso a vender al trader  registrado: "+ self.cod_trader)
            elif "/trader"==mensaje.text.lower():
                if (self.sentinela):
                    self.trader = not self.trader
                    self.app.send_message(self.ids["helper"], "Trader activado" if self.trader else "Trader desactivado")
                else:
                    self.app.send_message(self.ids["helper"], "Deja el invento que tú no eres sentinela /mem 🌚")
            elif "/aq"==mensaje.text.lower():
                self.auto_quest = not self.auto_quest
                self.app.send_message(self.ids["helper"], "Autoquest activado" if self.auto_quest else "Autoquest desactivado")
            elif 'swamp'==mensaje.text.lower():
                self.quest='🍄Swamp'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Información de quest actualizada: "+ self.quest)
            elif 'forest'==mensaje.text.lower():
                self.quest='🌲Forest'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Información de quest actualizada: "+ self.quest)
            elif 'valley'==mensaje.text.lower():
                self.quest='⛰️Valley'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Información de quest actualizada: "+ self.quest)
            elif 'loop_quest' == mensaje.text.lower():
                self.loop_quest = True
                self.quest='🌲🍄⛰️loop_quest'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Información de quest actualizada: "+ self.quest)
            elif ("/gc"==mensaje.text.lower()):
                self.GC = not self.GC
                self.app.send_message(self.ids["helper"], "Las funciones del GC se encuentran activadas" if self.GC else "Las funciones del GC se encuentran desactivadas")
            elif ("/general"==mensaje.text.lower()):
                self.general = not self.general
                self.app.send_message(self.ids["helper"], "El envío de órdenes automáticas está activado" if self.general else "El envío de órdenes automáticas está desactivado")
            elif ("/captain"==mensaje.text.lower()):
                self.general2 = not self.general2
                self.app.send_message(self.ids["helper"], "El envío de órdenes automáticas está activado" if self.general2 else "El envío de órdenes automáticas está desactivado")            
            elif "/caza"==mensaje.text.lower():
                self.caza = not self.caza
                if(self.me.id == self.mainIds["yoyi"]):
                    if(os.environ["YOYI_HUNT_GLOBAL"] == "TRUE"):
                        os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                    else:
                        os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                self.app.send_message(self.ids["helper"], "La caza de mobs se encuentra activada" if self.caza else "La caza de mobs se encuentra desactivada")
            elif "/caza_on"==mensaje.text.lower():
                self.caza = True
                if(self.me.id == self.mainIds["yoyi"]):
                    os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                    # hunt_count = 0
                self.app.send_message(self.ids["helper"], "La caza de mobs se encuentra activada")
            elif "/caza_off"==mensaje.text.lower():
                self.caza = False
                if(self.me.id == self.mainIds["yoyi"]):
                    os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                self.app.send_message(self.ids["helper"], "La caza de mobs se encuentra desactivada") 
            elif "/ff"==mensaje.text.lower():
                self.ff = not self.ff
                self.app.send_message(self.ids["helper"], "La autoarena está activada" if self.ff else "La autoarena está desactivada")
            elif "/ambush"==mensaje.text.lower():
                self.ambush = not self.ambush
                self.app.send_message(self.ids["helper"], "La ayuda a las ambush está activada" if self.ambush else "La ayuda a las ambush está desactivada")
            elif "/ordenes"==mensaje.text.lower():
                self.ordenes = not self.ordenes
                self.app.send_message(self.ids["helper"], "Las órdenes automáticas están activadas" if self.ordenes else "Las órdenes automáticas están desactivadas") 
            elif "/apuntar"==mensaje.text.lower():
                self.apuntar = not self.apuntar
                self.app.send_message(self.ids["helper"], "Las órdenes adelantadas están activadas" if self.apuntar else "Las órdenes adelantadas están desactivadas")        
            elif 'moon'==mensaje.text.lower():
                self.tactics='/tactics_moonlight'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Tactics actualizadas: "+self.tactics)  
            elif 'potato'==mensaje.text.lower():
                self.tactics='/tactics_potato'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Tactics actualizadas: "+self.tactics)
            elif 'eagle'==mensaje.text.lower():
                self.tactics='/tactics_highnest'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Tactics actualizadas: "+self.tactics)  
            elif 'deer'==mensaje.text.lower():
                self.tactics='/tactics_deerhorn'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Tactics actualizadas: "+self.tactics)
            elif 'shark'==mensaje.text.lower():
                self.tactics='/tactics_sharkteeth'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Tactics actualizadas: "+self.tactics)
            elif 'dragon'==mensaje.text.lower():
                self.tactics='/tactics_dragonscale'
                time.sleep(2)
                self.app.send_message(self.ids["helper"], "Tactics actualizadas: "+self.tactics)
            elif "/stamina"==mensaje.text.lower():
                self.gast_stmn = not self.gast_stmn
                self.app.send_message(self.ids["helper"], "Se activará el loop de quest cuando se llene la stamina" if self.ordenes else "No se activará el loop de quest cuando se llene la stamina")
            elif "/oferta"==mensaje.text.lower():
                self.ofertas = not self.ofertas
                self.app.send_message(self.ids["helper"], "Las ofertas del auction se encuentran activadas" if self.ofertas else "Las ofertas del auction se encuentran desactivadas") 
            elif "/dice"==mensaje.text.lower():
                self.dice = not self.dice
                self.app.send_message(self.ids["helper"], "El loop de los dados se encuentra activado" if self.dice else "El loop de los dados se encuentra desactivado") 
            # elif "/taberna"==mensaje.text.lower():
            #     taberna = not taberna
            #     self.app.send_message(ids["helper"], "El loop de taberna está activado" if taberna else "El loop de taberna se encuentra desactivado")
            elif "/mascota"==mensaje.text.lower():
                self.pet = not self.pet
                self.app.send_message(self.ids["helper"], "You are now the proud owner of a cute pet" if self.pet else "You just kill your pet I hope you feel great about it")
                if self.pet:
                    self.mascota()
            elif "/gopher"==mensaje.text.lower():
                self.gopher = not self.gopher
                self.app.send_message(self.ids["helper"], "You are now the proud owner of a cute gopher" if self.gopher else "You just kill your gopher I hope you feel great about it")
                #if gopher:
                    #gopher()                
            elif "/sa"==mensaje.text.lower():
                self.stamina_alt = not self.stamina_alt
                self.app.send_message(self.ids["helper"], "True stamina_alt" if self.stamina_alt else "False stamina_alt")                    
            elif "/report"==mensaje.text.lower():
                self.reporte()
            elif "/on"==mensaje.text.lower():
                (self.caza,self.ff,self.ambush,self.auto_quest,self.ordenes)=(True,True,True,True,True)
                self.reporte()
            elif "/off"==mensaje.text.lower():
                (self.caza,self.ff,self.ambush,self.auto_quest,self.ordenes)=(False,False,False,False,False)
                self.reporte()
            #added by Yoyi for testing porpouse 
            # elif "/test"==mensaje.text.lower():
            #     self.app.send_message(ids["helper"], "Mensaje de prueba")                 
            elif (re.search("/set_ratio.([0-9]+)", mensaje.text)):
                temp = int(re.findall("/set_ratio.([0-9]+)", mensaje.text)[0])
                if temp <= 100 and temp >= 0:
                    self.ratio = float(temp)/100
                    self.app.send_message(self.ids["helper"], "Valor de ratio modificado correctamente, el nuevo valor es: " + str(int(self.ratio*100)))  
                else:
                    self.app.send_message(self.ids["helper"], "Valor de ratio incorrecto, inserte un valor entre 0 y 100.")
            # elif (re.search("/set_hpRegen.([0-9]+)", mensaje.text)):
            #     hp_regen_rate = int(re.findall("/set_hpRegen.([0-9]+)", mensaje.text)[0])
            #     self.app.send_message(ids["helper"], "Valor de ratio modificado correctamente, el nuevo valor es: " + str(int(hp_regen_rate)))
            elif "/vago_yoyi" == mensaje.text.lower():
                self.vago_yoyi = not self.vago_yoyi
                # if(os.environ["YOYI_HUNT_GLOBAL"] == "TRUE"):
                #     os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                # else:
                #     os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                self.app.send_message(self.ids["helper"], "vago_yoyi activado" if self.vago_yoyi else "vago_yoyi desactivado")
            elif "/vago_yoyi_on" == mensaje.text.lower():
                self.vago_yoyi = True
                # os.environ["YOYI_HUNT_GLOBAL"] = "TRUE"
                self.app.send_message(self.ids["helper"], "Vago yoyi se encuentra activado")
            elif "/vago_yoyi_off" == mensaje.text.lower():
                self.vago_yoyi = False
                # os.environ["YOYI_HUNT_GLOBAL"] = "FALSE"
                self.app.send_message(self.ids["helper"], "Vago yoyi se encuentra desactivado")
            elif "/ambush_off" == mensaje.text.lower():
                self.ambush = False
                self.app.send_message(self.ids["helper"], "Ambush se encuentra desactivado")
            elif "/ambush_on" == mensaje.text.lower():
                self.ambush = True
                self.app.send_message(self.ids["helper"], "Ambush se encuentra activado")
            elif "/hunt_report" == mensaje.text.lower():
                self.reporte_caza()
            elif "/me" == mensaje.text.lower():
                self.send_me()
            elif "/hero" == mensaje.text.lower():
                self.send_hero()                               
            elif "/use_peace" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"], '/use_p04')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p05')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p06')
                time.sleep(randint(2, 6))
            elif "/use_rage" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"], '/use_p01')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p02')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p03')
                time.sleep(randint(2, 6))
            elif "/use_morph" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"], '/use_p19')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p20')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p21')
                time.sleep(randint(2, 6))
            elif "/use_mana" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"], '/use_p13')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p14')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p15')
                time.sleep(randint(2, 6))
            elif "/use_greed" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"], '/use_p07')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p08')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p09')
                time.sleep(randint(2, 6))
            elif "/use_nature" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"], '/use_p10')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p11')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p12')
                time.sleep(randint(2, 6))
            elif "/use_duality" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"], '/use_p37')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p38')
                time.sleep(randint(2, 6))
                self.app.send_message(self.ids["CW"], '/use_p39')
                time.sleep(randint(2, 6))
            elif "/loop_quest" == mensaje.text.lower():
                self.auto_quest = not self.auto_quest
                if self.auto_quest:
                    self.loop_quest = True
                    self.app.send_message(self.ids["helper"], "Autoquest activado")
                    self.quest='🌲🍄⛰️loop_quest'
                    time.sleep(2)
                    self.app.send_message(self.ids["helper"], "Información de quest actualizada: "+ self.quest)
                else:
                    self.loop_quest = False
                    self.app.send_message(self.ids["helper"], "Autoquest desactivado")
            elif "/loop_tavern" == mensaje.text.lower():
                self.taberna = not self.taberna
                self.app.send_message(self.ids["helper"], "El loop de taberna está activado" if self.taberna else "El loop de taberna se encuentra desactivado")
            elif "/event_on" == mensaje.text.lower():
                self.event_flag = True
                self.app.send_message(self.ids["helper"], "Funcionalidad del evento habilitada.")
            elif "/event_off" == mensaje.text.lower():
                self.event_flag = False
                self.app.send_message(self.ids["helper"], "Funcionalidad del evento deshabilitada.")
            elif "/event" == mensaje.text.lower():
                self.event_flag = not self.event_flag
                self.app.send_message(self.ids["helper"], "Funcionalidad del evento deshabilitada." if self.event_flag else "Funcionalidad del evento deshabilitada.")
            #For testing porpouses
            elif "/print" == mensaje.text.lower():
                self.app.send_message(self.ids["helper"], "La lista de ids de mensajes salvade es: " + str(self.mensaje_id))
            elif "/mytest" == mensaje.text.lower():
                self.app.send_message(self.ids["helper"], "Probando, probando, 1,2,3.")                    
                # self.app.send_message(ids["helper"], print(functions.messages.GetChats(id=mainIds ["yoyi"])))
                mypeer = self.app.resolve_peer(peer_id=self.ids["helper"])
                # self.app.send(data=types.UpdateDraftMessage(peer=mypeer,draft=myDraftMessage))
                # types.UpdateDraftMessage(peer=types.InputPeerChat(chat_id =  mainIds ["yoyi"]),draft=myDraftMessage)
                time.sleep(1)
                self.app.send(data = functions.messages.SaveDraft(peer=mypeer, message="@LycaonBot " + "Esto es una prueba"))
                # time.sleep(3)
                #  functions.messages.SaveDraft(peer=types.InputPeerSelf(), message="@LycaonBot " + "Esto es una prueba")
                # types.DraftMessage(message="@LycaonBot " + "Esto es una prueba", date=int(time.time()))                                    
            elif "/command_list" == mensaje.text.lower():
                self.app.send_message(self.ids["helper"], "Added by yoyi"+"\n" + "Comandos de caza:\n" + "/caza_on\n" + "/caza_off\n" + "/vago_yoyi_on\n" + "/vago_yoyi_off\n" + "/set_ratio\n" + "/set_hpRegen\n" + "/check_delay\n" + "/hunt_report\n\n" + 
                "Comandos de batalla:\n" + "/use_peace\n" + "/use_rage\n" + "/use_morph\n" + "/use_duality\n\n" + 
                "Comandos de quest:\n" + "/use_greed\n" + "/use_nature\n\n" + 
                "Comandos de programación:\n" + "/venom_on\n" + "/venom_off\n" + "/offhand_atack\n" + "/offhand_defend\n" + "/auto_open_shop_on\n" + "/auto_open_shop_off\n\n" +
                "Otros:\n" + "/use_mana\n" + "/hero\n" + "/me\n" + "/report\n" + "/loop_quest\n" + "/loop_tavern\n" + "/event_off")
            elif "No cogió class" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"],"🏅Me")
                time.sleep(10)
            elif "No cogió level" == mensaje.text.lower():
                self.app.send_message(self.ids["CW"],"/hero")
                time.sleep(10)
            elif ((re.search("/ga_atk [A-z0-9]+", mensaje.text) or re.search("/ga_atk_[A-z0-9]+", mensaje.text))):
                temporal_time = datetime.utcnow()
                actual_hour = int(temporal_time.hour)
                # self.app.send_message(ids["helper"], "Hora actual: " + str(actual_hour))
                if(actual_hour >= self.battle_hours["Batalla_3am_-4UTC"] and actual_hour < self.battle_hours["Batalla_11am_-4UTC"]):#próxima batalla es la de las 11am(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=((self.battle_hours["Batalla_11am_-4UTC"]-1) - int(temporal_time.hour)))
                elif(actual_hour >= self.battle_hours["Batalla_11am_-4UTC"] and actual_hour < self.battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 7pm(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=((self.battle_hours["Batalla_7pm_-4UTC"]-1) - int(temporal_time.hour)))
                elif(actual_hour >= self.battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=(self.battle_hours["Batalla_7pm_-4UTC"] - int(temporal_time.hour)) + self.battle_hours["Batalla_3am_-4UTC"] - 1)
                elif(actual_hour < self.battle_hours["Batalla_3am_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=(self.battle_hours["Batalla_3am_-4UTC"] - 1 - int(temporal_time.hour)))
                temporal_time = temporal_time.replace(minute= 53)
                # self.app.send_message(ids["helper"], "Hora programada para rage: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                if self.venom:
                    self.app.send_message(self.ids["helper"], "/use_rage", schedule_date = int(datetime.timestamp(temporal_time)))
                if self.alch:
                    temporal_time = temporal_time.replace(minute= 55)
                    self.app.send_message(self.ids["CW"], "/on_508", schedule_date = int(datetime.timestamp(temporal_time)))
                else:
                    if(self.offhand_atack != 'none'):
                        temporal_time = temporal_time.replace(minute= 55)
                        self.app.send_message(self.ids["CW"], self.offhand_atack, schedule_date = int(datetime.timestamp(temporal_time)))
                temporal_time = temporal_time.replace(minute= 59)
                # self.app.send_message(ids["helper"], "Hora programada para orden: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                self.app.send_message(self.ids["CW"], mensaje.text, schedule_date = int(datetime.timestamp(temporal_time)))
                self.app.send_message(self.ids["helper"], "Programada la orden y el rage satisfactoriamente")
            # elif ((me.id == mainIds["yoyi"]) and (re.search("/ga_def [A-z0-9]+", mensaje.text) or re.search("/ga_def_[A-z0-9]+", mensaje.text)  or re.search("/ga_def", mensaje.text))):
            elif ((re.search("/ga_def [A-z0-9]+", mensaje.text) or re.search("/ga_def_[A-z0-9]+", mensaje.text)  or re.search("/ga_def", mensaje.text))):
                temporal_time = datetime.utcnow()
                actual_hour = int(temporal_time.hour)
                # self.app.send_message(ids["helper"], "Hora actual: " + str(actual_hour))
                if(actual_hour >= self.battle_hours["Batalla_3am_-4UTC"] and actual_hour < self.battle_hours["Batalla_11am_-4UTC"]):#próxima batalla es la de las 11am(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=((self.battle_hours["Batalla_11am_-4UTC"]-1) - int(temporal_time.hour)))
                elif(actual_hour >= self.battle_hours["Batalla_11am_-4UTC"] and actual_hour < self.battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 7pm(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=((self.battle_hours["Batalla_7pm_-4UTC"]-1) - int(temporal_time.hour)))
                elif(actual_hour >= self.battle_hours["Batalla_7pm_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=(self.battle_hours["Batalla_7pm_-4UTC"] - int(temporal_time.hour)) + self.battle_hours["Batalla_3am_-4UTC"] - 1)
                elif(actual_hour < self.battle_hours["Batalla_3am_-4UTC"]):#próxima batalla es la de las 3am(-4UTC)
                    temporal_time = temporal_time + timedelta(hours=(self.battle_hours["Batalla_3am_-4UTC"] - 1 - int(temporal_time.hour)))
                temporal_time = temporal_time.replace(minute= 53)
                # self.app.send_message(ids["helper"], "Hora programada para peace: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                if self.venom:
                    self.app.send_message(self.ids["helper"], "/use_peace", schedule_date = int(datetime.timestamp(temporal_time)))
                if self.alch:
                    temporal_time = temporal_time.replace(minute= 55)
                    self.app.send_message(self.ids["CW"], "/on_506", schedule_date = int(datetime.timestamp(temporal_time)))
                else:
                    if(self.offhand_defend != 'none'):
                        temporal_time = temporal_time.replace(minute= 55)
                        self.app.send_message(self.ids["CW"], self.offhand_defend, schedule_date = int(datetime.timestamp(temporal_time)))
                temporal_time = temporal_time.replace(minute= 59)
                # self.app.send_message(ids["helper"], "Hora programada para orden: " + str(temporal_time.hour) + ":" + str(temporal_time.minute))
                self.app.send_message(self.ids["CW"], mensaje.text, schedule_date = int(datetime.timestamp(temporal_time)))  
                self.app.send_message(self.ids["helper"], "Programada la orden y el peace satisfactoriamente")                 
            elif "/check_delay" == mensaje.text.lower():
                self.app.send_message(self.ids["helper"], "El tiempo de espera para cazar es de " +str(self.wait_time)+" segundos")              
            elif "/auto_open_shop" == mensaje.text.lower():
                self.autoOpenShop = not self.autoOpenShop
                self.app.send_message(self.ids["helper"], "Apertura automática de shop luego de la batalla activada.\n" if self.autoOpenShop else "Apertura automática de shop luego de la batalla desactivada.\n")                
            elif "/auto_open_shop_on" == mensaje.text.lower():
                self.autoOpenShop = True
                self.app.send_message(self.ids["helper"], "Apertura automática de shop luego de la batalla activada.\n")                  
            elif "/auto_open_shop_off" == mensaje.text.lower():
                self.autoOpenShop = False
                self.app.send_message(self.ids["helper"], "Apertura automática de shop luego de la batalla desactivada.\n")                                                    
            # elif "/test" == mensaje.text.lower():
            #     self.app.send_message(ids["helper"], str(os.environ["TEST_ENVIRONMENT_VARIABLE"]))
            #     test_time = datetime.now()
            #     test_time = test_time.replace(minute = (test_time.minute + 3))
            #     self.app.send_message(ids["helper"], str(test_time.minute))
            #     self.app.send_message(ids["helper"], "probando mensajes programados", schedule_date = int(datetime.timestamp(test_time)))                                        
            # elif re.search("/write_env [A-z0-9]+", mensaje.text):
            #     os.environ["TEST_ENVIRONMENT_VARIABLE"] = str(re.findall("/write_env [A-z0-9]+", mensaje.text)[0])
            #     self.app.send_message(ids["helper"], str(os.environ["TEST_ENVIRONMENT_VARIABLE"]))
            elif (re.search("/offhand_atack (/on_[A-z0-9]+)", mensaje.text)):
                temp = str(re.findall("/offhand_atack (/on_[A-z0-9]+)", mensaje.text)[0])
                self.offhand_atack = temp
                self.app.send_message(self.ids["helper"], "Offhand para ataque modificado correcatmente, el nuevo valor es: " + self.offhand_atack)                  
            elif (re.search("/offhand_defend (/on_[A-z0-9]+)", mensaje.text)):
                temp = str(re.findall("/offhand_defend (/on_[A-z0-9]+)", mensaje.text)[0])
                self.offhand_defend = temp
                self.app.send_message(self.ids["helper"], "Offhand para defensa modificado correcatmente, el nuevo valor es: " + self.offhand_defend)                 
            elif "/venom_on" == mensaje.text.lower():
                    self.venom = True
                    self.app.send_message(self.ids["helper"], "Programación de rage y peace antes de la batalla activada.")
            elif "/venom_off" == mensaje.text.lower():
                    self.venom = False
                    self.app.send_message(self.ids["helper"], "Programación de rage y peace antes de la batalla desactivada.")
            elif "/venom" == mensaje.text.lower():
                self.venom = not self.venom
                self.app.send_message(self.ids["helper"], "Programación de rage y peace antes de la batalla activada." if self.venom else "Programación rage y peace antes de la batalla desactivada.")                    
            #end added by Yoyi                
            elif (re.search("🏅Level: ([0-9]+)", mensaje.text)) and ('Battle of the seven castles in' in mensaje.text):
                self.level = int(re.findall("🏅Level: ([0-9]+)", mensaje.text)[0])
                hp = int(re.findall("Hp\:.([0-9]+)", mensaje.text)[0])
                if self.vago:
                    if hp < 500:
                        self.caza = False
                        time.sleep(1800+timer_aq)
                        self.app.send_message(self.ids["CW"], "🏅Me")
                    else:
                        self.caza = True    
            elif (self.GC) or (self.general):
                if '🛡Defenders defend the castle wall' in mensaje.text:
                    time.sleep(timer-2)
                    self.app.send_message(self.ids["Canal"], '#def_castillo')
                    time.sleep(timer-2)
                    self.app.send_message(self.ids["CW"], '🛡Defend')
                #elif ('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text):
                    #programar_ataque(mensaje.text, timer)
            elif self.general2:     
                if '🛡Defenders defend the castle wall' in mensaje.text:
                    time.sleep(timer-1)
                    self.app.send_message(self.ids["Canal"], '#def_castillo')
                    time.sleep(timer-1)
                    self.app.send_message(self.ids["CW"], '🛡Defend')
                #elif (('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text)) and (orden_adelantada):
                    #orden_adelant(mensaje.text, timer)
                    self.orden_adelantada = False
                elif '⚔BATTLE IS OVER⚔' in mensaje.text:
                    self.orden_adelantada = True                       
                            
                                   
    """
    nonlocal FUNCTION
    """
    #Borrar aquellos que ids que no son utiles. 
    def chat_on(self):
        dialogs = [i.chat.id for i in self.app.get_dialogs()]
        faltan = False
        for k, v in self.ids.items():
            if  v not in dialogs:
                self.ids[k]=1217879961
                faltan = True
        if -1001386769293 in dialogs: #🔲 Alianza DRK EKE & no #🔰DRKyEKE alianza
            #Allies = Allies_cuadrado
            if faltan:
                try:
                    self.app.send_message("@shitandtrash_bot", "/start")
                    self.app.send_message(1217879961,"mandaré aquí lo que deberia mandar a otros chats pero no pude."+
                                        "puedes moverlo a archivados, pero no lo borres por favor...")
                except:
                    log.warning("No se ha podido unir al bot de Basuramia_bot")
                    
    def stop(self):
        self.app.stop()

    def start(self):
        try:
            self.app.start()
        except AuthKeyUnregistered:
            log.warning("Han desactivado este HASH: "+ self.api_session)
            return
        except AuthKeyDuplicated:
            raise Exception("ERROR!! HASH DUPLICADO" + self.api_session)
 