#calor menor a 983
#frio aumenta mas de 983
import serial
import time
import base64
from Examples.EchoClient import WhatsappEchoClient             #Importa la Clace WhatsappEchoClient, dedicada a envio de mensajes.
arduino = serial.Serial('/dev/ttyACM0',9600,timeout=5);
time.sleep(1)
print "Iniciando"
cont =1
arduino.flush()
Aseguradora =0
Antes = 0
while 1:
	
	if(cont==1):
		dato_recibido=arduino.readline()
		time.sleep(1)
		convert = int (dato_recibido)
		if convert == 1:
			mensaje = "Precaucion la Temperatura se incremento rapidamente !!!"
			if Aseguradora == 0 and Antes==0:
				archivo=open("/home/pi/Desktop/BD.txt", "a")
				#print "nombre del archivo: ", archivo.name
				archivo.write('CREATE (Raspberry)-[:SEND_MESAGE_TO{accion:['+'"la temperatura se incremento"'+']}]->(User) \n')
				archivo.close()
				print "la temperatura se incremento"

				#................Clave de Acceso a WhatsApp............................
				#password = "YtuJcYLQqNvzF++9lRqeq5IV5A8="                      #Password dada al registrar el numero.
				#password = base64.b64decode(bytes(password.encode('utf-8')))   #Codificacion de Password para envio a los servidores de whatsApp.
				#username = '50251189264'                                     #Numero de telefono para el inicio de secion.
				#keepAlive= False                                               #Conexion persistente con el servidor.
				#......................................................................
				#whats = WhatsappEchoClient("50258344904", mensaje, keepAlive)     #Inicia el cliente para el envio de mensajes por WhatsApp.
				#whats.login(username, password)	
				Antes = 0
				Aseguradora=1
			
		if convert == 2:
			mensaje = "La Temperatura decendio rapidamente es recomendable usar SWeter"
			
			if Aseguradora == 1 and Antes == 0:
				archivo=open("/home/pi/Desktop/BD.txt", "a")
				#print "nombre del archivo: ", archivo.name
				archivo.write('CREATE (Raspberry)-[:SEND_MESAGE_TO{accion:['+'"la temperatura decendio"'+']}]->(User) \n')
				archivo.close()
				print "la temperatura se redujo"
				#................Clave de Acceso a WhatsApp............................
				#password = "YtuJcYLQqNvzF++9lRqeq5IV5A8="                      #Password dada al registrar el numero.
				#password = base64.b64decode(bytes(password.encode('utf-8')))   #Codificacion de Password para envio a los servidores de whatsApp.
				#username = '50251189264'                                     #Numero de telefono para el inicio de secion.
				#keepAlive= False                                               #Conexion persistente con el servidor.
				#......................................................................
				#whats = WhatsappEchoClient("50258344904", mensaje, keepAlive)     #Inicia el cliente para el envio de mensajes por WhatsApp.
				#whats.login(username, password)	
				Aseguradora=0

		cont = 1
	time.sleep(1)
	if(cont==2):
		var=str("Enviando")
		arduino.write(var)
		time.sleep(2)
		
	

