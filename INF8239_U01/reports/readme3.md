# INF-8239 U01 – Reproducible Environment & Green AI

## Descripción
Este proyecto implementa un entorno reproducible para comparar modelos de clasificación bajo criterios de rendimiento y costo computacional. Se incluyen experimentos con SVM, Random Forest y Boosting, además de técnicas de reducción de dimensionalidad (PCA y t‑SNE). El objetivo es aplicar principios de **Green AI**, priorizando eficiencia y sostenibilidad.

## Entorno
- **Sistema operativo:** Windows 10
- **Python:** 3.13.0  
- **scikit-learn:** (ver salida en notebook)  
- **Procesador:** (ver salida en notebook)  

> Nota: Los tiempos de entrenamiento son contextuales al hardware disponible. No deben interpretarse como consumo energético exacto.

## Estructura del proyecto
INF8239_U01/
├── inf8239_u01/
│   ├── init.py
│   └── green.py
├── reports/
│   ├── tsne_two_seeds.png
│   ├── pareto.png
│   └── green_ai_results.csv
├── tests/
│   ├── init.py
│   └── test_green.py
├── notebooks/
│   └── ejercicio02.ipynb
├── requirements.txt
└── README.md

## Experimentos realizados
- Dataset y partición del Ejercicio 01.  
- **≥6 configuraciones** de modelos probados.  
- Algoritmos: **SVM, Random Forest, Boosting**.  
- Reducción de dimensionalidad: **PCA** y justificación alternativa.  
- **t‑SNE** con dos semillas distintas.  
- **3 repeticiones temporales** → cálculo de mediana.  
- Medición de **tamaño serializado** y **tiempo de inferencia**.  
- **Pruebas unitarias** (`pytest`) para validar frontera de Pareto.  

## Resultados
- CSV con métricas: `reports/green_ai_results.csv`.  
- Figuras:  
  - `reports/tsne_two_seeds.png`  
  - `reports/pareto.png`  
- Frontera de Pareto calculada y visualizada.  
- Texto de conclusiones Green AI (~300 palabras) incluido en el notebook.  

## Conclusiones Green AI
El análisis mostró que el modelo con mayor F1 macro no siempre es la opción más sostenible. La alternativa seleccionada ofreció un ahorro temporal significativo (>40%) y menor tamaño en disco, con una diferencia de F1 mínima respecto al mejor. Esto refuerza la importancia de evaluar el compromiso entre precisión y eficiencia. Los resultados son dependientes del hardware, pero las relaciones relativas entre modelos se mantienen. La decisión final se orienta hacia un modelo que equilibra rendimiento y eficiencia, alineado con los principios de Green AI.

## Versionado
```bash
git add .
git commit -m "feat: compare ensembles PCA and Green AI costs"
git tag u01-ejercicio02
