from model.ClienteModelo import ClienteModelo
from model.MascotaModelo import MascotaModelo
from model.CitasModelo import citasModelo
from utils.Validaciones import validar_telefono,validar_fecha,validar_hora
from datetime import datetime




class ClienteController: 

 def __init__(self):
        self.clientes = []
    
def registrar_cliente(self):
        print("\n--Registro del cliente---")
        nombre= input("Ingrese el nombre del cliente:")
        telefono=input("Ingrese el telefono del cliente:")
        while not validar_telefono(telefono):
            print("Telefono no valido. Intente nuevamente")
            telefono=input("Ingrese el telefono del cliente:")
        direccion=input("Ingrese la direccion del cliente:")
        cliente=ClienteModelo(nombre,telefono,direccion)
        self.clientes.append(cliente)
        print(f"\nCliente {nombre} registrado con exito ")
