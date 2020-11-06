from flask import Flask, render_template, request, redirect, session, flash, url_for ,send_from_directory
from dao import JogoDao , UsuarioDao
from models import Jogo , Usuario
from flask_mysqldb import MySQL
import os
import time

app = Flask(__name__)
app.secret_key = 'alura'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Lary2703"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306
app.config['upload_path'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

db = MySQL(app)

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    jogo =  jogo_dao.salvar(jogo)
    arquivo = request.files['arquivo']
    upload = app.config['upload_path']
    timestamp = time.time()
    arquivo.save(f'{upload}/{jogo.id}.jpg ')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('edit')))
    jogo = jogo_dao.busca_por_id(id)
    return render_template('edit.html', titulo='update Games',jogo = jogo, capa_jogo =f'{jogo.id}.jpg')

@app.route('/update', methods=['POST',])
def update():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console , id=request.form['id'])
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    jogo_dao.deletar(id)
    flash('O jogo Foi Removido Com Sucesso')
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads' , nome_arquivo)

app.run(debug=True)
