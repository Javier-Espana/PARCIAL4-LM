# SIMULADOR DE MÁQUINA DE TURING DETERMINISTA
## PARCIAL 4 - Lógica Matemática

---

## Descripción

Programa simulador de Máquina de Turing Determinista que implementa la notación de clase vista en el curso. Reconoce el lenguaje L = {0^n 1^n | n ≥ 1} con casos de aceptación, rechazo y ciclo infinito.

**Aspectos a notar del programa:**
- Notación u q v sin buffers externos
- Interfaz gráfica con visualización animada de la cinta
- Manejo robusto de errores y casos excepcionales
- Validación exhaustiva de especificaciones
- Arquitectura modular profesional

---

## Uso

### Interfaz Gráfica (Recomendado)
```powershell
python gui.py
```

**Funcionalidades:**
- Cargar y visualizar especificaciones
- Validar componentes de la MT (10 validaciones)
- Ejecutar simulación paso a paso
- Visualización gráfica animada de la cinta
- Control de pasos (anterior/siguiente)
- Verificar cumplimiento de requisitos

### Línea de Comandos
```powershell
python main.py
```
Ingresa la ruta cuando se solicite, ejemplo: `especificaciones/caso_aceptacion.txt`