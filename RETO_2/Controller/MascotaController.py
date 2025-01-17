# from model.ClienteModelo import ClienteModelo
from model.MascotaModelo import MascotaModelo
# from model.CitasModelo import citasModelo
# from utils.Validaciones import validar_telefono,validar_fecha,validar_hora
# from datetime import datetime

class MascotaController:
    def registrar_mascota(self):
        print("\n--Registro de la mascota---")
        if not self.clientes:
            print("No hay clientes registrados")
            return
        nombre_cliente=input("ingrese el nombre del propietario :")
        cliente=next ((c for c in self.clientes if c.nombre==nombre_cliente),None)
        
        if cliente:
            nombre_mascota=input("Ingrese el nombre de la mascota:")
            especie=input("Ingrese la especie de la mascota(perro,gato,etc):")
            raza=input("Ingrese la raza de la mascota:")
            edad=input("Ingrese la edad de la mascota:")
            mascota=MascotaModelo(nombre_mascota,raza,especie,edad)
            cliente.agregar_mascota(mascota)
            print(f"Mascota{nombre_mascota} registrada para cliente {nombre_cliente} con exito ")
        else: 
            print("Cliente no encontrado")
