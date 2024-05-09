
import sqlite3

conn = sqlite3.connect('Colegio.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE usuarios (
    usuario VARCHAR(20),
    pass VARCHAR(50)
)""")


cur.execute("""CREATE TABLE profesores (
    DNI_prof VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100)
); """)

cur.execute("""CREATE TABLE alumnos (
    DNI_alumno VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    clase VARCHAR(20),
    edad INT,
    tutor VARCHAR(20),
    contacto BIGINT,
    FOREIGN KEY (tutor) REFERENCES profesores(DNI_prof) ON DELETE SET NULL ON UPDATE CASCADE
);""")



cur.execute("""CREATE TABLE asignaturas (
    id_asignatura INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100),
    curso INT,
    profesor VARCHAR(20),
    FOREIGN KEY (profesor) REFERENCES profesores(DNI_prof) ON DELETE SET NULL ON UPDATE CASCADE
);""")

cur.execute("""CREATE TABLE notas (
    id_calificacion INTEGER PRIMARY KEY AUTOINCREMENT, 
    alumno VARCHAR(20),
    asignatura INT,
    nota INT,
    FOREIGN KEY (alumno) REFERENCES alumnos(DNI_alumno) ON DELETE CASCADE ON UPDATE CASCADE
);
""")


cur.execute(""" INSERT INTO usuarios VALUES('admin', '');""")


list_profes = ["INSERT INTO profesores VALUES('X11111111', 'Ricardo', 'Palomos');",
"INSERT INTO profesores VALUES('Z22222222', 'Pablo', 'Perez');",
"INSERT INTO profesores VALUES('A33333333', 'Concha', 'Espina');",
"INSERT INTO profesores VALUES('X44444444', 'Alvaro', 'Rojas');",
"INSERT INTO profesores VALUES('X55555555', 'Nuria', 'Mendez');",
"INSERT INTO profesores VALUES('Z66666666', 'Gloria', 'Gallego');"]

for profesor in list_profes:
    conn.execute(profesor)


lista_alumnos = ["INSERT INTO alumnos VALUES('11111111A', 'Rodion', 'Bondarets', '1A', 6, 'X11111111', 603396960);",
"INSERT INTO alumnos VALUES('22222222Z', 'Helios', 'Gomes', '1A', 7, 'X11111111', 611111111);",
"INSERT INTO alumnos VALUES('33333333K', 'Pepe', 'Galvez', '1B', 6, 'Z22222222', 622222222);",
"INSERT INTO alumnos VALUES('44444444Z', 'Nicolas', 'Perez', '1B', 6, 'Z22222222', 633333333);",
"INSERT INTO alumnos VALUES('55555555Z', 'Alvaro', 'Garcia', '2A', 8, 'A33333333', 644444444);",
"INSERT INTO alumnos VALUES('66666666K', 'Marco', 'Fusco', '2A', 7, 'A33333333', 655555555);",
"INSERT INTO alumnos VALUES('J77777777', 'Rodrigo', 'Dominguez', '2B', 7, 'X44444444', 666666666);",
"INSERT INTO alumnos VALUES('88888888M', 'Inigo', 'Martin', '2B', 7, 'X44444444', 677777777);",
"INSERT INTO alumnos VALUES('99999999L', 'Alejandro', 'Rabazo', '3A', 9, 'X55555555', 688888888);",
"INSERT INTO alumnos VALUES('10111111X', 'Francisco', 'Gordillo', '3A', 9, 'Z66666666', 699999999);"]
for alumno in lista_alumnos:
    conn.execute(alumno)


lista_asignaturas = ["INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Matematicas', 1, 'X11111111');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Lengua', 1, 'Z22222222');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Ciencias Sociales', 1, 'A33333333');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Conocimiento del Medio', 1, 'X44444444');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Ingles', 1, 'X55555555');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Educacion Fisica', 1, 'Z66666666');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Matematicas', 2, 'X11111111');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Lengua', 2, 'Z22222222');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Ciencias Sociales', 2, 'A33333333');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Conocimiento del Medio', 2, 'X44444444');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Ingles', 2, 'X55555555');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Educacion Fisica', 2, 'Z66666666');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Matematicas', 3, 'X11111111');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Lengua', 3, 'Z22222222');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Ciencias Sociales', 3, 'A33333333');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Conocimiento del Medio', 3, 'X44444444');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Ingles', 3, 'X55555555');",
"INSERT INTO asignaturas (nombre, curso, profesor) VALUES('Educacion Fisica', 3, 'Z66666666');",
]

for asignatura in lista_asignaturas:
    conn.execute(asignatura)

lista_notas = ["INSERT INTO notas (alumno, asignatura, nota) VALUES('11111111A', 1, 8);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('22222222Z', 2, 7);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('33333333K', 3, 7);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('44444444Z', 4, 6);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('55555555Z', 7, 5);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('66666666K', 8, 4);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('J77777777', 9, 6);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('88888888M', 10, 7);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('99999999L', 13, 8);",
"INSERT INTO notas (alumno, asignatura, nota) VALUES('10111111X', 14, 9);",
]

for nota in lista_notas:
    cur.execute(nota)

conn.commit()

conn.close()

