from os import walk
import csv
import string
from xml.etree.ElementInclude import include

def sort_dict(x):
    return x['file']

def read_heuristics(path, heuristic):
    for (dirpath, dirnames, filenames) in walk(path):
        for file_name in filenames:
            text_find = ""
            if (heuristic == 1):
                # HEURISTICA
                text_find = '.out'
            else:
                # SOLVER
                text_find = '.txt'

            # if file_name.find('.out') != -1: # heuristica
            # if file_name.find('.txt') != -1: # solver
            if file_name.find(text_find) != -1:
                dato = {}
                datos = []
                f = open(path + file_name, "r")
                for l in f.readlines():
                    # print(l)
                    if l.find('.dat') != -1:
                        file = l.split("nL1_")[1]
                    if l.find("COSTO") != -1:
                        cost = float(l.split("=")[1])
                    if l.find("TIEMPO") != -1:
                        runtime = float(l.split(": ")[1])
                        
                        dato = {'file': file, 'cost': cost, 'runtime': runtime}
                        datos.append(dato)
                datos.sort(key=sort_dict)
                
                path_out = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL1\\config{config}\\OUT\\".format(config=config)
                
                if (heuristic == 1):
                    # HEURISTICA
                    file_name_out = "HEURISTICA_" + file_name.split("OUT_")[1].split(".out")[0] + ".csv"
                else:
                    # SOLVER
                    file_name_out = "SOLVER_" + file_name.split("icor_")[1].split(".txt")[0] + ".csv"
                
                # HEURISTICA
                # file_name_out = "HEURISTICA_" + file_name.split("OUT_")[1].split(".out")[0] + ".csv"

                # SOLVER
                # file_name_out = "SOLVER_" + file_name.split("icor_")[1].split(".txt")[0] + ".csv"

                print("CSV " + file_name_out)
                with open(path + file_name_out, 'w', newline='') as csvfile:
                    fieldnames = ['file', 'cost', 'runtime']
                    writer = csv.DictWriter(csvfile, fieldnames)
                    writer.writeheader()

                    writer.writerows(datos)

if __name__ == "__main__":
    it = 50
    config = 10
    heuristic = 1 # heuristic = 0 solver, heuristic = 1 heuristica
    
    #### path = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL1\\config{config}\\OUT\\".format(config=config)
    # file_name = path + "OUT_{version}_it{it}_datos_nT12_nL1.out".format(version=version, it=it)

    for c in range(1, config+1):
        path = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL1\\config{config}\\OUT\\".format(config=c)
        # path = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL1\\config{config}_huL5\\OUT\\".format(config=c)
        print(path)
        read_heuristics(path, heuristic)

    """
    for (dirpath, dirnames, filenames) in walk(path):
        for file_name in filenames:
            if file_name.find('.out') != -1: # heuristica
            # if file_name.find('.txt') != -1: # solver
                dato = {}
                datos = []
                f = open(path + file_name, "r")
                for l in f.readlines():
                    # print(l)
                    if l.find('.dat') != -1:
                        file = l.split("nL1_")[1]
                    if l.find("COSTO") != -1:
                        cost = float(l.split("=")[1])
                    if l.find("TIEMPO") != -1:
                        runtime = float(l.split(": ")[1])
                        
                        dato = {'file': file, 'cost': cost, 'runtime': runtime}
                        datos.append(dato)
                datos.sort(key=sort_dict)
                
                path_out = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL1\\config{config}\\OUT\\".format(config=config)
                
                # HEURISTICA
                file_name_out = "HEURISTICA_" + file_name.split("OUT_")[1].split(".out")[0] + ".csv"

                # SOLVER
                # file_name_out = "SOLVER_" + file_name.split("icor_")[1].split(".txt")[0] + ".csv"

                print("CSV " + file_name_out)
                with open(path + file_name_out, 'w', newline='') as csvfile:
                    fieldnames = ['file', 'cost', 'runtime']
                    writer = csv.DictWriter(csvfile, fieldnames)
                    writer.writeheader()

                    writer.writerows(datos)
    """





