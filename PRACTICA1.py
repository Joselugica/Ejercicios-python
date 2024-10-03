# practica python #
# uso de prints, inputs , conversor numérico, str,  #

print ("Por favor, introduce los siguientes datos: ")
nombre=input ("Introduce tu nombre: ")
apellido1=input ("Introduce tu primer apelido: ")
apellido2=input (" introduce tu segundo apellido: ")
edad=input ("Introduce tu edad: ")
edad=int(edad)

if edad > 18:
    print("Perfecto, eres mayor de edad.")

    promo=input("¿ Quieres acceder a la promo: Y/N ? ")
    promo1= "Y"

    if promo == promo1:
        print ("perfecto. Recuerda tener a mano el código promocional")
        print ("")
        codigo = input("introduce el código de 8 CIFRAS dela promoción sin espacios:")
        a,b,c,d,e,f,g,h = codigo
        if c == "d":
              if e == "g":
                    print ("HAS GANADO !!!")


              else:
                    print (" el código no es correcto")
        else:
              print ("Lo sentimos " + nombre + ", pero el código no ha sido premiado.")
           


        print( "Sigue participando en la promo. Tienes hasta final de mes")

    else:
          print ("Hasta luego. Nos vemos pronto")

else:
    print("Eres menor de edad. Lo sentimos, pero deberás consultar con un adulto")
    valor=input("¿ Quieres seguir con el proceso Y/N ?")
    valor=str(valor)
    valor1= "Y"

    if valor == valor1:
            print ("De acuerdo")

    else: 
            print ("Adiós. Nos vemos pronto")




