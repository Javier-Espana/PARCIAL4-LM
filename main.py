"""
MANUAL Simulador de Máquina de Turing Determinista
Programa principal para ejecutar el simulador de Máquina de Turing.
"""

from src.maquina_turing import MaquinaTuring


def main():
    print("\n" + "=" * 20)
    print("SIMULADOR DE MÁQUINA DE TURING DETERMINISTA")
    print("=" * 20 + "\n")
    
    archivo_entrada = input("Ingrese la ruta del archivo de especificación: ").strip()
    
    mt = MaquinaTuring()
    
    if not mt.cargar_archivo(archivo_entrada):
        return
    
    mt.mostrar_resumen()
    
    if not mt.validar_maquina():
        print("\nNo se puede continuar debido a errores en la especificación.")
        return
    
    resultado = mt.simular(pasos_max=1000)
    
    if archivo_entrada.endswith('.txt'):
        archivo_salida = archivo_entrada.replace('.txt', '_configuraciones.txt')
    else:
        archivo_salida = archivo_entrada + '_configuraciones.txt'
    
    mt.guardar_resultado(archivo_salida)
    
    print("\n" + "=" * 20)
    print("RESULTADO FINAL")
    print("=" * 20)
    if resultado == 'ACEPTADA':
        print("La cadena fue ACEPTADA por la Máquina de Turing")
    elif resultado == 'RECHAZADA':
        print("La cadena fue RECHAZADA por la Máquina de Turing")
    else:
        print("La Máquina de Turing entró en un CICLO INFINITO")
    print("=" * 20 + "\n")


if __name__ == "__main__":
    main()
