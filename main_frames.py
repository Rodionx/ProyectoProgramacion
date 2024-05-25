import importaciones as imp
import tkinter as tk
import dbBrowse_Profesores as profesores
import dbBrowse_Estudiantes as estudiantes

class Mainframe:
    def __init__(self,root):
        self.root = root
        self.root.title ('GestoSchool' )
        fondo = '#232A2F'
        relieve = 'solid'
        letra = 'white'
        fondo_botones= "#5c2331"

        


        # ----- Basic Layout ----- 
        self.root.geometry('800x500')
        self.root.config(background='#ffffff')
        icon = tk.PhotoImage(file = 'logo.png')
        self.root.iconphoto(True,icon)

        # ------ Gridconfigure -----
        self.col1 = self.root.columnconfigure(0, weight = 1)
        self.col2 = self.root.columnconfigure(1, weight = 3)

        self.row = self.root.rowconfigure(0,weight = 1)

        # ------ Frames -------
        self.dashboard = tk.Frame(self.root,bg=fondo)
        self.display = tk.Frame(self.root,bg="white")



        
        ## --- |Display|---
        self.dashboard.grid(row=0,column=0,sticky='nsew')
        self.display.grid(row=0,column=1,sticky='nsew')
        


        ## --- |Dashboard|-----
                # ---- Text Buttons ----
        profesores_button = tk.Button(self.dashboard,bg=fondo_botones,fg='white',relief='solid',bd=2,text='Profesores',font=('arial',16),width=10,command = lambda: profesores.myBrowse(self.display)) 
        notas_button = tk.Button(self.dashboard,bg=fondo_botones, fg='white',relief='solid',bd=2,text='Notas',font=('arial',16),width=10) #command = lambda: pon aqui tu constructor
        alumnos_butto = tk.Button(self.dashboard,bg=fondo_botones,fg='white',relief='solid',bd=2,text='Alumnos',font=('arial',16),width=10,command = lambda: estudiantes.myBrowse(self.display))
        asignaturas_button = tk.Button(self.dashboard,bg=fondo_botones,fg='white',bd=2,relief='solid', text='Asignaturas',font=('arial',16),width=10, ) #command = lambda: pon aqui tu constructor

             # ---- Button Placement ---- 
        profesores_button.pack(side='top',expand=True)
        notas_button.pack(side='top',expand=True)
        alumnos_butto.pack(side='top',expand=True)
        asignaturas_button.pack(side='top',expand=True)

       

        self.root.mainloop()

app = tk.Tk()
root = Mainframe(app)
