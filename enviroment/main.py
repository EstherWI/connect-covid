from models.tables import DataPatient
from flask import Flask, json, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

class Paciente:
    def __init__(self, cpf, temp, freq, pressao, resp):
        self.cpf = cpf
        self.temp = temp
        self.freq = freq
        self.pressao = pressao
        self.resp = resp

p = Paciente(1,1,1,1,1)
lista = [p]

dbPatients = DataPatient()

@app.route('/')
def raiz():
    return "Hello world"

@app.route('/doctor')
def doc():
    return render_template('doctor.html', titulo='Pacientes', patients=lista)

@app.route('/patients', methods=['GET'])
def getAll():
    return jsonify(dbPatients.getAllPatients()), 200

@app.route('/patient/<int:cpf>', methods=['PUT'])
def update(cpf: int):
    dataUpdate = request.json
    if dbPatients.updatePatient(cpf, dataUpdate):
        return jsonify({'status': 'Sucess'}), 200
    else:
        return jsonify({'status': 'Pacient not found'}), 404

@app.route('/patient/<int:cpf>', methods=['GET'])
def get(cpf: int):
    return jsonify(dbPatients.getPatient(cpf)), 200

@app.route('/patient', methods=['POST'])
def criar():
    patient = request.json
    dbPatients.addPatient(patient)
    return jsonify({'status': 'Sucess'}), 200

app.run(debug=True)
