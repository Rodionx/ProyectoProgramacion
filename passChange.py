import tkinter as tk
from tkinter import messagebox
import bcrypt
import sqlite3
import importaciones as imp
import menu as menu
import Inicio as inicio

class PassApp:
    pos = 0
    
    def __init__(self, root):
        self.root = root
        self.root.title("Creacion de Contraseña")
        self.root.iconbitmap("icono.ico")

        self.pass_frame = tk.Frame(root)
        self.pass_frame.pack(expand=True)

        self.fPass = tk.Frame(self.pass_frame)
        self.fPass.pack(expand=True)
        
        self.sPass = tk.Frame(self.pass_frame)
        self.sPass.pack(expand=True)

        self.fPassLabel = tk.Label(self.fPass, text="Introduce la contraseña:")
        self.fPassLabel.pack(padx=11, pady=5, side=tk.LEFT)
        self.fPassEntry = tk.Entry(self.fPass, show="*")
        self.fPassEntry.pack(padx=10, pady=5, side=tk.LEFT)

        # Etiqueta y campo de entrada para la contraseña
        self.sPassLabel = tk.Label(self.sPass, text="Confirma tu contraseña:")
        self.sPassLabel.pack(padx=10, pady=5, side=tk.LEFT)
        self.sPassEntry = tk.Entry(self.sPass, show="*")
        self.sPassEntry.pack(padx=10, pady=5, side=tk.LEFT)

        # Botón de inicio de sesión
        self.continueButton = tk.Button(self.pass_frame, text="Continuar", command=self.login)
        self.continueButton.pack(padx=10, pady=5, fill=tk.X)

        # Centra el panel de login en la ventana
        self.pass_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def login(self):
        firstPass = self.fPassEntry.get()
        secondPass = self.sPassEntry.get()

        if firstPass == secondPass: 
            cryptPass= firstPass.encode('utf-8')
            imp.salt = bcrypt.gensalt()
            imp.hashed = bcrypt.hashpw(cryptPass,imp.salt)
            imp.hashed = imp.hashed.decode('utf-8')
            #Cambiar contraseña en base de datos
            try:
                tabla="usuarios"
                print(f"Registros tabla: {tabla}")
                conexion = sqlite3.connect("Colegio.db")
                conexion.execute(f"UPDATE {tabla} SET pass = '{imp.hashed}' WHERE usuario = '{imp.usuarioGeneral}'")
                conexion.commit()
            except Exception as e:
                print(e)
            self.login_frame.destroy()
            imp.ancho_ventana = 850
            imp.alto_ventana = 650
            menu.Menu(self.root)
        else:
                    messagebox.showerror("Las contraseñas no coinciden", "Las contraseñas no coinciden\nIntentelo de nuevo")

        