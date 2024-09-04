import pandas as pd
import matplotlib.pyplot as plt
#Normalizar datos con la funcion MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

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

def IsValdemorilloAndGalapagarMeanPPSEqual(df):
    pps = df.price / df.surface
    df['pps'] = pps
    ppsValdemorillo = df[df['level5'] == "Valdemorillo"]
    ppsGalapagar = df[df['level5'] == "Galapagar"]
    print (f"El precio medio de Valdemorillo por metro cuadrado es de {ppsValdemorillo.pps.mean()}.\nEl precio medio de Galapagar por metro cuadrado es de {ppsGalapagar.pps.mean()}.")
    if ppsValdemorillo.pps.mean() == ppsGalapagar.pps.mean():
        print ("El precio medio por metro cuadrado de Valdemorillo y Galapagar es el mismo.")
    elif ppsValdemorillo.pps.mean() > ppsGalapagar.pps.mean():
        print ("El precio medio por metro cuadrado de Valdemorillo es superior al de Galapagar.")
    else:
        print ("El precio medio por metro cuadrado de Galapagar es superior al de Valdemorillo.")
    return None
  
###Analizamos la relación entre el precio y la superficie de las casas.###

def RelPriceSurface(df): #SIN ACABAR
    plt.figure(figsize=(10,5))
    plt.scatter(df.price, df.surface, label = "Precio")

    plt.title("Relación Superficie/Precio")
    plt.legend()
    plt.show()
    return None

###Buscamos cuantas agencias contiene el DataSet###
def HowManyRealEstatesAre(df):
    return len(df.id_realEstates.value_counts()) #Juntamos todas las ID de las Inmobiliarias y devolvemos la longitud.

###Buscamos la población con más cantidad de casas###

def HowCityHaveMoreHouses(df):
    return df.level5.value_counts().head(1)

###Creamos un nuevo DataFrame que contenga Fuenlabrada, Leganes, Getafe y Alcorcón"###

def CinturonSur(df):
    filt_cinturonSur =df['level5'].isin(["Fuenlabrada","Leganés","Getafe","Alcorcón"])
    cinturonsur = df[filt_cinturonSur]
    return cinturonsur

###Grafico de barra de la mediana de los precios de Cinturon Sur###

def CinturonSurMeanPrice(df):
    labels = ["Fuenlabrada","Alcorcón","Leganés","Getafe"]
    fuenlabrada = df[df['level5'] == "Fuenlabrada"].price.mean()
    alcorcon = df[df['level5'] == "Alcorcón"].price.mean()
    leganes = df[df['level5'] == "Leganés"].price.mean()
    getafe = df[df['level5'] == "Getafe"].price.mean()
    values = (fuenlabrada, alcorcon, leganes, getafe)
    plt.figure(figsize=(10,5))
    plt.bar(labels, values)

    plt.title("Precios Medios Cinturón Sur")
    plt.show()

    return None

###Calcula la medía y la varianza de muestra del Cinturón Sur###

def MeanAndVar(df):
    #Para calcular la varianza típica hemos de asegurarnos que ddof es 0.
    
    return f"La media de precios del cinturón sur es de {df.price.mean()} y la varianza de precios es de {df.price.var(ddof = 0)}\nLa media de habitaciones en el cinturón sur es de {df.rooms.mean()} y la varianza es de {df.rooms.var(ddof = 0)}\nLa media de baños en el cinturón sur es de {df.bathrooms.mean()} y la varianza es de {df.bathrooms.var(ddof = 0)}\nLa media de superficie del cinturón sur es de {df.surface.mean()} y la varianza es de {df.surface.var(ddof = 0)}"

def HowIsMostExpensiveHouse(df):
    fuenlabrada = df[df['level5'] == "Fuenlabrada"].sort_values(by = 'price').tail(1).squeeze()
    alcorcon = df[df['level5'] == "Alcorcón"].sort_values(by = 'price').tail(1).squeeze()
    leganes = df[df['level5'] == "Leganés"].sort_values(by = 'price').tail(1).squeeze()
    getafe = df[df['level5'] == "Getafe"].sort_values(by = 'price').tail(1).squeeze()
    return f"La casa más cara de {fuenlabrada.level5} en {fuenlabrada.address} tiene un precio de {fuenlabrada.price} €.\nLa casa más cara de {alcorcon.level5} en {alcorcon.address} tiene un precio de {alcorcon.price} €.\nLa casa más cara de {leganes.level5} en {leganes.address} tiene un precio de {leganes.price} €.\nLa casa más cara de {getafe.level5} en {getafe.address} tiene un precio de {getafe.price} €."

###Historiograma de precios del Cinturon Sur###

def HistogramPriceCinturonSur(df):
    #Formula de normalización: x' = x-xmin/xmax-xmin
    fuenlabrada = df[df['level5'] == "Fuenlabrada"]
    fuenlabrada_scaled = scaler.fit_transform(fuenlabrada[['price']])
    alcorcon = df[df['level5'] == "Alcorcón"]
    alcorcon_scaled =scaler.fit_transform(alcorcon[['price']])
    leganes = df[df['level5'] == "Leganés"]
    leganes_scaled = scaler.fit_transform(leganes[['price']])
    getafe = df[df['level5'] == "Getafe"]
    getafe_scaled = scaler.fit_transform(getafe[['price']])

    #Creamos el Histograma

    plt.figure(figsize=(10,5))
    plt.hist([fuenlabrada_scaled, alcorcon_scaled, leganes_scaled, getafe_scaled], bins=30, alpha=0.8, label="Fuenlabrada")
    plt.hist(alcorcon_scaled,bins=30, alpha=0.8, label="Alcorcón")
    plt.hist(leganes_scaled, bins=30, alpha=0.8, label="Leganés")
    plt.hist(getafe_scaled, bins=30, alpha=0.8, label="Getafe")

    plt.legend()
    plt.show()

    return None

###Precio medio/m2 Getafe y Alcorcón###

def PricePerSquareGetafeAndAlcorcon(df):
    #Creamos la columna pps
    pps = float(df.price / df.surface)
    df['pps'] = pps

    getafe = df[df['level5'] == "Getafe"]
    getafe_scaled = scaler.fit_transform([['pps']])
    alcorcon = df[df['level5'] == "Alcorcón"]
    alcorcon_scaled = scaler.fit_transform([['pps']])
    

    return None

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
#print (IsValdemorilloAndGalapagarMeanEqual(df_estates))

#Ejercicio10
#print (IsValdemorilloAndGalapagarMeanPPSEqual(df_estates))

#Ejercicio11
#print (RelPriceSurface(df_estates))

#Ejercicio12
#print (HowManyRealEstatesAre(df_estates))

#Ejercicio13
#print(HowCityHaveMoreHouses(df_estates))

#Ejercicio14
CinturonSur(df_estates)

#Ejercicio15
#print(CinturonSurMeanPrice(CinturonSur(df_estates)))

#Ejercicio16
#print (MeanAndVar(CinturonSur(df_estates)))

#Ejercicio17
#print (HowIsMostExpensiveHouse(CinturonSur(df_estates)))

#Ejercicio18
#print(HistogramPriceCinturonSur(CinturonSur(df_estates)))

#Ejercicio19
print (PricePerSquareGetafeAndAlcorcon(CinturonSur(df_estates)))
