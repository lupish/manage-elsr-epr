from os import walk
import csv
import string
from xml.etree.ElementInclude import include

def sort_dict(x):
    return x['file']

if __name__ == "__main__":
    path = "C:\\proy_io\\CPLEX\\icor\\"
    file_name = path + "icor_nT12_nL3.txt"

    dato = {}
    datos = []
    f = open(file_name, "r")
    for l in f.readlines():
        # print(l)
        if l.find('.dat') != -1:
            file = l
        if l.find("COSTO") != -1:
            cost = float(l.split("=")[1])
        if l.find("TIEMPO") != -1:
            runtime = float(l.split(": ")[1])
            
            dato = {'file': file, 'cost': cost, 'runtime': runtime}
            datos.append(dato)
    datos.sort(key=sort_dict)
    print("CSV")

    path = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL3\\OUT"
    with open(path + '\\solver_OUT.csv', 'w', newline='') as csvfile:
        fieldnames = ['file', 'cost', 'runtime']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

        writer.writerows(datos)




