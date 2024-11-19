from datetime import datetime
import statistics 
ListaExperimentos=[]

class InvestigacionCientifica:
    # metodo constructor , init es para inicializar el metodo 
    def __init__(self,nombreExperimento,fechaExperimento,tipoExperimento, resultados):
        self.nombreExperimento=nombreExperimento
        self.fechaExperimento=fechaExperimento
        self.tipoExperimento=tipoExperimento
        self.resultados = resultados

# funcion para agregar experimento 
def agregarExperimento(listaExperimentos):
    
    print('\n============Agregar Experimentos ===============\n')
    nombreExperimento=input("\nIngrese el nombre del experimento:")
    fechaExperimento_str=input("\ningrese la fecha del experimento  (DD/MM/AAAA):")
    try:
        fechaExperimento=datetime.strptime(fechaExperimento_str,"%d/%m/%Y")
    except Exception as ex:
        print(f"fecha invalida :{ex}")
        return
    tipoDeExperimento=input("\nIngrese el tipo de experimento \n 1) fisica, \n 2) biologia, \n 3) quimica:")

        
    if tipoDeExperimento.lower() == 'fisica' or tipoDeExperimento.lower() == 'biologia' or tipoDeExperimento.lower() == 'quimica':
        tipoExperimento = tipoDeExperimento
    else:
        print('Debe seleccionar el tipo de experimento valido')
        
    resultados = input('Ingrese los resultados separados por coma')
        
    investigacionAdd= InvestigacionCientifica(nombreExperimento,fechaExperimento,tipoExperimento, resultados)
    listaExperimentos.append(investigacionAdd)
    print("Experimento agregado exitosamente")
    

agregarExperimento(ListaExperimentos)
        

       

    