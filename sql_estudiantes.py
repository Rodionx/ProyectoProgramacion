from tkinter import messagebox
import sqlite3 as sqlite

def mod_data_student(dni,params):
            values_set = [] 
            fields = []
            for key in params:
                  if params[key] != '':
                    fields.append(key + '=?')
                    values_set.append(params[key])
                  else:
                       continue
                  
            set_statement = ", ".join(fields)      
            values_set.append(dni)
            command = "UPDATE alumnos SET " + set_statement + " WHERE DNI_Alumno = ?"

            try:
                conn = sqlite.connect('Colegio.db')
                c = conn.cursor()

                c.execute(command,tuple(values_set))

                conn.commit()
                print("Update successful")
            except  Exception as e:
                messagebox.showerror(message=f"Error {e}")
            finally:
                conn.close()

def delete_data_students(dni):
    try:
        conn = sqlite.connect('Colegio.db')
        c = conn.cursor()
        c.execute('DELETE FROM alumnos WHERE  DNI_alumno = ?',(dni,))
        conn.commit()
        print(f"registro {dni} eliminado")
    except  Exception as e:
        messagebox.showerror(message=f"Error {e}")
    finally:
            conn.close()


def insert_data_student(dni,nombre,apellido,clase,edad,tutor,contacto):
            try:
                conn = sqlite.connect('Colegio.db')
                c = conn.cursor()

                c.execute('''INSERT INTO alumnos
                (DNI_alumno,nombre,apellido,clase,edad,tutor,contacto)
                          VALUES
                          (?,?,?,?,?,?,?)

                ''',(nombre,apellido,clase,edad,tutor,contacto,dni))
                
                conn.commit()
                print("Update successful")
            except  Exception as e:
                messagebox.showerror(message=f"Error {e}")
            finally:
                conn.close()