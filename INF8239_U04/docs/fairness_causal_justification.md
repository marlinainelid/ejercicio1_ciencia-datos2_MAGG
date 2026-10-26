### 1. Presencia de Variables Confundidoras

Las métricas de equidad miden correlaciones observables, no relaciones causales. Una brecha puede ser el resultado de diferencias legítimas y subyacentes en las distribuciones de riesgo o en los perfiles de los datos entre los grupos (por ejemplo, factores socioeconómicos, históricos o geográficos legítimos en el contexto territorial), y no a un sesgo intrínseco del algoritmo.

### 2. Incertidumbre y Variabilidad Muestral

Como se evidenció en la auditoría con el subgrupo `G2` (con un tamaño de muestra reducido de 59 registros frente a 101 de `G1`), las diferencias numéricas pueden estar influenciadas por **ruido estadístico** o alta varianza debido a muestras pequeñas, lo que limita la robustez de la conclusión hasta contar con mayor volumen de datos.

### 3. Omisión de Atributos Predictivos Relegados

Si los datos de entrenamiento carecen de variables explicativas clave o legítimas que se correlacionen con el grupo protegido, el modelo absorberá estas limitaciones. La disparidad reflejada en las métricas puede ser consecuencia de **omisiones en el diseño de los datos** y no de una discriminación deliberada o sistémica.

### 4. Distinción entre Impacto Dispar y Discriminación Causal

* **Disparidad Observada (Impacto):** Refleja un desequilibrio en los resultados (a quién se le asigna qué). Es una señal de que el sistema afecta de manera desigual a los grupos.
* **Discriminación Causal:** Implica una relación de causa y efecto donde el algoritmo o el proceso de decisión penaliza injustamente a un grupo debido a prejuicios, diseño defectuoso o uso de atributos protegidos de forma ilegítima.

---

