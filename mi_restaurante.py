from tkinter import *

from prompt_toolkit.key_binding.bindings.mouse import CONTROL

# INICIAR Y CONFIGURAR TKINTER
aplicacion = Tk()  # Crear la ventana principal de la aplicación

# Configurar el tamaño de la ventana (1020x630 píxeles) y su posición inicial (en la esquina superior izquierda)
aplicacion.geometry("1020x630+0+0")

# Evitar que la ventana sea redimensionable (ancho y alto fijos)
aplicacion.resizable(0, 0)

# Establecer el título de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# Establecer el color de fondo de la ventana principal
aplicacion.config(bg="azure4")

# PANELES
# Los paneles son contenedores que ayudan a organizar los widgets (elementos gráficos) dentro de la ventana.

# Panel superior (un contenedor sin bordes ni relleno)
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)  # Colocar el panel en la parte superior

# Etiqueta en el panel superior que muestra el título de la aplicación
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", fg="black",
                        font=("Dosis", 58), bg="gray", width=27)
etiqueta_titulo.grid(row=0, column=0)  # Ubicar la etiqueta en la primera fila y columna del panel

# Panel izquierdo (contendrá varios sub-paneles de productos)
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)  # Colocar el panel en la parte izquierda

# Panel para mostrar los costos (ubicado en la parte inferior del panel izquierdo)
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="gray", padx=50)
panel_costos.pack(side=BOTTOM)

# Panel para mostrar las opciones de comida
panel_comida = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, "bold"),
                           bd=1, relief=FLAT, fg="azure4")
panel_comida.pack(side=LEFT)

# Panel para mostrar las opciones de bebida
panel_bebida = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"),
                           bd=1, relief=FLAT, fg="azure4")
panel_bebida.pack(side=LEFT)

# Panel para mostrar las opciones de postre
panel_postre = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"),
                           bd=1, relief=FLAT, fg="azure4")
panel_postre.pack(side=LEFT)

# PANEL DERECHO
# Panel derecho donde se mostrarán la calculadora, el recibo y los botones
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel para la calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="gray")
panel_calculadora.pack()

# Panel para mostrar el recibo de la factura
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="gray")
panel_recibo.pack()

# Panel para los botones de acción (como calcular o generar la factura)
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg="gray")
panel_botones.pack()

# LISTAS DE PRODUCTOS
# Se definen las opciones disponibles en el sistema para comida, bebida y postre
lista_comida = ["Pollo", "Cordero", "Salmon", "Pizza", "Asado", "Pastas", "Papas"]
lista_bebida = ["Soda", "Jugo", "Coca", "Fanta", "Sprite", "Cerveza", "Vino"]
lista_postre = ["Chocolate", "Helado", "Fruta", "Tiramisu", "Flan", "Mousse", "Chocolinas"]

# GENERAR ITEMS DE COMIDA ---------------------------------------------------
variables_comida = []  # Lista para almacenar las variables de estado (IntVar) de los Checkbuttons
contador = 0  # Contador para posicionar los elementos en la grilla
cuadros_comida = []
texto_comida = []

# Recorrer la lista de comida para generar dinámicamente los elementos gráficos (Checkbuttons)
for comida in lista_comida:
    variables_comida.append("")  # Agregar un espacio vacío para reservar el lugar en la lista
    variables_comida[contador] = IntVar()  # Crear una variable que almacena el estado del Checkbutton (1 = marcado, 0 = desmarcado)

    # Crear un Checkbutton para cada comida
    comida = Checkbutton(
        panel_comida,  # Panel donde se agregará el Checkbutton
        text=comida.title(),  # Texto que muestra el nombre de la comida con la primera letra en mayúscula
        font=("Dosis", 19, "bold"),  # Estilo del texto (fuente, tamaño y peso)
        onvalue=1,  # Valor que tendrá la variable cuando el Checkbutton esté marcado
        offvalue=0,  # Valor que tendrá la variable cuando el Checkbutton esté desmarcado
        variable=variables_comida[contador]  # Asocia el estado del Checkbutton con la variable correspondiente
     )

    comida.grid(row=contador, column=0, sticky=W)  # Ubica el Checkbutton en la fila correspondiente, alineado a la izquierda (W)

    # Crear los cuadros e entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(panel_comida,
                                     font=("dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1  # Incrementar el contador para pasar al siguiente Checkbutton



# GENERAR ITEMS DE bebida ----------------------------------------------------
variables_bebida = []  # Lista para las variables de estado de las bebidas
contador = 0  # Reiniciar el contador
cuadros_bebida = []
texto_bebida = []

# Recorrer la lista de bebida para generar dinámicamente los elementos gráficos (Checkbuttons)
for bebida in lista_bebida:
    variables_bebida.append("")  # Agregar un espacio vacío para reservar el lugar en la lista
    variables_bebida[contador] = IntVar()  # Crear una variable que almacena el estado del Checkbutton (1 = marcado, 0 = desmarcado)

    # Crear un Checkbutton para cada bebida
    bebida = Checkbutton(
        panel_bebida,  # Panel donde se agregará el Checkbutton
        text=bebida.title(),  # Texto que muestra el nombre de la bebida con la primera letra en mayúscula
        font=("Dosis", 19, "bold"),  # Estilo del texto (fuente, tamaño y peso)
        onvalue=1,  # Valor que tendrá la variable cuando el Checkbutton esté marcado
        offvalue=0,  # Valor que tendrá la variable cuando el Checkbutton esté desmarcado
        variable=variables_bebida[contador]  # Asocia el estado del Checkbutton con la variable correspondiente
    )
    bebida.grid(row=contador, column=0, sticky=W)  # Ubica el Checkbutton en la fila correspondiente, alineado a la izquierda (W)                      column=1)  # Ubica el cuadro de texto en la columna 1, alineado a la izquierda

    # Crear los cuadros e entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebida,
                                     font=("dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1  # Incrementar el contador para pasar al siguiente Checkbutton



# GENERAR ITEMS DE postre ---------------------------------------------------------------
variables_postre = []  # Lista para las variables de estado de los postres
contador = 0  # Reiniciar el contador
cuadros_postre = []
texto_postre = []

# Recorrer la lista de postre para generar dinámicamente los elementos gráficos (Checkbuttons)
for postre in lista_postre:
    variables_postre.append("")  # Agregar un espacio vacío para reservar el lugar en la lista
    variables_postre[
        contador] = IntVar()  # Crear una variable que almacena el estado del Checkbutton (1 = marcado, 0 = desmarcado)

    # Crear un Checkbutton para cada postre
    postre = Checkbutton(
        panel_postre,  # Panel donde se agregará el Checkbutton
        text=postre.title(),  # Texto que muestra el nombre del postre con la primera letra en mayúscula
        font=("Dosis", 19, "bold"),  # Estilo del texto (fuente, tamaño y peso)
        onvalue=1,  # Valor que tendrá la variable cuando el Checkbutton esté marcado
        offvalue=0,  # Valor que tendrá la variable cuando el Checkbutton esté desmarcado
        variable=variables_postre[contador]  # Asocia el estado del Checkbutton con la variable correspondiente
    )
    postre.grid(row=contador, column=0,
                 sticky=W)  # Ubica el Checkbutton en la fila correspondiente, alineado a la izquierda (W)

    # Crear los cuadros e entrada
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")
    cuadros_postre[contador] = Entry(panel_postre,
                                     font=("dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)

    contador += 1  # Incrementar el contador para pasar al siguiente Checkbutton


var_costo_comida = StringVar()
# Etiquetas de costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text="Costos Comida",
                              font=("Dosis", 12, "bold"),
                              bg="gray",
                              fg="black")
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12,"bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)


var_costo_bebida = StringVar()
# Etiquetas de costos y campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costos bebida",
                              font=("Dosis", 12, "bold"),
                              bg="gray",
                              fg="black")
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12,"bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)


var_costo_postre = StringVar()
# Etiquetas de costos y campos de entrada
etiqueta_costo_postre = Label(panel_costos,
                              text="Costos postre",
                              font=("Dosis", 12, "bold"),
                              bg="gray",
                              fg="black")
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos,
                           font=("Dosis", 12,"bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)


# Etiquetas de subtotal
var_subtotal = StringVar()

etiqueta_subtotal = Label(panel_costos,
                              text="Subtotal",
                              font=("Dosis", 12, "bold"),
                              bg="gray",
                              fg="black")
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                           font=("Dosis", 12,"bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Etiquetas de subtotal
var_impuesto = StringVar()

etiqueta_impuesto = Label(panel_costos,
                              text="Impuestos",
                              font=("Dosis", 12, "bold"),
                              bg="gray",
                              fg="black")
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(panel_costos,
                           font=("Dosis", 12,"bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)


# Etiquetas de total
var_total = StringVar()

etiqueta_total = Label(panel_costos,
                              text="Total",
                              font=("Dosis", 12, "bold"),
                              bg="gray",
                              fg="black")
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,
                           font=("Dosis", 12,"bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)



# Botones

botones = ["total", "recibo", "guardar", "resetear"]
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 9, "bold"),
                   fg="gray",
                   bg="black",
                   bd=1,
                   width=8)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

# Area de recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)
# Evitar que la ventana se cierre inmediatamente
aplicacion.mainloop()