# Diccionario de datos

## Base de datos 1

| **Variable**            | **Descripción**                                                                 | **Tipo de dato**   | **Rango/Valores posibles**             | **Fuente de datos**                   |
|--------------------------|-------------------------------------------------------------------------------|--------------------|-----------------------------------------|---------------------------------------|
| **verse**               | Texto del versículo original.                                                | Texto (`object`)   | Cualquier cadena de caracteres.         | Dataset público de Kaggle.           |
| **has_invalid_chars**   | Indica si el versículo contiene caracteres inválidos o no reconocidos.        | Booleano (`bool`)  | `True`, `False`.                        | Procesamiento propio.                |
| **chars_length**        | Longitud total del versículo en caracteres.                                  | Entero (`int64`)   | Mayor o igual a `0`.                    | Procesamiento propio.                |
| **chars_length_cat**    | Categoría basada en la longitud del versículo en caracteres.                 | Categórico         | `Corto`, `Medio`, `Largo`, etc.         | Procesamiento propio.                |
| **cleaned_verses**      | Texto del versículo después de ser limpiado y preprocesado.                  | Texto (`object`)   | Cualquier cadena de caracteres.         | Procesamiento propio.                |
| **verse_length**        | Longitud en palabras del versículo original.                                 | Entero (`int64`)   | Mayor o igual a `0`.                    | Procesamiento propio.                |
| **cleaned_verse_length**| Longitud en palabras del versículo limpio.                                   | Entero (`int64`)   | Mayor o igual a `0`.                    | Procesamiento propio.                |
| **NER_entities**        | Entidades nombradas identificadas en el versículo.                          | Texto (`object`)   | Lista de entidades en formato de texto. | Modelo de Reconocimiento de Entidades. |
| **sentiment_label**     | Clasificación de sentimiento del versículo (positivo, negativo, neutro).     | Texto (`object`)   | `positivo`, `negativo`, `neutro`.       | Modelo de Análisis de Sentimiento.   |
| **sentiment_score**     | Puntuación numérica asociada al sentimiento del versículo.                   | Decimal (`float64`)| Rango continuo (-1 a 1).                | Modelo de Análisis de Sentimiento.   |

### Notas adicionales:  
- **Datos nulos:** Ninguna de las columnas contiene valores nulos, asegurando la integridad de los datos.  
- **Fuentes:** Los datos originales provienen de un dataset público de Kaggle, mientras que las variables derivadas han sido generadas mediante preprocesamiento y modelos de PLN (Procesamiento de Lenguaje Natural).  
- **Objetivo:** Estas variables permiten realizar análisis avanzados de los textos religiosos, como identificación de entidades y evaluación de emociones/sentimientos.  
