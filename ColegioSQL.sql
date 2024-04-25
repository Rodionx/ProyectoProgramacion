/*--------------------------------Creacion de base de datos-----------------------------------------*/

DROP DATABASE IF EXISTS colegio;
CREATE DATABASE colegio CHARACTER SET utf8;
USE colegio;

/*--------------------------------Creacion de tablas------------------------------------------------*/

CREATE TABLE profesores(
    DNI_prof VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100)
);

CREATE TABLE alumnos(
    DNI_alumno VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    clase VARCHAR(20),
    edad INT(2),
    tutor VARCHAR(20),
    contacto INT(20),
    FOREIGN KEY (tutor) REFERENCES profesores(DNI_prof) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE asignaturas(
    id_asignatura INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    curso INT(2),
    profesor VARCHAR(20),
    FOREIGN KEY (profesor) REFERENCES profesores(DNI_prof) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE notas(
    id_calificacion INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    alumno VARCHAR(20),
    asignatura INT UNSIGNED,
    nota INT(2),
    FOREIGN KEY (alumno) REFERENCES alumnos(DNI_alumno) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (asignatura) REFERENCES asignaturas(id_asignatura) ON DELETE NO ACTION ON UPDATE CASCADE
);

/*---------------------------------Insercion de datos-----------------------------------------------*/

INSERT INTO profesores VALUES('X11111111', 'Ricardo', 'Palomos');
INSERT INTO profesores VALUES('Z22222222', 'Pablo', 'Perez');
INSERT INTO profesores VALUES('A33333333', 'Concha', 'Espina');
INSERT INTO profesores VALUES('X44444444', 'Alvaro', 'Rojas');
INSERT INTO profesores VALUES('X55555555', 'Nuria', 'Mendez');
INSERT INTO profesores VALUES('Z66666666', 'Gloria', 'Gallego');

INSERT INTO alumnos VALUES('11111111A', 'Rodion', 'Bondarets', '1A', 6, 'X11111111', 603396960);
INSERT INTO alumnos VALUES('22222222Z', 'Helios', 'Gomes', '1A', 7, 'X11111111', 611111111);
INSERT INTO alumnos VALUES('33333333K', 'Pepe', 'Galvez', '1B', 6, 'Z22222222', 622222222);
INSERT INTO alumnos VALUES('44444444Z', 'Nicolas', 'Perez', '1B', 6, 'Z22222222', 633333333);
INSERT INTO alumnos VALUES('55555555Z', 'Alvaro', 'Garcia', '2A', 8, 'A33333333', 644444444);
INSERT INTO alumnos VALUES('66666666K', 'Marco', 'Fusco', '2A', 7, 'A33333333', 655555555);
INSERT INTO alumnos VALUES('J77777777', 'Rodrigo', 'Dominguez', '2B', 7, 'X44444444', 666666666);
INSERT INTO alumnos VALUES('88888888M', 'Inigo', 'Martin', '2B', 7, 'X44444444', 677777777);
INSERT INTO alumnos VALUES('99999999L', 'Alejandro', 'Rabazo', '3A', 9, 'X55555555', 688888888);
INSERT INTO alumnos VALUES('10111111X', 'Francisco', 'Gordillo', '3A', 9, 'Z66666666', 699999999);

INSERT INTO asignaturas VALUES(1, 'Matematicas', 1, 'X11111111');
INSERT INTO asignaturas VALUES(2, 'Lengua', 1, 'Z22222222');
INSERT INTO asignaturas VALUES(3, 'Ciencias Sociales', 1, 'A33333333');
INSERT INTO asignaturas VALUES(4, 'Conocimiento del Medio', 1, 'X44444444');
INSERT INTO asignaturas VALUES(5, 'Ingles', 1, 'X55555555');
INSERT INTO asignaturas VALUES(6, 'Educacion Fisica', 1, 'Z66666666');
INSERT INTO asignaturas VALUES(7, 'Matematicas', 2, 'X11111111');
INSERT INTO asignaturas VALUES(8, 'Lengua', 2, 'Z22222222');
INSERT INTO asignaturas VALUES(9, 'Ciencias Sociales', 2, 'A33333333');
INSERT INTO asignaturas VALUES(10, 'Conocimiento del Medio', 2, 'X44444444');
INSERT INTO asignaturas VALUES(11, 'Ingles', 2, 'X55555555');
INSERT INTO asignaturas VALUES(12, 'Educacion Fisica', 2, 'Z66666666');
INSERT INTO asignaturas VALUES(13, 'Matematicas', 3, 'X11111111');
INSERT INTO asignaturas VALUES(14, 'Lengua', 3, 'Z22222222');
INSERT INTO asignaturas VALUES(15, 'Ciencias Sociales', 3, 'A33333333');
INSERT INTO asignaturas VALUES(16, 'Conocimiento del Medio', 3, 'X44444444');
INSERT INTO asignaturas VALUES(17, 'Ingles', 3, 'X55555555');
INSERT INTO asignaturas VALUES(18, 'Educacion Fisica', 3, 'Z66666666');

INSERT INTO notas VALUES(1,'11111111A',1,8);
INSERT INTO notas VALUES(2,'22222222Z',2,7);
INSERT INTO notas VALUES(3,'33333333K',3,7);
INSERT INTO notas VALUES(4,'44444444Z',4,6);
INSERT INTO notas VALUES(5,'55555555Z',7,5);
INSERT INTO notas VALUES(6,'66666666K',8,4);
INSERT INTO notas VALUES(7,'J77777777',9,6);
INSERT INTO notas VALUES(8,'88888888M',10,7);
INSERT INTO notas VALUES(9,'99999999L',13,8);
INSERT INTO notas VALUES(10,'10111111X',14,9);

