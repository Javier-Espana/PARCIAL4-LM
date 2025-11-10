"""
Módulo de Validación
Contiene funciones para validar los componentes de una Máquina de Turing.
"""

from typing import Set, Dict, Tuple, List


def validar_maquina(
    Q: Set[str],
    Sigma: Set[str],
    Gamma: Set[str],
    q0: str,
    q_accept: str,
    q_reject: str,
    delta: Dict[Tuple[str, str], Tuple[str, str, str]],
    cadena_entrada: str
) -> Tuple[bool, List[str]]:
    """Valida que todos los componentes de la MT sean correctos y consistentes"""
    errores = []
    
    if not Q:
        errores.append("Q (conjunto de estados) está vacío")
    
    if q0 not in Q:
        errores.append(f"Estado inicial '{q0}' no está en Q")
    
    if q_accept not in Q:
        errores.append(f"Estado de aceptación '{q_accept}' no está en Q")
    
    if q_reject not in Q:
        errores.append(f"Estado de rechazo '{q_reject}' no está en Q")
    
    if q_accept == q_reject:
        errores.append("Estado de aceptación y rechazo deben ser diferentes")
    
    if not Sigma.issubset(Gamma):
        errores.append("El alfabeto de entrada Σ debe ser subconjunto de Γ")
    
    if '⊔' not in Gamma:
        errores.append("El símbolo blanco '⊔' debe estar en Γ")
    
    if '⊔' in Sigma:
        errores.append("El símbolo blanco '⊔' no debe estar en Σ")
    
    for simbolo in cadena_entrada:
        if simbolo not in Sigma:
            errores.append(f"Símbolo '{simbolo}' en cadena de entrada no está en Σ")
            break
    
    for (estado, simbolo), (nuevo_estado, nuevo_simbolo, direccion) in delta.items():
        if estado not in Q:
            errores.append(f"Estado '{estado}' en δ no está en Q")
        if simbolo not in Gamma:
            errores.append(f"Símbolo '{simbolo}' en δ no está en Γ")
        if nuevo_estado not in Q:
            errores.append(f"Estado '{nuevo_estado}' en δ no está en Q")
        if nuevo_simbolo not in Gamma:
            errores.append(f"Símbolo '{nuevo_simbolo}' en δ no está en Γ")
        if direccion not in ['L', 'R', 'S']:
            errores.append(f"Dirección '{direccion}' en δ es inválida")
    
    return len(errores) == 0, errores
