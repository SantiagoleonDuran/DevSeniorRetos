from .PersonaModelo import PersonaModelo

class Cliente(PersonaModelo):   

    def __init__(self,nombre,telefono,direccion):
        super().__init__(nombre,telefono,direccion)
        self.mascotas=[]

    def agregar_mascota(self,mascotaModelo):
        self.mascotas.append(mascotaModelo)

    def mostrar_info(self):
        print(f"Nombre: {self._nombre} \nTelefono: {self._telefono} \nDireccion: {self._direccion}")
