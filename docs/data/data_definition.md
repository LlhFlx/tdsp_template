# Definición de los datos

## Origen de los datos

Los textos que serán utilizados en el proyecto provienen del Antiguo Testamento de la Biblia versión King James (KJV) en inglés

Estos datos se encuentran disponibles en el dataset público alojado en Kaggle: [https://www.kaggle.com/datasets/patricklford/bible-and-quran-sentiment-analysis](https://www.kaggle.com/datasets/patricklford/bible-and-quran-sentiment-analysis)

## Especificación de los scripts para la carga de datos

Se cargan los datos a través del script main.py de la carpeta data_acquisition, para ello se sigue el siguiente procedimiento:

1. Con el bash ```get_data_from_kaggle.sh``` donde se descarga la carpeta .zip de la ruta de kaggle.

2. Con el script de python ```main.py``` se carga los archivos descargados de kaggle en dos dataframes de pandas.

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- [ ] Especificar la ubicación de los archivos de origen de los datos.
- [ ] Especificar la estructura de los archivos de origen de los datos.
- [ ] Describir los procedimientos de transformación y limpieza de los datos

La ruta de origen de la data es: [https://www.kaggle.com/datasets/patricklford/bible-and-quran-sentiment-analysis](https://www.kaggle.com/datasets/patricklford/bible-and-quran-sentiment-analysis) 


### Base de datos de destino

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.
