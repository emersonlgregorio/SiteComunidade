from flask import render_template, url_for, redirect, request, flash
from crestani import app, database, bcrypt
from crestani.forms import FormCriarConta, FormLogin
from crestani.models import Usuario

lista_usuarios = ['Emerson', 'Francieli', 'João', 'Fulano', 'Morfeu']
vagas = ['Auxiliar de Produção', "Mecânico de Maquinas Pesadas", 'Especialista de TI', 'Auxiliar Contábil']

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
    return render_template('trabalhe_conosco.html', vagas=vagas)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        #criar o Usuario
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          email=form_criarconta.email.data,
                          senha=senha_cript)
        #adicionar a sessão
        database.session.add(usuario)
        #commit a sessao
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)