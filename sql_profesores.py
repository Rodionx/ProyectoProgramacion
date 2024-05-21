
from tkinter import messagebox
import sqlite3 as sqlite



def mod_data_profs(i,x,y):
            try:
                conn = sqlite.connect('Colegio.db')
                c = conn.cursor()

                c.execute('''UPDATE profesores
                        SET
                            nombre = ?,
                            apellido = ?
                        WHERE
                            DNI_prof = ?

                ''',(x,y,i))


                conn.commit()
                print("Update successful")
            except  Exception as e:
                messagebox.showerror(message=f"Error {e}")
            finally:
                conn.close()

def delete_data_profs(i):
    try:
        conn = sqlite.connect('Colegio.db')
        c = conn.cursor()
        c.execute('DELETE FROM profesores WHERE  DNI_prof = ?',(i,))
        conn.commit()
        print(f"registro {i} eliminado")
    except  Exception as e:
        messagebox.showerror(message=f"Error {e}")
    finally:
            conn.close()


def insert_profs(i,x,y):
            try:
                conn = sqlite.connect('Colegio.db')
                c = conn.cursor()

                c.execute('''INSERT INTO profesores(DNI_prof,nombre,apellido) VALUES(?, ?, ?)''',(i,x,y))

                conn.commit()
                print("Update successful")
            except Exception as e :
                messagebox.showerror(message=f"Error {e}")
            finally:
                conn.close()

