import servico
tables = {
    'patients': [

    ]
}


class DataPatient():

    def getAllPatients(self, N: int)->dict:
        return servico.ordenada

    def addPatient(self, patient: dict):
        index = - 1
        cont = 0
        for p in tables['patients']:
            if(p['id']==patient['id']):
                index = cont
                break
            cont = cont+1
        if index == -1:
            tables['patients'].append(patient)

    def addPatients(self, patients: dict):
        tables['patients'] = patients
    
    def sendAlert(self, id: int, data: dict) -> bool:
        index = -1
        cont = 0
        table = tables['patients']
        for p in table:
            if(p['id']==id):
                index = cont
            cont = cont+1
        if index!=-1:
            table[index]['status'] = data['status']
            return True
        else:
            return False

    def updatePatient(self, id: int, data: dict) -> bool:
        index = -1
        cont = 0
        table = tables['patients']
        for p in table:
            if(p['id']==id):
                index = cont
            cont = cont+1
        if index!=-1:
            table[index]['temp'] = data['temp']
            table[index]['freq'] = data['freq']
            table[index]['pressao1'] = data['pressao1']
            table[index]['pressao2'] = data['pressao2']
            table[index]['saturacao'] = data['saturacao']
            table[index]['status'] = data['status']
            return True
        else:
            return False

    def getPatient(self, id: int)->dict:
        table = tables['patients']
        for p in table:
            if(p['id']==id):
                return p
        return None
    
    def getPatientByName(self, nome: str)->dict:
        table = tables['patients']
        for p in table:
            if(p['nome']==nome):
                return p
        return None





