import os
import pandas as pd
import streamlit as st
import plotly.express as px  # Librería para gráficos interactivos corporativos

# ==============================================================================
# 1. CONFIGURACIÓN GLOBAL DE LA INTERFAZ
# ==============================================================================
st.set_page_config(
    page_title="Proyecto Final UCG", 
    page_icon="📊", 
    layout="wide"
)

# Inyección de estilos CSS para unificar la identidad visual (Azul y Gris)
st.markdown("""
    <style>
        /* Títulos principales en Azul Marino Corporativo */
        h1 {
            color: #1E3A8A !important;
            font-weight: 700 !important;
            padding-bottom: 0px !important;
        }
        /* Subtítulos en Gris Profesional */
        h2, h3, h4 {
            color: #475569 !important;
            font-weight: 600 !important;
        }
        /* Resaltado del color de los KPIs numéricos */
        [data-testid="stMetricValue"] {
            color: #1E3A8A !important;
            font-weight: bold;
        }
        /* Línea de separación sutil */
        hr {
            margin-top: 1rem !important;
            margin-bottom: 1.5rem !important;
            border-top: 2px solid #E2E8F0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado institucional fijo de la aplicación
st.title("Proyecto Final UCG")
st.markdown(
    """
    *Sistema de Análisis Exploratorio y Visualización Aplicada de Datos.* Esta aplicación permite cargar un dataset, 
    explorar su estructura, analizar variables clave y visualizar patrones relevantes para un proyecto aplicado de ciencia de datos.
    """
)
st.divider()

# ==============================================================================
# 2. LOGICA DE CARGA Y GESTIÓN DE DATOS (Mantenida optimizada con Cache)
# ==============================================================================
@st.cache_data
def load_dataset(path: str) -> pd.DataFrame:
    """Carga de forma eficiente el dataset por defecto utilizando la caché de Streamlit."""
    return pd.read_csv(path)

# Ruta del dataset local por defecto
DEFAULT_DATASET = os.path.join("archive", "material.csv")

# Barra lateral para el control de carga de archivos por parte del usuario
st.sidebar.markdown("### 📁 Configuración de Datos")
uploaded_file = st.sidebar.file_uploader("Cargar un dataset CSV", type=["csv"])

# Control de flujo para la asignación del DataFrame analítico
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    source_label = uploaded_file.name
else:
    df = load_dataset(DEFAULT_DATASET)
    source_label = DEFAULT_DATASET

# Feedback visual en la barra lateral indicando el archivo en ejecución
st.sidebar.success(f"Activo: {source_label}")

# ==============================================================================
# 3. SISTEMA DE NAVEGACIÓN POR PESTAÑAS HORIZONTALES (UI Elegante)
# ==============================================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Exploración Inicial", 
    "📈 Análisis de Variables", 
    "🔍 Visualizaciones Clave", 
    "🧠 Interpretación"
])

# ------------------------------------------------------------------------------
# PESTAÑA 1: EXPLORACIÓN INICIAL DE DATOS
# ------------------------------------------------------------------------------
with tab1:
    st.markdown("### Resumen Ejecutivo de las Dimensiones")
    
    # Tarjetas de Métricas (Mapeo de dimensiones del dataset)
    col1, col2, col3 = st.columns(3)
    col1.metric("Filas Totales", f"{df.shape[0]:,}")
    col2.metric("Columnas", df.shape[1])
    col3.metric("Valores Nulos Detectados", f"{int(df.isna().sum().sum()):,}")
    
    st.markdown("---")
    st.markdown("#### Vista Previa del Dataset (Primeros 10 registros)")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.markdown("---")
    st.markdown("#### Tipos de Datos y Completitud de Columnas")
    # Construcción de la tabla de metadatos del DataFrame
    info = pd.DataFrame({
        "Columna": df.columns,
        "Tipo de Dato": df.dtypes.astype(str).values,
        "Registros Nulos": df.isna().sum().values,
        "Valores Únicos": df.nunique().values,
    })
    st.dataframe(info, use_container_width=True)
    
    st.markdown("---")
    st.markdown("#### Resumen Estadístico Descriptivo")
    # Extracción automática de columnas numéricas para el análisis estadístico
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        st.dataframe(df[numeric_cols].describe().T, use_container_width=True)
    else:
        st.info("No hay columnas numéricas disponibles para resumir.")

# ------------------------------------------------------------------------------
# PESTAÑA 2: ANÁLISIS DE VARIABLES (Frecuencias e Histogramas)
# ------------------------------------------------------------------------------
with tab2:
    st.markdown("### Análisis de Distribución de Frecuencias")
    left, right = st.columns(2)
    
    with left:
        st.markdown("#### Distribución de Variable Seleccionada")
        selected_col = st.selectbox("Selecciona una variable para visualizar", df.columns.tolist(), key="var_select")
        
        # Procesamiento de conteos para Plotly Express
        counts_selected = df[selected_col].value_counts().head(10).reset_index()
        counts_selected.columns = [selected_col, 'Frecuencia']
        
        # Creación del gráfico interactivo utilizando la paleta Azul Marino
        fig_selected = px.bar(
            counts_selected, x=selected_col, y='Frecuencia',
            color_discrete_sequence=['#1E3A8A'], template='plotly_white'
        )
        fig_selected.update_layout(plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_selected, use_container_width=True)
        
    with right:
        # Validación condicional de la presencia de la variable 'Use'
        if "Use" in df.columns:
            st.markdown("#### Distribución de la Variable Objetivo ('Use')")
            counts_use = df["Use"].value_counts().reset_index()
            counts_use.columns = ['Use', 'Frecuencia']
            
            # Creación del gráfico de barras utilizando la paleta Gris Corporativo
            fig_use = px.bar(
                counts_use, x='Use', y='Frecuencia',
                color_discrete_sequence=['#475569'], template='plotly_white'
            )
            fig_use.update_layout(plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_use, use_container_width=True)
        else:
            st.info("La columna objetivo 'Use' no está presente en el dataset actual.")

# ------------------------------------------------------------------------------
# PESTAÑA 3: VISUALIZACIONES CLAVE (Correlación y Tendencias)
# ------------------------------------------------------------------------------
with tab3:
    st.markdown("### Análisis de Correlaciones y Tendencias Temporales")
    if numeric_cols:
        st.markdown("#### Matriz de Correlación Lineal")
        corr = df[numeric_cols].corr().fillna(0)
        st.dataframe(corr, use_container_width=True)
        
        st.markdown("---")
        st.markdown("#### Comparación Rápida de Tendencias Continuas")
        feature = st.selectbox("Variable para comparar en el tiempo", numeric_cols, key="feature_compare")
        
        # Estructuración de datos para gráfico lineal continuo
        line_data = df[feature].astype(float).reset_index()
        
        # Gráfico interactivo lineal en color Azul Marino
        fig_line = px.line(
            line_data, x='index', y=feature,
            color_discrete_sequence=['#1E3A8A'], template='plotly_white'
        )
        fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("Se requieren variables numéricas para generar análisis analítico avanzado.")

# ------------------------------------------------------------------------------
# PESTAÑA 4: INTERPRETACIÓN Y CONCLUSIONES
# ------------------------------------------------------------------------------
with tab4:
    st.markdown("### Conclusiones de Negocio y Modelado")
    if "Use" in df.columns:
        # Cálculo de las proporciones exactas de la variable objetivo
        use_counts = df["Use"].value_counts(normalize=True).mul(100).round(1)
        st.markdown("#### Proporción Estimada por Clase (Porcentaje):")
        st.json(use_counts.to_dict())
    else:
        st.info("Cargue un dataset que contenga la variable objetivo 'Use' para visualizar su interpretación.")

# Pie de página institucional homologado
st.markdown("---")
st.caption("© 2026 Proyecto desarrollado con Streamlit | Unidad de Ciencias de la Gestión (UCG) | Análisis de Datos Aplicado.")
