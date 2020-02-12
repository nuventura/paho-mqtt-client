# paho-mqtt-client

 Python example script that subscribes to a topic and publishes messages on that topic.

------------------------------------------------------

## Requirements to run the script

- **Intalling python locally**

Check if you have it already installed

<code>pip --version</code>


- **Install Paho MQTT client using the followin pip command**

<code> pip install paho-mqtt </code>

or depending on which version you using specify which version you installing the client

<code> pip2.7 install paho-mqtt </code>
<code> pip3.4 install paho-mqtt </code>
<code> pip3.5 install paho-mqtt </code>

> Please check if you have multiple versions of python installed, and make sure to install Paho MQTT client accordingly with the correct version you will run your code.

------------------------------------------------------

### Methods

The paho mqtt client class has several methods.The main ones are:

- connect() and disconnect()
- subscribe() and unsubscribe()
- publish()

### Connecting To a Broker or Server

A connection needs to be stablished with a broker in order to subscribe and publish messages.
To do this use the connect method of the Python mqtt client.

The method can be called with 4 parameters. 

<code> connect(host, port=1883, keepalive=60, bind_address="") </code>

### Publishing Messages

Once you have a connection you can start to publish messages.
To do this we use the publish method.

The publish method accepts 4 parameters.

<code> publish(topic, payload=None, qos=0, retain=False) </code>

### Subscribing topics

To subscribe to a topic you use the subscribe method of the Paho MQTT Class object.

The subscribe method accepts 2 parameters – A topic or topics and a QOS (quality of Service)

<code> subscribe(topic, qos=0) </code>