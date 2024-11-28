# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Análisis de Entidades y Sentimientos en Textos Bíblicos con Procesamiento de Lenguaje Natural

## Objetivo del Proyecto

Desarrollar y evaluar un modelo eficiente de procesamiento de lenguaje natural (PLN) para el reconocimiento de entidades nombradas y análisis de sentimiento en los textos del Antiguo Testamento de la Biblia versión King James (KJV). Se busca facilitar la extracción de información clave y el análisis académico de estos textos, contribuyendo al trabajo de historiadores, teólogos, lingüistas y particulares interesados en su estudio. Este proyecto es importante porque permitirá automatizar tareas complejas y no triviales, optimizando los procesos de investigación y análisis.

## Alcance del Proyecto

### Incluye:

- Datos disponibles
  1. Textos bíblicos provenientes del dataset público de Kaggle.
  2. Cada fila del archivo `.csv` contiene un versículo del Antiguo Testamento en inglés (versión KJV).

- Resultados esperados
  1. Modelos de PLN capaces de identificar entidades nombradas (personajes, lugares, eventos) dentro de los textos bíblicos.
  2. Análisis de sentimiento que clasifique pasajes selectos en categorías como positivo, negativo o neutral, reflejando el tono general del texto.
  3. Comparación del desempeño de modelos clásicos, modelos propios, y un modelo de lenguaje grande (`LLM`).
     
- Criterios de éxito del proyecto
  1. Implementación de un modelo con métricas satisfactorias en tareas de reconocimiento de entidades nombradas (`precisión`, `recall`, `F1 score`).
  2. Generación de análisis de sentimiento coherente con el contexto del texto bíblico.
  3. Disponibilidad de una solución final que sea útil para los beneficiarios, con documentación clara y resultados reproducibles.

### Excluye:

1. Textos que no pertenezcan al Antiguo Testamento de la versión King James (KJV) en inglés.
2. Traducciones adicionales o análisis en otros idiomas.
3. Investigación profunda de las diferencias teológicas o interpretativas entre tradiciones religiosas, más allá del análisis técnico de los textos.

## Metodología
En este proyecto se usará la metodología CRISP-DM (Cross Industry Standard Process for Data Mining), que proporciona un enfoque estructurado y sistemático para proyectos basados en datos, y se compone por las siguientes fases:
- Entendimiento del negocio
- Entendimiento de los datos
- Preparación de los datos
- Análisis de datos
- Visualización de información y entrega final

## Cronograma

| **Etapa**                                      | **Duración Estimada** | **Fechas**               | **Descripción**                                                                                                                                  |
|------------------------------------------------|------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Entendimiento del negocio y carga de datos** | 1 semana             | del 21 al 28 ed noviembre | Reunión con beneficiarios para definir objetivos y necesidades. Descarga del dataset de Kaggle. Validación inicial de la calidad y formato de los datos. |
| **Preprocesamiento y análisis exploratorio**   | 1 semana             | del 28 de noviembre al 5 de diciembre | Limpieza del dataset (normalización, eliminación de ruido). Exploración de patrones en los textos (frecuencia de palabras, longitud promedio de versículos). Preparación de datos para modelado. |
| **Modelamiento y extracción de características** | 1 semana             | del 5 de diciembre al 12 de diciembre | Implementación y ajuste de diferentes modelos de PLN (NER y análisis de sentimiento). Comparación de enfoques clásicos y modernos (CRF, BERT, LLMs). |
| **Evaluación y optimización de modelos**       | 1 semana             | ... | Evaluación de métricas de desempeño (precisión, recall, F1). Optimización del modelo seleccionado según los resultados. Validación con un conjunto de prueba. |
| **Despliegue e implementación**               | 1 semana             | ... | Generación de documentación para usuarios finales y entrega del producto final.                                             |

## Equipo del Proyecto

- Andrés Díaz
- Leonardo Delgado
- Fellhipe Gutierrez

## Presupuesto

El presupuesto actual, dado que es un proyecto académico, puede estimarse como la cantidad de horas multiplicado el valor hora de cada uno de los miembros del equipo.

Son 5 semanas, cada semana con una dedicación horaria de 10 horas.
10 horas x 5 semanas x 3 integrantes x 150.000 COP / hora = 22.500.000 COP

## Stakeholders

- [Nombre y cargo de los stakeholders del proyecto]
- [Descripción de la relación con los stakeholders]
- [Expectativas de los stakeholders]

## Aprobaciones

- [Nombre y cargo del aprobador del proyecto]
- [Firma del aprobador]
- [Fecha de aprobación]
