saldo = int(input("ingresar un saldo: "))

opcion ="0"


while opcion != "3":
        
    print("cajero automatico")
    print ("1. depositar dinero")
    print (" 2. retirar dinero")
    print ("3. salir")
    opcion = input("escoger: ")
    
    if opcion == "1":
        deposito = int(input("¿cuanto dinero quieres depositar?"))
        saldo = saldo + deposito
        print("saldo actual:", saldo)
    elif opcion == "2":
        retiro = int(input("¿cuanto dinero deseas retirar"))
        saldo = saldo - retiro
        print("saldo actual:",saldo)
    elif opcion == "3":
        salir  = int(input(" gracias por usar el cajero"))
    
    elif retiro > saldo:
        print("saldo insuficiente")
    
    else:
        print("opcion no valida")
        
    
        

