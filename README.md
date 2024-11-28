# MLDS 6 ~ Metodologías Ágiles para el Desarrollo de Aplicaciones con Machine Learning

## Autores
- Fellhipe Gutierrez
- Santiago Delgado  
- Andrés Díaz

## Team Data Science Project Template

Esta plantilla es una implementación de la plantilla de proyecto de Team Data Science Process que actualmente se utiliza en el "Programa de Formación en Machine Learning y Data Science" en la Universidad Nacional de Colombia.

Esta plantilla proporciona las siguientes carpetas y archivos:

* `src`: acá debe ir el código o implementación del proyecto en Python.
* `docs`: en esta carpeta se encuentran las plantillas de los documentos definidos en la metodología.
* `scripts`: esta carpeta debe contener los scripts/notebooks que se ejecutarán.
* `pyproject.toml`: archivo de definición del proyecto en Python.



## Para ejecutar el proyecto:
1. Ejecutar el script `setup.sh`, el cual creará el ambiente virtual de python e instalará las dependencias encesarias. Tenga en cuenta que debe tener python en su sistema, y ajustar el script como lo indica el archivo dependiendo si su sistema operativo es Windows o Unix.

2. Para obtener los datos ejecute el script `get_data_from_kaggle.sh`. Los archivos se guardarán en el directorio `data`. Una vez que el directorio tenga los dos archivos csv (la biblia y el corán), podrá ejecutar el `main.py` para cargar los datos

