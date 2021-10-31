from models.tables import DataPatient
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
dbPatients = DataPatient()

@app.route('/', methods=['GET'])
def raiz():
    return jsonify({'status': 'Sucess'}), 200

@app.route('/patients', methods=['GET'])
def getAll():
    return jsonify(dbPatients.getAllPatients()), 200

@app.route('/patients', methods=['POST'])
def addPatients():
    patients = request.json
    dbPatients.addPatients(patients)
    return jsonify({'status': 'Sucess'}), 200

@app.route('/patient/<int:id>', methods=['PUT'])
def update(id: int):
    dataUpdate = request.json
    if dbPatients.updatePatient(id, dataUpdate):
        return jsonify({'status': 'Sucess'}), 200
    else:
        return jsonify({'status': 'Pacient not found'}), 404

@app.route('/patient/alert/<int:id>', methods=['PUT'])
def alert(id: int):
    dataUpdate = request.json
    if dbPatients.sendAlert(id, dataUpdate):
        return jsonify({'status': 'Sucess'}), 200
    else:
        return jsonify({'status': 'Pacient not found'}), 404

@app.route('/patient/<int:id>', methods=['GET'])
def get(id: int):
    return jsonify(dbPatients.getPatient(id)), 200

@app.route('/patientByName/<string:nome>', methods=['GET'])
def getByName(nome: str):
    return jsonify(dbPatients.getPatientByName(nome)), 200

@app.route('/patient', methods=['POST'])
def criar():
    patient = request.json
    dbPatients.addPatient(patient)
    return jsonify({'status': 'Sucess'}), 200

port = int(os.environ.get("PORT", 5000))
app.run(debug=True ,host='0.0.0.0', port=port)
