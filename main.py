from heapq import heapify
from models.tables import DataPatient
from flask import Flask, request, jsonify
import json, os, random, paho.mqtt.client


host = 'broker.hivemq.com'
port_mqtt = 1883
port = int(os.environ.get("PORT", 5000))
topic = "paciente_broker"
fog1 = []
fog2 = []
ordenada = []
paciente = {
        "nome": "Gustavo Alves",
        "id": "0",
        "saturacao":random.randint(96, 100),
        "temp":round(random.uniform(35.5, 37.4), 1),
        "freq":random.randint(60,99),
        "pressao1":random.randint(110,130),
        "pressao2":random.randint(70,84),
        "status":0,
    }
cont = 0

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

app = Flask(__name__)
dbPatients = DataPatient()

@app.route('/', methods=['GET'])
def raiz():
    return jsonify({'status': 'Sucess'}), 200

@app.route('/get/patients/<int:N>', methods=['GET'])
def getAll(N: int):
    dbPatients.updateN(N)
    return jsonify(getAllPatients(N)), 200

@app.route('/patient/<int:id>', methods=['GET'])
def get(id: int):
    dbPatients.updateId(id)
    return jsonify(getPatient()), 200

@app.route('/getId', methods=['GET'])
def getId():
    dbPatients.updateId(id)
    return jsonify(getId()), 200

@app.route('/getN', methods=['GET'])
def getN():
    return jsonify(getN()), 200


def connect_mqtt() -> paho.mqtt.client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = paho.mqtt.client.Client(client_id)
    client.on_connect = on_connect
    client.connect(host, port_mqtt)
    return client


def subscribe(client: paho.mqtt.client):
    def on_message(client, userdata, msg):
        global fog1
        global fog2
        global ordenada
        data = eval(json.loads(json.dumps(str(msg.payload.decode("utf-8")))))
        if(data[0]['fog']=="FOG1"):
            fog1 = data
        else:
            fog2 = data
        data = fog1 + fog2
        ordenada = sorted(data, key=lambda k: k['status'], reverse=True)
    client.subscribe([(topic, 1), ("MonitorarPaciente", 1)])
    client.on_message = on_message

def getAllPatients(N: int)->list:
    return ordenada[0:N]

def getPatient()->dict:
    return paciente

if __name__ == '__main__':
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    app.run(debug=True ,host='0.0.0.0', port=port)


