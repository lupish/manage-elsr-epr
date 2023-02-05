from os import walk
import os


if __name__ == "__main__":
    
    for i in range(1, 11):
        path = "C:\\proy_io\\Codigo\\archivosDAT\\nT12-nL3\\config{i}\\OUT\\".format(i=i)
        print(path)

        text = "__"
        for (dirpath, dirnames, filenames) in walk(path):
            for file_name in filenames:
                if file_name.find(text) != -1:
                    print(file_name)
                    os.rename(path + file_name, path + file_name.replace(text, "_"))
