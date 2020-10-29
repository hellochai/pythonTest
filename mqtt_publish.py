#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 11:49
# @Author  : fchai
# @Desc    :
# @File    : mqtt_client.py
# @Software: PyCharm
import json
import random
import time
from datetime import datetime
from queue import Queue

from paho.mqtt import client as mqtt_client

# generate client ID with pub prefix randomly
import uuid

client_id = f'python-mqtt-{uuid.uuid1()}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:

            print("Connected to MQTT-sub Broker!")
        else:
            print("Failed to connect sub_MQTT, return code %d\n", rc)

    try:
        client = mqtt_client.Client(client_id)
        client.username_pw_set(username='zmm', password='dhlktech')
        client.on_connect = on_connect
        client.connect('127.0.0.1', 1883)
        return client
    except Exception as e:
        print("sub-content-mqtt Exception: %s" % str(e))
        write_sub_err(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + "sub-sub-mqtt Exception: %s" % str(e))


def publish(client):
    data = {'energy_ts': '', 'energy_id': 3, 't_act_energy': 0, 't_react_energy': 0, 't_act_pwr': 0, 't_react_pwr': 0,
            't_act_energy_A': 0, 't_react_energy_A': 0, 'E_V_A': 0, 'E_I_A': 0, 'act_pwr_A': 0, 'react_pwr_A': 0,
            'pwr_rate_A': 0, 't_act_energy_B': 0, 't_react_energy_B': 0, 'E_V_B': 0, 'E_I_B': 0, 'act_pwr_B': 0,
            'react_pwr_B': 0, 'pwr_rate_B': 0, 't_act_energy_C': 0, 't_react_energy_C': 0, 'E_V_C': 0, 'E_I_C': 0,
            'act_pwr_C': 0, 'react_pwr_C': 0, 'pwr_rate_C': 0, 'freq': 0}
    while True:
        date_str = datetime.now().strftime('%Y%m%d%H%M%S')
        ts = int(date_str[2:], 16)
        v_A = random.uniform(220.0, 220.7)
        v_B = random.uniform(220.0, 220.8)
        v_C = random.uniform(220.0, 220.8)
        data['energy_ts'] = ts
        data['E_V_A'] = round(v_A, 3)
        data['E_V_B'] = round(v_B, 3)
        data['E_V_C'] = round(v_C, )

        energy_id = random.choice([2, 3])
        data['energy_id'] = energy_id

        data_json = {
            "data": data
        }
        client.publish('dhlk_Energy', payload=json.dumps(data_json))

        time.sleep(5)


def write_sub_err(data):
    with open("sub_err.logs", 'w') as f:
        f.write(data)


def exe_sub():
    client = connect_mqtt()
    publish(client)
    client.loop_forever()


if __name__ == '__main__':
    exe_sub()
