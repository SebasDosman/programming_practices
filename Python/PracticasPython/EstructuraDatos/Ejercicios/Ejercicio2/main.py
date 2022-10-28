from cola import Cola, arribo, atencion, barrido, tamano, barrido_eliminar
from mensaje import Mensaje
from menu import Menu

cola = Cola()

Menu.opcionesMenu()
opcion = int(input("Digite una opcion \n"))

while(opcion != 5):    
    if (opcion == 1):
        usuarioMensaje = input("Ingrese el mensaje \n")
        
        mensaje = Mensaje(usuarioMensaje)
        arribo(cola, mensaje)
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))
    elif (opcion == 2):
        print("Se desencoló: ", atencion(cola))
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))
    elif (opcion == 3):
        print("Se eliminará: ")
        barrido_eliminar(cola)
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))
    elif (opcion == 4):
        print("Mensajes: ")
        barrido(cola)
        print("Tamaño cola: ", tamano(cola))
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))
    else:
        print("Digite una opcion correspondiente")
        
        Menu.opcionesMenu()
        opcion = int(input("Digite una opcion \n"))

print("Gracias por usar el programa")