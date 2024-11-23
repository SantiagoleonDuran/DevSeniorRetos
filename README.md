# DevSeniorRetos
# Proyecto de Investigación Científica

Este repositorio contiene un programa en Python para gestionar experimentos científicos. Permite agregar, visualizar, analizarPromedio,eliminar, comparar y generar informes de los experimentos realizados. A continuación, se explica cada función en detalle.

## Estructura del Código

### Clase `InvestigacionCientifica`

La clase `InvestigacionCientifica` representa un experimento científico y contiene los siguientes atributos:

- `IdExperimento`: Identificador único del experimento.
- `nombreExperimento`: Nombre del experimento.
- `fechaExperimento`: Fecha en que se realizó el experimento.
- `tipoExperimento`: Tipo de experimento (física, biología, química).
- `resultados`: Lista de resultados obtenidos del experimento.
- `analizarPromedio`: Promedio de los resultados (inicialmente 0.0).
- Método principal:
- `to_dict()`: Convierte los atributos del objeto a un diccionario.

### Funciones

#### `agregarExperimento`

Permite agregar un nuevo experimento a la lista:
1. Solicita al usuario el nombre, la fecha, el tipo y los resultados del experimento.
2. Valida las entradas.
3. Crea un objeto de la clase `InvestigacionCientifica` y lo agrega a la lista.

#### `visualizarExperimento`

Muestra todos los experimentos registrados:
- Itera sobre la lista de experimentos y muestra sus atributos principales.
- Verifica si la lista está vacía.

#### `analizarPromedio`

Analiza las métricas principales de los resultados:
- Calcula el promedio, el valor máximo y el mínimo de los resultados.
- Actualiza el promedio en el objeto del experimento.
- Muestra los datos calculados.

#### `eliminarExperimento`

Elimina un experimento específico por su ID:
- Busca el experimento en la lista.
- Lo elimina si se encuentra, o muestra un mensaje de error si no existe.

#### `Comparar experimentos`

Analiza los promedios de los experimentos:
- Compara el valor del promedio entre los experimentos solicitados
- Muestra los valores de los promedios a comparar
- #### `generarInforme`

Genera un informe en un archivo de texto con los datos de los experimentos:
- Escribe los detalles de cada experimento en un archivo llamado `informe_investigacion_cientifica.txt`.
- Maneja excepciones para evitar errores en la escritura.

#### `validar_seleccion_menu`

Valida las entradas del usuario en el menú principal:
- Intenta convertir la entrada a un número entero.
- Devuelve `False` si no es válida.

#### `menuInvestigacionCientifica`

Es el punto de entrada principal del sistema. Contiene un menú interactivo con las siguientes opciones:

1. Agregar experimento.
2. Visualizar experimento.
3. Eliminar experimento.
4. Generar informe.
5. Analizar promedio de resultados.
6. Salir del programa.

Cada opción llama a las funciones correspondientes según la selección del usuario.
