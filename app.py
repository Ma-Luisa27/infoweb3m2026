from flask import Flask, render_template, request,redirect, url_for
from datetime import datetime

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

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    datanasc = request.form['datanasc']
    data_objeto = datetime.strptime(datanasc, "%Y-%m-%d")
    data_formatada = data_objeto.strftime("%d-%m-%Y")
    estado = request.form['estado']
    escola = request.form.getlist('escola')
    # info = request.args
    return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, email=email, data_formatada=data_formatada, estado=estado, escola=escola)

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/recebecompras', methods=['POST'])
def recebecompras():
    itens = request.form.getlist('item')
    return render_template('lista.html', itens=itens)

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return 'Você é MAIOR de idade'
    else:
        return 'Você é MENOR de idade'

@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/verificalogin', methods=['POST'])
# def verificalogin():
#     usuario = request.form.get('login')
#     senha = request.form.get('senha')
#     if usuario == 'admin' and senha == '12345':
#         return render_template('arearestrita.html')
#     else:
#         return render_template('acessonegado.html')

@app.route('/verificalogin', methods=['POST'])
def verificalogin():
    usuario = request.form.get('login')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha == '12345':
        return redirect(url_for('arearestrita'))
    else:
        return redirect(url_for('acessonegado'))

@app.route('/arearestrita')
def arearestrita():
    return render_template('arearestrita.html')

@app.route('/acessonegado')
def acessonegado():
    return render_template('acessonegado.html')

@app.route('/exemplolaco')
def exemplolaco():
    return render_template('exemplolaco.html')

@app.route('/produtos')
def produtos():
    itens = [
        {'nome':'Teclado','preco':'200', 'categoria':'Computador', 'imagem':'https://images3.kabum.com.br/produtos/fotos/585203/teclado-sem-fio-mecanico-gamer-logitech-g-pro-x-60-lightspeed-rgb-bluetooth-compativel-com-windows-rosa-magenta-920-011940_1754997398_gg.jpg'},
        {'nome':'Smartphone','preco':'1500', 'categoria':'Celular', 'imagem':'https://m.media-amazon.com/images/I/71Z-rd+PWgL._AC_SX679_.jpg'},
        {'nome':'Pen-drive 1','preco':'50', 'categoria':'Computador', 'imagem':'https://ecoms1.com/29609/@v3/1671711747990-pendrive32gbsandiskz50ccruzerbladeusb2.0rosa-copia.jpg'}
    ]
    qtd = len(itens)
    return render_template('produtos.html', itens=itens, qtd=qtd)

if __name__ == '__main__':
    app.run()
