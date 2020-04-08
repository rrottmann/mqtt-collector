import json
import datetime
import subprocess
import paho.mqtt.client as mqtt

# get the docker host ip address (where a mqtt broker should run. alternatively, use ip or hostname
# broker_address = '192.168.1.100'
broker_address = subprocess.check_output("ip route show | awk '/default/ {print $3}'", shell=True).strip()
data_file = '/data/data.json'
topic = 'mytopic/#'
client_name = 'Collector'


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    ts = datetime.datetime.now().isoformat() + 'Z'
    data = {
        'ts': ts,
        'payload': str(message.payload.decode("utf-8"))
    }
    with open(data_file, 'a') as fd:
        json.dump(data, fd)
        fd.write('\n')


client = mqtt.Client(client_name)
client.on_message = on_message
client.connect(broker_address)
client.loop_start()
client.subscribe(topic)

while True:
    pass
