#MQTT Paho Client


#import client class 
import paho.mqtt.client as mqtt
import time

#creating a callback funtion to receive any incoming payloads
def send_payload(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
    #loop_flag=0

broker_address = "192.168.0.27"
#broker_address="iot.eclipse.org" 

#create a client instace
#Client(client_id=””, clean_session=True, userdata=None, 
#protocol=MQTTv311, transport=”tcp”)
#creating an instance
client = mqtt.Client("client1")

#attach function to a callback
client.on_message= send_payload 

#connect method
#connect(host, port=1883, keepalive=60, bind_address="")
client.connect(broker_address)

#loop to check incoming callback messages
client.loop_start()


#publish a message
#publish(topic, payload=None, qos=0, retain=False)
#client.publish("messages/001","paola")
print ("subscribing the topic")
client.subscribe("senseor/temp")

#loop_flag= 1
#counter = 0

#while loop_flag == 1
#print ("subscribing the topic", counter)
time.sleep(3000)
#counter+=1
#client.disconnect()
client.loop_stop()
   


