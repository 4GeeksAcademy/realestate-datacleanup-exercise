import pandas as pd
import matplotlib.pyplot as plt

###Creamos el data frame con a partir del CSV, la separación es ; ###

df_estates = pd.read_csv('assets/real_estate.csv', sep=';')
###Imprimir dirección de la casa más cara y la más barata###

def HighPrice(df):
    #Cogemos el valor más grande de la columna Price (El ultimo en este caso) y lo convertimos en una Serie con squeeze para trabajarlo mejor.
    df_estates_highprice = df.sort_values('price').tail(1).squeeze()
    return f"La casa con dirección en Calle {df_estates_highprice['level7']} es la más cara y su precio es de {df_estates_highprice['price']} €."

def LowPrice(df):
    df_estates_lowprice = df.sort_values('price').head(1).squeeze()
    return f"La casa con dirección en Calle {df_estates_lowprice['level7']} es la más barata y su precio es de {df_estates_lowprice['price']} €."
###Imprimimos la casa más grande y la más pequeña###

def MoreSurface(df):
    df_estates_moresurface = df.sort_values('surface').tail(1).squeeze()
    return f"La casa más grande está en la Calle {df_estates_moresurface['level7']} y su superficie es de {df_estates_moresurface['surface']} metros."

def LessSurface(df):
    df_estates_lesssufrface = df.sort_values('surface').head(1).squeeze()
    return f"La casa más pequeña está en la Calle {df_estates_lesssufrface['level7']} y su superficie es de {df_estates_lesssufrface['surface']} metros."

###Nombre de las poblaciones###

def Populations(df):
    populations = df.level5.squeeze()
    list_population = []
    for i in range(len(populations)):
       list_population.append(populations[i])
    return list_population

### Comprobar si hay valores no admitidos en la lista ###

def NanIdentificy(df):
    cols_nan = df.columns[df.isnull().any()] #Localizamos las columnas con valores NaN
    rows_nan = df[df.isnull().any(axis = 1)][cols_nan] #Localizamos las filas con valores NaN
    return rows_nan.isnull().any() #Solo devolvemos las columnas con valor NaN = True

### Eliminar los NAs del dataset###

def Filter(df):
   df_filter = df.dropna(axis = 1) #Eliminanos solo las columnas porque si eliminamos las filas se borraría todo el DataSet
   return df_filter

###Media de precios de Arroyomolinos###

def MeanArroyomolinos(df):
    arroyomolinos = df[df['level5'] == "Arroyomolinos (Madrid)"]
    return arroyomolinos.price.mean()

###Historiograma de los precios de Arroyomolinos###

def HistogramPriceArroyomolinos(df):
    arroyomolinos = df[df['level5'] == "Arroyomolinos (Madrid)"]
    plt.figure (figsize=(10,5))
    plt.hist (arroyomolinos.price, bins=30, alpha=1)
    plt.title ("Precios de Arroyomolinos (Madrid)")
    plt.show()
    return None

###Comprobar si el precio promedio de Valdemorillo y de Galapagar son el mismo###

def IsValdemorilloAndGalapagarMeanEqual(df):
    valdemorillo = df[df['level5'] == "Valdemorillo"]
    galapagar = df[df['level5'] == "Galapagar"]
    print (f"El precio medio de Valdemorillo es de {valdemorillo.price.mean()}.\nEl precio medio de Galapagar es de {galapagar.price.mean()}.")
    if valdemorillo.price.mean() == galapagar.price.mean():
        print ("El precio medio de Valdemorillo y Galapagar es igual.")
    elif valdemorillo.price.mean() > galapagar.price.mean():
        print ("El precio medio de Valdemorillo es superior al de Galapagar")
    else:
        print ("El precio medio de Galapagar es superior al de Valdemorillo")
    return None

###Comprobar si el precio/m2 promedio de Valdemorillo y Galapagar son el mismo###

def PricePerSquare(df):
    pps = df.price / df.surface
    df['pps'] = pps
    return df.pps

def PpsValdemorillo(df):
    ppsValdemorillo = df[df['level5'] == "Valdemorillo"].set_index('level5')
    return ppsValdemorillo.pps.mean()

def PpsGalapagar(df):
    ppsgalapagar = df[df['level5'] == "Galapagar"].set_index('level5')
    return ppsgalapagar.pps.mean()

#########Ejercicios########

#Ejercicio1
#print (HighPrice(df_estates))

#Ejercicio2
#print (LowPrice(df_estates))

#Ejercicio3.1
#print (MoreSurface(df_estates))

#Ejercicio3.2
#print (LessSurface(df_estates))

#Ejercicio4
#print (Populations(df_estates))

#Ejercicio5
#print (NanIdentificy(df_estates))

#Ejercicio6
#print(Filter(df_estates))
#print (df_estates)

#Ejercicio7
#print(MeanArroyomolinos(df_estates))

#Ejercicio8
#print(HistogramPriceArroyomolinos(df_estates))

#Ejercicio9
print (IsValdemorilloAndGalapagarMeanEqual(df_estates))