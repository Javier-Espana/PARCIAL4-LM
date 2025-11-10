"""
Módulo de Simulación
Contiene la lógica de simulación de la Máquina de Turing.
"""

from typing import List, Dict, Tuple


class SimuladorMT:
    """Clase que maneja la simulación de una Máquina de Turing"""
    
    def __init__(
        self,
        delta: Dict[Tuple[str, str], Tuple[str, str, str]],
        q0: str,
        q_accept: str,
        q_reject: str,
        cadena_entrada: str
    ):
        self.delta = delta
        self.q0 = q0
        self.q_accept = q_accept
        self.q_reject = q_reject
        self.cadena_entrada = cadena_entrada
        self.cinta: List[str] = []
        self.cabeza: int = 0
        self.estado_actual: str = ""
        self.configuraciones: List[str] = []
    
    def inicializar_cinta(self):
        if self.cadena_entrada:
            self.cinta = list(self.cadena_entrada)
        else:
            self.cinta = ['⊔']
        
        self.cabeza = 0
        self.estado_actual = self.q0
        self.configuraciones = []
        
        config_inicial = self.obtener_configuracion_actual()
        self.configuraciones.append(config_inicial)
    
    def obtener_configuracion_actual(self) -> str:
        """Genera la configuración actual en notación de clase: u q v"""
        izquierda = ''.join(self.cinta[:self.cabeza])
        derecha = ''.join(self.cinta[self.cabeza:])
        
        if not derecha:
            derecha = '⊔'
        
        return f"{izquierda}{self.estado_actual}{derecha}"
    
    def extender_cinta_si_necesario(self):
        while self.cabeza >= len(self.cinta):
            self.cinta.append('⊔')
        
        if self.cabeza < 0:
            self.cabeza = 0
    
    def simular(self, pasos_max: int = 1000) -> str:
        """Ejecuta la simulación de la Máquina de Turing paso a paso"""
        print("Iniciando simulación de la Máquina de Turing...\n")
        
        self.inicializar_cinta()
        print(f"Paso 0: {self.configuraciones[0]}\n")
        
        paso = 0
        
        while paso < pasos_max:
            paso += 1
            
            if self.estado_actual == self.q_accept:
                config_final = self.obtener_configuracion_actual()
                self.configuraciones.append(config_final)
                print(f"Paso {paso}: {config_final}")
                print("\nEstado de ACEPTACIÓN alcanzado\n")
                return 'ACEPTADA'
            
            if self.estado_actual == self.q_reject:
                config_final = self.obtener_configuracion_actual()
                self.configuraciones.append(config_final)
                print(f"Paso {paso}: {config_final}")
                print("\nEstado de RECHAZO alcanzado\n")
                return 'RECHAZADA'
            
            self.extender_cinta_si_necesario()
            simbolo_actual = self.cinta[self.cabeza]
            clave = (self.estado_actual, simbolo_actual)
            
            if clave not in self.delta:
                config_final = self.obtener_configuracion_actual()
                self.configuraciones.append(config_final)
                print(f"Paso {paso}: {config_final}")
                print("\nNo hay transición definida - RECHAZO\n")
                return 'RECHAZADA'
            
            nuevo_estado, simbolo_escribir, direccion = self.delta[clave]
            self.cinta[self.cabeza] = simbolo_escribir
            self.estado_actual = nuevo_estado
            
            if direccion == 'L':
                self.cabeza = max(0, self.cabeza - 1)
            elif direccion == 'R':
                self.cabeza += 1
            
            config = self.obtener_configuracion_actual()
            self.configuraciones.append(config)
            print(f"Paso {paso}: {config}")
        
        print(f"\nCICLO INFINITO detectado (límite de {pasos_max} pasos alcanzado)")
        return 'CICLO_INFINITO'
