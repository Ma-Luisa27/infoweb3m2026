from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ola')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faleconosco')
@app.route('/email')
@app.route('/contato')
def contato():
    dados = {'nome': 'Italo', 'email': 'italo@email.com'}
    return render_template ('contato.html', dados=dados)

@app.route('/usuario', defaults={'nome': 'Desconhecido', 'sobrenome':'Desconhecido'})
@app.route('/usuario/<nome>/<sobrenome>')
def usuario (nome, sobrenome):
    info = {'nome':nome, 'sobrenome':sobrenome}
    return render_template('usuario.html', info=info)

@app.route('/semestre/<int:x>')
def semestre (x):
    atual = x
    anterior = x-1
    return render_template('semestre.html', atual=atual, anterior=anterior)

@app.route('/perfil/<usuario>')
def perfil (usuario):
    return render_template('perfil.html', usuario=usuario)

if __name__ == '__main__':
    app.run()
