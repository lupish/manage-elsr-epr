import re
import csv
from os import walk

def print_instances(path, file_name, file_name_out_txt):
    with open(path+file_name_out_txt, "w") as f_o:
        with open(path+file_name, "r") as f:
            for l in f:
                if l.find(begin_instance) != -1:
                    f_o.write(l.split("/")[2])


def analyze_file(file, tasa, config):
    datos = []

    with open(file, "r") as f:
        instance = ""
        gap = ""
        elapsed_time = 0
        relmipgap = 0
        total_time = 0
        timeout = False
        for l in f:
            if l.find(begin_instance) != -1:
                if instance != "":
                    # print("---> ", instance, gap, elapsed_time, relmipgap, total_time)
                    dato = {
                        "tasa": tasa,
                        "config": config,
                        "instance": instance.split("/")[2],
                        "gap": gap,
                        "elapsed_time": elapsed_time,
                        "relmipgap": relmipgap,
                        "total_time": total_time
                    }
                    datos.append(dato)
                    
                instance = l.strip()
                gap = ""
                elapsed_time = 0
                relmipgap = 0
                total_time = 0
                timeout = False
            elif l.startswith("*"):
                if len(l.split()) > 0:
                    gap = l.split()[len(l.split())-1]

                    continuar = True
                    while continuar:
                        l2 = f.readline()
                        if l2 is None:
                            continuar = False
                        if l2.find(begin_instance) == -1 and l2.startswith("*"):
                            gap = l2.split()[len(l2.split())-1]
                        if re.search(r'Elapsed time = (\d+\.\d+) sec.', l2):
                            elapsed_time = float(re.search(r'Elapsed time = (\d+\.\d+) sec.', l2).group(1))
                            continuar = False
                        if re.search(r'Total \(root\+branch&cut\) =\s+(\d+\.\d+) sec\. \((\d+\.\d+) ticks\)', l2):
                            elapsed_time = re.search(r'Total \(root\+branch&cut\) =\s+(\d+\.\d+) sec\. \((\d+\.\d+) ticks\)', l2).group(1)
                            total_time = elapsed_time
                            continuar = False
                        elif l2.find(begin_instance) != -1:
                            print(l2)
                            raise ValueError("NO ENCONTRO TIEMPO TOTAL")
            
            if l.find("optimal integer solution; objective"):
                timeout = True
            if re.search(r'relmipgap = (\d+\.?\d+?)', l) and not re.search(r'e-', l) and timeout:
                relmipgap = float(re.search(r'relmipgap = (\d+(\.\d+)?)', l).group(1))
                timeout = False
            if re.search(r'Total \(root\+branch&cut\) =\s+(\d+\.?\d+?) sec\. \((\d+\.?\d+?) ticks\)', l):
                total_time = re.search(r'Total \(root\+branch&cut\) =\s+(\d+\.?\d+?) sec\. \((\d+\.?\d+?) ticks\)', l).group(1)
        if instance != "":
            # print("---> ", instance, gap, elapsed_time, relmipgap, total_time)
            dato = {
                "tasa": tasa,
                "config": config,
                "instance": instance.split("/")[2],
                "gap": gap,
                "elapsed_time": elapsed_time,
                "relmipgap": relmipgap,
                "total_time": total_time
            }
            datos.append(dato)
    
    return datos

if __name__ == "__main__":
    print("BEGIN SOLVER GAP")

    begin_instance = "***** Instancia:"
    
    """
    path = "C:\\proy_io\\Codigo\\archivosDAT\\nT24-nL3\\OUT\\analisis\\datos_solver\\"
    file_name_out = "SOLVER_gaps-runtime.csv"
    file = "tasa00_nohup_config1.out"
    datos = []
    tasa = 0
    config = "config1"
    datos = analyze_file(file, tasa, config)
    """

    path = "C:\\proy_io\\Codigo\\archivosDAT\\nT24-nL3\\OUT\\analisis\\datos_solver\\"
    file_name_out = "SOLVER_gaps-runtimev2.csv"
    file_name_out_txt = "SOLVER_instances.txt"
    with open(path + file_name_out, "w", newline="") as csvfile:
        fieldnames = ['tasa', 'config', 'instance', 'gap', 'elapsed_time', 'relmipgap', "total_time"]
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

        for (dirpath, dirnames, filenames) in walk(path):
            for file_name in filenames:
                if file_name.find("nohup") != -1:
                    # print(file_name)
                    tasa = file_name.split("_")[0]
                    config = file_name.split("_")[2].split(".")[0]
                    datos = analyze_file(path + file_name, tasa, config)
                    writer.writerows(datos)

                    print_instances(path, file_name, file_name_out_txt)


    
                
                    

    print("END SOLVER GAP")