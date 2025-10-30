from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    usuarios = ['Da Vinci', 'Ghami', 'Elias', 'Facu', 'Sistemas']
    return render_template('usuario.html', usuarios=usuarios)

@app.route('/inicio')
def index():
    
    return render_template('index.html')


#manejar errores

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html'), 404


# este siempre va al final
if __name__ == '__main__':
    app.run(debug=True)
