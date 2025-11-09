"""
Módulo de Simulación
====================
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
        """Inicializa el simulador con los componentes de la MT"""
        self.delta = delta
        self.q0 = q0
        self.q_accept = q_accept
        self.q_reject = q_reject
        self.cadena_entrada = cadena_entrada
        
        # Estado de la simulación
        self.cinta: List[str] = []
        self.cabeza: int = 0
        self.estado_actual: str = ""
        self.configuraciones: List[str] = []
    
    def inicializar_cinta(self):
        """Inicializa la cinta con la cadena de entrada"""
        if self.cadena_entrada:
            self.cinta = list(self.cadena_entrada)
        else:
            self.cinta = ['⊔']
        
        self.cabeza = 0
        self.estado_actual = self.q0
        self.configuraciones = []
        
        # Guardar configuración inicial
        config_inicial = self.obtener_configuracion_actual()
        self.configuraciones.append(f"Configuración inicial: {config_inicial}")
    
    def obtener_configuracion_actual(self) -> str:
        """
        Genera la configuración actual en notación: u q v
        - u: contenido a la izquierda de la cabeza
        - q: estado actual
        - v: contenido desde la cabeza hacia la derecha
        """
        # Parte izquierda (antes de la cabeza)
        izquierda = ''.join(self.cinta[:self.cabeza])
        
        # Parte derecha (desde la cabeza)
        derecha = ''.join(self.cinta[self.cabeza:])
        
        # Si derecha está vacía, agregar símbolo blanco
        if not derecha:
            derecha = '⊔'
        
        # Configuración: u q v
        return f"{izquierda}{self.estado_actual}{derecha}"
    
    def extender_cinta_si_necesario(self):
        """Extiende la cinta con símbolos blancos si la cabeza se sale"""
        # Extender a la derecha si es necesario
        while self.cabeza >= len(self.cinta):
            self.cinta.append('⊔')
        
        # No permitir que la cabeza vaya a la izquierda de la posición 0
        if self.cabeza < 0:
            self.cabeza = 0
    
    def simular(self, pasos_max: int = 1000) -> str:
        """
        Ejecuta la simulación de la Máquina de Turing paso a paso.
        
        Args:
            pasos_max: Número máximo de pasos antes de detectar ciclo infinito
            
        Returns:
            String indicando el resultado: 'ACEPTADA', 'RECHAZADA', o 'CICLO_INFINITO'
        """
        print("Iniciando simulación de la Máquina de Turing...\n")
        
        # Inicializar la cinta y el estado
        self.inicializar_cinta()
        
        print(f"Paso 0: {self.configuraciones[0]}\n")
        
        paso = 0
        
        while paso < pasos_max:
            paso += 1
            
            # Verificar si llegamos a un estado final
            if self.estado_actual == self.q_accept:
                config_final = self.obtener_configuracion_actual()
                mensaje = f"Paso {paso}: ACEPTACIÓN - {config_final}"
                self.configuraciones.append(mensaje)
                print(f"{mensaje}\n")
                return 'ACEPTADA'
            
            if self.estado_actual == self.q_reject:
                config_final = self.obtener_configuracion_actual()
                mensaje = f"Paso {paso}: RECHAZO - {config_final}"
                self.configuraciones.append(mensaje)
                print(f"{mensaje}\n")
                return 'RECHAZADA'
            
            # Extender cinta si es necesario
            self.extender_cinta_si_necesario()
            
            # Leer símbolo actual
            simbolo_actual = self.cinta[self.cabeza]
            
            # Buscar transición
            clave = (self.estado_actual, simbolo_actual)
            
            if clave not in self.delta:
                # No hay transición definida - rechazo implícito
                config_final = self.obtener_configuracion_actual()
                mensaje = f"Paso {paso}: RECHAZO (sin transición) - {config_final}"
                self.configuraciones.append(mensaje)
                print(f"{mensaje}\n")
                return 'RECHAZADA'
            
            # Aplicar transición
            nuevo_estado, simbolo_escribir, direccion = self.delta[clave]
            
            # Escribir símbolo
            self.cinta[self.cabeza] = simbolo_escribir
            
            # Cambiar estado
            self.estado_actual = nuevo_estado
            
            # Mover cabeza
            if direccion == 'L':
                self.cabeza = max(0, self.cabeza - 1)
            elif direccion == 'R':
                self.cabeza += 1
            # Si es 'S', la cabeza no se mueve
            
            # Guardar configuración
            config = self.obtener_configuracion_actual()
            mensaje = f"Paso {paso}: {config}"
            self.configuraciones.append(mensaje)
            print(mensaje)
        
            # Si llegamos aquí, es un ciclo infinito
            mensaje = f"\nCICLO INFINITO detectado (límite de {pasos_max} pasos alcanzado)"
            self.configuraciones.append(mensaje)
            print(mensaje)
            return 'CICLO_INFINITO'
