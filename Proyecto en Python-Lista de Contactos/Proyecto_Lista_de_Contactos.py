# Proyecto Final del Curso de Python.
#** Nombre del Proyecto: Sitema de contactos

# Docente: Juan David Velandia
# Nombre: Marcos Soto Zapata
# Fecha: 10 de Octubre de 2025


# Problema: 
# 1- Crear un sistema que permita Registrar los siguientes datos de los usuarios: Nombre, Teléfono, Categoría. 
# 2- El sistema debe poder ser capaz de realizar las siguientes funciones: Crear usuuarios, Modificar contactos, Mostrar Lista de contactos,
# Buscar contactos y Eliminar contactos.
# 3- Opncional: El sistema debe contar con una opción salir para cerrar el funcionamiento de la aplicación.


from ast import Expression
import os

CARPETA = 'contactos/'  # Carpeta de Contactos
EXTENSION = '.txt'      # Extensión de archivos

# Contactos
class Contacto:  
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre       # Atributos
        self.telefono = telefono   # Atributos
        self.categoria = categoria # Atributos


def app():
    # Revisa si la carpeta existe o no
    crear_directorio()

    # Mostrar el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: (1-6) \r\n')
        opcion = int(opcion)

        # Ejecutar la acción según la opción seleccionada
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            salir_contacto()
            preguntar = False


# Mostrar Menú del panel de opciones
def mostrar_menu():   # Definimos la cantidad de opciones que tendrá el Menú
    print("Seleccione una opción del Menú:")
    print("1. Crear Contacto")
    print("2. Editar Contacto")
    print("3. Ver Contacto")
    print("4. Buscar Contacto")
    print("5. Eliminar Contacto")
    print("6. Salir")


# Crear contacto
def agregar_contacto():  # Defeinimos la función crear contacto
    print("Escribe los datos para crear el nuevo contacto") # Aquí puedes agregar la lógica para crear un contacto
    nombre_contacto = input('Nombre del Contacto: \r\n')    # Escribir el nombre del contacto a registrar

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Resto de datos
            telefono_contacto = input('Agregar Teléfono: \r\n')
            categoria_contacto = input('Categoria Contacto: \r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')     # Aquí puedes agregar la lógica para guardar los datos del contacto
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n') 
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            # Mostrar un mensaje de éxito
            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('\r\nEse Contacto ya existe \r\n')

    # Reiniciar la app
    app()


# Validar si un contacto ya existe o no
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


# Modificar contactos
def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    # Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de los datos
            nombre_contacto = input('Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input('Agregar el Nuevo Teléfono: \r\n')
            categoria_contacto = input('Agrega la Nueva Categoria: \r\n')

            # Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        # Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        # Mostrar mensaje de éxito
        print('\r\n Contacto editado Correctamente \r\n')
    else:
        print('Ese contacto no existe')

    # Reiniciar la aplicación
    app()


# Mostrar Lista de Contactos
def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:

                # Imprime el contenido
                print(linea.rstrip())
            
            # Imprime un separador entre contactos
            print('\r\n')

    if len(archivos_txt) == 0:
        print("No hay contactos registrados.")


# Buscar contactos dentro de una lista
def buscar_contacto(): 
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')

    # Creamos una excepción
    try: 
        with open(CARPETA + nombre + EXTENSION) as contacto: # Try intenta abrir este archivo
            print('\r\n Información del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())    
            print('\r\n')               # Salto de línea
    except IOError: # Si por ABC el archivo no existe, automaticamente se pasa a esta línea
        print('El archivo no existe')
        print(IOError)

    # Reiniciar la app para que siga funcionando, trar ejecutar nuestra opción
    app()


# Eliminar contactos
def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Eliminado Correctamente')
    except Expression as identifier:
        print('No existe ese contacto')
    
    # Reiniciar app
    app()


# Función para salir del programa
def salir_contacto():
    print("Saliendo del sistema. ¡Hasta luego!")
    exit()


# Crear directorio o carpeta donde se almacenarán nuestros archivos
def crear_directorio():
    if not os.path.exists('contactos/'):
        # Crear la carpeta si no existe
        os.makedirs('contactos/')
    #else:
        #print("La carpeta 'contactos/' ya existe.")

# Fin de la aplicación
app()


# Academia Udemy, Curso: Programación con Python de Principiante hasta Avanzado, Docente: Juan Pablo De la Torre Valdez.

