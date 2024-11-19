from datetime import datetime
import statistics 
ListaExperimentos=[]
class InvestigacionCientifica:
# metodo constructor , init es para inicializar el metodo 
    def _init_(self,nombreExperimento,fechaExperimento,tipoExperimento):
        self.nombre=nombreExperimento
        self.fecha=fechaExperimento
        self.tipoExperimento=tipoExperimento

# funcion para agregar experimento 
    def agregarExperimento(listaExperimentos):

        nombreExperimento=input("Ingrese el nombre del experimento:")
        fechaExperimento_str=input("ingrese la fecha del experimento  (DD/MM/AAAA):")
        try:
            fechaExperimento=datetime.strptime(fechaExperimento_str,"%d/%m/%Y")
        except Exception as ex:
            print(f"fecha invalida :{ex}")
            return
        tipoDeExperimento=input("Ingrese el tipo de experimento (fisica,biologia,quimica):")

   
        
        if tipoDeExperimento.lower() == 'fisica' or tipoDeExperimento.lower() == 'biologia' or tipoDeExperimento.lower() == 'quimica':
            investigacionAdd=InvestigacionCientifica(nombreExperimento,fechaExperimento,tipoDeExperimento)
            listaExperimentos.append(investigacionAdd)
            print("Experimento agregado exitosamente ")
        else:
            print('Debe seleccionar el tipo de experimento valido')



    agregarExperimento(ListaExperimentos)
        

       

    