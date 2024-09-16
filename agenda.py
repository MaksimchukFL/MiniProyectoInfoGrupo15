import tkinter as tk
from tkinter import messagebox

# Función para agregar un contacto a la lista
def agregar_contacto():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    area = entrada_area.get()
    numero = entrada_numero.get()
    
    if nombre != "" and apellido != "" and area != "" and numero != "":
        contacto = f"{nombre} {apellido}, Área: {area}, Número: {numero}"  # Formato "Nombre Apellido, Área: ..., Número: ..."
        lista_contactos.insert(tk.END, contacto)
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_area.delete(0, tk.END)
        entrada_numero.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

# Función para eliminar el contacto seleccionado
def eliminar_contacto():
    seleccion = lista_contactos.curselection()  # Obtener el índice del contacto seleccionado
    if seleccion:
        lista_contactos.delete(seleccion[0])  # Eliminar el contacto seleccionado
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un contacto para eliminar.")

# Función para seleccionar un contacto de la lista y rellenar los campos
def seleccionar_contacto():
    seleccion = lista_contactos.curselection()  # Obtener el índice del contacto seleccionado
    if seleccion:
        contacto_seleccionado = lista_contactos.get(seleccion[0])  # Obtener el texto del contacto
        nombre_completo, info_contacto = contacto_seleccionado.split(", Área: ")
        nombre, apellido = nombre_completo.split(" ", 1)  # Separar Nombre y Apellido
        area, numero = info_contacto.split(", Número: ")

        entrada_nombre.delete(0, tk.END)
        entrada_nombre.insert(tk.END, nombre)
        entrada_apellido.delete(0, tk.END)
        entrada_apellido.insert(tk.END, apellido)
        entrada_area.delete(0, tk.END)
        entrada_area.insert(tk.END, area)
        entrada_numero.delete(0, tk.END)
        entrada_numero.insert(tk.END, numero)
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un contacto para modificar.")

# Función para modificar el contacto seleccionado
def modificar_contacto():
    seleccion = lista_contactos.curselection()  # Obtener el índice del contacto seleccionado
    if seleccion:
        nombre = entrada_nombre.get()
        apellido = entrada_apellido.get()
        area = entrada_area.get()
        numero = entrada_numero.get()
        
        if nombre != "" and apellido != "" and area != "" and numero != "":
            contacto_modificado = f"{nombre} {apellido}, Área: {area}, Número: {numero}"  # Formato "Nombre Apellido, Área: ..., Número: ..."
            lista_contactos.delete(seleccion[0])  # Eliminar el contacto actual
            lista_contactos.insert(seleccion[0], contacto_modificado)  # Insertar el contacto modificado en el mismo lugar
            entrada_nombre.delete(0, tk.END)
            entrada_apellido.delete(0, tk.END)
            entrada_area.delete(0, tk.END)
            entrada_numero.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un contacto para modificar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda de Contactos")
root.geometry("500x400")

# Frame para contener la lista de contactos y el scrollbar
frame_contactos = tk.Frame(root)
frame_contactos.pack(pady=10)

# Scrollbar para la lista de contactos
scrollbar = tk.Scrollbar(frame_contactos)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Lista de contactos (Listbox)
lista_contactos = tk.Listbox(frame_contactos, yscrollcommand=scrollbar.set, height=10, width=60)
lista_contactos.pack(side=tk.LEFT)
scrollbar.config(command=lista_contactos.yview)

# Frame para las entradas de datos (Nombre, Apellido, Área, Número)
frame_entradas = tk.Frame(root)
frame_entradas.pack(pady=10)

# Entrada de Nombre con su etiqueta
label_nombre = tk.Label(frame_entradas, text="Nombre")
label_nombre.grid(row=0, column=0, sticky=tk.W)
entrada_nombre = tk.Entry(frame_entradas, width=40)
entrada_nombre.grid(row=0, column=1)

# Entrada de Apellido con su etiqueta
label_apellido = tk.Label(frame_entradas, text="Apellido")
label_apellido.grid(row=1, column=0, sticky=tk.W)
entrada_apellido = tk.Entry(frame_entradas, width=40)
entrada_apellido.grid(row=1, column=1)

# Entrada de Área con su etiqueta
label_area = tk.Label(frame_entradas, text="Área")
label_area.grid(row=2, column=0, sticky=tk.W)
entrada_area = tk.Entry(frame_entradas, width=40)
entrada_area.grid(row=2, column=1)

# Entrada de Número con su etiqueta
label_numero = tk.Label(frame_entradas, text="Número")
label_numero.grid(row=3, column=0, sticky=tk.W)
entrada_numero = tk.Entry(frame_entradas, width=40)
entrada_numero.grid(row=3, column=1)

# Frame para contener los botones lado a lado
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para agregar contactos
boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_contacto)
boton_agregar.pack(side=tk.LEFT, padx=5)

# Botón para eliminar el contacto seleccionado
boton_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_contacto)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# Botón para seleccionar el contacto a modificar
boton_seleccionar = tk.Button(frame_botones, text="Seleccionar", command=seleccionar_contacto)
boton_seleccionar.pack(side=tk.LEFT, padx=5)

# Botón para modificar el contacto seleccionado
boton_modificar = tk.Button(frame_botones, text="Modificar", command=modificar_contacto)
boton_modificar.pack(side=tk.LEFT, padx=5)

# Iniciar el loop de la aplicación
root.mainloop()
