import paho.mqtt.client as mqtt
import json
import time


def lambda_handler(event, context):
    # Set up the MQTT client
    client = mqtt.Client()
    client.username_pw_set("some_token")
    client.connect("some_endpoint_address.compute.amazonaws.com", 1883, 60)
    
    internal_temp=event['decoding_output']['TransformedPayloadData']['temperature_internal']
    battery_val=event['decoding_output']['TransformedPayloadData']['battery_value']
    humidity=event['decoding_output']['TransformedPayloadData']['humidity']
    battery_status=event['decoding_output']['TransformedPayloadData']['battery_status']
    
    
    #a84041d55182720b
    #a84041d8118388cc
    #a840419e71837d77
    #a8404164718388cd
    #a840416c118388ce
    #a8404198618319a2
    
    dev_eui=event['decoding_output']['LNSData']['WirelessMetadata']['LoRaWAN']['DevEui']
    
    

    # Publish the data to the specified topic
    topic = "v1/devices/telemetry"
    pld = '{"internal_temperature_' + dev_eui + '": ' + str((internal_temp)) + '}'
    #pld = '{"temperature": "877", "humidity": "55"}' 
    client.publish(topic, pld, qos=1, retain=True)
    print(str(pld))


    time.sleep(0.1)

    # Disconnect from the MQTT broker
    client.disconnect()
