# interfaz_grafica
# Se define la interfaz de usuario con etiquetas, cuadros de entrada y botones.
# Permite seleccionar rutas de origen y destino, así como codificaciones.
# Incluye una barra de progreso para mostrar el estado de la conversión.

# Importamos las bibliotecas y módulos necesarios.
import tkinter as tk  # Importamos la biblioteca tkinter para crear la interfaz gráfica.
from tkinter import filedialog, ttk, messagebox  # Importamos filedialog para abrir cuadros de diálogo de selección de directorio, ttk para widgets mejorados y messagebox para mensajes de diálogo.
from funcionalidades import Funcionalidades  # Importamos la clase Funcionalidades desde el archivo funcionalidades.py
import os  # Importamos el módulo os para trabajar con rutas y directorios.
import codecs  # Importamos la biblioteca codecs para manejar diferentes codificaciones de archivos de texto.

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
        self.combobox_codificacion_origen = ttk.Combobox(self.ventana, values=["ANSI", "UTF-8"], state="readonly")
        self.combobox_codificacion_origen.set("ANSI")

        self.label_codificacion_destino = tk.Label(self.ventana, text="Codificación Destino:")
        self.combobox_codificacion_destino = ttk.Combobox(self.ventana, values=["ANSI", "UTF-8"], state="readonly")
        self.combobox_codificacion_destino.set("UTF-8")

        self.button_carpeta_origen = tk.Button(self.ventana, text="Abrir Carpeta Origen", command=self.abrir_carpeta_origen)
        self.button_carpeta_destino = tk.Button(self.ventana, text="Abrir Carpeta Destino", command=self.abrir_carpeta_destino)
        self.button_convertir = tk.Button(self.ventana, text="Convertir", command=self.convertir_archivos)

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

        # Creamos una etiqueta para la lista de archivos procesados con éxito.
        self.label_exitosos = tk.Label(self.ventana, text="Archivos Procesados con Éxito:")
        self.label_exitosos.grid(row=6, column=0, padx=10, pady=5)

        # Creamos una Listbox para mostrar los archivos procesados con éxito.
        self.lista_exitosos = tk.Listbox(self.ventana, width=40, height=10)
        self.lista_exitosos.grid(row=7, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")  # Usamos "sticky" para centrar en todas las direcciones.

        # Creamos una barra de desplazamiento para la Listbox.
        scrollbar = ttk.Scrollbar(self.ventana, orient="vertical", command=self.lista_exitosos.yview)
        scrollbar.grid(row=7, column=3, sticky="ns")
        self.lista_exitosos.config(yscrollcommand=scrollbar.set)

        # Creamos una barra de progreso para mostrar el progreso de la conversión.
        self.barra_progreso = ttk.Progressbar(self.ventana, length=300)
        self.barra_progreso.grid(row=5, column=0, columnspan=3, pady=10)

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

        # Si las entradas están vacías, utilizamos las rutas por defecto.
        if not carpeta_origen:
            carpeta_origen = self.carpeta_origen_por_defecto
        if not carpeta_destino:
            carpeta_destino = self.carpeta_destino_por_defecto

        # Verificamos si las rutas de origen y destino existen.
        if not os.path.exists(carpeta_origen) or not os.path.exists(carpeta_destino):
            self.mostrar_mensaje_error("Ingrese rutas de origen y destino válidas.")
            return

        # Realizamos la conversión según la codificación seleccionada.
        if codificacion_origen == codificacion_destino:
            self.mostrar_mensaje_informacion("Mismo formato detectado. No se realizará la conversión.")
            return

        funcionalidades = Funcionalidades()

        # Obtenemos la lista de archivos a convertir en la carpeta de origen con extensión .txt.
        archivos_a_convertir = [f for f in os.listdir(carpeta_origen) if f.endswith('.txt')]
        errores = []  # Creamos una lista para rastrear errores durante la conversión.
        archivos_exitosos = []  # Creamos una lista para rastrear archivos procesados con éxito.

        # Agregamos el mensaje de inicio a la Listbox.
        self.lista_exitosos.insert(tk.END, "====== Iniciando conversión ======")

        # Configuramos el máximo valor de la barra de progreso.
        self.barra_progreso["maximum"] = len(archivos_a_convertir)

        # Recorremos la lista de archivos a convertir.
        for archivo in archivos_a_convertir:
            try:
                # Abrimos el archivo de origen con la codificación seleccionada.
                with codecs.open(os.path.join(carpeta_origen, archivo), 'r', codificacion_origen) as archivo_origen:
                    contenido = archivo_origen.read()  # Leemos el contenido del archivo de origen.
                
                # Creamos un nuevo archivo en la carpeta de destino con la codificación seleccionada y escribimos el contenido convertido.
                with codecs.open(os.path.join(carpeta_destino, archivo), 'w', codificacion_destino) as archivo_destino:
                    archivo_destino.write(contenido)  # Escribimos el contenido convertido en el nuevo archivo.

                archivos_exitosos.append(archivo)  # Agregamos el archivo a la lista de exitosos.

            except Exception as e:
                errores.append(f"Error al convertir {archivo}: {str(e)}")  # Capturamos y registramos errores.

            # Actualizamos el valor de la barra de progreso.
            self.barra_progreso["value"] += 1
            self.ventana.update_idletasks()  # Actualizamos la ventana para reflejar el progreso.

        # Si se producen errores, mostramos un mensaje de error con detalles.
        if errores:
            self.mostrar_mensaje_error("Se produjeron errores al convertir algunos archivos:\n\n" + "\n".join(errores))

        # Mostramos un mensaje de éxito si no hay errores y al menos un archivo fue procesado con éxito.
        elif archivos_exitosos:
            self.mostrar_mensaje_informacion("La conversión se completó exitosamente.")

        # Agregamos los archivos procesados con éxito a la Listbox.
        for archivo_exitoso in archivos_exitosos:
            self.lista_exitosos.insert(tk.END, archivo_exitoso)
        
        # Agregamos el mensaje de fin a la Listbox.
        self.lista_exitosos.insert(tk.END, "====== Proceso terminado ========")

    # Función para mostrar un mensaje de error.
    def mostrar_mensaje_error(self, mensaje):
        tk.messagebox.showerror("Error", mensaje)

    # Función para mostrar un mensaje de información.
    def mostrar_mensaje_informacion(self, mensaje):
        tk.messagebox.showinfo("Información", mensaje)

    # Función para iniciar la aplicación y comenzar a escuchar eventos de la interfaz de usuario.
    def iniciar(self):
        self.ventana.mainloop()
