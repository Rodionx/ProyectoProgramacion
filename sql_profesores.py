
from tkinter import messagebox
import sqlite3 as sqlite



def mod_data_profs(dni,params):
            fields = []
            values = []
            for key in params:
                  if params[key] != '':
                        fields.append(key)
                        values.append(params[key])
                  else:
                        continue
                  
            set_statement = ", ".join(fields)      
            values.append(dni)
            command = "UPDATE profesores SET " + set_statement + " WHERE DNI_profesores = ?"
                        
            try:
                conn = sqlite.connect('Colegio.db')
                c = conn.cursor()

                c.execute(command,tuple(values))


                conn.commit()
                print("Update successful")
            except  Exception as e:
                messagebox.showerror(message=f"Error {e}")
            finally:
                conn.close()

def delete_data_profs(dni):
    try:
        conn = sqlite.connect('Colegio.db')
        c = conn.cursor()
        c.execute('DELETE FROM profesores WHERE  DNI_prof = ?',(dni,))
        conn.commit()
        print(f"registro {i} eliminado")
    except  Exception as e:
        messagebox.showerror(message=f"Error {e}")
    finally:
            conn.close()


def insert_profs(dni,nombre,apellido):
            try:
                conn = sqlite.connect('Colegio.db')
                c = conn.cursor()

                c.execute('''INSERT INTO profesores(DNI_prof,nombre,apellido) VALUES(?, ?, ?)''',(dni,nombre,apellido))

                conn.commit()
                print("Update successful")
            except Exception as e :
                messagebox.showerror(message=f"Error {e}")
            finally:
                conn.close()

