from os import walk
import numpy as np
import csv


def sort_dict(x):
    return (x['tasa'] + x['file'])

def analizarSoluciones(file, tasa, textoLlega, textoNoLlega, textoGap):
    cantLlega = 0
    cantNoLlega = 0
    f = open(file, "r")
    relmipgaps = []
    for l in f.readlines():
        if l.find(textoLlega) != -1:
            cantLlega += 1
        if l.find(textoNoLlega) != -1:
            cantNoLlega += 1
        if l.find(textoGap) != -1:
            try:
                relmipgap = l.split(textoGap)[1]
                relmipgap_float = float(relmipgap)
                if relmipgap_float > 0.001:
                    relmipgaps.append(relmipgap_float)
            except:
                print("No es número")
    promedio_gap = np.median(relmipgaps)
    max_gap = np.max(relmipgaps)
    dato = {
        'tasa': tasa,
        'file': file,
        'alcanza_optimo': cantLlega,
        'no_alcanza_optimo': cantNoLlega,
        'promedio_gap': promedio_gap,
        'max_gap': max_gap

    }

    return dato

if __name__ == "__main__":
    print("Analizando los resultados del solver")
    textoLlega = "optimal integer solution"
    textoNoLlega = "time limit with integer solution"
    textoGap = "relmipgap = "
    tasa = "tasas10"

    path = "C:\\proy_io\\Codigo\\archivosDAT\\nT24-nL3\\OUT\\analisis\\datos_solver\\"

    datos = []
    file_name_out = "SOLVER_analisis.csv"
    print("CSV " + file_name_out)

    with open(path + file_name_out, 'w', newline='') as csvfile:
        fieldnames = ['tasa', 'file', 'alcanza_optimo', 'no_alcanza_optimo', 'promedio_gap', 'max_gap']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

        for (dirpath, dirnames, filenames) in walk(path):
            for file_name in filenames:
                if file_name.find("nohup") != -1:
                    print(file_name)
                    tasa = file_name.split("_")[0]
                    file = path + file_name
                    dato = analizarSoluciones(file, tasa, textoLlega, textoNoLlega, textoGap)
                    datos.append(dato)

                    file_name_out = file_name.split(".out")[0] + ".csv"
        datos.sort(key=lambda e: (e['tasa'], e['file']))
        writer.writerows(datos)