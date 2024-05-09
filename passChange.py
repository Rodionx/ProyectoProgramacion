import tkinter as tk
from tkinter import messagebox
import sqlite3

class PassApp:
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

        

if __name__ == "__main__":
    root = tk.Tk()
    app = PassApp(root)
    ancho_ventana = 600
    alto_ventana = 300

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    # root.geometry("700x400")
    root.mainloop()