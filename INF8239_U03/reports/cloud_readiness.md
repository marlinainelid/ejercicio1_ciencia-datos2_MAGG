## Preparación para despliegue

Se verificó que el proyecto utiliza rutas relativas y no depende de directorios personales del sistema operativo.

Los datos son descargados mediante scripts reproducibles y no requieren archivos manuales externos.

El proyecto incluye un archivo requirements-cloud.txt para facilitar la instalación de dependencias en entornos de despliegue.

La aplicación Streamlit utiliza artefactos generados durante el proceso de entrenamiento y puede ejecutarse localmente o en servicios compatibles con Python.