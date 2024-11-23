from datetime import datetime
from prettytable import PrettyTable
import statistics
import os 


# Clase principal que representa un experimento de investigación científica
class InvestigacionCientifica:
    # metodo constructor , init es para inicializar el metodo 
    def __init__(self,IdExperimento, nombreExperimento,fechaExperimento,tipoExperimento, resultados,analizarPromedio):
        self.IdExperimento = IdExperimento
        self.nombreExperimento=nombreExperimento
        self.fechaExperimento=fechaExperimento
        self.tipoExperimento=tipoExperimento
        self.resultados = resultados
        self.analizarPromedio=analizarPromedio

# Función para agregar un experimento a la lista
# Solicita al usuario información sobre el experimento y lo agrega a la lista
# Si ocurre algún error en la entrada, se notifica al usuario 
def agregarExperimento(listaExperimentos, count):
    
    print('\n===============  Agregar Experimentos  ===============\n')
    IdExperimento = count # Genera un nuevo ID basado en el contador
    nombreExperimento=input("\nIngrese el nombre del experimento: ")
    fechaExperimento_str=input("\ningrese la fecha del experimento  (DD/MM/AAAA):") 
    try:
        fechaExperimento=datetime.strptime(fechaExperimento_str,"%d/%m/%Y") # Validación de fecha
    except Exception as ex:
        print(f"fecha invalida :{ex}")
        return
      # Validación del tipo de experimento
    while True:
        tipoDeExperimento=input("\nPor favor, escriba el nombre del experimento que desea realizar. \n 1) fisica, \n 2) biologia, \n 3) quimica: \n")
        if (tipoDeExperimento.lower() == 'fisica') or tipoDeExperimento.lower() == 'biologia' or tipoDeExperimento.lower() == 'quimica':
            tipoExperimento = tipoDeExperimento
            break
        else:
            print('Debe seleccionar el tipo de experimento valido')
        
    try:
        resultados = input('Ingrese los resultados separados por coma \n')
        resultados_separado = list(map(float, resultados.split(",")))  # Convierte los resultados en números
    except Exception as ex:
        print('resultados ingresados no validos solo se permite valores numericos')
    analizarPromedio=0.0
    investigacionAdd= InvestigacionCientifica(IdExperimento, nombreExperimento,fechaExperimento,tipoExperimento, resultados_separado,analizarPromedio)
    listaExperimentos.append(investigacionAdd)
    print("\nExperimento agregado exitosamente\n")
    # Una vez ingrese el esperimento se activa el metodo para visualizar los registros
    visualizarExperimento(listaExperimentos)

    # Función para visualizar todos los experimentos registrados
# Imprime las propiedades principales de cada experimento
def visualizarExperimento(ListaExperimentos):
    table = PrettyTable()
    print('\n===============  Lista de experimentos creados  ===============\n')
    
    if len(ListaExperimentos) <=0:
        print("NO hay experimentos registrados")
        return
    
    table.field_names = ["Id Experimento", "Nombre Experimento", "Fecha Experimento", "Tipo Experimento", "Resultado", "Promedio"]
    
    for item in ListaExperimentos:
        table.add_row([item.IdExperimento, item.nombreExperimento, item.fechaExperimento, item.tipoExperimento, item.resultados, item.analizarPromedio])
        
    print(table.get_string(fields=["Id Experimento", "Nombre Experimento", "Fecha Experimento", "Tipo Experimento", "Resultado", "Promedio"]))
        
    input("por favor, presione enter para continuar.")

# Función para analizar los resultados de los experimentos
# Calcula el promedio, el valor máximo y el mínimo de los resultados
# Actualiza la propiedad analizarPromedio en los experimentos registrados
    
def analizarPromedio(ListaExperimentos):
    print('\n===============  Generar Promedio  ===============\n')
    table = PrettyTable()
    if not ListaExperimentos:
        print("No hay experimentos registrados")
        return
    
    table.field_names = ["Promedio", "Maximo", "Minimo"]
    promedio = 0
    for experimento in ListaExperimentos:
        if experimento.resultados:
            promedio = sum(experimento.resultados) / len(experimento.resultados)
            experimento.analizarPromedio = round(promedio, 2)
          
            maximo=max(experimento.resultados)
            minimo=min(experimento.resultados)
            table.add_row([experimento.analizarPromedio, maximo, minimo])
    # print(f"El promedio de los resultados es: {round(promedio,2)}  ")
    # print(f"El maximo de los resultados es: {maximo}")
    # print(f"El minimo de los resultados es: {minimo}")
    # se agrega el promedio a la lista para generar el  informe 
    print(table.get_string(fields=["Promedio", "Maximo", "Minimo"]))
    input("Por favor, presione enter para continuar.")
    

# Función para eliminar un experimento de la lista
# Recibe el ID del experimento que se desea eliminar
def eliminarExperimento(ListaExperimentos, IdExperimento):
    # Convertir el ID a entero para asegurarse de que es del tipo correcto
    print('\n===============  Eliminar Experimento  ===============\n')
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
    input("Por favor, presione enter para continuar.")

    
# Función para comparar un experimento de la lista
# Recibe el ID del experimento que se desea comparar
def compararExperimento(ListaExperimentos):
    print('\n===============  Comparar Experimentos  ===============\n')
    #Compara el promedio de los resultados de experimentos seleccionados por su ID.
    #ListaExperimentos: Lista que contiene los experimentos registrados.
    
    if not ListaExperimentos:
        print("No hay experimentos registrados para comparar.")
        input("Por favor, oprima enter para continuar")
        return

    # Mostrar todos los experimentos disponibles
    print("\nLista de experimentos registrados:")
    for experimento in ListaExperimentos:
        print(f"Id experimento: {experimento.IdExperimento} - Nombre experimento: {experimento.nombreExperimento}")

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
        promedio = 0
        if experimento.resultados:
            promedio = sum(experimento.resultados) / len(experimento.resultados)
            resultados_comparados.append((experimento.nombreExperimento, promedio))

    # Ordenar los resultados por promedio
    resultados_comparados.sort(key=lambda x: x[1])

    # Mostrar los resultados
    print("\nResultados de la comparación (ordenados por promedio):")
    for nombre, promedio in resultados_comparados:
        print(f"Experimento: {nombre} - Promedio: {promedio:.2f}")
    
    input("Por favor presione enter para continuar.")
  
# Función para eliminar un experimento de la lista
# Recibe el ID del experimento que se desea eliminar
def generarInforme(ListaExperimentos):
    print('\n===============  Generar Informe ===============\n')
    if not ListaExperimentos:
        print("NO hay experimentos registrados")
        return
    
    nombreInforme = "informe_investigacion_cientifica.txt"
    path = os.path.abspath(nombreInforme)
    directorio=os.path.dirname(path)    
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)
        print("Directorio creado exitosamente")
    # Validar si hay experimentos registrados
        
    try:
        # Abrir el archivo para escritura
        with open(path, "w") as informe:
            for experimento in ListaExperimentos:
                informe.write(f"Id Experimento: {experimento.IdExperimento}")
                informe.write(f"Nombre experimento: {experimento.nombreExperimento}")
                informe.write(f"Fecha Experimento: {experimento.fechaExperimento}")
                informe.write(f"Tipo Experimento: {experimento.tipoExperimento}")
                informe.write("Resultados: " + ", ".join(map(str, experimento.resultados)) + "\n")
                informe.write(f"Promedio: {experimento.analizarPromedio}")
                informe.write("\n") 
        print("Informe generado exitosamente como informe_investigacion_cientifica.txt")
        input("por favor, presione enter para continuar.")
    
    except Exception as e:
        print(f"Error al generar el informe: {e}")

# Función para validar si una entrada del menú es numérica
def validar_seleccion_menu(dato_entrada):
    try:
        return int(dato_entrada)
    except Exception as ex:
        return False
        
 # Menú principal del sistema de investigación científica
# Permite al usuario realizar diversas operaciones sobre los experimentos registrados   
def menuInvestigacionCientifica():
    ListaExperimentos=[]
    count = 0

    while True:
        print('\n ===============Bienvenido al sistema de investigación científica=============== ')
        print('\n')
        print('1) Agregar experimento ')
        print('2) Visualizar experimento ')
        print('3) Eliminar experimento ')
        print('4) Generar Promedio')
        print('5) Comparar experimento ')
        print('6) Generar informe ')
        print('7) Salir (exit)')
        opcionSeleccionada = input('\n====Selecciona la opción que desea realizar====\n')
        if validar_seleccion_menu(opcionSeleccionada):
            count += 1 # Se crear un contador para el id del experimetno
            #Agregar experimento
            if int(opcionSeleccionada) == 1:
                agregarExperimento(ListaExperimentos, count)
            #Listar experimento
            if int(opcionSeleccionada) == 2:
                visualizarExperimento(ListaExperimentos)
            #Eliminar experimento
            if int(opcionSeleccionada) == 3:
                while True:
                    IdExperimento = input('Ingrese el Id del experimento que desea eliminar: ')
                    if validar_seleccion_menu(IdExperimento):
                        eliminarExperimento(ListaExperimentos, IdExperimento)
                        break
                    else:
                        print('El Id ingresado no es valido')
            #Generar promedio
            if  int(opcionSeleccionada) == 4:
               analizarPromedio(ListaExperimentos)
            #Comparar experimento
            if  int(opcionSeleccionada) == 5:
                compararExperimento(ListaExperimentos)
            #Generar Informe
            if int(opcionSeleccionada) == 6:
                generarInforme(ListaExperimentos)
            #Salida segura
            if int(opcionSeleccionada) == 7:
                print('Grcias por utilizar el sistema investigación científica \n')
                break
        else:
            print('Seleccione una opción valida')
            
    
if __name__ == '__main__': 
  menuInvestigacionCientifica()









    
        

       

    