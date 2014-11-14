#	Universidad del Valle de Guatemala
#	Proyecto 1 algoritmos y estructuras de datos
#	Por:
#	Diego Juarez		13280
#	Daniel Mejia		13271
#	Esteban Barrera		13413

#importamos el control de los puertos Gpio de la raspberry
import RPi.GPIO as GPIO


# GPIO.BCM hace una referencia a los puertos GPIO por medio del numero
GPIO.setmode(GPIO.BCM)

# Configuramos el pin como una salida
GPIO.setup(10, GPIO.OUT)

# le enviamos al pin estableciso un valor
GPIO.output(10, False)


archivo=open("/home/pi/Desktop/BD.txt", "a")
#print "nombre del archivo: ", archivo.name
archivo.write('CREATE(User)-[:TURN_OFF{accion:['+'"APAGA"'+']}]->(Raspberry) \n')

archivo.close()

