
from app import app
from flask import render_template, request
from flask import flash, redirect
from flask_mail import Mail, Message
from flask_wtf import FlaskForm


@app.route('/')
@app.route('/index/<nome>/<proprietario>/<youtube>')
@app.route('/index')
def index(nome="Marcos",
          titulo='Você está no site Blind Vision criado para você!',
          texto="Este site foi criado com a linguagem de programação Python com a Biblioteca Flask, mas o importante, é que estamos aqui para lhe auxiliar no que necessitar!"):
    return render_template('index.html', nome=nome, titulo=titulo, texto=texto)






@app.route('/')
@app.route('/contato')
def contato():
    ola = "bem vindos a página de contato!"
    return render_template('contato.html', ola=ola)








@app.route('/')
@app.route('/index')
def diferenciais(cursos='Neste espaço temos disponível para você nossos cursos',
                 java="Cursos de java onde você deficiente visual terá a oportunidade de ter um curso acessível.",
                 python="Curso de Python do básico ao avançado contemplando um projeto real com a biblioteca Flask e uso de html em rotas."):
    return render_template('diferenciais.html', cursos=cursos, java=java, python=python)


@app.route('/<string:nome>')
def error(nome):
    variavel = f' página ({nome}) não encontrada.'
    return render_template('error.html', variavel=variavel)
