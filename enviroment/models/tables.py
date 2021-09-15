tables = {
    'patients': [

    ]
}


class DataPatient():

    def getAllPatients(self)->dict:
        return tables['patients']

    def addPatient(self, patient: dict):
        tables['patients'].append(patient)

    def updatePatient(self, cpf: int, data: dict) -> bool:
        index = -1
        cont = 0
        table = tables['patients']
        for p in table:
            if(p['cpf']==cpf):
                index = cont
            cont = cont+1
        if index!=-1:
            table[index]['temp'] = data['temp']
            table[index]['freq'] = data['freq']
            table[index]['pressao1'] = data['pressao1']
            table[index]['pressao2'] = data['pressao2']
            table[index]['resp'] = data['resp']
            return True
        else:
            return False

    def getPatient(self, cpf: int)->dict:
        table = tables['patients']
        for p in table:
            if(p['cpf']==cpf):
                return p
        return None





