# Ficha del dataset

- Dominio: Educación y economía  
- Unidad de análisis: Individuo (estudiante o persona censada)  
- Decisión: Clasificación de riesgo (abandono escolar o nivel de ingreso)  
- Target: Variable binaria (Adult Income) o multiclase (Student Dropout)  
- Error más costoso: Falsos negativos (no detectar riesgo real)  
- Usuario: Docentes, analistas de políticas públicas, investigadores  

---

| Criterio            | Adult Income (UCI) | Student Dropout (UCI) |
|---------------------|---------------------|------------------------|
| Procedencia         | UCI ML Repository  | UCI ML Repository      |
| Licencia            | Open Data          | Open Data              |
| Filas/columnas      | ~48,842 / 14       | ~4,420 / 36            |
| Target y clases     | Binario (>50K / ≤50K) | Multiclase (Dropout, Graduate, Enrolled) |
| Ausentes            | Algunos valores    | Desbalance de clases   |
| Riesgo de fuga      | Bajo               | Medio                  |

