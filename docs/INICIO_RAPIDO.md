# INICIO RÁPIDO - Simulador de Máquina de Turing

## Ejecución Rápida

### Opción 1: Demo Interactivo (Recomendado)
```bash
python3 demo.py
```
Menú interactivo para seleccionar qué caso ejecutar.

### Opción 2: Ejecución Manual
```bash
python3 maquina_turing.py
# Cuando pida archivo, escribir: caso_aceptacion.txt
```

### Opción 3: Suite de Pruebas Completa
```bash
python3 test_all.py
```
Ejecuta los 3 casos automáticamente.

---

## Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `maquina_turing.py` | Simulador principal |
| `demo.py` | Demo interactivo |
| `test_all.py` | Pruebas automáticas |
| `caso_aceptacion.txt` | Especificación - Aceptación |
| `caso_rechazo.txt` | Especificación - Rechazo |
| `caso_ciclo_infinito.txt` | Especificación - Ciclo |

---

## Casos de Prueba

### Caso Aceptación
- **Entrada:** `0011`
- **Resultado:** ACEPTADA
- **Salida:** `caso_aceptacion_configuraciones.txt`

### Caso Rechazo
- **Entrada:** `0001`
- **Resultado:** RECHAZADA
- **Salida:** `caso_rechazo_configuraciones.txt`

### Caso Ciclo Infinito
- **Entrada:** `01`
- **Resultado:** CICLO INFINITO
- **Salida:** `caso_ciclo_infinito_configuraciones.txt`

---

## Estructura de Archivo de Entrada

```text
Q = q0,q1,q_accept,q_reject
Σ = 0,1
Γ = 0,1,X,⊔
q0 = q0
q_accept = q_accept
q_reject = q_reject
δ:
q0,0 → q1,X,R
q0,⊔ → q_accept,⊔,R
q1,0 → q1,0,R
#
w = 0011
```

---

## Documentación Completa

README.md - Manual completo del usuario  
DIAGRAMA_MT.md - Diagrama y tabla de transiciones  
ENTREGA.md - Documento de entrega para el examen

---

## Requisitos

- Python 3.7 o superior
- No requiere instalación de paquetes adicionales

---

## Comandos Útiles

```bash
# Ver ayuda de Python
python3 --version

# Ejecutar casos individuales
python3 maquina_turing.py

# Ver contenido de un archivo de salida
cat caso_aceptacion_configuraciones.txt

# Listar todos los archivos
ls -lh *.txt *.py *.md
```

---

## Demo Rápida (30 segundos)

```bash
# Terminal 1: Ejecutar demo
python3 demo.py
# Seleccionar opción 1 (Aceptación)

# Terminal 2: Ver resultado
cat caso_aceptacion_configuraciones.txt
```

---

## Para el Día del Examen

1. Abrir terminal en la carpeta del proyecto
2. Ejecutar: `python3 demo.py`
3. Seleccionar caso a demostrar
4. Mostrar archivo de salida generado
5. Explicar el código si se requiere

---

## Archivos para Subir a Canvas

Código:
- `maquina_turing.py`

Especificaciones:
- `caso_aceptacion.txt`
- `caso_rechazo.txt`
- `caso_ciclo_infinito.txt`

Salidas:
- `caso_aceptacion_configuraciones.txt`
- `caso_rechazo_configuraciones.txt`
- `caso_ciclo_infinito_configuraciones.txt`

Documentación:
- `DIAGRAMA_MT.md`
- `README.md`
- `ENTREGA.md`

---

**Total: 10 archivos listos para Canvas**

---

Creado por: Javier España  
Fecha: 8 de noviembre de 2025  
Curso: Lenguajes y Máquinas - Parcial 4
