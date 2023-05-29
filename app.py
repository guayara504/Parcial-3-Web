from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
   
        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/inicio')
def inicio():

    nombre = "John Doe"
    programa_academico = "Ingeniería de Software"
    return render_template('inicio.html', nombre=nombre, programa_academico=programa_academico)


@app.route('/registro_estudiantes')
def registro_estudiantes():
    return render_template('registro_estudiantes.html')

@app.route('/listado_estudiantes')
def listado_estudiantes():

    estudiantes = [
        {'id': 1, 'nombres': 'John', 'apellidos': 'Doe'},
        {'id': 2, 'nombres': 'Jane', 'apellidos': 'Smith'}
    ]
    return render_template('listado_estudiantes.html', estudiantes=estudiantes)


@app.route('/editar_estudiante', methods=['GET', 'POST'])
def editar_estudiante():
    if request.method == 'POST':
        return redirect(url_for('listado_estudiantes'))
    return render_template('editar_estudiante.html')

@app.route('/eliminar_estudiante/<int:id>', methods=['POST'])
def eliminar_estudiante(id):

    return redirect(url_for('listado_estudiantes'))

@app.route('/consulta_carreras')
def consulta_carreras():

    carreras = [
        {'id': 1, 'nombre': 'Ingeniería de Software'},
        {'id': 2, 'nombre': 'Administración de Empresas'}
    ]
    return render_template('consulta_carreras.html', carreras=carreras)

@app.route('/editar_carrera', methods=['GET', 'POST'])
def editar_carrera():
    if request.method == 'POST':
        return redirect(url_for('consulta_carreras'))
    return render_template('editar_carrera.html')

@app.route('/eliminar_carrera/<int:id>', methods=['POST'])
def eliminar_carrera(id):
    return redirect(url_for('consulta_carreras'))

if __name__ == '__main__':
    app.run(debug=True)
