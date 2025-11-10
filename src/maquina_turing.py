"""
Módulo Principal de Máquina de Turing
Contiene la clase principal MaquinaTuring que integra todos los módulos.
"""

from typing import Set, Dict, Tuple, List
from .parser import (
    parsear_estados,
    parsear_alfabeto_entrada,
    parsear_alfabeto_cinta,
    parsear_estado_inicial,
    parsear_estado_aceptacion,
    parsear_estado_rechazo,
    parsear_funcion_transicion,
    parsear_cadena_entrada
)
from .validador import validar_maquina
from .simulador import SimuladorMT


class MaquinaTuring:
    """Clase que representa una Máquina de Turing Determinista"""
    
    def __init__(self):
        self.Q: Set[str] = set()
        self.Sigma: Set[str] = set()
        self.Gamma: Set[str] = set()
        self.q0: str = ""
        self.q_accept: str = ""
        self.q_reject: str = ""
        self.delta: Dict[Tuple[str, str], Tuple[str, str, str]] = {}
        self.cadena_entrada: str = ""
        self.archivo_origen: str = ""
        self.simulador: SimuladorMT = None
    
    def cargar_archivo(self, ruta: str) -> bool:
        """Carga y parsea el archivo de especificación de la MT"""
        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                
            self.archivo_origen = ruta
            print(f"Cargando especificación desde: {ruta}")
            
            self.Q = parsear_estados(contenido)
            self.Sigma = parsear_alfabeto_entrada(contenido)
            self.Gamma = parsear_alfabeto_cinta(contenido)
            self.q0 = parsear_estado_inicial(contenido)
            self.q_accept = parsear_estado_aceptacion(contenido)
            self.q_reject = parsear_estado_rechazo(contenido)
            self.delta = parsear_funcion_transicion(contenido)
            self.cadena_entrada = parsear_cadena_entrada(contenido)
            
            print("Archivo cargado exitosamente\n")
            return True
            
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta}'")
            return False
        except Exception as e:
            print(f"Error al cargar archivo: {str(e)}")
            return False
    
    def validar_maquina(self) -> bool:
        """Valida que todos los componentes de la MT sean correctos y consistentes"""
        print("\nValidando especificación de la Máquina de Turing...")
        
        valido, errores = validar_maquina(
            self.Q, self.Sigma, self.Gamma,
            self.q0, self.q_accept, self.q_reject,
            self.delta, self.cadena_entrada
        )
        
        if errores:
            print("Validación FALLIDA. Errores encontrados:")
            for i, error in enumerate(errores, 1):
                print(f"  {i}. {error}")
            return False
        else:
            print("Validación EXITOSA. La MT está correctamente especificada.\n")
            return True
    
    def simular(self, pasos_max: int = 1000) -> str:
        """Ejecuta la simulación de la Máquina de Turing"""
        self.simulador = SimuladorMT(
            self.delta,
            self.q0,
            self.q_accept,
            self.q_reject,
            self.cadena_entrada
        )
        
        return self.simulador.simular(pasos_max)
    
    def guardar_resultado(self, ruta_salida: str):
        """Guarda las configuraciones en un archivo de texto"""
        if not self.simulador:
            print("Error: No se ha ejecutado ninguna simulación")
            return
        
        try:
            with open(ruta_salida, 'w', encoding='utf-8') as archivo:
                archivo.write("=" * 70 + "\n")
                archivo.write("SIMULACIÓN DE MÁQUINA DE TURING - CONFIGURACIONES\n")
                archivo.write("=" * 70 + "\n\n")
                
                archivo.write(f"Archivo de especificación: {self.archivo_origen}\n")
                archivo.write(f"Cadena de entrada: '{self.cadena_entrada}'\n")
                archivo.write(f"Total de pasos: {len(self.simulador.configuraciones) - 1}\n\n")
                
                archivo.write("=" * 70 + "\n")
                archivo.write("SECUENCIA DE CONFIGURACIONES\n")
                archivo.write("=" * 70 + "\n\n")
                
                for config in self.simulador.configuraciones:
                    archivo.write(config + "\n")
                
                archivo.write("\n" + "=" * 70 + "\n")
                archivo.write("FIN DE LA SIMULACIÓN\n")
                archivo.write("=" * 70 + "\n")
            
            print(f"\nConfiguraciones guardadas en: {ruta_salida}")
            
        except Exception as e:
            print(f"Error al guardar archivo de salida: {str(e)}")
    
    def mostrar_resumen(self):
        """Muestra un resumen de la especificación cargada"""
        print("\n" + "=" * 70)
        print("RESUMEN DE LA MÁQUINA DE TURING")
        print("=" * 70)
        print(f"Estados (Q): {len(self.Q)} estados")
        print(f"  {sorted(self.Q)}")
        print(f"\nAlfabeto entrada (Σ): {sorted(self.Sigma)}")
        print(f"Alfabeto cinta (Γ): {sorted(self.Gamma)}")
        print(f"\nEstado inicial: {self.q0}")
        print(f"Estado aceptación: {self.q_accept}")
        print(f"Estado rechazo: {self.q_reject}")
        print(f"\nTransiciones (δ): {len(self.delta)} reglas definidas")
        print(f"Cadena de entrada: '{self.cadena_entrada}'")
        print("=" * 70 + "\n")
