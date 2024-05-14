import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self,menu_root):
        self.menu_root = menu_root
        self.menu_root.title ('GestoSchool' )

        # ----- Basic Layout ----- 
        self.menu_root.geometry("800x500")
        self.menu_root.minsize(600,300)
        self.menu_root.config(background='#ffffff')
        icon = tk.PhotoImage(file = 'logo.png')
        self.menu_root.iconphoto(True,icon)

        # ---- Frame ----
        self.frame = tk.Frame(self.menu_root,bg='white')
        self.frame.pack()



        #---- Column Configure ----
        self.frame.columnconfigure(0, weight = 1)
        self.frame.columnconfigure(1, weight = 1)
        self.frame.columnconfigure(2, weight = 1)
        self.frame.columnconfigure(3, weight = 1)
        self.frame.columnconfigure(4, weight = 1)
        self.frame.columnconfigure(5, weight = 1)

        # ---- Row Configure ----
        self.frame.rowconfigure(0,weight_= 1)
        self.frame.rowconfigure(1,weight_= 5)
        self.frame.rowconfigure(2,weight_= 1)

        # ---- Title----
        Title = tk.Label(self.frame, text='Bienvenido admin,', fg='black', width=50, font=('Arial', 16, 'italic'), anchor='w',padx = 10,pady = 20)
        Title.grid(row= 0 , columnspan = 6 ,sticky='n')
        
        #---- Icon Labels ----
        img_profesor = tk.PhotoImage(file='ProyectoProgramacion\menu_icons\profesora.png')
        profesores_label= tk.Label(self.frame,width=5,image=img_profesor)
        
        img_notas = tk.PhotoImage(file='ProyectoProgramacion\menu_icons\grades.png')
        notas_label = tk.Label(self.frame,width=5, image=img_notas)

        img_alumnos = tk.PhotoImage(file='ProyectoProgramacion\menu_icons\estudiante.png')
        alumnos_label = tk.Label(self.frame,width=5,image=img_alumnos)


        img_asignaturas = tk.PhotoImage(file='ProyectoProgramacion\menu_icons\clases.png')
        asignaturas_label = tk.Label(self.frame,width=5, image=img_asignaturas)

        # ---- Icon Placement ----
        profesores_label.grid(row=1,column=1,padx= 10,pady=10,sticky='we')
        notas_label.grid(row=1,column=2,padx= 10,pady=10,sticky='we')
        alumnos_label.grid(row=1,column=3,padx= 10,pady=10,sticky='we')
        asignaturas_label.grid(row=1,column=4,padx= 10,pady=10,sticky='we')



        # ---- Text Buttons ----
        profesores_button = tk.Button(self.frame, text='Profesores',font=('arial',16),width=10,height=2)
        notas_button = tk.Button(self.frame, text='Notas',font=('arial',16),width=10,height=2)
        alumnos_button = tk.Button(self.frame, text='Alumnos',font=('arial',16),width=10,height=2)
        asignaturas_button = tk.Button(self.frame, text='Asignaturas',font=('arial',16),width=10,height=2)
    

        # ---- Button Placement ---- 
        profesores_button.grid(row=2,column=1,padx= 20,pady=10,sticky='we')
        notas_button.grid(row=2,column=2,padx= 20,pady=10,sticky='we')
        alumnos_button.grid(row=2,column=3,padx= 20,pady=10,sticky='we')
        asignaturas_button.grid(row=2,column=4,padx= 20,pady=10,sticky='we')

        



        self.menu_root.mainloop()




menu = tk.Tk()
window = Menu(menu)
