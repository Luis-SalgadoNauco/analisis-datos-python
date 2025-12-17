# Análisis de Datos con Python – Días 1, 2 y 3

## Descripción
Proyecto introductorio de análisis de datos usando Python.  
Corresponde a los Días 1, 2 y 3 del módulo de Python dentro del curso de Análisis de Datos.

El proyecto cubre la configuración del entorno de trabajo y la extracción de datos desde múltiples fuentes utilizadas comúnmente en contextos reales de análisis de datos.

---

## Objetivos
- Configurar un entorno de análisis de datos con Python
- Utilizar entornos virtuales para aislar dependencias
- Instalar y verificar librerías esenciales
- Extraer datos desde múltiples fuentes heterogéneas
- Convertir distintas fuentes en DataFrames de Pandas
- Versionar y documentar el trabajo usando Git y GitHub
- Diagnosticar problemas de calidad de datos
- Limpiar y transformar datos para su análisis

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

## Estructura del proyecto

```text
analisis-datos-python/
├── analisis_datos_dia1.ipynb
├── dia2_extraccion_fuentes.ipynb
├── dia3_limpieza_y_transformacion_datos.ipynb
├── comparacion_limpieza_dia3.xlsx
├── test_analisis.py
├── primer_grafico.png
├── ventas.csv
├── datos.xlsx
├── productos.json
├── ventas.db
├── README.md
├── .gitignore
```