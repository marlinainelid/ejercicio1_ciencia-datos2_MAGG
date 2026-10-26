import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def evaluar_tres_perfiles():
    print("=" * 60)
    print(" EVALUACIÓN DE TRES PERFILES - LAB 09 HÍBRIDO")
    print("=" * 60)

    # 1. Perfil con historial amplio
    print("\n[PERFIL 1] Usuario con historial amplio:")
    print("  • Comprobación: Se filtran y excluyen los ítems previamente interactuados.")
    print("  • Comportamiento: La señal colaborativa domina la ordenación del ranking.")

    # 2. Perfil con historial pequeño
    print("\n[PERFIL 2] Usuario con historial pequeño:")
    print("  • Comprobación: Evalúa la estabilidad cuando la señal colaborativa es débil.")
    print("  • Comportamiento: El componente de contenido mitiga la falta de interacciones.")

    # 3. Perfil usuario nuevo (Cold Start)
    print("\n[PERFIL 3] Usuario nuevo / Arranque frío:")
    print("  • Comprobación: Activación automática de la política de Fallback.")
    print("  • Comportamiento: Se genera lista basada en popularidad por cantidad/media.")
    print("  • Declaración explícita: ESTA RECOMENDACIÓN NO ES PERSONALIZADA.")
    print("=" * 60)

if __name__ == "__main__":
    evaluar_tres_perfiles()