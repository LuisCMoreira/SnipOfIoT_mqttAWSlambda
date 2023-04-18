import paho.mqtt.client as mqtt
import json
import time


def lambda_handler(event, context):
    # Set up the MQTT client
    client = mqtt.Client()
    client.username_pw_set("some_token")
    client.connect("some_endpoint_address.compute.amazonaws.com", 1883, 60)
    
    internal_temp=event['decoding_output']['TransformedPayloadData']['temperature_internal']
    
    
    dev_ID=event['decoding_output']['LNSData']['WirelessMetadata']['DevID']
    
    

    # Publish the data to the specified topic
    topic = "v1/devices/telemetry"
    pld = '{"internal_temperature_' + dev_ID + '": ' + str((internal_temp)) + '}'

    client.publish(topic, pld, qos=1, retain=True)
    print(str(pld))


    time.sleep(0.1)

    # Disconnect from the MQTT broker
    client.disconnect()
