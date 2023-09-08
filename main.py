#main.py
# Importamos las clases y módulos necesarios.
from interfaz_grafica import InterfazGrafica  # Importamos la clase InterfazGrafica desde el archivo interfaz_grafica.py
from funcionalidades import Funcionalidades  # Importamos la clase Funcionalidades desde el archivo funcionalidades.py

# Verificamos si este archivo se está ejecutando como el programa principal.
# Esto asegura que el código dentro de este bloque solo se ejecute cuando se ejecuta main.py directamente,
# no cuando se importa como un módulo en otro archivo.
if __name__ == "__main__":
    # Creamos una instancia de la clase InterfazGrafica, que controla la interfaz de usuario.
    app = InterfazGrafica()

    # Creamos una instancia de la clase Funcionalidades, que contiene las funciones para realizar la conversión de codificación.
    funcionalidades = Funcionalidades()

    # Asociamos la función 'convertir_archivos' de la instancia de InterfazGrafica al botón de la interfaz gráfica.
    app.button_convertir.config(command=app.convertir_archivos)

    # Iniciamos la aplicación, que comienza a escuchar eventos de la interfaz de usuario.
    app.iniciar()
