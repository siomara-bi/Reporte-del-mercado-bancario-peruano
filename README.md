# Reporte-del-mercado-bancario-peruano
Este proyecto es un análisis integral del sistema financiero peruano basado en datos públicos de la SBS (Superintendencia de Banca, Seguros y AFP). El objetivo fue consolidar balances generales dispersos  para analizar la evolución de los principales bancos del país.

El resultado final es un Dashboard interactivo que permite visualizar indicadores clave como ROA, ROE, Activos, Utilidad Neta y Participación de Mercado
![av2_page-0001](https://github.com/user-attachments/assets/96c8f8c6-8dbe-41fd-b832-b82335bfab12)

El proyecto sigue un flujo ETL:

1.  **PYTHON (Extracción y Consolidación):**
    *   Automatización de la lectura de **6 Balances Generales** anuales (archivos Excel de la SBS).
    *   Limpieza inicial y estandarización de columnas con `Pandas`.
    *   Consolidación de la data histórica en un único archivo.

2.  **SQL SERVER 2022 (Consulta):**
    *   Importación del dataset consolidado.
    *   Creación de **Rankings Dinámicos** utilizando funciones de ventana (`RANK() OVER`).

3.  **POWER BI (Visualización e Inteligencia de Negocios):**
    *   Conexión directa a la base de datos SQL.
    *   Modelado de datos y creación de medidas DAX (Crecimiento, ROE, ROA).
    *   Diseño de Dashboard interactivo para el monitoreo de KPIs.

**Lenguajes:** Python (Pandas, OpenPyXL).
*   **Herramientas:** SQL Server Management Studio (SSMS), Power BI Desktop.
*   **Fuente de Datos:** Datos públicos de la SBS.

##  Principales Resultados

*   **Concentración de Mercado:** El **BCP** lidera el sector con una cuota de mercado del **38.46%**, seguido por el BBVA (23.07%). Los "4 Grandes" concentran más del 90% de los activos.
*   **Rentabilidad:** El sector muestra una recuperación sólida post-pandemia con un **ROE promedio del 13.67%**.
*   **Eficiencia:** El BCP no solo lidera en activos, sino que duplica la Utilidad Neta de su competidor más cercano, demostrando una alta eficiencia operativa.

---
*Autor: Siomara Aguirre | Estudiante de Economía UNALM*
