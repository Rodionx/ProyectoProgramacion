import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")

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
        
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Exitoso", "¡Bienvenido, {}!".format(username))
        else:
            messagebox.showerror("Error de Login", "Usuario o contraseña incorrectos")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    ancho_ventana = 600
    alto_ventana = 300

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    # root.geometry("700x400")
    root.mainloop()