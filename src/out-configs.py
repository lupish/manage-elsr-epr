from os import walk
import csv

def sort_dict(x):
    return (str(x['config']) + x['file'])

if __name__ == "__main__":
    config = 10
    path_in = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL1\\config{i}\\OUT\\"
    name_in = "HEURISTICA_tasas10_v3_it200_datos_nT12_nL1.csv"
    path_out = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL1\\OUT\\all\\"
    name_out = "CONFIGS-" + name_in

    datos = []
    for i in range(1, config+1):
        path_file = path_in.format(i=i) + name_in
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

        

