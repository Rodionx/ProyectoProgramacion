import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

class myBrowse:
    # Create Window
    def __init__(self,browser_root) :
        self.browser_root = browser_root
        self.browser_root.title('GestoSchool')

        # Basic Layout
        self.browser_root.geometry()
        self.browser_root.geometry("800x500")
        self.browser_root.minsize(600,300)
        self.browser_root.config(background='#ffffff')
        icon = tk.PhotoImage(file = 'logo.png')
        self.browser_root.iconphoto(True,icon)

        #Grid Structure

        # -- Columns
        #self.col0= self.browser_root.columnconfigure(0, weight = 1)
        self.col1 = self.browser_root.columnconfigure(0, weight = 1)
        self.col2= self.browser_root.columnconfigure(1, weight = 1)
        self.col3= self.browser_root.columnconfigure(2, weight = 1)
        #-- Rows
        self.row0 = self.browser_root.rowconfigure(0,weight= 1)
        self.row1 = self.browser_root.rowconfigure(1,weight= 1)
        self.row2 = self.browser_root.rowconfigure(2,weight= 1)
        self.row3 = self.browser_root.rowconfigure(3,weight= 1)

        #--Frame Para Entradas
        self.frame_entry = tk.Frame(self.browser_root,bg='#EDEADE')
        self.frame_entry.grid(column=1,row=1,padx=1,pady=1,sticky='nswe')

        # -- Entries
        self.dni = tk.Entry(self.frame_entry,bd=3)
        self.nombre = tk.Entry(self.frame_entry,bd=3)
        self.apellidos = tk.Entry(self.frame_entry,bd=3)

        self.dni_label = tk.Label(self.frame_entry,text='DNI')
        self.nombre_label = tk.Label(self.frame_entry,text='Nombre')
        self.apellidos_label = tk.Label(self.frame_entry,text='Apellido')

        self.dni.grid(row=1,column=1,sticky='w',padx='5',pady='5')
        self.nombre.grid(row=2,column=1,sticky='ew',padx='5',pady='5')
        self.apellidos.grid(row=3,column=1,sticky='e',padx='5',pady='5')

        self.dni_label.grid(row=1,column=2,sticky='w',padx='5',pady='5')
        self.nombre_label.grid(row=2,column=2,sticky='ew',padx='5',pady='5')
        self.apellidos_label.grid(row=3,column=2,sticky='e',padx='5',pady='5')

        # -- Botones
        self.boton_insertar = tk.Button(self.frame_entry,text='Insertar Entrada')
        self.boton_insertar.grid(row=4, column = 1,pady=10)

        self.boton_modificar = tk.Button(self.frame_entry,text='Modificar Entrada')
        self.boton_modificar.grid(row=5, column = 1,pady=10)

        
        self.boton_modificar = tk.Button(self.frame_entry,text='Eliminar Entrada')
        self.boton_modificar.grid(row=6, column = 1,pady=10)


        # -- Frame para SQLITE display
        self.frame_data = tk.Frame(self.browser_root,bg='#EDEADE')
        self.frame_data.grid(column=2,row=1,padx=1,pady=1,sticky='nswe')
        
        # Labels
        profesores_label = tk.Label(self.browser_root,bg='grey', text= 'profesores',font=('Arial',16),width=3,height=3)

        # --Image
        img_profesor = tk.PhotoImage(file='ProyectoProgramacion\menu_icons\profesora.png')
        profesores_icon= tk.Label(self.browser_root,width=5,image=img_profesor)
        

        # --Grid Packing
        profesores_icon.grid(row=1, column=0,padx=5,pady=5,sticky='we')
        profesores_label.grid(row = 2, column = 0,pady=5,padx=5,sticky='we')

        
     # --Data Display

        # Connect to the SQLite database
        conn = sql.connect('ProyectoProgramacion\Colegio.db')
        c = conn.cursor()

        c.execute("PRAGMA table_info(profesores)")  # Replace 'your_table_name' with the actual table name
        column_names = [row[1] for row in c.fetchall()]
        
        # Fetch data from the database
        c.execute("SELECT * FROM profesores")  # Replace 'your_table_name' with the actual table name
        data = c.fetchall()
        
        # Close the connection
        conn.close()
        
        for col_index, column_name in enumerate(column_names):
            label = tk.Label(self.frame_data, text=column_name, borderwidth=1, relief="solid", bg="lightgrey")
            label.grid(row=0, column=col_index, sticky="nsew")

        # Display data inside the frame
        for row_index, row_data in enumerate(data):
            for col_index, cell_value in enumerate(row_data):
                label = tk.Label(self.frame_data, text=cell_value, borderwidth=1, relief="solid",width=10)
                label.grid(row=row_index+1, column=col_index, sticky = 'nsew')


         # -- Funciones de SQL       

        def mod_data_profs(dni,x,y):
                    conn = sql.connect('ProyectoProgramacion\Colegio.db')
                    c = conn.cursor()

                    c.execute('''UPDATE profesores
                            SET
                                nombre = ?,
                                apellido = ?
                            WHERE
                                DNI_prof = ?

                    ''',(x,y,dni))


                    conn.commit()
                    conn.close()



        


        








        # Mainloop
        self.browser_root.mainloop()

app = tk.Tk()
root = myBrowse(app)