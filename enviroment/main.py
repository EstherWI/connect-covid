from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def raiz():
    return 'Ola mundo'


@app.route('/doctor')
def doc():
    return 'Ola médico'


@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        cpf = request.form.get('cpf')
    return render_template('patient.html')


app.run(debug=True)
