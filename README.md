# mqtt-wifi-collector

A simple linux container to run a python MQTT collector script.
It mounts a directory `/data` as bindmount and writes all received messages
as JSON with current timestamp.

## Dependencies

* Dockerhost
  * ... running a MQTT broker 
     * ... with default port 1883
     * ... with message topic 'mytopic/#'

## Usage

Just execute `run.sh` and send messages to your topic.