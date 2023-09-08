#funcionalidades.py
# Importamos los módulos y bibliotecas necesarios.
import os  # Importamos el módulo os para trabajar con rutas y directorios.
import codecs  # Importamos la biblioteca codecs para manejar diferentes codificaciones de archivos de texto.
from tkinter import messagebox  # Importamos el módulo messagebox de tkinter para mostrar mensajes de diálogo.

# Definimos la clase Funcionalidades, que contiene métodos para realizar la conversión de codificación de archivos.
class Funcionalidades:
    def __init__(self):
        pass  # El constructor de la clase no realiza ninguna acción específica.

    # Función para convertir archivos a UTF-8 en la carpeta de origen a la carpeta de destino.
    def convertir_a_utf8(self, carpeta_origen, carpeta_destino):
        # Obtenemos la lista de archivos a convertir en la carpeta de origen con extensión .txt.
        archivos_a_convertir = [f for f in os.listdir(carpeta_origen) if f.endswith('.txt')]
        errores = []  # Creamos una lista para rastrear errores durante la conversión.

        # Recorremos la lista de archivos a convertir.
        for archivo in archivos_a_convertir:
            try:
                # Abrimos el archivo de origen con codificación ANSI.
                with codecs.open(os.path.join(carpeta_origen, archivo), 'r', 'ansi') as archivo_origen:
                    contenido = archivo_origen.read()  # Leemos el contenido del archivo de origen.

                # Creamos un nuevo archivo en la carpeta de destino con codificación UTF-8 y escribimos el contenido convertido.
                with codecs.open(os.path.join(carpeta_destino, archivo), 'w', 'utf-8') as archivo_destino:
                    archivo_destino.write(contenido)  # Escribimos el contenido convertido en el nuevo archivo.
            except Exception as e:
                errores.append(f"Error al convertir {archivo}: {str(e)}")  # Capturamos y registramos errores.

        # Si se producen errores, mostramos un mensaje de error con detalles.
        if errores:
            self.mostrar_mensaje_error("Se produjeron errores al convertir algunos archivos:\n\n" + "\n".join(errores))
        else:
            self.mostrar_mensaje_informacion("La conversión a UTF-8 se completó exitosamente.")  # Mostramos un mensaje de éxito si no hay errores.

    # Función para convertir archivos a ANSI en la carpeta de origen a la carpeta de destino.
    def convertir_a_ansi(self, carpeta_origen, carpeta_destino):
        # Obtenemos la lista de archivos a convertir en la carpeta de origen con extensión .txt.
        archivos_a_convertir = [f for f in os.listdir(carpeta_origen) if f.endswith('.txt')]
        errores = []  # Creamos una lista para rastrear errores durante la conversión.

        # Recorremos la lista de archivos a convertir.
        for archivo in archivos_a_convertir:
            try:
                # Abrimos el archivo de origen con codificación UTF-8.
                with codecs.open(os.path.join(carpeta_origen, archivo), 'r', 'utf-8') as archivo_origen:
                    contenido = archivo_origen.read()  # Leemos el contenido del archivo de origen.

                # Creamos un nuevo archivo en la carpeta de destino con codificación ANSI y escribimos el contenido convertido.
                with codecs.open(os.path.join(carpeta_destino, archivo), 'w', 'ansi') as archivo_destino:
                    archivo_destino.write(contenido)  # Escribimos el contenido convertido en el nuevo archivo.
            except Exception as e:
                errores.append(f"Error al convertir {archivo}: {str(e)}")  # Capturamos y registramos errores.

        # Si se producen errores, mostramos un mensaje de error con detalles.
        if errores:
            self.mostrar_mensaje_error("Se produjeron errores al convertir algunos archivos:\n\n" + "\n".join(errores))
        else:
            self.mostrar_mensaje_informacion("La conversión a ANSI se completó exitosamente.")  # Mostramos un mensaje de éxito si no hay errores.

    # Función para mostrar un mensaje de confirmación con la lista de archivos a convertir.
    def mostrar_confirmacion(self, mensaje, archivos):
        return messagebox.askyesno("Confirmar Conversión", f"{mensaje}\n\nArchivos a convertir:\n{', '.join(archivos)}")

    # Función para mostrar un mensaje de error.
    def mostrar_mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    # Función para mostrar un mensaje de información.
    def mostrar_mensaje_informacion(self, mensaje):
        messagebox.showinfo("Información", mensaje)
