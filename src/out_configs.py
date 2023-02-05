from os import walk
import csv
import read_heuristica
from enum import Enum

class Tasas(Enum):
    tasa0 = "tasas0"
    tasa05 = "tasas05"
    tasa1 = "tasas10"

class Saltos(Enum):
    saltos0 = ""
    saltos3 = "saltos3_"
    saltos3Odd = "saltosOdd3_"
    saltos5 = "saltos5_"
    saltos5Odd = "saltosOdd5_"

class Algoritmo(Enum):
    heuristica = "HEURISTICA"
    solver = "SOLVER"

class Clientes(Enum):
    cliente1 = "nL1"
    cliente2 = "nL2"
    cliente3 = "nL3"

class SolverTipo(Enum):
    noAplica = "na"
    miMaquina = "miMaquina"
    inco_15min = "inco"


def sort_dict(x):
    return (str(x['config']) + x['file'])

if __name__ == "__main__":
    config = 10
    version = "v3"
    its = "50"
    tasa = Tasas.tasa0.value
    saltos = Saltos.saltos3.value
    algoritmo = Algoritmo.heuristica.value
    cliente = Clientes.cliente3.value
    run_ReadHeuristic = 1
    solverTipo = SolverTipo.inco_15min
    
    path_in = "C:\\proy_io\\Codigo\\archivosDAT\\nT24-{cliente}\\config{i}\\OUT\\"
    if (algoritmo == Algoritmo.heuristica.value):
        if (tasa == Tasas.tasa0.value):
            name_in = "{algoritmo}_{version}_it{its}_{saltos}datos_nT24_{cliente}.csv".format(algoritmo=algoritmo, version=version, its=its, saltos=saltos, cliente=cliente)
        else:
            name_in = "{algoritmo}_{tasa}_{version}_it{its}_{saltos}datos_nT24_{cliente}.csv".format(algoritmo=algoritmo, tasa=tasa, version=version, its=its, saltos=saltos, cliente=cliente)    
        # name_in = "HEURISTICA_tasas10_{v}_it50_datos_nT24_nL3.csv".format(v=version)
    else:
        if (solverTipo.inco_15min):
            if (tasa == Tasas.tasa0.value):
                name_in = "{algoritmo}_tasas00_nT24_{cliente}_nuevoMod_INCO.csv".format(algoritmo=algoritmo, cliente=cliente)
            else:
                name_in = "{algoritmo}_{tasa}_nT24_{cliente}_nuevoMod_INCO.csv".format(algoritmo=algoritmo, tasa=tasa, cliente=cliente)
        else:
            if (tasa == Tasas.tasa0.value):
                # name_in = "{algoritmo}_nT24_{cliente}_nuevoMod.csv".format(algoritmo=algoritmo, cliente=cliente)
                name_in = "{algoritmo}_tasas00_nT24_{cliente}_nuevoMod_INCO.csv".format(algoritmo=algoritmo, cliente=cliente)
            else:
                name_in = "{algoritmo}_{tasa}_nT24_{cliente}_nuevoMod.csv".format(algoritmo=algoritmo, tasa=tasa, cliente=cliente)
    
    if (algoritmo == Algoritmo.solver.value):
        path_out = "C:\\proy_io\\Codigo\\archivosDAT\\nT24-{cliente}\\OUT\\all\\{tasa}\\".format(cliente=cliente, tasa=tasa)
    else:
        path_out = "C:\\proy_io\\Codigo\\archivosDAT\\nT24-{cliente}\\OUT\\all\\{tasa}\\{version}\\".format(cliente=cliente, tasa=tasa, version=version)

    name_out = "CONFIGS-" + name_in

    hueristic = 1
    if (algoritmo == Algoritmo.solver.value):
        hueristic = 0
    
    if run_ReadHeuristic:
        read_heuristica.main(config, hueristic)

    datos = []
    for i in range(1, config+1):
        path_file = path_in.format(cliente=cliente, i=i) + name_in
        print(path_file)

        with open(path_file, "r") as f:
            spamreader = csv.reader(f, delimiter=',')
            # print(spamreader)
            for row in spamreader:
                # print(row)
                if row[0] != "file":
                    dato = {'config': i, 'file': row[0], 'cost': row[1], 'runtime': row[2]}
                    datos.append(dato)
    # datos.sort(key=sort_dict)
    datos.sort(key=lambda e: (int(e['config']), e['file']))

    print("OUT = " + path_out + name_out)      
    with open(path_out + name_out, 'w', newline='') as csvfile:
        print("creando el output")
        fieldnames = ['config','file', 'cost', 'runtime']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(datos)

        

