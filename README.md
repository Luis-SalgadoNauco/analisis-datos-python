# Análisis de Datos con Python – Días 1, 2, 3, 4 y 5

## Descripción
Proyecto introductorio de análisis de datos usando Python.  
Corresponde a los Días 1, 2, 3, 4 y 5 del módulo de Python dentro del curso de Análisis de Datos.

El proyecto cubre la configuración del entorno de trabajo, la extracción, limpieza, transformación y análisis de datos, utilizando múltiples fuentes y técnicas comunes en contextos reales de análisis de datos.

---

## Objetivos
- Configurar un entorno de análisis de datos con Python
- Utilizar entornos virtuales para aislar dependencias
- Instalar y verificar librerías esenciales
- Extraer datos desde múltiples fuentes heterogéneas
- Convertir distintas fuentes en DataFrames de Pandas
- Diagnosticar problemas de calidad de datos
- Limpiar y transformar datos para su análisis
- Aplicar filtrado avanzado para responder preguntas analíticas
- Analizar datos por categorías mediante agregaciones
- Combinar múltiples conjuntos de datos para generar análisis integrales
- Versionar y documentar el trabajo usando Git y GitHub

---

## Tecnologías utilizadas
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- SQLite
- Jupyter Notebook
- Git & GitHub

---

## Fuentes de datos trabajadas (Día 2)
- Archivos CSV
- Archivos Excel con múltiples hojas
- Archivos JSON
- Base de datos SQLite
- API REST simulada (estructura tipo JSON)

---

## Día 3 – Diagnóstico, Limpieza y Transformación de Datos

En este día se trabajó con un conjunto de datos que contenía problemas comunes de calidad, aplicando un flujo sistemático de limpieza y transformación de datos utilizando Pandas y NumPy.

### Problemas identificados
- Registros duplicados
- Tipos de datos incorrectos (edad como texto)
- Inconsistencias en nombres y departamentos
- Capitalización irregular

### Técnicas aplicadas
- Diagnóstico con `df.dtypes`, `df.duplicated()`, `df.unique()`
- Eliminación de duplicados con `drop_duplicates()`
- Conversión de tipos con `pd.to_numeric()`
- Normalización de texto con `.str.title()`
- Creación de columnas calculadas

### Transformaciones
- Cálculo de salario mensual
- Categorización de edad (Joven, Adulto, Senior)

### Evidencia de limpieza de datos
Se generó un archivo Excel con dos hojas:

- **datos_originales**: datos con problemas de calidad
- **datos_limpios**: datos depurados y transformados

Este archivo permite comparar el estado inicial y final del conjunto de datos.

Archivo:
- `comparacion_limpieza_dia3.xlsx`

---
## Día 4 – Filtrado Avanzado, Agrupación y Unión de Datos

En este día se profundizó en técnicas de análisis de datos orientadas a la exploración avanzada y la combinación de múltiples conjuntos de datos, utilizando operaciones clave de Pandas.

### Filtrado avanzado de datos
Se aplicaron filtros complejos para seleccionar información relevante:

- Filtrado con `query()` usando sintaxis legible y similar a SQL
- Uso de variables externas en consultas
- Filtrado por rangos de fechas y valores numéricos
- Indexación booleana con máscaras lógicas
- Selección condicional de filas y columnas con `.loc[]`

### Agrupación y agregación con GroupBy
Se realizó análisis por categorías aplicando el patrón **Split – Apply – Combine**:

- Agrupación de ventas por producto y cliente
- Cálculo de sumas, promedios y conteos
- Agregaciones múltiples con `.agg()`
- Análisis de métricas consolidadas por grupo
- Identificación de clientes con mayor volumen de compras

### Unión de conjuntos de datos (Merge)
Se combinaron múltiples fuentes de datos para generar análisis integrales:

- Unión de ventas con productos
- Unión posterior con información de clientes
- Cálculo de montos totales por venta
- Análisis final de ventas por ciudad y cliente

### Evidencia del análisis
Se generó un archivo Excel con múltiples hojas que contiene los resultados intermedios y finales del ejercicio práctico, permitiendo revisar cada etapa del análisis.

Archivo:
- `ejercicio_dia4_analisis_completo.xlsx`

Notebook:
- `dia4_filtrado_groupby_merge.ipynb`

---

## Día 5 – Manejo de Datos Faltantes y Valores Atípicos

En este día se trabajó un pipeline completo de preparación de datos enfocado en dos de los problemas más críticos del análisis de datos: **datos faltantes (missing values)** y **valores atípicos (outliers)**.

### 1. Detección y análisis de datos faltantes
Se analizaron patrones y magnitudes de datos faltantes considerando su impacto analítico:

- Identificación de valores nulos con `isnull()` y `info()`
- Cálculo de porcentajes de datos faltantes por columna
- Análisis de patrones de missing values por departamento
- Visualización de valores faltantes utilizando la librería `missingno`

Se discutieron los tipos de datos faltantes:
- MCAR (Completamente al azar)
- MAR (Al azar)
- MNAR (No al azar)

### 2. Estrategias de imputación
Se aplicaron distintas técnicas de imputación según el tipo de variable y el contexto analítico:

- Imputación por **media** para `horas_trabajo`
- Imputación por **mediana** para `salario`, por su robustez frente a outliers
- Verificación posterior de ausencia total de valores faltantes

### 3. Detección de valores atípicos (outliers)
Se identificaron outliers mediante métodos estadísticos:

- Método del **Rango Intercuartílico (IQR)**
- Comparación de la cantidad de outliers antes y después del tratamiento
- Análisis del impacto de los valores extremos en estadísticas descriptivas

### 4. Manejo de valores atípicos
Se aplicaron estrategias diferenciadas según la variable:

- **Horas de trabajo**: capping de valores máximos en 60 horas
- **Salario**: transformación logarítmica (`log1p`) para reducir asimetría y el impacto de valores extremos

Se verificó la efectividad mediante:
- Estadísticas descriptivas antes y después
- Reducción del número de outliers
- Visualización con boxplots comparativos

### Evidencia del ejercicio
Se generó un archivo Excel con múltiples hojas que documenta todo el proceso:

Archivo:
- `ejercicio_dia5_missing_outliers.xlsx`

Notebook:
- `dia5_missing_y_outliers.ipynb`
---

## Estructura del proyecto

```text
analisis-datos-python/
├── analisis_datos_dia1.ipynb
├── dia2_extraccion_fuentes.ipynb
├── dia3_limpieza_y_transformacion_datos.ipynb
├── dia4_filtrado_groupby_merge.ipynb
├── dia5_missing_y_outliers.ipynb
├── comparacion_limpieza_dia3.xlsx
├── ejercicio_dia4_analisis_completo.xlsx
├── ejercicio_dia5_missing_outliers.xlsx
├── boxplot_salario_outliers_dia5.png
├── test_analisis.py
├── primer_grafico.png
├── ventas.csv
├── datos.xlsx
├── productos.json
├── ventas.db
├── README.md
├── .gitignore
```