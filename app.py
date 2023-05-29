from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = 'database.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

# Página de inicio con login y clave
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validar el login y la clave
        # Aquí debes agregar la lógica para validar el usuario y contraseña ingresados
        # Puedes utilizar la base de datos para esto

        # Si la validación es exitosa, redirigir a la página de inicio
        return redirect(url_for('inicio'))
    return render_template('login.html')

# Página de inicio después del login exitoso
@app.route('/inicio')
def inicio():
    # Aquí debes obtener la información del usuario y programa académico desde la base de datos
    # Puedes utilizar una consulta SQL para obtener esta información

    # Ejemplo:
    nombre = "John Doe"
    programa_academico = "Ingeniería de Software"
    return render_template('inicio.html', nombre=nombre, programa_academico=programa_academico)

# Página de registro de estudiantes
@app.route('/registro_estudiantes')
def registro_estudiantes():
    # Aquí debes obtener y mostrar el formulario de registro de estudiantes
    return render_template('registro_estudiantes.html')

# Página de listado de estudiantes
@app.route('/listado_estudiantes')
def listado_estudiantes():
    # Aquí debes obtener la lista de estudiantes desde la base de datos
    # Puedes utilizar una consulta SQL para obtener esta información

    # Ejemplo:
    estudiantes = [
        {'id': 1, 'nombres': 'John', 'apellidos': 'Doe'},
        {'id': 2, 'nombres': 'Jane', 'apellidos': 'Smith'}
    ]
    return render_template('listado_estudiantes.html', estudiantes=estudiantes)

# Página para crear o editar un estudiante
@app.route('/editar_estudiante', methods=['GET', 'POST'])
def editar_estudiante():
    if request.method == 'POST':
        # Aquí debes obtener los datos del formulario de edición
        # y guardarlos en la base de datos
        return redirect(url_for('listado_estudiantes'))
    return render_template('editar_estudiante.html')

# Página para eliminar un estudiante
@app.route('/eliminar_estudiante/<int:id>', methods=['POST'])
def eliminar_estudiante(id):
    # Aquí debes eliminar el estudiante con el ID proporcionado de la base de datos
    return redirect(url_for('listado_estudiantes'))

# Página de consulta de carreras
@app.route('/consulta_carreras')
def consulta_carreras():
    # Aquí debes obtener la lista de carreras desde la base de datos
    # Puedes utilizar una consulta SQL para obtener esta información

    # Ejemplo:
    carreras = [
        {'id': 1, 'nombre': 'Ingeniería de Software'},
        {'id': 2, 'nombre': 'Administración de Empresas'}
    ]
    return render_template('consulta_carreras.html', carreras=carreras)

# Página para crear o editar una carrera
@app.route('/editar_carrera', methods=['GET', 'POST'])
def editar_carrera():
    if request.method == 'POST':
        # Aquí debes obtener los datos del formulario de edición
        # y guardarlos en la base de datos
        return redirect(url_for('consulta_carreras'))
    return render_template('editar_carrera.html')

# Página para eliminar una carrera
@app.route('/eliminar_carrera/<int:id>', methods=['POST'])
def eliminar_carrera(id):
    # Aquí debes eliminar la carrera con el ID proporcionado de la base de datos
    return redirect(url_for('consulta_carreras'))

if __name__ == '__main__':
    app.run(debug=True)
