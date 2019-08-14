#!/usr/bin/env python3
from hermes_python.hermes import Hermes 
import requests

from datetime import datetime
from pytz import timezone

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def extraer_hora():
    now = datetime.now(timezone('Europe/Madrid'))
    print("Hora actual {0}".format(now))
    if now.hour == 1:
        sentence = 'Es la una ' + " " + "{0}".format(str(now.minute))
    else:
        sentence = 'Son las ' + "{0}".format(str(now.hour)) + " " + "{0}".format(str(now.minute))

    sentence = sentence.strip()
    return sentence

def intent_received(hermes, intent_message):
    print("Intent recibido {0}".format(intent_message.intent.intent_name))
    if intent_message.intent.intent_name == 'gemalb:NowTime':
        mensaje = extraer_hora()
    else:
        mensaje = 'Ahora no lo se'
    hermes.publish_end_session(intent_message.session_id, mensaje)
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
