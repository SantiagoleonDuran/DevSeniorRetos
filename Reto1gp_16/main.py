from datetime import datetime

import statistics
import os.path 





class InvestigacionCientifica:
    # metodo constructor , init es para inicializar el metodo 
    def __init__(self,IdExperimento, nombreExperimento,fechaExperimento,tipoExperimento, resultados):
        self.IdExperimento = IdExperimento
        self.nombreExperimento=nombreExperimento
        self.fechaExperimento=fechaExperimento
        self.tipoExperimento=tipoExperimento
        self.resultados = resultados
        
    def to_dict(self):
        return ([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])

# funcion para agregar experimento 
def agregarExperimento(listaExperimentos, count):
    
    IdExperimento = count
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
        resultados = input('Ingrese los resultados separados por coma \n')
        resultados_separado = list(map(float, resultados.split(","))) 
    except Exception as ex:
        print('resultados ingresados no validos solo se permite valores numericos')
        
    investigacionAdd= InvestigacionCientifica(IdExperimento, nombreExperimento,fechaExperimento,tipoExperimento, resultados_separado)
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
    print(f"El promedio de los resultados es: {round(promedio,2)}  ")
    print(f"El maximo de los resultados es: {maximo}")
    print(f"El minimo de los resultados es: {minimo}")

def eliminarExperimento(ListaExperimentos, IdExperimento):
    ListaExperimentos.remove(IdExperimento)
    print('La eliminación se realizo con exito')
    visualizarExperimento(ListaExperimentos)
    

def compararExperimento():
    pass

def generarInforme(ListaExperimentos):
    nombreInforme = "informe_investigacion_cientifica.txt"
    path = os.path.abspath(nombreInforme)
    if not ListaExperimentos:
        print("NO hay experimentos registrados")
        return
    
    with open(path, "w") as informe:
        for experimento in ListaExperimentos:
            informe.write(f"\nNombre experimento:  {experimento.nombreExperimento}\n")
            informe.write(f"Fecha Experimento: {experimento.fechaExperimento}\n")
            informe.write(f"Tipo Experimento: {experimento.tipoExperimento}\n")
            informe.write("Resultados: " + ", ".join(map(str, experimento.resultados)) + "\n")
            informe.write("\n")
    
    print("Informe generado como informe_investigacion_cientifica.txt")


def validar_seleccion_menu(dato_entrada):
    try:
        return int(dato_entrada)
    except Exception as ex:
        return False
        
    
def menuInvestigacionCientifica():
    ListaExperimentos=[]
    count = 0
    ListaExperimentos=[]
    
    # file name    
    file_name = 'GFG.txt'
  
  
    # prints the absolute path of current 
    # working directory with  file name 
    print(os.path.abspath(file_name))
    while True:
        print('\n ===============Bienvenido al sistema de Investigación cientifica=============== ')
        print('====Selecciona la opción que desea realizar====')
        print('\n')
        print('1) Agregar experimento ')
        print('2) Visualizar experimento ')
        print('3) Eliminar experimento ')
        print('4) Generar informe ')
        print('5) Promedio experimento ')
        print('6) Salir (exit)')
        opcionSeleccionada = input('****Seleccione Opción**** \n')
        if validar_seleccion_menu(opcionSeleccionada):
            if int(opcionSeleccionada) == 1:
                agregarExperimento(ListaExperimentos, count+1)
            if int(opcionSeleccionada) == 2:
                visualizarExperimento(ListaExperimentos)
            if int(opcionSeleccionada) == 3:
                while True:
                    IdExperimento = input('Ingrese el Id del experimento que desea eliminar')
                    if validar_seleccion_menu(IdExperimento):
                        eliminarExperimento(ListaExperimentos, IdExperimento)
                        break
                    else:
                        print('El Id ingresado no es valido')
            if int(opcionSeleccionada) == 4:
                generarInforme(ListaExperimentos)
            if  int(opcionSeleccionada) == 5:
               analizarpromedio(ListaExperimentos)
            if opcionSeleccionada == 6:
                break
        else:
            print('Seleccione una opción valida')
    
if __name__ == '__main__': 

  menuInvestigacionCientifica()









    
        

       

    