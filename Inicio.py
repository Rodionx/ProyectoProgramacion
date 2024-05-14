import tkinter as tk
from tkinter import messagebox
import sqlite3
from passChange import PassApp
import importaciones as imp
import bcrypt
import menu as menu

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GestoSchool")
        self.root.iconbitmap("icono.ico")

        self.img = tk.PhotoImage(file='logo.png')

        self.login_frame = tk.Frame(root)
        self.login_frame.pack(expand=True)

        self.logo_frame = tk.Frame(self.login_frame)
        self.logo_frame.pack(expand=True)

        self.userFrame = tk.Frame(self.login_frame)
        self.userFrame.pack(expand=True)
        
        self.passFrame = tk.Frame(self.login_frame)
        self.passFrame.pack(expand=True)

        #logo
        self.logo_label = tk.Label(self.logo_frame, image=self.img)
        self.logo_label.pack(padx=22, pady=20, side=tk.LEFT)

        # Etiqueta y campo de entrada para el usuario
        self.username_label = tk.Label(self.userFrame, text="Usuario:")
        self.username_label.pack(padx=22, pady=5, side=tk.LEFT)
        self.username_entry = tk.Entry(self.userFrame)
        self.username_entry.pack(padx=10, pady=5, side=tk.LEFT)

        # Etiqueta y campo de entrada para la contraseña
        self.password_label = tk.Label(self.passFrame, text="Contraseña:")
        self.password_label.pack(padx=10, pady=5, side=tk.LEFT)
        self.password_entry = tk.Entry(self.passFrame, show="*")
        self.password_entry.pack(padx=10, pady=5, side=tk.LEFT)

        # Botón de inicio de sesión
        self.login_button = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(padx=10, pady=5, fill=tk.X)

        # Centra el panel de login en la ventana
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        tabla="usuarios"
        print(f"Registros tabla: {tabla}")
        conexion = sqlite3.connect("Colegio.db")
        cursor=conexion.execute(f"select * from {tabla}")
        consultas = {}
        for fila in cursor:
            consultas.update({fila[0] : fila[1]})
            # conexion.execute(f"INSERT INTO {tabla} VALUES('user1','')")
            # conexion.commit()
            
        for u,p in consultas.items():
            imp.usuarioGeneral = u
            passComp = str(p)
            
            if username == u:
                if username == u and p == '':
                    self.login_frame.destroy() 
                    PassApp(self.root)
                else:
                    if username == u and bcrypt.checkpw(password.encode('utf-8'),passComp.encode('utf-8')):
                        self.login_frame.destroy()
                        imp.ancho_ventana = 850
                        imp.alto_ventana = 650
                        menu.Menu(self.root)
                    else:

                        messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos")

        conexion.close()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)

    x_ventana = root.winfo_screenwidth() // 2 - imp.ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - imp.alto_ventana

    posicion = str(imp.ancho_ventana) + "x" + str(imp.alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.mainloop()