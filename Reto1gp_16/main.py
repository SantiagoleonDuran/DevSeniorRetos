from datetime import datetime
import statistics 


class InvestigacionCientifica:
    # metodo constructor , init es para inicializar el metodo 
    def __init__(self,nombreExperimento,fechaExperimento,tipoExperimento, resultados):
        self.nombreExperimento=nombreExperimento
        self.fechaExperimento=fechaExperimento
        self.tipoExperimento=tipoExperimento
        self.resultados = resultados
        
    def to_dict(self):
        return ([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])

# funcion para agregar experimento 
def agregarExperimento(listaExperimentos):
    
    print('\n===============  Agregar Experimentos  ===============\n')
    nombreExperimento=input("\nIngrese el nombre del experimento: ")
    fechaExperimento_str=input("\ningrese la fecha del experimento  (DD/MM/AAAA):")
    try:
        fechaExperimento=datetime.strptime(fechaExperimento_str,"%d/%m/%Y")
    except Exception as ex:
        print(f"fecha invalida :{ex}")
        return
    
    while True:
        tipoDeExperimento=input("\nIngrese el tipo de experimento \n 1) fisica, \n 2) biologia, \n 3) quimica: \n")
        if (tipoDeExperimento.lower() == 'fisica') or tipoDeExperimento.lower() == 'biologia' or tipoDeExperimento.lower() == 'quimica':
            tipoExperimento = tipoDeExperimento
            break
        else:
            print('Debe seleccionar el tipo de experimento valido')
        
    try:
        resultados = input('Ingrese los resultados separados por coma')
        resultados_separado = list(map(float, resultados.split(","))) 
    except Exception as ex:
        print('resultados ingresados no validos solo se permite valores numericos')
        
    investigacionAdd= InvestigacionCientifica(nombreExperimento,fechaExperimento,tipoExperimento, resultados_separado)
    listaExperimentos.append(investigacionAdd)
    print("Experimento agregado exitosamente")
    
def visualizarExperimento(ListaExperimentos):
    if len(ListaExperimentos) <=0:
        print("NO hay experimentos registrados")
        return
        
    for item in ListaExperimentos:
         
        print(f"\nNombre experimento:  {item.nombreExperimento}")
        print(f"\nFecha Experimento: {item.fechaExperimento}")
        print(f"\nTipo Experimento: {item.tipoExperimento}")
        
def analizarpromedio(ListaExperimentos):
    if not ListaExperimentos:
        print("NO hay experimentos registrados")
        return
    for experimento in ListaExperimentos:
          promedio = statistics.mean(experimento.resultados)
    maximo=max(experimento.resultados)
    minimo=min(experimento.resultados)
    print(f"El promedio de los resultados es: {promedio}")
    print(f"El maximo de los resultados es: {maximo}")
    print(f"El minimo de los resultados es: {minimo}")






    


def eliminarExperimento():
    pass



def compararExperimento():
    pass

def generarInforme():
    pass

def validar_seleccion_menu(dato_entrada):
    try:
        return int(dato_entrada)
    except Exception as ex:
        return False
        
    
def menuInvestigacionCientifica():
    ListaExperimentos=[]
    while True:
        print('\n ===============Bienvenido al sistema de Investigación cientifica=============== ')
        print('====Selecciona la opción que desea realizar====')
        print('\n')
        print('1) Agregar experimento ')
        print('2) Visualizar experimento ')
        print('3) eliminar experimento ')
        print('4) Generar informe ')
        print('5) Salir (exit)')
        opcionSeleccionada = input('****Seleccione Opción**** \n')
        if validar_seleccion_menu(opcionSeleccionada):
            if int(opcionSeleccionada) == 1:
                agregarExperimento(ListaExperimentos)
            if int(opcionSeleccionada) == 2:
                visualizarExperimento(ListaExperimentos)
            if opcionSeleccionada == 7:
                break
        else:
            print('Seleccione una opción valida')
    
if __name__ == '__main__': 
    menuInvestigacionCientifica()








    
        

       

    