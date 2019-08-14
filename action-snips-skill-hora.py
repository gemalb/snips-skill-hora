#!/usr/bin/env python3
from hermes_python.hermes import Hermes 
import requests

from datetime import datetime

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def extraer_hora():
    now = datetime.now()
    if now.hour == 1:
        sentence = 'Es la una ' + " " + "{0}".format(str(now.minute))
    else:
        sentence = 'Son las ' + " " + "{0}".format(str(now.minute))

    sentence = sentence.strip()
    return sentence

def intent_received(hermes, intent_message):
    
    
    if intent_message.intent.intent_name == 'gemalb:NowTime':
        mensaje = extraer_hora()
        hermes.publish_end_session(intent_message.session_id, mensaje)               
    else:
        mensaje = 'Te lo digo mañana'
        hermes.publish_end_session(intent_message.session_id, mensaje) 
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
