from os import walk
import csv

if __name__ == "__main__":
    path = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL3\\OUT"


    for (dirpath, dirnames, filenames) in walk(path):
        print(filenames)

        for file in filenames:
            with open(path + "\\" + file + '.csv', 'w', newline='') as csvfile:
                f = open(path + "\\" + file, "r")
                fieldnames = ['cost']
                writer = csv.DictWriter(csvfile, fieldnames)
                writer.writeheader()

                for x in f:
                    # print(x)
                    if (x.find("COSTO") != -1):
                        cost = x.split("=")
                        writer.writerow({'cost': cost})
