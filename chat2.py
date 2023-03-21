import pywhatkit
# Usamos Un try-except
try: 

  # Enviamos el mensaje

  pywhatkit.sendwhatmsg("+543874 68-4617",  
                        "Mensaje De Prueba",
                        12,48) 

  print("Mensaje Enviado") 

  

except: 

  print("Ocurrio Un Error")