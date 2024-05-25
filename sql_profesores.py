
from tkinter import messagebox
import sqlite3 as sqlite



def mod_data_profs(dni,params):
            if dni != '':
                fields = []
                values = []
                for key in params:
                    if params[key] != '':
                            fields.append(key + '=?')
                            values.append(params[key])
                    else:
                            continue
                    
                set_statement = ", ".join(fields)      
                values.append(dni)
                command = "UPDATE profesores SET " + set_statement + " WHERE DNI_prof = ?"
                            
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
            else:
                messagebox.showerror(message=f"Se requiere del campo DNI para hacer la operacion")


def delete_data_profs(dni):
    if dni != '':
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
    else:
        messagebox.showerror(message=f"Se requiere del campo DNI para hacer la operacion")



def insert_profs(dni,nombre,apellido):
            if dni != '' and nombre != '' and apellido != '':
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
            else:
                messagebox.showerror(message="Todos los campos deben estar llenos")

def data_display(treeframe):
    # Connect to the SQLite database
    conn = sqlite.connect('Colegio.db')
    c = conn.cursor()

    c.execute("PRAGMA table_info(profesores)")  # Replace 'your_table_name' with the actual table name
    column_names = [row[1] for row in c.fetchall()]
    
    # Fetch data from the database
    c.execute("SELECT * FROM profesores")  # Replace 'your_table_name' with the actual table name
    data = c.fetchall()
    
    # Close the connection
    conn.close()
    treeframe.delete(*treeframe.get_children())
    for tupla in data:
            lista = list(tupla)
            treeframe.insert("",'end',text=id,values=tupla)
