import paho.mqtt.client as paho
import json
import time
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.username_pw_set("comunidade", "comunidade")
client.connect("m12.cloudmqtt.com", 16903, 60)
client.loop_start()

def sendRanny(sender, text, alert = False, timeslice = False):
    j = {"sender": sender,
            "msg": text
           }
    retorno = json.dumps(j)
    if alert == True:
        print("Json Enviado:{}".format(retorno))
    (rc, mid) = client.publish("comunidade", retorno, qos=1)
    time.sleep(1)
    
'''
sendRanny vai enviar a msg. Text é o texto da sua aplicação e o sender voce consegue a partir da funcao "meuid"
'''