# SIMULADOR DE MÁQUINA DE TURING DETERMINISTA
## PARCIAL 4 - Lenguajes y Máquinas

---

## Descripción del Proyecto

Este proyecto implementa un **simulador completo de Máquina de Turing determinista** en Python, siguiendo estrictamente la notación vista en clase. El simulador puede cargar especificaciones de MT desde archivos de texto, validar su correctitud y ejecutar la simulación paso a paso, generando las configuraciones en el formato correcto.

---

## Características Principales

✅ **Carga de especificaciones** desde archivos de texto  
✅ **Validación exhaustiva** de todos los componentes de la MT  
✅ **Simulación paso a paso** con historial completo de configuraciones  
✅ **Detección automática** de aceptación, rechazo y ciclos infinitos  
✅ **Notación de clase**: configuraciones en formato `u q v`  
✅ **Generación de archivos de salida** con todas las configuraciones  
✅ **Sin buffers externos**: solo usa la cinta interna  

---

## 📦 Archivos del Proyecto

```
PARCIAL4-LM/
│
├── maquina_turing.py           # Simulador principal (código completo)
├── caso_aceptacion.txt         # Especificación MT + cadena aceptada
├── caso_rechazo.txt            # Especificación MT + cadena rechazada
├── caso_ciclo_infinito.txt     # Especificación MT + cadena en ciclo
├── DIAGRAMA_MT.md              # Diagrama y explicación de la MT
└── README.md                   # Este archivo
```

---

## Instalación y Requisitos

### Requisitos
- Python 3.7 o superior
- No se requieren bibliotecas externas (solo módulos estándar)

### Instalación
```bash
# Clonar o descargar el repositorio
cd PARCIAL4-LM

# Verificar que Python esté instalado
python3 --version
```

---

## 💻 Uso del Simulador

### Modo Interactivo (Recomendado)

```bash
python3 maquina_turing.py
```

El programa solicitará la ruta del archivo de especificación:
```
Ingrese la ruta del archivo de especificación: caso_aceptacion.txt
```

### Modo Programático

También puedes usar el simulador desde código Python:

```python
from maquina_turing import MaquinaTuring

# Crear instancia
mt = MaquinaTuring()

# Cargar especificación
mt.cargar_archivo('caso_aceptacion.txt')

# Mostrar resumen
mt.mostrar_resumen()

# Validar especificación
if mt.validar_maquina():
    # Simular
    resultado = mt.simular(pasos_max=1000)
    
    # Guardar configuraciones
    mt.guardar_resultado('salida_configuraciones.txt')
```

---

## 📝 Formato del Archivo de Especificación

El archivo de entrada debe seguir esta estructura exacta:

```text
# Máquina de Turing - Especificación
Q = q0,q1,q2,q_accept,q_reject
Σ = 0,1
Γ = 0,1,X,Y,⊔
q0 = q0
q_accept = q_accept
q_reject = q_reject
δ:
q0,0 → q1,X,R
q0,Y → q2,Y,R
q1,0 → q1,0,R
q1,1 → q2,Y,L
q2,X → q0,X,R
q2,⊔ → q_accept,⊔,R
#
w = 0011
```

### Componentes:
- **Q**: Conjunto de estados (separados por comas)
- **Σ**: Alfabeto de entrada (sin el símbolo blanco)
- **Γ**: Alfabeto de cinta (incluye ⊔ y todos los símbolos de Σ)
- **q0**: Estado inicial
- **q_accept**: Estado de aceptación
- **q_reject**: Estado de rechazo
- **δ**: Función de transición (formato: `estado,símbolo → nuevo_estado,nuevo_símbolo,dirección`)
- **w**: Cadena de entrada a procesar

### Direcciones válidas:
- **L**: Left (izquierda)
- **R**: Right (derecha)
- **S**: Stay (permanece)

---

## Casos de Prueba Incluidos

### 1. Caso de Aceptación (`caso_aceptacion.txt`)
- **Cadena**: `0011`
-- **Resultado esperado**: ACEPTADA
- **Descripción**: Cadena con igual número de 0s y 1s consecutivos

### 2. Caso de Rechazo (`caso_rechazo.txt`)
- **Cadena**: `0001`
-- **Resultado esperado**: RECHAZADA
- **Descripción**: Cadena con más 0s que 1s

### 3. Caso de Ciclo Infinito (`caso_ciclo_infinito.txt`)
- **Cadena**: `010`
-- **Resultado esperado**: CICLO INFINITO
- **Descripción**: Cadena que no cumple el patrón y causa bucle

---

## Formato de Salida

El simulador genera un archivo con todas las configuraciones:

```text
======================================================================
SIMULACIÓN DE MÁQUINA DE TURING - CONFIGURACIONES
======================================================================

Archivo de especificación: caso_aceptacion.txt
Cadena de entrada: '0011'
Total de pasos: 13

======================================================================
SECUENCIA DE CONFIGURACIONES
======================================================================

Configuración inicial: q00011
Paso 1: Xq1011
Paso 2: X0q111
Paso 3: Xq20Y1
Paso 4: q2X0Y1
Paso 5: Xq00Y1
Paso 6: XXq1Y1
Paso 7: XXYq11
Paso 8: XXq2YY
Paso 9: Xq2XYY
Paso 10: XXq0YY
Paso 11: XXYq3Y
Paso 12: XXYYq3⊔
Paso 13: ACEPTACIÓN - XXYY⊔q_accept

======================================================================
FIN DE LA SIMULACIÓN
======================================================================
```

---

## Máquina de Turing Implementada

La MT incluida reconoce el lenguaje **L = {0^n 1^n | n ≥ 1}**

### Estrategia:
1. Marca el primer `0` con `X`
2. Busca el primer `1` y lo marca con `Y`
3. Regresa al inicio
4. Repite hasta procesar todos los símbolos
5. Acepta si todos los `0` tienen su `1` correspondiente

Ver `DIAGRAMA_MT.md` para el diagrama completo y tabla de transiciones.

---

## Validaciones Realizadas

El simulador verifica:

1. Q no está vacío
2. q0 ∈ Q
3. q_accept ∈ Q
4. q_reject ∈ Q
5. q_accept ≠ q_reject
6. Σ ⊆ Γ
7. ⊔ ∈ Γ
8. ⊔ ∉ Σ
9. ✅ Cadena de entrada usa solo símbolos de Σ
10. ✅ Todas las transiciones usan estados y símbolos válidos

---

## 🏃 Ejecución de Pruebas

### Probar Caso de Aceptación
```bash
python3 maquina_turing.py
# Cuando pida archivo: caso_aceptacion.txt
```

### Probar Caso de Rechazo
```bash
python3 maquina_turing.py
# Cuando pida archivo: caso_rechazo.txt
```

### Probar Ciclo Infinito
```bash
python3 maquina_turing.py
# Cuando pida archivo: caso_ciclo_infinito.txt
```

---

## 📚 Notación Utilizada

### Configuración: `u q v`
- **u**: Contenido de la cinta a la izquierda de la cabeza
- **q**: Estado actual de la MT
- **v**: Contenido desde la cabeza hacia la derecha

### Ejemplo:
`101q701111` significa:
- Cinta: `101701111`
- Estado: `q7`
- Cabeza apunta al primer `0` después de `101`

---

## 🛠️ Arquitectura del Código

```python
MaquinaTuring
├── __init__()                    # Inicializa componentes
├── cargar_archivo()              # Carga especificación
│   ├── _parsear_estados()
│   ├── _parsear_alfabeto_entrada()
│   ├── _parsear_alfabeto_cinta()
│   ├── _parsear_estado_inicial()
│   ├── _parsear_estado_aceptacion()
│   ├── _parsear_estado_rechazo()
│   ├── _parsear_funcion_transicion()
│   └── _parsear_cadena_entrada()
├── validar_maquina()             # Valida componentes
├── inicializar_cinta()           # Prepara la cinta
├── simular()                     # Ejecuta la MT
│   ├── obtener_configuracion_actual()
│   └── extender_cinta_si_necesario()
├── guardar_resultado()           # Exporta configuraciones
└── mostrar_resumen()             # Muestra especificación
```

---

## ⚙️ Características Técnicas

- **Lenguaje**: Python 3.7+
- **Paradigma**: Orientado a Objetos
- **Tipo de MT**: Determinista de una cinta
- **Límite de pasos**: 1000 (configurable)
- **Codificación**: UTF-8 (soporta símbolo ⊔)
- **Gestión de cinta**: Extensión dinámica con símbolos blancos

---

## 📄 Archivos de Salida Generados

Después de ejecutar cada caso, se generan:

- `caso_aceptacion_configuraciones.txt`
- `caso_rechazo_configuraciones.txt`
- `caso_ciclo_infinito_configuraciones.txt`

---

## 👨‍💻 Autor

**Javier España**  
Lenguajes y Máquinas - Parcial 4  
Fecha: 8 de noviembre de 2025

---

## 📖 Referencias

- Notación y definiciones según lo visto en clase
- Máquina de Turing determinista estándar
- Configuraciones en formato `u q v`

---

## ✅ Checklist del Examen

- [x] a) Programa que simula MT determinista
- [x] b) Diseñar MT con aceptación, rechazo y ciclo infinito
- [x] c) Archivo con cadena que llega a aceptación
- [x] d) Archivo de salida con configuraciones de aceptación
- [x] e) Archivo con cadena que llega a rechazo
- [x] f) Archivo de salida con configuraciones de rechazo
- [x] g) Archivo con cadena que causa ciclo infinito
- [x] h) Archivo de salida con configuraciones de ciclo infinito

---

## 🎯 Notas Importantes

1. El simulador NO usa buffers o memorias externas
2. Solo trabaja con la cinta interna
3. Las configuraciones siguen estrictamente la notación `u q v`
4. Se detectan ciclos infinitos automáticamente
5. Todos los componentes son validados antes de la simulación

---

**¡El simulador está listo para ser ejecutado y evaluado! 🚀**
