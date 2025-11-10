# Notación Utilizada

**Configuraciones en formato u q v:**
- u: contenido de la cinta a la izquierda del cabezal
- q: estado actual de la MT
- v: contenido de la cinta desde el cabezal hacia la derecha

**Ejemplo:** `0Xq21Y` significa:
- Cinta izquierda: 0X
- Estado actual: q2
- Cinta derecha (desde cabezal): 1Y

**Sin buffers externos:** Solo se utiliza la cinta interna de la MT

---

## Arquitectura Modular

### `src/maquina_turing.py`
Clase principal que integra todos los componentes con manejo de errores:
- FileNotFoundError
- PermissionError
- ValueError (formato inválido)
- UnicodeDecodeError (UTF-8/Latin-1)

### `src/parser.py`
Parseo robusto de especificaciones:
- 8 funciones especializadas para cada componente
- Validación de formato de transiciones
- Validación de direcciones (L, R, S)

### `src/validador.py`
10 validaciones exhaustivas:
- Q no vacío
- Estados q0, q_accept, q_reject en Q
- Estados de aceptación y rechazo diferentes
- Σ subconjunto de Γ
- Símbolo blanco en Γ y no en Σ
- Cadena usa solo símbolos de Σ
- Transiciones con estados válidos
- Transiciones con símbolos válidos
- Direcciones válidas

### `src/simulador.py`
Simulación paso a paso con manejo de excepciones:
- Detección de estados finales
- Detección de ciclos infinitos
- Manejo de transiciones indefinidas
- Protección contra errores de runtime

---

## Visualización Gráfica

La interfaz incluye una pestaña de visualización con:

- **Canvas animado** mostrando la cinta
- **Indicador visual** del cabezal (flecha roja)
- **Celda destacada** en amarillo para posición actual
- **Control de pasos** con slider y botones anterior/siguiente
- **Estado actual** destacado en azul
- **Estados finales** destacados (verde=aceptación, rojo=rechazo)
- **Configuración actual** en notación u q v
- **Transición anterior** para contexto

---

## Manejo de Errores Robusto

El programa maneja todos los casos excepcionales:

**Errores de archivo:**
- Archivo no encontrado
- Permisos insuficientes para lectura/escritura
- Errores de codificación (UTF-8/Latin-1)

**Errores de formato:**
- Componentes faltantes en especificación
- Transiciones mal definidas
- Direcciones inválidas (no L/R/S)
- Estados no definidos en Q
- Símbolos no definidos en Γ o Σ

**Errores de runtime:**
- Transición indefinida durante simulación
- Estados finales inesperados
- Errores en visualización gráfica

**Respuesta a errores:**
- Mensajes descriptivos al usuario
- No crashea el programa
- Permite continuar con otros archivos
- Registro de errores en GUI

---

## Lenguaje Reconocido

**L = {0^n 1^n | n ≥ 1}**

Cadenas con igual número de ceros seguidos de igual número de unos.

**Ejemplos:**
- Acepta: 01, 0011, 000111, 00001111
- Rechaza: 0, 1, 001, 0111, 10, 0001
- Ciclo: 00, 11, 01001, 010011 (patrones irregulares)

**Estrategia:**
1. Marca el primer 0 con X
2. Busca el primer 1 y marca con Y
3. Regresa al inicio
4. Repite hasta procesar todos
5. Acepta si todos están emparejados
6. Rechaza si quedan símbolos sin emparejar