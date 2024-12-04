# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Datos clave de nuestro corpus

- Nuestro corpus es el antigüo testamento de la Biblia. Específicamente la versión King James (KJV).
- Al ser esta una versión anglosajona de la biblia, nuestro corpus está completamente en idioma inglés.
- Un Documento para nosotros es un versículo de la Biblia.
- El tamaño del corpus es 4.22 MB.
- Nuestro corpus contiene, inicialmente y sin preprocesamiento adicional, 24.606 documentos.
- Todos los documentos tienen una relación ya que pertenecen al mismo texto. 
- Adicionalmente están organizados de forma secuencial de forma que componen una estructura más grande.

## Resumen de calidad de los datos

- En un principio No hay datos faltantes, además los datos vienen de Kaggle, que garantiza cierta calidad de los datos.
- El número de documentos de nuestro corpus que cambia al codificarlo con unidecode es: 1,724. El principal caracter que hace que al codificarlo cambie es el símbolo <’>.
- Dado que la Biblia fue completamente traducida en inglés no hay mezcla de idiomas.

## Variable objetivo [TODO]

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

## Variables individuales [TODO]

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables [TODO]

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo [TODO]

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
