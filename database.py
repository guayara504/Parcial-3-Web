import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Creación de la tabla secciones
c.execute('''CREATE TABLE secciones (
                id INT PRIMARY KEY,
                nombre CHAR
            )''')

# Creación de la tabla estudiantes
c.execute('''CREATE TABLE estudiantes (
                id INT PRIMARY KEY,
                num_lista INT,
                nombres VARCHAR,
                apellidos VARCHAR,
                genero CHAR,
                id_grado INT,
                id_seccion INT,
                FOREIGN KEY (id_grado) REFERENCES programa(id),
                FOREIGN KEY (id_seccion) REFERENCES secciones(id)
            )''')

# Creación de la tabla notas
c.execute('''CREATE TABLE notas (
                id INT PRIMARY KEY,
                nota DECIMAL,
                observaciones VARCHAR,
                id_alumno INT,
                id_materia INT,
                FOREIGN KEY (id_alumno) REFERENCES estudiantes(id),
                FOREIGN KEY (id_materia) REFERENCES materias(id)
            )''')

# Creación de la tabla programa
c.execute('''CREATE TABLE programa (
                id INT PRIMARY KEY,
                nombre VARCHAR,
                ciclo VARCHAR
            )''')

# Creación de la tabla materias
c.execute('''CREATE TABLE materias (
                id INT PRIMARY KEY,
                nombre VARCHAR,
                num_evaluaciones INT,
                id_grado INT,
                FOREIGN KEY (id_grado) REFERENCES programa(id)
            )''')

# Creación de la tabla users
c.execute('''CREATE TABLE users (
                id INT PRIMARY KEY,
                username VARCHAR,
                password VARCHAR,
                nombre VARCHAR,
                rol VARCHAR
            )''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
