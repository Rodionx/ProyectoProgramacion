import tkinter as tk
import sqlite3 as sql
from tkinter import ttk
import sql_estudiantes as imp


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
        #self.col3= self.browser_root.columnconfigure(2, weight = 1)
        #-- Rows
        self.row0 = self.browser_root.rowconfigure(0,weight= 1)
        self.row1 = self.browser_root.rowconfigure(1,weight= 1)
        # self.row2 = self.browser_root.rowconfigure(2,weight= 1)
        # self.row3 = self.browser_root.rowconfigure(3,weight= 1)

        #--Frame Para Entradas
        self.frame_entry = tk.Frame(self.browser_root,bg='#EDEADE')
        self.frame_entry.grid(column=1,row=0,padx=1,pady=1,sticky='nswe')

        # -- Entries
        self.dni = tk.Entry(self.frame_entry,bd=3)
        self.nombre = tk.Entry(self.frame_entry,bd=3)
        self.apellidos = tk.Entry(self.frame_entry,bd=3)
        self.clase = tk.Entry(self.frame_entry,bd=3)
        self.edad = tk.Entry(self.frame_entry,bd=3)
        self.tutor = tk.Entry(self.frame_entry,bd=3)
        self.contacto = tk.Entry(self.frame_entry,bd=3)


        self.dni_label = tk.Label(self.frame_entry,text='DNI')
        self.nombre_label = tk.Label(self.frame_entry,text='Nombre')
        self.apellidos_label = tk.Label(self.frame_entry,text='Apellido')
        self.clase_label = tk.Label(self.frame_entry,text='Clase')
        self.edad_label = tk.Label(self.frame_entry,text='Edad')
        self.tutor_label = tk.Label(self.frame_entry,text='Tutor')
        self.contacto_label = tk.Label(self.frame_entry,text='Contacto')

        self.dni.grid(row=1,column=1,sticky='nsew',padx='5',pady='5')
        self.nombre.grid(row=2,column=1,sticky='nsew',padx='5',pady='5')
        self.apellidos.grid(row=3,column=1,sticky='nsew',padx='5',pady='5')
        self.clase.grid(row=1,column=3,sticky='nsew',padx='5',pady='5')
        self.edad.grid(row=2,column=3,sticky='nsew',padx='5',pady='5')
        self.tutor.grid(row=3,column=3,sticky='nsew',padx='5',pady='5')
        self.contacto.grid(row=4,column=1,sticky='nsew',padx='5',pady='5')


        self.dni_label.grid(row=1,column=0,sticky='nsew',padx='5',pady='5')
        self.nombre_label.grid(row=2,column=0,sticky='nsew',padx='5',pady='5')
        self.apellidos_label.grid(row=3,column=0,sticky='nsew',padx='5',pady='5')
        self.clase_label.grid(row=1,column=2,sticky='nsew',padx='5',pady='5')
        self.edad_label.grid(row=2,column=2,sticky='nsew',padx='5',pady='5')
        self.tutor_label.grid(row=3,column=2,sticky='nsew',padx='5',pady='5')
        self.contacto_label.grid(row=4,column=0,sticky='nsew',padx='5',pady='5')
       

        # -- Botones
        self.boton_insertar = tk.Button(self.frame_entry,text='Insertar Entrada', command= lambda : imp.insert_data_student(self.dni.get(),self.nombre.get(),self.apellidos.get(),self.clase.get(),self.edad.get(),self.tutor.get(),self.contacto.get()))
        self.boton_insertar.grid(row=1, column = 4,pady=10,padx=0)

        self.boton_modificar = tk.Button(self.frame_entry,text='Modificar Entrada',command= lambda : imp.mod_data_student(self.dni.get(),self.nombre.get(),self.apellidos.get(),self.clase.get(),self.edad.get(),self.tutor.get(),self.contacto.get()))
        self.boton_modificar.grid(row=2, column = 4,pady=10,padx=10)

        
        self.boton_modificar = tk.Button(self.frame_entry,text='Eliminar Entrada',command= lambda : imp.delete_data_students(self.dni.get()))
        self.boton_modificar.grid(row=3, column = 4,pady=10,padx=10)

                


        # -- Frame para SQLITE display
        self.frame_data =   ttk.Treeview(self.browser_root) # tk.Frame(self.browser_root,bg='#EDEADE')
        self.frame_data.grid(column=1,row=1,padx=1,pady=1,sticky='nswe')
        self.frame_data['columns'] = ('DNI','Nombre','Apellido','Clase','Edad','Tutor','Contacto')

        self.frame_data.column('#0',width=0,stretch='NO')
        self.frame_data.heading('#0',text=" ",)

        self.frame_data.column('DNI',anchor='center',width=10)
        self.frame_data.heading('DNI',text='DNI')

        self.frame_data.column('Nombre',anchor='center',width=10)
        self.frame_data.heading('Nombre',text='Nombre')

        self.frame_data.column('Apellido',anchor='center',width=10)
        self.frame_data.heading('Apellido',text='Apellido')

        self.frame_data.column('Clase',anchor='center',width=3)
        self.frame_data.heading('Clase',text='Clase')

        self.frame_data.column('Edad',anchor='center',width=3)
        self.frame_data.heading('Edad',text='Edad')

        self.frame_data.column('Tutor',anchor='center',width=10)
        self.frame_data.heading('Tutor',text='Tutor')

        self.frame_data.column('Contacto',anchor='center',width=10)
        self.frame_data.heading('Contacto',text='Contacto')

        
        # Labels
        #profesores_label = tk.Label(self.browser_root,bg='grey', text= 'profesores',font=('Arial',16),width=3,height=3)

        # --Image
        #img_profesor = tk.PhotoImage(file='profesora.png')
        #profesores_icon= tk.Label(self.browser_root,width=5,image=img_profesor)
        

        # --Grid Packing
        #profesores_icon.grid(row=1, column=0,padx=5,pady=5,sticky='we',columnspan=2)
        #profesores_label.grid(row = 2, column = 0,pady=5,padx=5,sticky='we',columnspan=2)

        
     # --Data Display
             # --------------Data Display------------------
        def data_display():
            # Connect to the SQLite database
            conn = sql.connect('Colegio.db')
            c = conn.cursor()

            c.execute("PRAGMA table_info(profesores)")  # Replace 'your_table_name' with the actual table name
            column_names = [row[1] for row in c.fetchall()]
            
            # Fetch data from the database
            c.execute("SELECT * FROM alumnos")  # Replace 'your_table_name' with the actual table name
            data = c.fetchall()
            
            # Close the connection
            conn.close()
            self.frame_data.delete(*self.frame_data.get_children())
            for tupla in data:
                  lista = list(tupla)
                  self.frame_data.insert("",'end',text=id,values=tupla)
            # --------------Data Display------------------

        self.boton_refrescar = tk.Button(self.frame_entry,text='Refrescar Datos',command=data_display)
        self.boton_refrescar.grid(row=4, column = 4,pady=10,padx=10)


        
                        
                        
            
        """     for col_index, column_name in enumerate(column_names):
                label = tk.Label(self.frame_data, text=column_name, borderwidth=1, relief="solid", bg="lightgrey",width=28)
                label.grid(row=0, column=col_index, sticky="nsew")

            # Display data inside the frame
            for row_index, row_data in enumerate(data):
                for col_index, cell_value in enumerate(row_data):
                    label = tk.Label(self.frame_data, text=cell_value, borderwidth=1, relief="solid")
                    label.grid(row=row_index+1, column=col_index, sticky = 'nsew') """
        


        # Mainloop
        data_display()
        self.browser_root.mainloop()

app = tk.Tk()
root = myBrowse(app)