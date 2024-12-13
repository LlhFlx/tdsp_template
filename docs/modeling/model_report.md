# Reporte del Modelo Final

## Resumen Ejecutivo

En este reporte se presenta un resumen de los resultados obtenidos del modelo final de análisis de sentimientos aplicado a versos bíblicos. Los resultados muestran cómo el modelo clasifica los sentimientos asociados a los versos individuales y cómo su interpretación cambia al analizarse en conjunto. Las principales métricas de evaluación revelan que el modelo alcanza altos niveles de certeza en sus clasificaciones individuales (hasta 99%), pero también evidencia limitaciones en la captación de matices contextuales.

## Descripción del Problema

El problema abordado consiste en analizar los sentimientos expresados en versos bíblicos, los cuales poseen un carácter poético y simbólico que introduce desafíos para los modelos automáticos de lenguaje natural. El objetivo principal es determinar si el modelo es capaz de interpretar correctamente los sentimientos a nivel individual y en conjunto, destacando las diferencias en la clasificación según el contexto. La justificación del modelo radica en explorar las limitaciones y fortalezas de las técnicas modernas de análisis de sentimientos frente a textos antiguos y complejos.

## Descripción del Modelo

El modelo utilizado es un clasificador de análisis de sentimientos entrenado en corpus de textos modernos. Este modelo asigna etiquetas de sentimiento (positivo o negativo) junto con un puntaje de certeza ("***score***") a cada texto analizado. La metodología consistió en aplicar el modelo a versos individuales y conjuntos de versos, evaluando sus resultados mediante una inspección cualitativa y cuantitativa de las clasificaciones.

Por ejemplo, el verso "*The Lord is my shepherd; I shall not want.*" fue clasificado como negativo con un 99% de certeza cuando se analizó de forma individual, pero como positivo al ser evaluado junto con otros versos que ofrecen un contexto más amplio.

## Evaluación del Modelo

Se utilizaron las siguientes métricas de evaluación:

**Precisión**: Alta precisión en la clasificación de sentimientos individuales.

**Interpretabilidad contextual**: Limitada capacidad del modelo para captar sentimientos positivos cuando los versos se presentan de forma aislada.

## Conclusiones y Recomendaciones

El análisis revela que:

- Fortalezas: El modelo tiene un alto nivel de precisión en clasificaciones individuales cuando el sentimiento es evidente y directo.

- Debilidades: El modelo falla en capturar el contexto completo de textos poéticos o simbólicos cuando se analizan de manera aislada.

### Recomendaciones:

- Entrenar el modelo con un corpus que incluya textos antiguos y religiosos para mejorar su sensibilidad hacia estos estilos literarios.

## Referencias

- Textos bíblicos (Reina-Valera 1960).

- Documentación del modelo de análisis de sentimientos.

