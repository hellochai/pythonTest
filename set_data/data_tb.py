#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 17:29
# @Author  : fchai
# @Desc    :
# @File    : data_tb.py
# @Software: PyCharm

import json
import threading
import time
import datetime

import requests
from paho.mqtt import client as mqtt_client
import random

client_id = 'python-new-000000000000000000000'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT-heart Broker!")
        else:
            print("Failed to connect heart_mQTT, return code %d---", rc)

    try:
        print('----------------', client_id)
        client = mqtt_client.Client(client_id, clean_session=False)
        client.username_pw_set(username='0mgKSF99IXrZQ1Ascxw')
        client.on_connect = on_connect
        client.on_publish = on_publish
        client.on_disconnect = on_disconnect
        client.connect('thingsboard.dahanglink.com', 1883)
        return client
    except Exception as e:
        print("heart-connect-mqtt Exception: %s" % str(e))


def on_disconnect(client, userdata, rc):
    # 重连中
    while True:
        time.sleep(3)
        if client.is_connected():
            break
        else:
            client.reconnect()


def on_publish(client, userdata, mid):
    print("%s Publish time_proofread success %s" % (client, mid))


def publish(client):
    while True:
        ts = round(time.time())
        data = {
            'tmCycleTime': random.randint(1,20),
            'tmInjTime': random.randint(10,20),
            'tmTurnTime': random.randint(15,30),
            'tmChargeTime': random.randint(20,30),
            'tmInjStarPosi': random.randint(20,50),
            'tmInjEndPosi': random.randint(1,50),
            'tmTurnPosi': random.randint(1,30),
            'tmTurnPress':  random.randint(20,60),
            'tmInjMaxPress': random.randint(10,65)
        }
        print("----------------", data)
        # client.publish('v1/gateway/telemetry', payload=json.dumps(data))
        url = 'http://thingsboard.dahanglink.com:9090/api/v1/0mgKSF99IXrZQ1Ascxw/telemetry'
        result = requests.post(url, data=json.dumps(data))
        print("=======", result.status_code)
        time.sleep(3)

client = connect_mqtt()
ts = threading.Thread(target=publish, args=(client,))
ts.start()
