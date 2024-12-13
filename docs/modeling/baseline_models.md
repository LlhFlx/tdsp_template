# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores. Este modelo se basa en un pipeline de transformers para análisis de sentimientos.

### Implementación del modelo

El modelo utiliza la librería transformers de Hugging Face y un pipeline preentrenado para la tarea de análisis de sentimientos. La implementación incluye las siguientes etapas:

- Importar el pipeline de la librería ```transformers```.

- Crear una instancia del pipeline con la tarea de "sentiment-analysis".

- Analizar como entrada versos de la Biblia, por ejemplo: "The Lord is my shepherd; I shall not want."

El pipeline predice la polaridad del sentimiento (positivo o negativo) y su correspondiente puntuación.

## Variables de entrada

Lista de las variables de entrada utilizadas en el modelo:

Versos de la Biblia en formato de texto. Ejemplo:

- "The Lord is my shepherd; I shall not want."

- "I can do all things through Christ who strengthens me."

## Variable objetivo

La variable objetivo utilizada en el modelo es la polaridad del sentimiento, que puede tomar los valores:

```POSITIVE```: Indica un sentimiento positivo.

```NEGATIVE```: Indica un sentimiento negativo.

Adicionalmente, se proporciona una puntuación de confianza asociada al sentimiento predicho.

## Evaluación del modelo

### Métricas de evaluación

Métricas de evaluación

Las métricas utilizadas para evaluar el rendimiento del modelo baseline incluyen:

Precisión (Accuracy): Proporción de predicciones correctas respecto al total de predicciones.

Confianza promedio: Promedio de las puntuaciones de confianza proporcionadas por el modelo para las predicciones.

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

## Conclusiones

La idea de que los versos tienen diferentes connotaciones de sentimiento cuando se interpretan por separado, en comparación con cuando se toman en conjunto, refleja un fenómeno interesante en la interpretación automática del lenguaje natural. Esto se puede observar en los resultados del análisis de sentimiento aplicado a los versos bíblicos.

Ejemplo de interpretación:

Verso individual: Cuando el verso "The Lord is my shepherd; I shall not want." se analiza por separado, el modelo de sentimiento lo clasifica como negativo con un 99% de certeza. Sin embargo, este verso en su contexto espiritual puede ser visto como un mensaje de tranquilidad y seguridad, lo que sugiere que el modelo no logra capturar la tonalidad positiva al estar descontextualizado.

Versos en conjunto: Cuando se toman varios versos en conjunto, como en "The Lord is my shepherd; I shall not want. He maketh me to lie down in green pastures: he leadeth me beside the still waters...", el modelo lo clasifica como positivo con un (casi) 98% de certeza. En este caso, el modelo es más capaz de captar el tono global de paz y protección que proviene de la sumatoria de todos los versos, probablemente debido a que se proporcionan más pistas contextuales que generan una interpretación más precisa.

## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.

