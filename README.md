# Manage soluciones de ELSR para EPR

Genera los archivos de entrada para los algoritmos TSv1 a TSv5 y CPLEX, y parsea sus archivos de salida:
* read_heuristica: dado una ruta, lee todos los archivos de salida (huerística o exacto según se indique) y generea un CSV por cada salida con los siguientes datos:
  * file: nombre del archivo de salida.
  * cost: costo total de la solución hallada.
  * runtime: tiempo de ejecucion requerido para hallar la solución, medido en milisegundos.
* generar-dat: dado los valores de los parámetros del problema y una ruta, genera los archivos de entrada para los algortimos en la ruta mencionada.
* out_configs: dada una versión del algoritmo, genera todos los archivos de salida en un mismo CSV invocando a read_heuristicas.
* analisis_solver: dada una ruta, lee todos los archivos de salida de CPLEX y chequea si logra llegar a la solución exacta y genera un CSV con el análisis:
  * tasa: valor de las tasas de recolección y remanufacturación.
  * file: nombre del archivo de salida.
  * alcanza_optimo: cantidad de veces que se alcanzó la solución óptima.
  * no_alcanza_optimo: cantidad de veces que no se alcanzó la solución óptima debido a un timeout.
  * promedio_gap: gap promedio entre la solución encontrada y la solución óptima.
  * max_gap: máximo gap entre la solución encontrada y la solución óptima.

Trabajo realizado en el marco de la Maestría de Investigación de Operaciones de Facultad de Ingeniería UdelaR de Luciana Vidal.

# Input files
The input file na
mes follow a structured format to encode specific parameters related to the dataset. The format is as follows:

> `datos_nT{nT}_nL{nL}_{u}{kv}{km}{kr}{hu}.dat`

Each component of the file name represents specific information:

- nT: number of periods.
- nL: number of customers.
- U:  Number of used items available in customers.
    - B = N(30, 6).
    - A = N(70, 14).
- Kv: Set-up cost of visiting customers.
    - B = 200.
    - M = 500.
    - A = 2000.
- Km: : Set-up cost of manufacturing in periods.
    - B = 200.
    - M = 500.
    - A = 2000.
- Kr: Set-up cost of remanufacturing in periods.
    - B = 200.
    - M = 500.
    - A = 1000.
- hu: Unit cost for holding inventory of used items in customers and periods.
    - B = 0.2.
    - M = 0.5.
    - A = 0.8.

