from tkinter import messagebox
import sqlite3 as sqlite


def mod_data_student(dni,params):
            if dni != '':
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
            else:
                messagebox.showerror(message=f"Se requiere del campo DNI para hacer la operacion")


def delete_data_students(dni):
    if dni != '':
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
    else:
        messagebox.showerror(message=f"Se requiere del campo DNI para hacer la operacion")


def insert_data_student(dni,nombre,apellido,clase,edad,tutor,contacto):
            if dni !='':
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
            else:
                messagebox.showerror(message="Se requiere del campo DNI")

                    
def data_display(treeframe):
    # Connect to the SQLite database
    conn = sqlite.connect('Colegio.db')
    c = conn.cursor()

    c.execute("PRAGMA table_info(profesores)")  # Replace 'your_table_name' with the actual table name
    column_names = [row[1] for row in c.fetchall()]
    
    # Fetch data from the database
    c.execute("SELECT * FROM alumnos")  # Replace 'your_table_name' with the actual table name
    data = c.fetchall()
    
    # Close the connection
    conn.close()
    treeframe.delete(*treeframe.get_children())
    for tupla in data:
            lista = list(tupla)
            treeframe.insert("",'end',text=id,values=tupla)