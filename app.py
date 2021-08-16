from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuarios = ['Emerson', 'Francieli', 'João', 'Fulano', 'Morfeu']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/trabalhe-conosco')
def trabalhe_conosco():
    return render_template('trabalhe_conosco.html')


if __name__ == '__main__':
    app.run(debug=True)