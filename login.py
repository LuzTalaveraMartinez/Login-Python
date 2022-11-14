import tkinter 
from tkinter import * 
from  tkinter import messagebox
import pymysql


def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x450")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("login.ico")

    image= PhotoImage(file="utn.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al Sístema", bg="#383838", fg="white", width="300", height="3", font=("Calíbrí", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesíon", height="3", width="25", font=("Calíbrí", 12), command=inicio_sesion).pack()
    Label(text="").pack()
    Button(text="Registrar", height="3", width="25", font=("Calíbrí", 12), command=registrar).pack()


    pantalla.mainloop()


def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("login.ico")

    Label(pantalla1, text="Por favor ingrese su usuario y contraseña \n a continuación.", bg="#383838", fg="white", width="300", height="3", font=("Calíbrí", 10)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verificacion
    global contrasenausuario_verificacion

    nombreusuario_verificacion= StringVar()
    contrasenausuario_verificacion= StringVar()

    global nombre_usuario_entry 
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry= Entry(pantalla1, textvariable=nombreusuario_verificacion)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry= Entry(pantalla1, show="*", textvariable=contrasenausuario_verificacion)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar Sesión", command=validacion_datos).pack()


def registrar():
    global pantalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("login.ico")

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label(pantalla2, text="Por favor, ingrese un Usuario y contraseña de su elección,\n para el registro al sistema.", bg="#383838", fg="white", width="300", height="3", font=("Calíbrí", 10)).pack()
    Label (pantalla2, text="").pack()

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry= Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasena_entry= Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()


def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db= "bd2-python"
    )

    fcursor=bd.cursor()
    sql="INSERT INTO login (usuario, contrasena) VALUES ('{0}','{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado", title="Aviso")

    bd.close()



def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db= "bd2-python"
    )

    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verificacion.get()+"' and contrasena='"+contrasenausuario_verificacion.get()+"'")
    if fcursor.fetchall():
        messagebox.showinfo("Inicio de Sesión correcto", message="Usuario y Contraseña correcta")
    else:
        messagebox.showinfo("Inicio de Sesión Incorrecto", message="Usuario y Contraseña incorrecta")

    bd.close()

menu_pantalla()