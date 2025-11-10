"""
Módulo de Parseo de Especificaciones
Contiene funciones para parsear archivos de especificación de Máquinas de Turing.
"""

import re
from typing import Set, Dict, Tuple


def parsear_estados(contenido: str) -> Set[str]:
    match = re.search(r'Q\s*=\s*([^\n]+)', contenido)
    if not match:
        raise ValueError("No se encontró la definición de Q (estados)")
    
    estados_str = match.group(1).strip()
    estados = set(estado.strip() for estado in estados_str.split(','))
    print(f"  Q (Estados): {estados}")
    return estados


def parsear_alfabeto_entrada(contenido: str) -> Set[str]:
    match = re.search(r'Σ\s*=\s*([^\n]+)', contenido)
    if not match:
        raise ValueError("No se encontró la definición de Σ (alfabeto de entrada)")
    
    sigma_str = match.group(1).strip()
    sigma = set(simbolo.strip() for simbolo in sigma_str.split(','))
    print(f"  Σ (Alfabeto entrada): {sigma}")
    return sigma


def parsear_alfabeto_cinta(contenido: str) -> Set[str]:
    match = re.search(r'Γ\s*=\s*([^\n]+)', contenido)
    if not match:
        raise ValueError("No se encontró la definición de Γ (alfabeto de cinta)")
    
    gamma_str = match.group(1).strip()
    gamma = set(simbolo.strip() for simbolo in gamma_str.split(','))
    print(f"  Γ (Alfabeto cinta): {gamma}")
    return gamma


def parsear_estado_inicial(contenido: str) -> str:
    match = re.search(r'q0\s*=\s*([^\n]+)', contenido)
    if not match:
        raise ValueError("No se encontró la definición de q0 (estado inicial)")
    
    q0 = match.group(1).strip()
    print(f"  q0 (Estado inicial): {q0}")
    return q0


def parsear_estado_aceptacion(contenido: str) -> str:
    match = re.search(r'q_accept\s*=\s*([^\n]+)', contenido)
    if not match:
        raise ValueError("No se encontró la definición de q_accept")
    
    q_accept = match.group(1).strip()
    print(f"  q_accept (Aceptación): {q_accept}")
    return q_accept


def parsear_estado_rechazo(contenido: str) -> str:
    match = re.search(r'q_reject\s*=\s*([^\n]+)', contenido)
    if not match:
        raise ValueError("No se encontró la definición de q_reject")
    
    q_reject = match.group(1).strip()
    print(f"  q_reject (Rechazo): {q_reject}")
    return q_reject


def parsear_funcion_transicion(contenido: str) -> Dict[Tuple[str, str], Tuple[str, str, str]]:
    """Extrae la función de transición δ"""
    match = re.search(r'δ:\s*\n(.*?)(?:\n#|\nw\s*=)', contenido, re.DOTALL)
    if not match:
        raise ValueError("No se encontró la definición de δ (función de transición)")
    
    transiciones_str = match.group(1).strip()
    lineas = [linea.strip() for linea in transiciones_str.split('\n') if linea.strip()]
    
    print(f"  δ (Transiciones): {len(lineas)} reglas")
    
    delta = {}
    for linea in lineas:
        match_trans = re.match(r'([^,]+),([^→]+)\s*→\s*([^,]+),([^,]+),(.+)', linea)
        if not match_trans:
            print(f"    Advertencia: Formato inválido en transición: {linea}")
            continue
        
        estado_actual = match_trans.group(1).strip()
        simbolo_leido = match_trans.group(2).strip()
        nuevo_estado = match_trans.group(3).strip()
        simbolo_escrito = match_trans.group(4).strip()
        direccion = match_trans.group(5).strip()
        
        if direccion not in ['L', 'R', 'S']:
            print(f"    Advertencia: Dirección inválida '{direccion}' en: {linea}")
            continue
        
        clave = (estado_actual, simbolo_leido)
        delta[clave] = (nuevo_estado, simbolo_escrito, direccion)
        print(f"    δ({estado_actual}, {simbolo_leido}) = ({nuevo_estado}, {simbolo_escrito}, {direccion})")
    
    return delta


def parsear_cadena_entrada(contenido: str) -> str:
    match = re.search(r'w\s*=\s*([^\n]*)', contenido)
    if not match:
        raise ValueError("No se encontró la definición de w (cadena de entrada)")
    
    w = match.group(1).strip()
    print(f"  w (Cadena entrada): '{w}'")
    return w
