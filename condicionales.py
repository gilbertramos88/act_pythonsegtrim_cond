#ejercicio condicionales
print("programa de consulta del clima segun su latitud en el planeta tierra")

zona=float(input("ingrese la latitud de la zona a consultar: "))

def latitud(zona):
    if zona<= -0.1:
      
     return zona * -1
     
    else:
    
      return zona    
     

resultado = latitud(zona)


if resultado <= 20:
   
         print("clima caliente")
elif resultado<=30:
         print("clima calido")
elif resultado <=60:
         print("clima templado")
elif resultado <=75:
         print("clima frio")  
elif resultado <= 90:
         print ("clima polar")  
else:
         print("latitud inexacta, el planeta tierra tiene hasta 90°de latitud") 
print("ingrese el siguente...")  

         

