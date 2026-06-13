# Project-UCG
Proyecto Final de Universidad Casa Grande

# Plataforma Web Interactiva para Análisis Exploratorio de Datos (EDA)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Reactivo-FF4B4B.svg)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75.svg)](https://plotly.com)
[![UCG](https://img.shields.io/badge/UCG-Proyecto%20Final-003366.svg)](#)

Este repositorio contiene el código fuente y la arquitectura lógica de la **Plataforma Web Interactiva para la Carga, Exploración, Análisis y Visualización Automatizada de Datos Estructurados**. Este proyecto ha sido desarrollado como el entregable integrador final aplicando los conocimientos de Ciencia de Datos bajo las directrices académicas de la **Universidad de Ciencias de la Gestión (UCG)**.

La aplicación automatiza de forma centralizada las tareas críticas de un Análisis Exploratorio de Datos (EDA), transformando scripts tradicionales en un entorno interactivo basado en la nube para auditar la calidad, completitud y comportamiento estadístico de cualquier dataset en formato CSV.
---
## 🚀 Enlaces de Acceso Obligatorios

* **Aplicación en Producción (Streamlit Cloud):** [Acceder a la Plataforma Web](https://tu-app-url.streamlit.app) *(Sustituir con tu enlace real)*
* **Código Fuente (Repositorio GitHub):** [Ver Repositorio de Código](https://github.com/tu-usuario/tu-repositorio) *(Sustituir con tu enlace real)*

---

## ✨ Características y Funcionalidades del Sistema

La interfaz gráfica ha sido organizada mediante pestañas horizontales (`st.tabs`) para optimizar el flujo analítico y la experiencia visual del usuario final, incorporando las siguientes capacidades técnicas:

1. **📁 Módulo de Carga Inteligente (`st.file_uploader`):** Permite arrastrar y cargar archivos planos en formato `.csv`. Implementa un control de contingencia que carga automáticamente un dataset predeterminado (`material.csv`) en caso de no suministrarse un archivo propio, garantizando la disponibilidad del software.
2. **📊 Panel de Exploración Estructural:** Calcula dinámicamente las dimensiones totales del dataset (conteo exacto de filas y columnas), realiza el mapeo de tipos de datos por columna y despliega una previsualización tabular interactiva del conjunto de datos.
3. **🔍 Auditoría de Completitud y Calidad:** Cuantifica y visualiza la tasa de registros nulos o valores faltantes por campo, permitiendo identificar anomalías e inconsistencias críticas antes de la toma de decisiones analíticas.
4. **📈 Visualizaciones Interactivas (Plotly Express):** Renderiza diagramas de frecuencias estadísticas e histogramas reactivos dotados de funciones nativas de zoom, aislamiento de trazas y etiquetas flotantes (*tooltips*), unificados bajo una paleta de colores corporativa (Azul y Gris).
5. **⚙️ Programación Defensiva y Optimización:** Incorpora bloques de captura de excepciones (`try-except`) para neutralizar fallas críticas de lectura de archivos y utiliza decoradores de almacenamiento en caché (`@st.cache_data`) para minimizar los tiempos de respuesta del servidor.

---

## 🛠️ Arquitectura y Stack Tecnológico

El ecosistema de software se fundamenta en las siguientes tecnologías de computación científica:

| Componente | Tecnología | Propósito Técnico en el Proyecto |
| :--- | :--- | :--- |
| **Lenguaje** | Python 3.9+ | Lenguaje de programación base para la lógica de ciencia de datos. |
| **Frontend/Web** | Streamlit | Framework reactivo para la construcción de la interfaz web nativa. |
| **Procesamiento** | Pandas | Backend especializado en la manipulación y cálculo tabular del DataFrame. |
| **Gráficos** | Plotly Express | Librería declarativa de alto nivel para representaciones web interactivas. |

