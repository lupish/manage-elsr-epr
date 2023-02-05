from re import A
import numpy as np

def imprimir_valor(sep, val_nom, val_val):
    texto = "param {nom} := {val}".format(nom=val_nom, val=val_val) + sep

    return texto

def imprimir_array(sep, nT, arr_nom, arr_val):
    texto = "param {nom} :=".format(nom=arr_nom)

    for i in range(1, nT + 1):
        texto += " {i} {val}".format(i=i, val=arr_val[i-1])

        if (i != nT):
            texto += ","
    texto += sep

    return texto

def imprimir_matriz(enter, sep, tab, matriz_name, matriz_values, nT, nL):
    texto ="param {nom} :".format(nom=matriz_name) + enter

    for i in range(1, nT + 1):
        texto += tab + str(i)
    texto += ":=" + enter

    for l in range(1, nL+1):
        texto += str(l) + tab + tab.join(matriz_values[l-1])

        if (l != nL):
            texto += enter
    texto += sep



    return texto

def imprimir_datos(file_name, nT, nL, D, alpha, beta, M, hS, STU, U, U_0, Kv, Kr, Km, hU, hsL, huL, config):
    path = "C:\\proy_io\\Codigo\\archivosDAT\\nT{nT}-nL{nL}\\config{config}\\".format(nT = nT, nL = nL, config = config)
    enter = "\n"
    sep = ";" + enter
    tab = "\t"
    print("ARCHIVO " + path + file_name)
    
    f = open(path + file_name, "w+")
    f.write("######################## PARAMETROS ########################" + enter + enter)
    
    f.write("# GENERALES #" + enter)
    f.write(imprimir_valor(sep, "nT", nT))
    f.write(imprimir_valor(sep, "nL", nL))
    f.write(imprimir_matriz(enter, sep, tab, "D", D, nT, nL))
    f.write(imprimir_valor(sep, "M", M))
    f.write(imprimir_valor(sep, "U0", U_0))
    f.write(imprimir_matriz(enter, sep, tab, "U", U, nT, nL))
    f.write(imprimir_valor(sep, "alpha", alpha))
    f.write(imprimir_valor(sep, "beta", beta))

    f.write(enter + "# ORDENAR RETORNOS #" + enter)
    f.write(imprimir_matriz(enter, sep, tab, "Kv", Kv, nT, nL))

    f.write(enter + "# PRODUCCION #" + enter)
    f.write(imprimir_array(sep, nT, "cm", ["0"]*nT))
    f.write(imprimir_array(sep, nT, "cr", ["0"]*nT))

    f.write(enter + "# SETUP #" + enter)
    f.write(imprimir_array(sep, nT, "Km", Km))
    f.write(imprimir_array(sep, nT, "Kr", Kr))

    f.write(enter + "# STOCK #" + enter)
    f.write(imprimir_array(sep, nT, "hs", hS))
    f.write(imprimir_array(sep, nT, "hu", hU))
    f.write(imprimir_matriz(enter, sep, tab, "hsL", hsL, nT, nL))
    f.write(imprimir_matriz(enter, sep, tab, "huL", huL, nT, nL))

    f.write(enter + "# TRANSPORTE #" + enter)
    f.write(imprimir_array(sep, nL, "cvs", ["0"]*nL))
    f.write(imprimir_array(sep, nL, "cvu", ["0"]*nL))
    f.write(imprimir_valor(sep, "STU", STU))

    f.write(enter + "end" + sep)

    f.close()

def generar_dats(nT, nL, config):
    D_mu = 100 # mean
    D_sigma = 20 # standard deviation

    ###### FIJOS #######
    # demanda
    D = {}
    for l in range(0, nL):
        D[l] = [str(int(x)) for x in np.random.normal(D_mu, D_sigma, nT)]

    # tasas
    alpha = 0
    beta = 0

    # M
    M = 100000

    # hS
    hS = ["1"] * nT
    hsL = {}
    for l in range(0, nL):
        hsL[l] = ["1"] * nT

    # STU
    STU = 1

    ###### ESCENARIOS ######
    # U
    U_bajo = ["B", 30, 6]
    U_alto = ["A", 70, 14]
    U_esc = [U_bajo, U_alto]

    # Kv
    Kv_bajo = ["B", "200"]
    Kv_medio = ["M", "500"]
    Kv_alto = ["A", "2000"]
    Kv_esc = [Kv_bajo, Kv_medio, Kv_alto]

    # Km
    Km_bajo = ["B", "200"]
    Km_medio = ["M", "500"]
    Km_alto = ["A", "2000"]
    Km_esc = [Km_bajo, Km_medio, Km_alto]

    # Kr
    Kr_bajo = ["B", "200"]
    Kr_medio = ["M", "500"]
    Kr_alto = ["A", "2000"]
    Kr_esc = [Kr_bajo, Kr_medio, Kr_alto]

    # hU
    hU_bajo = ["B", "0.2"]
    hU_medio = ["M", "0.5"]
    hU_alto = ["A", "0.8"]
    hU_esc = [hU_bajo, hU_medio, hU_alto]

    U = {}
    for u in U_esc:
        U_0 = [str(int(x)) for x in np.random.normal(u[1], u[2], 1)][0]
        for l in range(0, nL):
            U[l] = [str(int(x)) for x in np.random.normal(u[1], u[2], nT)]

        Kv = {}
        for kv in Kv_esc:
            for l in range(0, nL):
                Kv[l] = [kv[1]] * nT
            
            for km in Km_esc:
                Km = [km[1]] * nT

                for kr in Kr_esc:
                    Kr = [kr[1]] * nT

                    huL = {}
                    for hu in hU_esc:
                        hU = [hu[1]] * nT

                        for l in range(0, nL):
                            huL[l] = [hu[1]] * nT

                        file_name = "datos_nT{nT}_nL{nL}_{u}{kv}{km}{kr}{hu}.dat".format(nT=nT, nL=nL, u=u[0], kv=kv[0], km=km[0], kr=kr[0], hu=hu[0],config=config)
                        imprimir_datos(file_name, nT, nL, D, alpha, beta, M, hS, STU, U, U_0, Kv, Kr, Km, hU, hsL, huL, config)

if __name__ == "__main__":
    print("*** GENERATE DAT FILES ***")

    nT = 24
    nL = 3
    configMAX = 10
    configMIN = 2

    for c in range(configMIN, configMAX+1):
        generar_dats(nT, nL, c)