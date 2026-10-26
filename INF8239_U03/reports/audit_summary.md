Auditoría del dataset MovieLens
Tamaño del conjunto
El dataset contiene 100,836 valoraciones realizadas por 610 usuarios sobre 9,742 películas.

Densidad
La densidad observada es aproximadamente 0.01697. Esto significa que la mayoría de las combinaciones usuario–película no poseen valoración registrada. Este comportamiento es normal en sistemas de recomendación y no debe interpretarse como rechazo explícito.

Distribución de ratings
Las valoraciones se encuentran dentro del rango esperado de 0.5 a 5.0 estrellas. La media observada es aproximadamente 3.50, indicando una ligera tendencia hacia evaluaciones positivas.

Usuarios e ítems
Los usuarios incluidos representan únicamente el universo observado por MovieLens. El conjunto no describe a todos los posibles usuarios ni a todas las películas existentes.

Timestamps
Los registros incluyen marcas temporales que permiten construir evaluaciones cronológicas y evitar el uso de interacciones futuras durante experimentos reproducibles.

Conclusión
La auditoría confirma que el dataset fue descargado correctamente, que los ratings se encuentran dentro del rango válido y que la estructura es adecuada para construir baselines de popularidad y sistemas de recomendación por contenido.
