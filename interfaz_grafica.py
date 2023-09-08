# interfaz_grafica
# Se define la interfaz de usuario con etiquetas, cuadros de entrada y botones.
# Permite seleccionar rutas de origen y destino, así como codificaciones.
# Incluye una barra de progreso para mostrar el estado de la conversión.

# Importamos las bibliotecas y módulos necesarios.
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from funcionalidades import Funcionalidades
import os
import codecs

# Definimos la clase InterfazGrafica, que gestionará la interfaz de usuario.
class InterfazGrafica:
    def __init__(self):
        # Creamos una ventana principal de la interfaz gráfica.
        self.ventana = tk.Tk()
        self.ventana.title("Convertir Archivos de Texto")  # Establecemos el título de la ventana.

        # Obtenemos la ruta del directorio actual donde se encuentra el archivo interfaz_grafica.py.
        directorio_actual = os.path.dirname(os.path.abspath(__file__))

        # Definimos valores por defecto para las rutas de origen y destino.
        self.carpeta_origen_por_defecto = os.path.join(directorio_actual, "Carpeta_origen")
        self.carpeta_destino_por_defecto = os.path.join(directorio_actual, "Carpeta_destino")

        # Bandera para rastrear si las rutas se han modificado.
        self.rutas_modificadas = False

        # Creamos etiquetas, cuadros de entrada y menús desplegables para configurar las rutas y codificaciones.
        self.label_carpeta_origen = tk.Label(self.ventana, text="Carpeta de Origen:")
        self.label_carpeta_destino = tk.Label(self.ventana, text="Carpeta de Destino:")
        self.entry_carpeta_origen = tk.Entry(self.ventana)
        self.entry_carpeta_destino = tk.Entry(self.ventana)

        # Establecemos los valores iniciales en las entradas de ruta.
        self.entry_carpeta_origen.insert(0, self.carpeta_origen_por_defecto)
        self.entry_carpeta_destino.insert(0, self.carpeta_destino_por_defecto)

        self.label_codificacion_origen = tk.Label(self.ventana, text="Codificación Origen:")
        self.combobox_codificacion_origen = ttk.Combobox(self.ventana, values=["ANSI", "UTF-8"])
        self.combobox_codificacion_origen.set("ANSI")

        self.label_codificacion_destino = tk.Label(self.ventana, text="Codificación Destino:")
        self.combobox_codificacion_destino = ttk.Combobox(self.ventana, values=["ANSI", "UTF-8"])
        self.combobox_codificacion_destino.set("UTF-8")

        self.button_carpeta_origen = tk.Button(self.ventana, text="Abrir Carpeta Origen", command=self.abrir_carpeta_origen)
        self.button_carpeta_destino = tk.Button(self.ventana, text="Abrir Carpeta Destino", command=self.abrir_carpeta_destino)
        self.button_convertir = tk.Button(self.ventana, text="Convertir", command=self.convertir_archivos)

        # Creamos una etiqueta para mostrar el progreso.
        self.label_progreso = tk.Label(self.ventana, text="Progreso:")
        self.label_progreso.grid(row=5, column=0, padx=10, pady=5)

        # Creamos una barra de progreso.
        self.barra_progreso = ttk.Progressbar(self.ventana, length=200, mode="determinate")
        self.barra_progreso.grid(row=5, column=1, padx=10, pady=5)
        self.barra_progreso["value"] = 0  # Inicializamos la barra de progreso en 0.

        # Colocamos los elementos en la ventana utilizando la cuadrícula.
        self.label_carpeta_origen.grid(row=0, column=0, padx=10, pady=5)
        self.label_carpeta_destino.grid(row=1, column=0, padx=10, pady=5)
        self.entry_carpeta_origen.grid(row=0, column=1, padx=10, pady=5)
        self.entry_carpeta_destino.grid(row=1, column=1, padx=10, pady=5)
        self.label_codificacion_origen.grid(row=2, column=0, padx=10, pady=5)
        self.label_codificacion_destino.grid(row=3, column=0, padx=10, pady=5)
        self.combobox_codificacion_origen.grid(row=2, column=1, padx=10, pady=5)
        self.combobox_codificacion_destino.grid(row=3, column=1, padx=10, pady=5)
        self.button_carpeta_origen.grid(row=0, column=2, padx=10, pady=5)
        self.button_carpeta_destino.grid(row=1, column=2, padx=10, pady=5)
        self.button_convertir.grid(row=4, column=0, columnspan=3, pady=10)

    # Función para abrir la carpeta de origen y seleccionar una nueva ruta.
    def abrir_carpeta_origen(self):
        carpeta_origen = filedialog.askdirectory()
        if carpeta_origen:
            self.entry_carpeta_origen.delete(0, tk.END)
            self.entry_carpeta_origen.insert(0, carpeta_origen)
            self.rutas_modificadas = True

    # Función para abrir la carpeta de destino y seleccionar una nueva ruta.
    def abrir_carpeta_destino(self):
        carpeta_destino = filedialog.askdirectory()
        if carpeta_destino:
            self.entry_carpeta_destino.delete(0, tk.END)
            self.entry_carpeta_destino.insert(0, carpeta_destino)
            self.rutas_modificadas = True

    # Función para realizar la conversión de archivos según las configuraciones seleccionadas.
    def convertir_archivos(self):
        codificacion_origen = self.combobox_codificacion_origen.get()
        codificacion_destino = self.combobox_codificacion_destino.get()
        
        carpeta_origen = self.entry_carpeta_origen.get()
        carpeta_destino = self.entry_carpeta_destino.get()

        if not carpeta_origen:
            carpeta_origen = self.carpeta_origen_por_defecto
        if not carpeta_destino:
            carpeta_destino = self.carpeta_destino_por_defecto

        if not os.path.exists(carpeta_origen) or not os.path.exists(carpeta_destino):
            self.mostrar_mensaje_error("Ingrese rutas de origen y destino válidas.")
            return

        archivos_a_convertir = [f for f in os.listdir(carpeta_origen) if f.endswith('.txt')]
        errores = []

        # Configuramos la barra de progreso.
        self.barra_progreso["maximum"] = len(archivos_a_convertir)
        self.barra_progreso["value"] = 0  # Inicializamos la barra de progreso en 0.

        funcionalidades = Funcionalidades()

        for idx, archivo in enumerate(archivos_a_convertir, start=1):
            try:
                with codecs.open(os.path.join(carpeta_origen, archivo), 'r', 'ansi') as archivo_origen:
                    contenido = archivo_origen.read()

                with codecs.open(os.path.join(carpeta_destino, archivo), 'w', 'utf-8') as archivo_destino:
                    archivo_destino.write(contenido)
            except Exception as e:
                errores.append(f"Error al convertir {archivo}: {str(e)}")

            # Actualizamos la barra de progreso.
            self.barra_progreso["value"] = idx
            self.ventana.update()  # Actualizamos la ventana para mostrar el progreso.

        if errores:
            self.mostrar_mensaje_error("Se produjeron errores al convertir algunos archivos:\n\n" + "\n".join(errores))
        else:
            self.mostrar_mensaje_informacion("La conversión se completó exitosamente.")
        
        # Restauramos la barra de progreso después de la conversión.
        self.barra_progreso["value"] = 0

    # Función para mostrar un mensaje de error.
    def mostrar_mensaje_error(self, mensaje):
        tk.messagebox.showerror("Error", mensaje)

    # Función para mostrar un mensaje de información.
    def mostrar_mensaje_informacion(self, mensaje):
        tk.messagebox.showinfo("Información", mensaje)

    # Función para iniciar la aplicación y comenzar a escuchar eventos de la interfaz de usuario.
    def iniciar(self):
        self.ventana.mainloop()
