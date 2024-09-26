#prograama de prueba
nombre = input("Por favor, introduce tu nombre:")
apellido1= input("Introduce tu primer apellido: ")
apellido2= input("introduce tu segundo apellido: ")
edad= input("introduce tu edad: ")
edad = int((edad))


print("tus datos son:")
print(nombre)
print(apellido1)
print(apellido2)
print(edad)

lista = [nombre, apellido1, apellido2, edad]
print(lista)

confirma = input("Son correctos Y/N: ")


if edad < 18:
            print("No puedes acceder al evento solo. Tienes menos de 18 años.")
            nombrepadre=input("Por favor, introduce el nombre de tu padre: ")
            tfnopadre=input("introduce el teléfono de tu padre: ")
            print("Muchas gracias, en breve recibirá una llamada de teléfono para autorizar la entrada.")

else:
            print("Puedes entrar, tienes más de 18 años.")
            reserva=input("Ahora por favor, introduce el número de reserva que hemos enviado: ")
            a,b,c,d,e = reserva
            print(d)
         












