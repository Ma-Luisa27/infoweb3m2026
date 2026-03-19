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
    return render_template ('contato.html')

if __name__ == '__main__':
    app.run()
