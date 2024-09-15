import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler #Normalizar datos con la funcion MinMaxScaler
from ipyleaflet import Map, basemaps, Marker #Mapas

# Este archivo CSV contiene puntos y comas en lugar de comas como separadores
df_estates = pd.read_csv('assets/real_estate.csv', sep=';')
df_estates

###Ejercicio 1: Imprimir dirección de la casa más cara###

def HighPrice(highprice):
    #Cogemos el valor más grande de la columna Price (El ultimo en este caso) y lo convertimos en una Serie con squeeze para trabajarlo mejor.
    highprice_house = highprice.sort_values('price').tail(1).squeeze()
    print (f"La casa con dirección {highprice_house['address']},{highprice_house['level5']} es la más cara y su precio es de {highprice_house['price']} €.")

print (HighPrice(df_estates))

###Ejercicio 2: Imprimir dirección de la casa más barata###

def LowPrice(lowprice):
    lowprice_house = lowprice.sort_values('price').head(1).squeeze()
    print (f"La casa con dirección en {lowprice_house['address']}, {lowprice_house['level5']} es la más barata y su precio es de {lowprice_house['price']} €.")

print (LowPrice(df_estates))


###Ejercicio 3: Imprimimos la casa más grande y la más pequeña###

def MoreSurface(moresurface):
    moresurface_house = moresurface.sort_values('surface').tail(1).squeeze()
    print (f"La casa más grande está en {moresurface_house['address']}, {moresurface_house['level5']} y su superficie es de {moresurface_house['surface']} metros.")

def LessSurface(lesssurface):
    lessfurface_house = lesssurface.sort_values('surface').head(1).squeeze()
    print (f"La casa más pequeña está en {lessfurface_house['address']}, {lessfurface_house['level5']} y su superficie es de {lessfurface_house['surface']} metros.")

print (MoreSurface(df_estates))
print (LessSurface(df_estates))

###Ejercicio 4: Nombre de las poblaciones###

def Populations(populations):
    counter = len(populations.level5)
    list_populations = list()
    for i in range(counter):
        list_populations.append(populations.level5[i])
    
    #Agrupamos los valores únicos.
    list_populations = np.unique(list_populations)
    
    return list_populations

for pop in (Populations(df_estates)):
    print (pop, end=", ")

###Ejercicio 5: Comprobar si hay valores no admitidos en la lista ###

def NanIdentificy(value):
    print (value.isnull().any())
    print (value.isnull().any(axis=1))

print (NanIdentificy(df_estates))

###Ejercicio 6: Eliminar los NAs del dataset###

def Filter(value):
   df_filter = value.dropna(axis=1)
   return df_filter

print(Filter(df_estates).shape)
print(df_estates.shape)

###Ejercicio 7: Media de precios de Arroyomolinos###

def MeanPrice(dataset, city):
    dataset_city = dataset[dataset['level5'] == city]
    return dataset_city.price.mean()

print (MeanPrice(df_estates, "Arroyomolinos (Madrid)"))

###Ejercicio 8: Historiograma de los precios de Arroyomolinos###

def HistogramPriceCity(dataset, city):
    plt.figure (figsize=(10,5))
    plt.hist (dataset[dataset['level5'] == city].price, bins=30, alpha=1, ec="black")
    plt.title (f"Precios de {city}")
    plt.show()

print (HistogramPriceCity(df_estates,"Arroyomolinos (Madrid)"))

###Ejercicio 9: Comprobar si el precio promedio de Valdemorillo y de Galapagar son el mismo###

print (MeanPrice(df_estates,"Valdemorillo"))
print (MeanPrice(df_estates,"Galapagar"))
print (MeanPrice(df_estates,"Valdemorillo") == MeanPrice(df_estates,"Galapagar"))

###Ejercicio 10: Comprobar si el precio/m2 promedio de Valdemorillo y Galapagar son el mismo###

def ColumnPPS(dataset):
    pps = dataset.price / dataset.surface
    dataset ['pps'] = pps
    return dataset

dfwith_pps = ColumnPPS(df_estates)

def MeanPPS(dataset, city):
    pps_datasetCity = dataset[dataset['level5'] == city]
    return pps_datasetCity.pps.mean()

print (MeanPPS(dfwith_pps, "Valdemorillo"))
print (MeanPPS(dfwith_pps, "Galapagar"))
print (MeanPPS(dfwith_pps,"Valdemorillo") == MeanPPS(dfwith_pps,"Galapagar"))
  
###Ejercicio 11: Analizamos la relación entre el precio y la superficie de las casas.###

def DataSetCity(dataset, city):
    datacity = dataset[dataset['level5'] == city]
    return datacity

df_valdemorillo = DataSetCity(df_estates, "Valdemorillo")
df_galapagar = DataSetCity(df_estates, "Galapagar")

def RelPriceSurfaceTwoCities(dataset1, dataset2, city1, city2):
    plt.figure(figsize=(10,5))
    plt.scatter(dataset1.price, dataset1.surface, label = city1)
    plt.scatter(dataset2.price, dataset2.surface, label = city2)
    plt.title("Relación Superficie/Precio")
    plt.legend()
    plt.show()

print (RelPriceSurfaceTwoCities(df_valdemorillo, df_galapagar, "Valdemorillo", "Galapagar"))

###Ejercicio 12: Buscamos cuantas agencias contiene el DataSet###
def HowManyRealEstatesAre(value):
    return len(value.id_realEstates.unique()) #Imprimimos solamente los valores unicos.

print (HowManyRealEstatesAre(df_estates))

###Ejercico 13: Buscamos la población con más cantidad de casas###

def HowCityHaveMoreHouses(data):
    city = data.level5.value_counts().head(1) #Aquí contamos las veces que un valor se repite y cogemos el primero
    houses = data.level5.value_counts().sum()
    print (city, houses)

print (HowCityHaveMoreHouses(df_estates))

###Ejercicio 14: Creamos un nuevo DataFrame que contenga Fuenlabrada, Leganes, Getafe y Alcorcón"###

def CityFilter(dataset, city1, city2, city3, city4):
    filt_cities =dataset['level5'].isin([city1,city2,city3,city4])
    new_dataset = dataset[filt_cities].reset_index()
    return new_dataset

cinturonsur = CityFilter(df_estates, "Fuenlabrada","Leganés","Getafe","Alcorcón")
print (cinturonsur)

###Ejercicio 15: Grafico de barra de la mediana de los precios de Cinturon Sur###

def MultiCityMeanPrice(dataset, city1, city2, city3, city4):
    labels = [city1, city2, city3, city4]
    city1 = dataset[dataset['level5'] == city1].price.mean()
    city2 = dataset[dataset['level5'] == city2].price.mean()
    city3 = dataset[dataset['level5'] == city3].price.mean()
    city4 = dataset[dataset['level5'] == city4].price.mean()
    values = (city1, city2, city3, city4)
    plt.figure(figsize=(10,5))
    plt.bar(labels, values, ec="black")

    plt.title("Precios Medios Cinturón Sur")
    plt.show()

print(MultiCityMeanPrice(cinturonsur, "Fuenlabrada","Leganés","Getafe","Alcorcón")) 

###Ejercicio 16: Calcula la medía y la varianza de muestra del Cinturón Sur###

def Variance(dataset, value):
    return dataset[value].var(ddof = 0)

def Mean(dataset, value):
    return dataset[value].mean()

print (f"Varianza del precio: {Variance(cinturonsur,'price')}")
print (f"Media de precios: {Mean(cinturonsur,'price')}")
print (f"Varianza de las habitaciones: {Variance(cinturonsur,'rooms')}")
print (f"Media de las habitaciones: {Mean(cinturonsur,'rooms')}")
print (f"Varianza de la superficie: {Variance(cinturonsur,'surface')}")
print (f"Media de la superficie: {Mean(cinturonsur,'surface')}")
print (f"Varianza de los baños: {Variance(cinturonsur,'bathrooms')}")
print (f"Media de baños: {Mean(cinturonsur, 'bathrooms')}")

###Ejercicio 17: Cual es la casa más cara de cada población###

def MostExpensiveHousePerCity(dataset, city):
    expensivehouse = dataset[dataset['level5'] == city].sort_values('price').tail(1).squeeze() #Squeeze sirve para eliminar dimensiones en una matriz.
    print (f"{city}. Precio: {expensivehouse.price}. Dirección: {expensivehouse.address}")

print (MostExpensiveHousePerCity(cinturonsur, "Fuenlabrada"))
print (MostExpensiveHousePerCity(cinturonsur, "Alcorcón"))
print (MostExpensiveHousePerCity(cinturonsur, "Leganés"))
print (MostExpensiveHousePerCity(cinturonsur, "Getafe"))

###Ejercicio 18: Historiograma de precios del Cinturon Sur###

scaler=MinMaxScaler() #Para poder normalizar datos. Formula de normalización: x' = x-xmin/xmax-xmin

def NormalicePriceCity(dataset,city):
    datacity = dataset[dataset['level5'] == city]
    price_scaled = scaler.fit_transform(datacity[['price']])
    return price_scaled

    #Creamos el Histograma

def MultigramaPricesNormalized(dataset, city1, city2, city3, city4):
    plt.figure(figsize = (10, 5))
    plt.hist(NormalicePriceCity(dataset, city1), bins=30, alpha=0.8, ec="Black", label=city1)
    plt.hist(NormalicePriceCity(dataset, city2), bins=30, alpha=0.8, ec="Black", label=city2)
    plt.hist(NormalicePriceCity(dataset, city3), bins=30, alpha=0.8, ec="Black", label=city3)
    plt.hist(NormalicePriceCity(dataset, city4), bins=30, alpha=0.8, ec="Black", label=city4)

    plt.legend()
    plt.show()

print (MultigramaPricesNormalized(cinturonsur,"Fuenlabrada","Alcorcón","Leganés","Getafe"))

### Ejercicio 19: Precio medio/m2 Getafe y Alcorcón###

def HistTwoCitiesPPS(dataset, city1, city2):
    plt.figure(figsize=(10,5))
    plt.title(f"Precio por metro cuadrado entre {city1} y {city2}.")
    plt.subplot(1,2,1)
    plt.hist(dataset[dataset['level5'] == city1].pps, bins=30, alpha=0.8, ec="black", label=city1)
    plt.legend()
    plt.subplot(1,2,2)
    plt.hist(dataset[dataset['level5'] == city2].pps, bins=30, alpha=0.8, ec="black", label=city2)
    plt.legend()
    plt.show()
    
print(HistTwoCitiesPPS(dfwith_pps, "Getafe", "Alcorcón"))

###Ejercicio 20: 4 subconjuntos en un grafico. ###

def MultiGrafic(dataset, city1,city2,city3,city4):
    plt.figure(figsize=(10,10))
    plt. title("Gráfica de dispersión precio/superficie")
    plt.subplot(2,2,1)
    plt.scatter((dataset[dataset['level5'] == city1].price),(dataset[dataset['level5'] == city1].surface), label = city1, color="red")
    plt.legend()
    plt.subplot(2,2,2)
    plt.scatter((dataset[dataset['level5'] == city2].price),(dataset[dataset['level5'] == city2].surface), label = city2, color="blue")
    plt.legend()
    plt.subplot(2,2,3)
    plt.scatter((dataset[dataset['level5'] == city3].price),(dataset[dataset['level5'] == city3].surface), label = city3, color="green")
    plt.legend()
    plt.subplot(2,2,4)
    plt.scatter((dataset[dataset['level5'] == city4].price),(dataset[dataset['level5'] == city4].surface), label = city4, color="orange")
    plt.legend()
    plt.show()
  

print (MultiGrafic(cinturonsur, "Fuenlabrada", "Leganés", "Getafe", "Alcorcón"))

###Ejercicio 21: Mapa
# Mapa centrado en (60 grados latitud y -2.2 grados longitud)
# Latitud, longitud
mapa = Map(center = (60 , -2.2), zoom = 2, min_zoom = 1, max_zoom = 20, 
    basemap = basemaps.OpenTopoMap)
## Aquí: traza la coordenadas de los estados
def GetCoordinatesDict(dataset):
    return dataset[['latitude','longitude']].to_dict()

coordenadas = GetCoordinatesDict(cinturonsur)

def AddMarker(dataset):
    for i in range(len(dataset['latitude'])):
        marker = Marker(location=(dataset["latitude"][i],dataset["longitude"][i]))
        mapa.add(marker)

print(AddMarker(coordenadas))
display (mapa)