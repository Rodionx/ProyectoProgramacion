import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
from tkinter import ttk
import sql_profesores as imp
import gui_tooltip as ttp

class myBrowse:
    # Create Window
    def __init__(self,browser_root) :
      
        fondo = '#153147'
        relieve = 'solid'
        letra = 'white'
        fondo_botones = '#5c2331'

        self.browser_root = browser_root
        # self.browser_root.title('GestoSchool')

        # Basic Layout
        # self.browser_root.geometry()
        # self.browser_root.geometry("800x500")
        # self.browser_root.minsize(600,300)
        # self.browser_root.config(background='#ffffff')
        # icon = tk.PhotoImage(file = 'logo.png')
        # self.browser_root.iconphoto(True,icon)

        #Grid Structure

        # -- Columns
        #self.col0= self.browser_root.columnconfigure(0, weight = 1)
        self.col1 = self.browser_root.columnconfigure(0, weight = 1)

        #self.col2= self.browser_root.columnconfigure(1, weight = 1)
        #self.col3= self.browser_root.columnconfigure(2, weight = 1)

        #-- Rows
        self.row0 = self.browser_root.rowconfigure(0,weight= 1)
        self.row1 = self.browser_root.rowconfigure(1,weight= 1)
        self.row2 = self.browser_root.rowconfigure(2,weight= 1)
        self.row3 = self.browser_root.rowconfigure(3,weight= 1)

        #--Frame Para Entradas

        self.frame_entry = tk.Frame(self.browser_root,bg='#1b2a3b')
        self.frame_entry.grid(column=0,row=0,padx=1,pady=1,sticky='nswe')

        # -- Entries
        self.dni = tk.Entry(self.frame_entry,bd=1,relief='solid')
        self.nombre = tk.Entry(self.frame_entry,bd=1.,relief='solid')
        self.apellidos = tk.Entry(self.frame_entry,bd=1,relief='solid')

        #Tooltip :
        self.dni_ttp = ttp.CreateToolTip(self.dni,
                                                    '**Clave Principal: DNI \n'
                                                    '**Descripción: \n'
                                                    'Este campo es el identificador único para cada usuario.\n'
                                                    '**USO:\n'
                                                    'Es imprescindible de usar ya que se requiere en todas las operaciones')

        self.dni_label = tk.Label(self.frame_entry,text='DNI',relief='solid',bg='#1b2a3b',fg='white',bd=0)
        self.nombre_label = tk.Label(self.frame_entry,text='Nombre',relief='solid',bg='#1b2a3b',fg='white',bd=0)
        self.apellidos_label = tk.Label(self.frame_entry,text='Apellido',relief='solid',bg='#1b2a3b',fg='white',bd=0)

        self.dni.grid(row=1,column=1,sticky='w',padx='5',pady='5')
        self.nombre.grid(row=2,column=1,sticky='ew',padx='5',pady='5')
        self.apellidos.grid(row=3,column=1,sticky='e',padx='5',pady='5')

        self.dni_label.grid(row=1,column=0,sticky='nsew',padx='5',pady='5')
        self.nombre_label.grid(row=2,column=0,sticky='nsew',padx='5',pady='5')
        self.apellidos_label.grid(row=3,column=0,sticky='nsew',padx='5',pady='5',)

        # -- Botones
        self.boton_insertar = tk.Button(self.frame_entry,text='Insertar Entrada',bg=fondo_botones,bd=2,fg='white',relief='solid',command=lambda :[imp.insert_profs(self.dni.get(),self.nombre.get(),self.apellidos.get()),clear_text(parameters),imp.data_display(self.frame_data)])
        self.boton_insertar.grid(row=1, column = 2,pady=10,padx = 5 ,sticky='nsew')

        self.boton_modificar = tk.Button(self.frame_entry,text='Modificar Entrada',bg=fondo_botones,relief='solid',bd=2,fg='white',command=lambda: [imp.mod_data_profs(self.dni.get(),{'nombre':self.nombre.get(),'profesores':self.apellidos.get()}),clear_text(parameters),imp.data_display(self.frame_data)])
        self.boton_modificar.grid(row=2, column = 2,pady=10,padx = 5 ,sticky='nsew')

        
        self.boton_modificar = tk.Button(self.frame_entry,text='Eliminar Entrada',bg=fondo_botones,bd=2,fg='white',relief='solid',command=lambda : [imp.delete_data_profs(self.dni.get()),clear_text(parameters),imp.data_display(self.frame_data)])
        self.boton_modificar.grid(row=3, column = 2,pady=10,padx = 5 ,sticky='nsew')

        self.boton_refrescar = tk.Button(self.frame_entry,text='Refrescar Datos',bg=fondo_botones,bd=2,fg='white',relief='solid',command= lambda : [imp.data_display(self.frame_data),clear_text(parameters)])
        self.boton_refrescar.grid(row=4, column = 2,pady=10)


        # -- Frame para SQLITE display
        self.frame_data =   ttk.Treeview(self.browser_root) # tk.Frame(self.browser_root,bg='#EDEADE')
        self.frame_data.grid(column=0,row=1,padx=1,pady=1,sticky='nswe')
        self.frame_data['columns'] = ('DNI','Nombre','Apellido')

        self.frame_data.column('#0',width=0,stretch='NO')
        self.frame_data.heading('#0',text=" ",)

        self.frame_data.column('DNI',anchor='center')
        self.frame_data.heading('DNI',text='DNI')

        self.frame_data.column('Nombre',anchor='center')
        self.frame_data.heading('Nombre',text='Nombre')

        self.frame_data.column('Apellido',anchor='center')
        self.frame_data.heading('Apellido',text='Apellido')
        


        def clear_text(params):
            for x in params:
                x.delete(0,"end")
        

        parameters = (self.dni,self.nombre,self.apellidos)

        # Connect to the SQLite database
        conn = sql.connect('Colegio.db')
        c = conn.cursor()

        c.execute("PRAGMA table_info(profesores)")  # Replace 'your_table_name' with the actual table name
        column_names = [row[1] for row in c.fetchall()]
        

                        
        # Mainloop
        imp.data_display(self.frame_data)
        # self.browser_root.mainloop()
