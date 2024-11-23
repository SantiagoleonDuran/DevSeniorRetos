# Proyecto de Investigación Científica
from datetime import datetime

import statistics
import os 





## Estructura del Código

### Clase `InvestigacionCientifica`
class InvestigacionCientifica:
    # metodo constructor , init es para inicializar el metodo 
    def __init__(self,IdExperimento, nombreExperimento,fechaExperimento,tipoExperimento, resultados,analizarPromedio):
        self.IdExperimento = IdExperimento
        self.nombreExperimento=nombreExperimento
        self.fechaExperimento=fechaExperimento
        self.tipoExperimento=tipoExperimento
        self.resultados = resultados
        self.analizarPromedio=analizarPromedio
       # Método para convertir las propiedades del experimento en un diccionario  
    def to_dict(self):
        return ([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])
### Funciones

# Función para agregar un experimento a la lista
# Solicita al usuario información sobre el experimento y lo agrega a la lista
# Si ocurre algún error en la entrada, se notifica al usuario
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
    analizarPromedio=0.0
    investigacionAdd= InvestigacionCientifica(IdExperimento, nombreExperimento,fechaExperimento,tipoExperimento, resultados_separado,analizarPromedio)
    listaExperimentos.append(investigacionAdd)
    print("Experimento agregado exitosamente")
 # Función para visualizar todos los experimentos registrados
# Imprime las propiedades principales de cada experimento

def visualizarExperimento(ListaExperimentos):
    if len(ListaExperimentos) <=0:
        print("NO hay experimentos registrados")
        return
        
    for item in ListaExperimentos:
        print(f"\nId Experimento: {item.IdExperimento}") 
        print(f"\nNombre experimento:  {item.nombreExperimento}")
        print(f"\nFecha Experimento: {item.fechaExperimento}")
        print(f"\nTipo Experimento: {item.tipoExperimento}")
   # Función para analizar los resultados de los experimentos
# Calcula el promedio, el valor máximo y el mínimo de los resultados
# Actualiza la propiedad analizarPromedio en los experimentos registrados   
def analizarPromedio(ListaExperimentos):
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
    # se agrega el promedio a la lista para generar el  informe 
    for resultado in ListaExperimentos:
        resultado.analizarPromedio=promedio
    
# Función para eliminar un experimento de la lista
# Recibe el ID del experimento que se desea eliminar 
def eliminarExperimento(ListaExperimentos, IdExperimento):
    # Convertir el ID a entero para asegurarse de que es del tipo correcto
    try:
        IdExperimento = int(IdExperimento)
    except ValueError:
        print("El ID proporcionado no es válido. Debe ser un número entero.")
        return

    # Buscar el experimento por ID
    experimento_a_eliminar = None
    for experimento in ListaExperimentos:
        if experimento.IdExperimento == IdExperimento:
            experimento_a_eliminar = experimento
            break

    # Si no se encuentra el experimento, informar al usuario
    if experimento_a_eliminar is None:
        print(f"No se encontró un experimento con el ID {IdExperimento}.")
        return

    # Eliminar el experimento y confirmar
    ListaExperimentos.remove(experimento_a_eliminar)
    print(f"El experimento con ID {IdExperimento} se eliminó exitosamente.")

    # Mostrar los experimentos restantes
    visualizarExperimento(ListaExperimentos)
    
# funcion para realizar comparaciones de experimentos con su promedio 
def compararExperimento(ListaExperimentos):
    """
    Compara el promedio de los resultados de experimentos seleccionados por su ID.
    
    :param ListaExperimentos: Lista que contiene los experimentos registrados.
    """
    if not ListaExperimentos:
        print("No hay experimentos registrados para comparar.")
        return

    # Mostrar todos los experimentos disponibles
    print("\nLista de experimentos registrados:")
    for experimento in ListaExperimentos:
        print(f"ID: {experimento.IdExperimento} - Nombre: {experimento.nombreExperimento}")

    # Solicitar al usuario los IDs de los experimentos a comparar
    ids_input = input("\nIngrese los IDs de los experimentos a comparar, separados por comas: ").strip()
    try:
        ids_seleccionados = [int(id.strip()) for id in ids_input.split(",") if id.strip().isdigit()]
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return

    if not ids_seleccionados:
        print("No se ingresaron IDs válidos.")
        return

    # Filtrar los experimentos correspondientes a los IDs ingresados
    experimentos_comparar = [exp for exp in ListaExperimentos if exp.IdExperimento in ids_seleccionados]

    if not experimentos_comparar:
        print("Ninguno de los IDs ingresados coincide con los experimentos registrados.")
        return

    # Calcular y mostrar los promedios de cada experimento
    resultados_comparados = []
    for experimento in experimentos_comparar:
        promedio = statistics.mean(experimento.resultados)
        resultados_comparados.append((experimento.nombreExperimento, promedio))

    # Ordenar los resultados por promedio
    resultados_comparados.sort(key=lambda x: x[1])

    # Mostrar los resultados
    print("\nResultados de la comparación (ordenados por promedio):")
    for nombre, promedio in resultados_comparados:
        print(f"Experimento: {nombre} - Promedio: {promedio:.2f}")
  
# Función para generar un informe en un archivo de texto
# Incluye los datos principales de cada experimento registrado

def generarInforme(ListaExperimentos):
    nombreInforme = "informe_investigacion_cientifica.txt"
    path = os.path.abspath(nombreInforme)
    directorio=os.path.dirname(path)    
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)
        print("Directorio creado exitosamente")
    # Validar si hay experimentos registrados
    if not ListaExperimentos:
        print("NO hay experimentos registrados")
        return
    
    try:
        # Abrir el archivo para escritura
        with open(path, "w") as informe:
            for experimento in ListaExperimentos:
                
                informe.write(f"Nombre experimento: {experimento.nombreExperimento}\n")
                informe.write(f"Fecha Experimento: {experimento.fechaExperimento}\n")
                informe.write(f"Tipo Experimento: {experimento.tipoExperimento}\n")
                informe.write("Resultados: " + ", ".join(map(str, experimento.resultados)) + "\n")
                informe.write(f"Promedio: {experimento.analizarPromedio} \n")
                informe.write("\n") 
        print("Informe generado exitosamente como informe_investigacion_cientifica.txt")
    
    except Exception as e:
        print(f"Error al generar el informe: {e}")

#### La funcion validar permite validar que los datos ingresados sean correctos
def validar_seleccion_menu(dato_entrada):
    try:
        return int(dato_entrada)
    except Exception as ex:
        return False
        
   #### `menuInvestigacionCientifica` 
   # Es el punto de entrada principal del sistema. Contiene un menú interactivo con las siguientes opciones:
 
def menuInvestigacionCientifica():
    ListaExperimentos=[]
    count = 0
  
    
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
        print('6) Comparar experimento ')
        print('7) Salir (exit)')
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
               analizarPromedio(ListaExperimentos)
            if  int(opcionSeleccionada) == 6:
                compararExperimento(ListaExperimentos)                               
            if opcionSeleccionada == 7:
                break
        else:
            print('Seleccione una opción valida')
    
if __name__ == '__main__': 
  menuInvestigacionCientifica()









    
        

       

    