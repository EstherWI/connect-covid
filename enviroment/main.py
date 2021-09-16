from models.tables import DataPatient
from flask import Flask, request, jsonify

app = Flask(__name__)
dbPatients = DataPatient()

@app.route('/', methods=['GET'])
def raiz():
    return jsonify({'status': 'Sucess'}), 200

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

@app.route('/patient/alert/<int:cpf>', methods=['PUT'])
def alert(cpf: int):
    dataUpdate = request.json
    if dbPatients.sendAlert(cpf, dataUpdate):
        return jsonify({'status': 'Sucess'}), 200
    else:
        return jsonify({'status': 'Pacient not found'}), 404

@app.route('/patient/<int:cpf>', methods=['GET'])
def get(cpf: int):
    return jsonify(dbPatients.getPatient(cpf)), 200

@app.route('/patientByName/<string:nome>', methods=['GET'])
def getByName(nome: str):
    return jsonify(dbPatients.getPatientByName(nome)), 200

@app.route('/patient', methods=['POST'])
def criar():
    patient = request.json
    dbPatients.addPatient(patient)
    return jsonify({'status': 'Sucess'}), 200

app.run(debug=True)
