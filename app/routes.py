from flask import Flask, render_template, request, redirect, url_for, flash
import os
from .models import db, Colaborador, Coletor
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/colaborador')
def colaborador():
    return render_template('colaborador.html')

@app.route('/cadastrar_colaborador')
def cadastrar_colaborador():
    if request.method == 'POST':
        nome = request.form['name']
        logradouro = request.form['street']
        numero = request.form['number']
        
        novo_colaborador = Colaborador(nome=nome, logradouro=logradouro, numero=numero)
        db.session.add(novo_colaborador)
        db.session.commit()
        return render_template('sucesso.html')

@app.route('/coletor')
def coletor():
    return render_template('coletor.html')

@app.route('/cadastrar_coletor', methods=['POST'])
def cadastrar_coletor():
    if request.method == 'POST':
        nome = request.form['name']
        logradouro = request.form['street']
        numero = request.form['number']
        
        novo_coletor = Coletor(nome=nome, logradouro=logradouro, numero=numero)
        db.session.add(novo_coletor)
        db.session.commit()
        return render_template('sucesso.html')

@app.route('/error')
def error_page():
    error_message = request.args.get('error_message', 'Ocorreu um erro desconhecido.')
    return render_template('error.html', error_message=error_message)