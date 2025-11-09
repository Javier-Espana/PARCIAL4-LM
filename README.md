# SIMULADOR DE MÁQUINA DE TURING DETERMINISTA
## PARCIAL 4 - Lenguajes y Máquinas

**Versión:** 2.0 (Refactorizada)  
**Fecha:** 9 de noviembre de 2025  

---

## Estructura del Proyecto

```
PARCIAL4-LM/
│
├── main.py                    # Punto de entrada principal
├── demo.py                    # Demo interactivo
├── test_all.py                # Suite de pruebas automáticas
│
├── src/                       # Código fuente modular
│   ├── __init__.py           
│   ├── maquina_turing.py     # Clase principal MaquinaTuring
│   ├── parser.py              # Módulo de parseo de especificaciones
│   ├── validador.py           # Módulo de validación
│   └── simulador.py           # Módulo de simulación
│
├── especificaciones/          # Archivos de entrada (.txt)
│   ├── caso_aceptacion.txt
│   ├── caso_rechazo.txt
│   └── caso_ciclo_infinito.txt
│
├── salidas/                   # Archivos de salida generados
│   ├── caso_aceptacion_configuraciones.txt
│   ├── caso_rechazo_configuraciones.txt
│   └── caso_ciclo_infinito_configuraciones.txt
│
└── docs/                      # Documentación
    ├── README.md
    ├── DIAGRAMA_MT.md
    ├── ENTREGA.md
    ├── INICIO_RAPIDO.md
    └── INSTRUCCIONES_CANVAS.md
```

---

## Uso Rápido

### Opción 1: Ejecución Principal
```bash
python3 main.py
# Ingresa la ruta del archivo cuando se solicite
# Ejemplo: especificaciones/caso_aceptacion.txt
```

### Opción 2: Demo Interactivo
```bash
python3 demo.py
# Menú interactivo para seleccionar casos
```

### Opción 3: Ejecutar Todas las Pruebas
```bash
python3 test_all.py
# Ejecuta los 3 casos automáticamente
```

---

## Arquitectura Modular

### `src/maquina_turing.py`
Clase principal que integra todos los componentes:
- `MaquinaTuring` - Clase principal

### `src/parser.py`
Funciones de parseo de especificaciones:
- `parsear_estados()` - Extrae Q
- `parsear_alfabeto_entrada()` - Extrae Σ
- `parsear_alfabeto_cinta()` - Extrae Γ
- `parsear_estado_inicial()` - Extrae q0
- `parsear_estado_aceptacion()` - Extrae q_accept
- `parsear_estado_rechazo()` - Extrae q_reject
- `parsear_funcion_transicion()` - Extrae δ
- `parsear_cadena_entrada()` - Extrae w

### `src/validador.py`
Validación de componentes:
- `validar_maquina()` - Valida todos los componentes de la MT

### `src/simulador.py`
Lógica de simulación:
- `SimuladorMT` - Clase que ejecuta la simulación paso a paso

---

## Características

- **Arquitectura Limpia**: Código dividido en módulos especializados  
- **Notación de Clase**: Configuraciones en formato `u q v`  
- **Sin Buffers Externos**: Solo usa la cinta interna  
- **Validación Exhaustiva**: 10 validaciones diferentes  
- **Detección Automática**: Aceptación, rechazo y ciclos infinitos  
- **Organización**: Carpetas separadas para especificaciones y salidas  

---

## 📝 Formato de Archivo de Entrada

Los archivos de especificación van en `especificaciones/`:

```text
Q = q0,q1,q_accept,q_reject
Σ = 0,1
Γ = 0,1,X,⊔
q0 = q0
q_accept = q_accept
q_reject = q_reject
δ:
q0,0 → q1,X,R
q1,1 → q_accept,1,R
#
w = 01
```

---

## Casos de Prueba Incluidos

### 1. Aceptación (`especificaciones/caso_aceptacion.txt`)
- **Cadena:** `0011`
- **Resultado:** ACEPTADA
- **Salida:** `salidas/caso_aceptacion_configuraciones.txt`

### 2. Rechazo (`especificaciones/caso_rechazo.txt`)
- **Cadena:** `0001`
- **Resultado:** RECHAZADA
- **Salida:** `salidas/caso_rechazo_configuraciones.txt`

### 3. Ciclo Infinito (`especificaciones/caso_ciclo_infinito.txt`)
- **Cadena:** `01`
- **Resultado:** CICLO INFINITO
- **Salida:** `salidas/caso_ciclo_infinito_configuraciones.txt`

---

## Uso Programático

```python
from src.maquina_turing import MaquinaTuring

# Crear instancia
mt = MaquinaTuring()

# Cargar especificación
mt.cargar_archivo('especificaciones/caso_aceptacion.txt')

# Mostrar resumen
mt.mostrar_resumen()

# Validar
if mt.validar_maquina():
    # Simular
    resultado = mt.simular(pasos_max=1000)
    
    # Guardar configuraciones
    mt.guardar_resultado('salidas/mi_salida.txt')
```

---

## Pruebas

Ejecutar todas las pruebas:
```bash
python3 test_all.py
```

Salida esperada:
```
CASO A - ACEPTACIÓN........................................... EXITOSO
CASO B - RECHAZO.............................................. EXITOSO
CASO C - CICLO INFINITO....................................... EXITOSO
```

---

## Documentación Adicional

- **DIAGRAMA_MT.md** - Diagrama de estados y tabla de transiciones
- **ENTREGA.md** - Documento de entrega completo para el examen
- **INICIO_RAPIDO.md** - Guía de inicio rápido
- **INSTRUCCIONES_CANVAS.md** - Instrucciones para subir a Canvas

---

## Máquina de Turing Implementada

**Lenguaje:** L = {0^n 1^n | n ≥ 1}

Acepta cadenas con igual número de ceros seguidos de igual número de unos.

**Componentes:**
- Q = {q0, q1, q2, q3, q_accept, q_reject}
- Σ = {0, 1}
- Γ = {0, 1, X, Y, ⊔}

Ver `DIAGRAMA_MT.md` para detalles completos.

---

## Requisitos

- Python 3.7 o superior
- Sin dependencias externas (solo bibliotecas estándar)

---

## Archivos para Canvas

Los 8 archivos obligatorios para el examen:

1. `main.py` o `src/` completo (código del simulador)
2. `DIAGRAMA_MT.md` (diagrama)
3. `especificaciones/caso_aceptacion.txt`
4. `salidas/caso_aceptacion_configuraciones.txt`
5. `especificaciones/caso_rechazo.txt`
6. `salidas/caso_rechazo_configuraciones.txt`
7. `especificaciones/caso_ciclo_infinito.txt`
8. `salidas/caso_ciclo_infinito_configuraciones.txt`

---

## Mejoras en Versión 2.0

- **Código Modularizado**: Dividido en 4 módulos especializados  
- **Mejor Organización**: Carpetas separadas para inputs/outputs  
- **Mantenibilidad**: Cada módulo tiene una responsabilidad única  
- **Escalabilidad**: Fácil agregar nuevas funcionalidades  
- **Claridad**: Código más legible y fácil de entender  

---

**El simulador está completamente refactorizado y listo para usar.**

Autor: Javier España  
Fecha: 9 de noviembre de 2025  
Curso: Lenguajes y Máquinas - Parcial 4
