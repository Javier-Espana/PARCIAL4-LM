#!/usr/bin/env python3
"""
Simulador de Máquina de Turing Determinista
============================================

Programa principal para ejecutar el simulador de Máquina de Turing.


"""

from src.maquina_turing import MaquinaTuring


def main():
    """Función principal para ejecutar el simulador"""
    print("\n" + "=" * 70)
    print("SIMULADOR DE MÁQUINA DE TURING DETERMINISTA")
    print("=" * 70 + "\n")
    
    # Solicitar archivo de entrada
    archivo_entrada = input("Ingrese la ruta del archivo de especificación: ").strip()
    
    # Crear instancia de la MT
    mt = MaquinaTuring()
    
    # Cargar especificación
    if not mt.cargar_archivo(archivo_entrada):
        return
    
    # Mostrar resumen
    mt.mostrar_resumen()
    
    # Validar especificación
    if not mt.validar_maquina():
        print("\nNo se puede continuar debido a errores en la especificación.")
        return
    
    # Simular
    resultado = mt.simular(pasos_max=1000)
    
    # Generar nombre de archivo de salida
    if archivo_entrada.endswith('.txt'):
        archivo_salida = archivo_entrada.replace('.txt', '_configuraciones.txt')
    else:
        archivo_salida = archivo_entrada + '_configuraciones.txt'
    
    # Guardar resultado
    mt.guardar_resultado(archivo_salida)
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESULTADO FINAL")
    print("=" * 70)
    if resultado == 'ACEPTADA':
        print("La cadena fue ACEPTADA por la Máquina de Turing")
    elif resultado == 'RECHAZADA':
        print("La cadena fue RECHAZADA por la Máquina de Turing")
    else:
        print("La Máquina de Turing entró en un CICLO INFINITO")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
