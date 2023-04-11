diccionario={
    "usuarios":{
        "miltonbadillo@gmail.com":{
            "nombre":"Milton",
            "apellido":"Badillo",
            "edad ":30,
            "antiguedad":5,
            "subscripicon":True
        }
    }
}
contador=1
while contador==1:
    user_options=int(input("Selecione una opción:\nagregar usuario (1)\neditar usuario (2)\neliminar usuario(3)\nsalir (4)\n"))
    if user_options==1:
        usuario=str(input("ingrese email de usuario: "))
        nombre=str(input("ingrese nombre: "))
        apellido=str(input("ingrese apellido: "))
        edad=int(input("ingrese edad: "))
        antiguedad=int(0)
        pregunta_subcripcion=str(input("¿El usuario pago la subscripcion? (Y/N) "))
        if pregunta_subcripcion=="Y":
            subscripcion=True
        subscripcion=False
        #revisar
        print(diccionario)
    elif user_options==2:
        usuario=str(input("Ingrese el correo del usuario: "))
        if usuario in diccionario["usuarios"]:
            print("Usuario encontrado...")
            diccionario["usuarios"][usuario]["nombre"]=str(input("ingrese nombre: "))
            diccionario["usuarios"][usuario]["apellido"]=str(input("ingrese apellido: "))
            diccionario["usuarios"][usuario]["edad"]=int(input("ingrese edad: "))
            diccionario["usuarios"][usuario]["antiguedad"]=int(input("Ingese antiguedad: "))
            pregunta_subcripcion=str(input("¿El usuario pago la subscripcion? (Y/N)"))
            if pregunta_subcripcion=="Y":
                diccionario["usuarios"][usuario]["subscripcion"]=True
            diccionario["usuarios"][usuario]["subscripcion"]=False
            #revisar
            print(diccionario)
        else:
            print("No se encontro al usuario")
    elif user_options==3:
        usuario=str(input("Ingrese el correo del usuario: "))
        if usuario in diccionario["usuarios"]:
            del diccionario["usuarios"][usuario]
            print("Usuario borrado...")
        else:
            print("No se encontro al usuario")
    elif user_options==4:
        print("saliendo...")
        contador=2
    else:
        print("Opcion invalida")
