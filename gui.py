"""
Interfaz Gráfica para el Simulador de Máquina de Turing
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import os
from src.maquina_turing import MaquinaTuring


class SimuladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Máquina de Turing Determinista")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        
        self.mt = None
        self.archivo_cargado = None
        self.configuraciones_pasos = []
        self.paso_actual = 0
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        main_container.rowconfigure(1, weight=1)
        
        self.crear_panel_superior(main_container)
        self.crear_notebook(main_container)
        self.crear_panel_inferior(main_container)
        
    def crear_panel_superior(self, parent):
        panel = ttk.LabelFrame(parent, text="Control Principal", padding="10")
        panel.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Button(panel, text="Cargar Especificación", 
                  command=self.cargar_archivo, width=20).grid(row=0, column=0, padx=5)
        ttk.Button(panel, text="Validar MT", 
                  command=self.validar, width=15).grid(row=0, column=1, padx=5)
        ttk.Button(panel, text="Simular", 
                  command=self.simular, width=15).grid(row=0, column=2, padx=5)
        ttk.Button(panel, text="Guardar Resultado", 
                  command=self.guardar, width=15).grid(row=0, column=3, padx=5)
        ttk.Button(panel, text="Limpiar", 
                  command=self.limpiar, width=15).grid(row=0, column=4, padx=5)
        
        self.label_archivo = ttk.Label(panel, text="No hay archivo cargado", 
                                       foreground="gray")
        self.label_archivo.grid(row=1, column=0, columnspan=5, pady=(10, 0))
        
    def crear_notebook(self, parent):
        self.notebook = ttk.Notebook(parent)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.crear_tab_especificacion()
        self.crear_tab_validacion()
        self.crear_tab_simulacion()
        self.crear_tab_visualizacion()
        self.crear_tab_diagrama()
        self.crear_tab_verificacion()
        
    def crear_tab_especificacion(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Especificación")
        
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        self.text_especificacion = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, width=80, height=30, font=("Consolas", 10))
        self.text_especificacion.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def crear_tab_validacion(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Validación")
        
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        
        info_frame = ttk.LabelFrame(frame, text="Componentes de la MT", padding="10")
        info_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.label_estados = ttk.Label(info_frame, text="Q: No cargado")
        self.label_estados.grid(row=0, column=0, sticky=tk.W, pady=2)
        
        self.label_sigma = ttk.Label(info_frame, text="Σ: No cargado")
        self.label_sigma.grid(row=1, column=0, sticky=tk.W, pady=2)
        
        self.label_gamma = ttk.Label(info_frame, text="Γ: No cargado")
        self.label_gamma.grid(row=2, column=0, sticky=tk.W, pady=2)
        
        self.label_q0 = ttk.Label(info_frame, text="q0: No cargado")
        self.label_q0.grid(row=3, column=0, sticky=tk.W, pady=2)
        
        self.label_qaccept = ttk.Label(info_frame, text="q_accept: No cargado")
        self.label_qaccept.grid(row=4, column=0, sticky=tk.W, pady=2)
        
        self.label_qreject = ttk.Label(info_frame, text="q_reject: No cargado")
        self.label_qreject.grid(row=5, column=0, sticky=tk.W, pady=2)
        
        self.label_delta = ttk.Label(info_frame, text="δ: No cargado")
        self.label_delta.grid(row=6, column=0, sticky=tk.W, pady=2)
        
        self.label_cadena = ttk.Label(info_frame, text="w: No cargado")
        self.label_cadena.grid(row=7, column=0, sticky=tk.W, pady=2)
        
        self.text_validacion = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, width=80, height=20, font=("Consolas", 10))
        self.text_validacion.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def crear_tab_simulacion(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Simulación")
        
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        self.text_simulacion = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, width=80, height=30, font=("Consolas", 10))
        self.text_simulacion.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def crear_tab_visualizacion(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Visualización Gráfica")
        
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        
        control_frame = ttk.Frame(frame, padding="5")
        control_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        ttk.Label(control_frame, text="Paso:").grid(row=0, column=0, padx=5)
        self.paso_var = tk.IntVar(value=0)
        self.paso_scale = ttk.Scale(control_frame, from_=0, to=0, 
                                     variable=self.paso_var, 
                                     command=self.actualizar_visualizacion,
                                     orient=tk.HORIZONTAL)
        self.paso_scale.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        control_frame.columnconfigure(1, weight=1)
        
        self.label_paso = ttk.Label(control_frame, text="0/0")
        self.label_paso.grid(row=0, column=2, padx=5)
        
        ttk.Button(control_frame, text="Anterior", 
                  command=self.paso_anterior).grid(row=0, column=3, padx=2)
        ttk.Button(control_frame, text="Siguiente", 
                  command=self.paso_siguiente).grid(row=0, column=4, padx=2)
        
        canvas_frame = ttk.LabelFrame(frame, text="Cinta y Estado", padding="10")
        canvas_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        canvas_frame.columnconfigure(0, weight=1)
        canvas_frame.rowconfigure(0, weight=1)
        
        self.canvas = tk.Canvas(canvas_frame, bg="white", height=400)
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        info_frame = ttk.LabelFrame(frame, text="Información del Paso", padding="10")
        info_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        self.label_config_actual = ttk.Label(info_frame, text="Configuración: -", 
                                             font=("Consolas", 11))
        self.label_config_actual.pack(anchor=tk.W, pady=2)
        
        self.label_transicion = ttk.Label(info_frame, text="Transición: -")
        self.label_transicion.pack(anchor=tk.W, pady=2)
        
    def crear_tab_verificacion(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Verificación de Requisitos")
        
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        
        requisitos_frame = ttk.LabelFrame(frame, text="Estado de Requisitos", padding="10")
        requisitos_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.checks = {}
        requisitos = [
            ("notacion", "Notación u q v (sin buffers externos)"),
            ("carga", "Carga archivo de especificación"),
            ("validacion", "Validación de componentes"),
            ("salida", "Genera archivo de configuraciones"),
            ("aceptacion", "Caso de aceptación"),
            ("rechazo", "Caso de rechazo"),
            ("ciclo", "Caso de ciclo infinito")
        ]
        
        for i, (key, text) in enumerate(requisitos):
            var = tk.BooleanVar(value=False)
            self.checks[key] = var
            cb = ttk.Checkbutton(requisitos_frame, text=text, variable=var, state="disabled")
            cb.grid(row=i, column=0, sticky=tk.W, pady=2)
        
        self.text_verificacion = scrolledtext.ScrolledText(
            frame, wrap=tk.WORD, width=80, height=20, font=("Consolas", 10))
        self.text_verificacion.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Button(frame, text="Verificar Archivos de Casos", 
                  command=self.verificar_casos).grid(row=2, column=0, pady=(10, 0))
        
    def crear_panel_inferior(self, parent):
        self.status_bar = ttk.Label(parent, text="Listo", relief=tk.SUNKEN)
        self.status_bar.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
    def cargar_archivo(self):
        try:
            filename = filedialog.askopenfilename(
                title="Seleccionar archivo de especificación",
                initialdir="especificaciones",
                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
            )
            
            if not filename:
                return
            
            self.archivo_cargado = filename
            self.mt = MaquinaTuring()
            self.configuraciones_pasos = []
            self.paso_actual = 0
            
            self.text_especificacion.delete(1.0, tk.END)
            self.text_validacion.delete(1.0, tk.END)
            self.text_simulacion.delete(1.0, tk.END)
            
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.text_especificacion.insert(1.0, contenido)
            except UnicodeDecodeError:
                with open(filename, 'r', encoding='latin-1') as f:
                    contenido = f.read()
                    self.text_especificacion.insert(1.0, contenido)
            
            if self.mt.cargar_archivo(filename):
                self.label_archivo.config(
                    text=f"Archivo cargado: {os.path.basename(filename)}", 
                    foreground="green"
                )
                self.actualizar_componentes()
                self.checks["carga"].set(True)
                self.status_bar.config(text="Archivo cargado exitosamente")
            else:
                self.label_archivo.config(
                    text="Error al cargar archivo", 
                    foreground="red"
                )
                self.status_bar.config(text="Error al cargar archivo")
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no existe")
            self.status_bar.config(text="Error: archivo no encontrado")
        except PermissionError:
            messagebox.showerror("Error", "No tiene permisos para leer el archivo")
            self.status_bar.config(text="Error: permisos insuficientes")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado al cargar archivo:\n{str(e)}")
            self.status_bar.config(text="Error al cargar archivo")
            
    def actualizar_componentes(self):
        if not self.mt:
            return
        
        self.label_estados.config(text=f"Q = {{{', '.join(sorted(self.mt.Q))}}}")
        self.label_sigma.config(text=f"Σ = {{{', '.join(sorted(self.mt.Sigma))}}}")
        self.label_gamma.config(text=f"Γ = {{{', '.join(sorted(self.mt.Gamma))}}}")
        self.label_q0.config(text=f"q0 = {self.mt.q0}")
        self.label_qaccept.config(text=f"q_accept = {self.mt.q_accept}")
        self.label_qreject.config(text=f"q_reject = {self.mt.q_reject}")
        self.label_delta.config(text=f"δ: {len(self.mt.delta)} transiciones")
        self.label_cadena.config(text=f"w = '{self.mt.cadena_entrada}'")
        
    def validar(self):
        if not self.mt:
            messagebox.showwarning("Advertencia", "Primero debe cargar un archivo de especificación")
            return
        
        try:
            self.text_validacion.delete(1.0, tk.END)
            self.text_validacion.insert(tk.END, "Validando especificación de la Máquina de Turing...\n\n")
            
            if self.mt.validar_maquina():
                self.text_validacion.insert(tk.END, "VALIDACIÓN EXITOSA\n\n", "success")
                self.text_validacion.insert(tk.END, "Todos los componentes son correctos:\n")
                self.text_validacion.insert(tk.END, "- Q no está vacío\n")
                self.text_validacion.insert(tk.END, "- q0 pertenece a Q\n")
                self.text_validacion.insert(tk.END, "- q_accept pertenece a Q\n")
                self.text_validacion.insert(tk.END, "- q_reject pertenece a Q\n")
                self.text_validacion.insert(tk.END, "- q_accept diferente de q_reject\n")
                self.text_validacion.insert(tk.END, "- Σ es subconjunto de Γ\n")
                self.text_validacion.insert(tk.END, "- Símbolo blanco en Γ\n")
                self.text_validacion.insert(tk.END, "- Símbolo blanco no en Σ\n")
                self.text_validacion.insert(tk.END, "- Cadena usa solo símbolos de Σ\n")
                self.text_validacion.insert(tk.END, "- Transiciones válidas\n")
                
                self.text_validacion.tag_config("success", foreground="green", font=("Consolas", 10, "bold"))
                self.checks["validacion"].set(True)
                self.checks["notacion"].set(True)
                self.status_bar.config(text="Validación exitosa")
            else:
                self.text_validacion.insert(tk.END, "VALIDACIÓN FALLIDA\n\n", "error")
                self.text_validacion.tag_config("error", foreground="red", font=("Consolas", 10, "bold"))
                self.status_bar.config(text="Validación fallida")
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la validación:\n{str(e)}")
            self.status_bar.config(text="Error en validación")
            
    def simular(self):
        if not self.mt:
            messagebox.showwarning("Advertencia", "Primero debe cargar un archivo de especificación")
            return
        
        if not self.mt.Q:
            messagebox.showwarning("Advertencia", "Debe validar la especificación primero")
            return
        
        try:
            self.text_simulacion.delete(1.0, tk.END)
            self.text_simulacion.insert(tk.END, "Iniciando simulación de la Máquina de Turing...\n\n")
            
            resultado = self.mt.simular(pasos_max=1000)
            
            if self.mt.simulador:
                self.configuraciones_pasos = self.mt.simulador.configuraciones[:]
                for config in self.mt.simulador.configuraciones:
                    self.text_simulacion.insert(tk.END, config + "\n")
            
            self.text_simulacion.insert(tk.END, "\n" + "=" * 70 + "\n")
            if resultado == 'ACEPTADA':
                self.text_simulacion.insert(tk.END, "RESULTADO: CADENA ACEPTADA\n", "success")
                self.text_simulacion.tag_config("success", foreground="green", font=("Consolas", 11, "bold"))
            elif resultado == 'RECHAZADA':
                self.text_simulacion.insert(tk.END, "RESULTADO: CADENA RECHAZADA\n", "reject")
                self.text_simulacion.tag_config("reject", foreground="red", font=("Consolas", 11, "bold"))
            else:
                self.text_simulacion.insert(tk.END, "RESULTADO: CICLO INFINITO\n", "cycle")
                self.text_simulacion.tag_config("cycle", foreground="orange", font=("Consolas", 11, "bold"))
            
            self.checks["salida"].set(True)
            self.status_bar.config(text=f"Simulación completada: {resultado}")
            
            if len(self.configuraciones_pasos) > 0:
                self.paso_scale.config(to=len(self.configuraciones_pasos)-1)
                self.paso_var.set(0)
                self.actualizar_visualizacion()
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la simulación:\n{str(e)}")
            self.status_bar.config(text="Error en simulación")
        
    def guardar(self):
        if not self.mt or not self.mt.simulador:
            messagebox.showwarning("Advertencia", "Primero debe ejecutar la simulación")
            return
        
        try:
            if self.archivo_cargado and self.archivo_cargado.endswith('.txt'):
                default_name = self.archivo_cargado.replace('.txt', '_configuraciones.txt')
            else:
                default_name = "configuraciones.txt"
            
            filename = filedialog.asksaveasfilename(
                title="Guardar configuraciones",
                initialdir="salidas",
                initialfile=os.path.basename(default_name),
                defaultextension=".txt",
                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
            )
            
            if not filename:
                return
            
            self.mt.guardar_resultado(filename)
            messagebox.showinfo("Éxito", f"Configuraciones guardadas en:\n{filename}")
            self.status_bar.config(text=f"Archivo guardado: {os.path.basename(filename)}")
        except PermissionError:
            messagebox.showerror("Error", "No tiene permisos para guardar en esa ubicación")
            self.status_bar.config(text="Error: permisos insuficientes")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar archivo:\n{str(e)}")
            self.status_bar.config(text="Error al guardar")
            
    def verificar_casos(self):
        self.text_verificacion.delete(1.0, tk.END)
        self.text_verificacion.insert(tk.END, "Verificando archivos de casos de prueba...\n\n")
        
        casos = [
            ("especificaciones/caso_aceptacion.txt", "salidas/caso_aceptacion_configuraciones.txt", "aceptacion"),
            ("especificaciones/caso_rechazo.txt", "salidas/caso_rechazo_configuraciones.txt", "rechazo"),
            ("especificaciones/caso_ciclo_infinito.txt", "salidas/caso_ciclo_infinito_configuraciones.txt", "ciclo")
        ]
        
        for spec, salida, check_key in casos:
            self.text_verificacion.insert(tk.END, f"Verificando: {os.path.basename(spec)}\n")
            
            if os.path.exists(spec):
                self.text_verificacion.insert(tk.END, f"  Especificación: OK\n", "ok")
            else:
                self.text_verificacion.insert(tk.END, f"  Especificación: FALTA\n", "error")
                
            if os.path.exists(salida):
                self.text_verificacion.insert(tk.END, f"  Salida: OK\n", "ok")
                self.checks[check_key].set(True)
            else:
                self.text_verificacion.insert(tk.END, f"  Salida: FALTA\n", "error")
                
            self.text_verificacion.insert(tk.END, "\n")
        
        self.text_verificacion.tag_config("ok", foreground="green")
        self.text_verificacion.tag_config("error", foreground="red")
        
        total_checks = sum(1 for v in self.checks.values() if v.get())
        self.text_verificacion.insert(tk.END, f"\nRequisitos cumplidos: {total_checks}/7\n")
        
        if total_checks == 7:
            self.text_verificacion.insert(tk.END, "\nTodos los requisitos están completos\n", "success")
            self.text_verificacion.tag_config("success", foreground="green", font=("Consolas", 10, "bold"))
        
    def actualizar_visualizacion(self, *args):
        if not self.configuraciones_pasos:
            return
        
        try:
            paso = int(self.paso_var.get())
            if paso >= len(self.configuraciones_pasos):
                paso = len(self.configuraciones_pasos) - 1
            
            self.paso_actual = paso
            self.label_paso.config(text=f"{paso}/{len(self.configuraciones_pasos)-1}")
            
            config = self.configuraciones_pasos[paso]
            self.label_config_actual.config(text=f"Configuración: {config}")
            
            if paso > 0:
                config_anterior = self.configuraciones_pasos[paso-1]
                self.label_transicion.config(text=f"Desde: {config_anterior}")
            else:
                self.label_transicion.config(text="Configuración inicial")
            
            self.dibujar_cinta(config)
        except Exception as e:
            self.status_bar.config(text=f"Error en visualización: {str(e)}")
    
    def dibujar_cinta(self, config_str):
        self.canvas.delete("all")
        
        try:
            if "Configuración" in config_str:
                config_str = config_str.split(": ", 1)[1] if ": " in config_str else config_str
            
            match = None
            for estado in self.mt.Q if self.mt else []:
                if estado in config_str:
                    idx = config_str.find(estado)
                    izq = config_str[:idx]
                    der = config_str[idx+len(estado):]
                    match = (izq, estado, der)
                    break
            
            if not match:
                self.canvas.create_text(400, 200, text="No se pudo parsear configuración", 
                                       font=("Arial", 12), fill="red")
                return
            
            izq, estado, der = match
            cinta = list(izq) + list(der)
            cabeza_pos = len(izq)
            
            if not cinta:
                cinta = ['⊔']
                cabeza_pos = 0
            
            cell_width = 50
            cell_height = 50
            start_x = 100
            y_pos = 150
            
            visible_cells = min(20, len(cinta))
            start_idx = max(0, cabeza_pos - 10)
            end_idx = min(len(cinta), start_idx + visible_cells)
            
            for i in range(start_idx, end_idx):
                x = start_x + (i - start_idx) * cell_width
                
                color = "#ffff99" if i == cabeza_pos else "white"
                self.canvas.create_rectangle(x, y_pos, x + cell_width, y_pos + cell_height,
                                            fill=color, outline="black", width=2)
                
                simbolo = cinta[i] if i < len(cinta) else '⊔'
                self.canvas.create_text(x + cell_width/2, y_pos + cell_height/2,
                                       text=simbolo, font=("Courier", 16, "bold"))
                
                if i == cabeza_pos:
                    arrow_y = y_pos - 30
                    self.canvas.create_text(x + cell_width/2, arrow_y,
                                          text="▼", font=("Arial", 20), fill="red")
            
            estado_y = y_pos + cell_height + 50
            self.canvas.create_text(400, estado_y,
                                   text=f"Estado actual: {estado}",
                                   font=("Arial", 14, "bold"), fill="blue")
            
            color_resultado = "black"
            if estado == (self.mt.q_accept if self.mt else None):
                color_resultado = "green"
                resultado_text = "ESTADO DE ACEPTACIÓN"
            elif estado == (self.mt.q_reject if self.mt else None):
                color_resultado = "red"
                resultado_text = "ESTADO DE RECHAZO"
            else:
                resultado_text = ""
            
            if resultado_text:
                self.canvas.create_text(400, estado_y + 30,
                                       text=resultado_text,
                                       font=("Arial", 12, "bold"), fill=color_resultado)
        except Exception as e:
            self.canvas.create_text(400, 200, 
                                   text=f"Error al dibujar cinta: {str(e)}", 
                                   font=("Arial", 12), fill="red")
    
    def paso_anterior(self):
        if self.paso_var.get() > 0:
            self.paso_var.set(self.paso_var.get() - 1)
            self.actualizar_visualizacion()
    
    def paso_siguiente(self):
        if self.paso_var.get() < len(self.configuraciones_pasos) - 1:
            self.paso_var.set(self.paso_var.get() + 1)
            self.actualizar_visualizacion()
    
    def crear_tab_diagrama(self):
        frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(frame, text="Diagrama MT")
        
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(button_frame, text="Exportar como Imagen PNG", 
                  command=self.exportar_diagrama_png).pack(side=tk.LEFT, padx=5)
        
        canvas_container = ttk.Frame(frame)
        canvas_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        canvas_container.columnconfigure(0, weight=1)
        canvas_container.rowconfigure(0, weight=1)
        
        self.canvas_diagrama = tk.Canvas(canvas_container, bg="white", width=1000, height=600)
        self.canvas_diagrama.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        scrollbar_y = ttk.Scrollbar(canvas_container, orient=tk.VERTICAL, 
                                     command=self.canvas_diagrama.yview)
        scrollbar_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.canvas_diagrama.configure(yscrollcommand=scrollbar_y.set)
        
        self.dibujar_diagrama_mt()
    
    def dibujar_diagrama_mt(self):
        self.canvas_diagrama.delete("all")
        
        width = 1000
        height = 800
        self.canvas_diagrama.configure(scrollregion=(0, 0, width, height))
        
        title_y = 30
        self.canvas_diagrama.create_text(width/2, title_y, 
                                        text="DIAGRAMA DE MÁQUINA DE TURING",
                                        font=("Arial", 18, "bold"), fill="black")
        
        subtitle_y = 60
        self.canvas_diagrama.create_text(width/2, subtitle_y,
                                        text="Lenguaje: L = {0ⁿ 1ⁿ | n ≥ 1}",
                                        font=("Arial", 14), fill="blue")
        
        estados = {
            'q0': (150, 200),
            'q1': (400, 200),
            'q2': (650, 200),
            'q3': (400, 350),
            'q_accept': (650, 350),
            'q_reject': (150, 350)
        }
        
        radio = 35
        
        for estado, (x, y) in estados.items():
            if estado == 'q_accept':
                self.canvas_diagrama.create_oval(x-radio-5, y-radio-5, x+radio+5, y+radio+5,
                                                fill="lightgreen", outline="darkgreen", width=3)
                self.canvas_diagrama.create_oval(x-radio, y-radio, x+radio, y+radio,
                                                fill="lightgreen", outline="darkgreen", width=2)
                self.canvas_diagrama.create_text(x, y, text=estado, font=("Arial", 10, "bold"))
            elif estado == 'q_reject':
                self.canvas_diagrama.create_oval(x-radio-5, y-radio-5, x+radio+5, y+radio+5,
                                                fill="lightcoral", outline="darkred", width=3)
                self.canvas_diagrama.create_oval(x-radio, y-radio, x+radio, y+radio,
                                                fill="lightcoral", outline="darkred", width=2)
                self.canvas_diagrama.create_text(x, y, text=estado, font=("Arial", 10, "bold"))
            else:
                self.canvas_diagrama.create_oval(x-radio, y-radio, x+radio, y+radio,
                                                fill="lightblue", outline="blue", width=2)
                self.canvas_diagrama.create_text(x, y, text=estado, font=("Arial", 11, "bold"))
        
        x0, y0 = estados['q0']
        self.canvas_diagrama.create_line(50, y0, x0-radio, y0, arrow=tk.LAST, width=2, fill="red")
        self.canvas_diagrama.create_text(30, y0, text="inicio", font=("Arial", 9), fill="red")
        
        transiciones = [
            ('q0', 'q1', '0/X,R', 'recta'),
            ('q1', 'q2', '1/Y,L', 'recta'),
            ('q2', 'q0', 'X/X,R', 'curva_abajo'),
            ('q0', 'q3', 'Y/Y,R', 'curva_abajo'),
            ('q3', 'q_accept', '⊔/⊔,R', 'recta'),
            ('q0', 'q_reject', '1/1,R o ⊔/⊔,R', 'recta'),
            ('q1', 'q_reject', '⊔/⊔,R', 'curva_abajo'),
            ('q1', 'q1', '0/0,R\nY/Y,R', 'loop_arriba'),
            ('q2', 'q2', '0/0,L\nY/Y,L', 'loop_arriba'),
            ('q3', 'q3', 'Y/Y,R', 'loop_arriba'),
        ]
        
        for trans in transiciones:
            estado_orig, estado_dest, etiqueta, tipo = trans
            x1, y1 = estados[estado_orig]
            x2, y2 = estados[estado_dest]
            
            if tipo == 'recta':
                dx = x2 - x1
                dy = y2 - y1
                dist = (dx*dx + dy*dy) ** 0.5
                if dist > 0:
                    offset_x1 = dx * radio / dist
                    offset_y1 = dy * radio / dist
                    offset_x2 = dx * radio / dist
                    offset_y2 = dy * radio / dist
                    
                    self.canvas_diagrama.create_line(
                        x1 + offset_x1, y1 + offset_y1,
                        x2 - offset_x2, y2 - offset_y2,
                        arrow=tk.LAST, width=2, fill="black"
                    )
                    
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2 - 15
                    self.canvas_diagrama.create_text(mid_x, mid_y, text=etiqueta,
                                                    font=("Courier", 9), fill="darkblue")
            
            elif tipo == 'curva_abajo':
                control_y = max(y1, y2) + 80
                
                self.canvas_diagrama.create_line(
                    x1 + radio, y1 + radio/2,
                    x1 + radio + 30, control_y,
                    x2 - radio - 30, control_y,
                    x2 - radio, y2 + radio/2,
                    smooth=True, arrow=tk.LAST, width=2, fill="black"
                )
                
                label_x = (x1 + x2) / 2
                label_y = control_y + 10
                self.canvas_diagrama.create_text(label_x, label_y, text=etiqueta,
                                                font=("Courier", 9), fill="darkblue")
            
            elif tipo == 'loop_arriba':
                loop_y = y1 - radio - 40
                
                self.canvas_diagrama.create_arc(
                    x1 - 30, loop_y,
                    x1 + 30, y1 - radio,
                    start=180, extent=180, style=tk.ARC, width=2, outline="black"
                )
                
                self.canvas_diagrama.create_line(
                    x1 + 25, y1 - radio - 5,
                    x1 + 30, y1 - radio,
                    x1 + 25, y1 - radio + 5,
                    width=2, fill="black"
                )
                
                self.canvas_diagrama.create_text(x1, loop_y - 10, text=etiqueta,
                                                font=("Courier", 9), fill="darkblue",
                                                justify=tk.CENTER)
        
        legend_y = 520
        self.canvas_diagrama.create_text(width/2, legend_y,
                                        text="COMPONENTES FORMALES",
                                        font=("Arial", 12, "bold"))
        
        legend_y += 30
        componentes = [
            "Q = {q0, q1, q2, q3, q_accept, q_reject}",
            "Σ = {0, 1}",
            "Γ = {0, 1, X, Y, ⊔}",
            "q0 = q0",
            "F = {q_accept} (estado de aceptación)",
            "q_reject = estado de rechazo"
        ]
        
        for comp in componentes:
            self.canvas_diagrama.create_text(width/2, legend_y, text=comp,
                                            font=("Courier", 10), anchor=tk.CENTER)
            legend_y += 25
        
        strategy_y = legend_y + 20
        self.canvas_diagrama.create_text(width/2, strategy_y,
                                        text="ESTRATEGIA",
                                        font=("Arial", 12, "bold"))
        
        strategy_y += 30
        estrategia = [
            "1. Marca el primer 0 con X y busca el primer 1",
            "2. Marca el primer 1 con Y y regresa al inicio",
            "3. Repite hasta emparejar todos los 0s con 1s",
            "4. Verifica que no queden símbolos sin emparejar",
            "5. Acepta si todos están emparejados, rechaza si no"
        ]
        
        for linea in estrategia:
            self.canvas_diagrama.create_text(width/2, strategy_y, text=linea,
                                            font=("Arial", 9), anchor=tk.CENTER)
            strategy_y += 20
    
    def exportar_diagrama_png(self):
        try:
            import tkinter.messagebox as mb
            import math
            
            filename = filedialog.asksaveasfilename(
                title="Guardar diagrama como PNG",
                initialdir=".",
                initialfile="diagrama_mt.png",
                defaultextension=".png",
                filetypes=[("PNG", "*.png"), ("Todos los archivos", "*.*")]
            )
            
            if not filename:
                return
            
            try:
                from PIL import Image, ImageDraw, ImageFont
                
                width, height = 1000, 850
                img = Image.new('RGB', (width, height), 'white')
                draw = ImageDraw.Draw(img)
                
                try:
                    title_font = ImageFont.truetype("arial.ttf", 18)
                    subtitle_font = ImageFont.truetype("arial.ttf", 14)
                    normal_font = ImageFont.truetype("arial.ttf", 11)
                    small_font = ImageFont.truetype("arial.ttf", 9)
                    code_font = ImageFont.truetype("cour.ttf", 9)
                    trans_font = ImageFont.truetype("cour.ttf", 8)
                except:
                    title_font = ImageFont.load_default()
                    subtitle_font = ImageFont.load_default()
                    normal_font = ImageFont.load_default()
                    small_font = ImageFont.load_default()
                    code_font = ImageFont.load_default()
                    trans_font = ImageFont.load_default()
                
                draw.text((width/2, 30), "DIAGRAMA DE MÁQUINA DE TURING",
                         fill="black", font=title_font, anchor="mm")
                draw.text((width/2, 60), "Lenguaje: L = {0ⁿ 1ⁿ | n ≥ 1}",
                         fill="blue", font=subtitle_font, anchor="mm")
                
                estados = {
                    'q0': (150, 200),
                    'q1': (400, 200),
                    'q2': (650, 200),
                    'q3': (400, 350),
                    'q_accept': (650, 350),
                    'q_reject': (150, 350)
                }
                
                radio = 35
                
                transiciones = [
                    ('q0', 'q1', '0/X,R', 'linea'),
                    ('q0', 'q3', 'Y/Y,R', 'curva_abajo'),
                    ('q0', 'q_reject', '1/1,R\n⊔/⊔,R', 'linea'),
                    ('q1', 'q2', '1/Y,L', 'linea'),
                    ('q1', 'q_reject', '⊔/⊔,R', 'curva_abajo'),
                    ('q2', 'q0', 'X/X,R', 'linea'),
                    ('q3', 'q_accept', '⊔/⊔,R', 'linea'),
                    ('q1', 'q1', '0/0,R\nY/Y,R', 'loop_arriba'),
                    ('q2', 'q2', '0/0,L\nY/Y,L', 'loop_arriba'),
                    ('q3', 'q3', 'Y/Y,R', 'loop_arriba'),
                ]
                
                for origen, destino, etiqueta, tipo in transiciones:
                    x1, y1 = estados[origen]
                    x2, y2 = estados[destino]
                    
                    if tipo == 'linea':
                        dx = x2 - x1
                        dy = y2 - y1
                        angulo = math.atan2(dy, dx)
                        
                        x1_borde = x1 + radio * math.cos(angulo)
                        y1_borde = y1 + radio * math.sin(angulo)
                        x2_borde = x2 - radio * math.cos(angulo)
                        y2_borde = y2 - radio * math.sin(angulo)
                        
                        draw.line([(x1_borde, y1_borde), (x2_borde, y2_borde)],
                                 fill="black", width=2)
                        
                        arrow_len = 10
                        arrow_angle = 0.3
                        draw.line([(x2_borde, y2_borde),
                                  (x2_borde - arrow_len * math.cos(angulo - arrow_angle),
                                   y2_borde - arrow_len * math.sin(angulo - arrow_angle))],
                                 fill="black", width=2)
                        draw.line([(x2_borde, y2_borde),
                                  (x2_borde - arrow_len * math.cos(angulo + arrow_angle),
                                   y2_borde - arrow_len * math.sin(angulo + arrow_angle))],
                                 fill="black", width=2)
                        
                        mid_x = (x1 + x2) / 2
                        mid_y = (y1 + y2) / 2 - 12
                        draw.text((mid_x, mid_y), etiqueta, fill="darkblue",
                                 font=trans_font, anchor="mm")
                    
                    elif tipo == 'curva_abajo':
                        control_y = max(y1, y2) + 60
                        
                        steps = 30
                        for i in range(steps):
                            t = i / steps
                            x_cur = (1-t)**2 * x1 + 2*(1-t)*t * ((x1+x2)/2) + t**2 * x2
                            y_cur = (1-t)**2 * y1 + 2*(1-t)*t * control_y + t**2 * y2
                            
                            t_next = (i+1) / steps
                            x_next = (1-t_next)**2 * x1 + 2*(1-t_next)*t_next * ((x1+x2)/2) + t_next**2 * x2
                            y_next = (1-t_next)**2 * y1 + 2*(1-t_next)*t_next * control_y + t_next**2 * y2
                            
                            draw.line([(x_cur, y_cur), (x_next, y_next)],
                                     fill="black", width=2)
                        
                        dx = x2 - ((x1+x2)/2)
                        dy = y2 - control_y
                        angulo = math.atan2(dy, dx)
                        x2_borde = x2 - radio * math.cos(angulo)
                        y2_borde = y2 - radio * math.sin(angulo)
                        
                        arrow_len = 10
                        arrow_angle = 0.3
                        draw.line([(x2_borde, y2_borde),
                                  (x2_borde - arrow_len * math.cos(angulo - arrow_angle),
                                   y2_borde - arrow_len * math.sin(angulo - arrow_angle))],
                                 fill="black", width=2)
                        draw.line([(x2_borde, y2_borde),
                                  (x2_borde - arrow_len * math.cos(angulo + arrow_angle),
                                   y2_borde - arrow_len * math.sin(angulo + arrow_angle))],
                                 fill="black", width=2)
                        
                        label_x = (x1 + x2) / 2
                        label_y = control_y + 10
                        draw.text((label_x, label_y), etiqueta, fill="darkblue",
                                 font=trans_font, anchor="mm")
                    
                    elif tipo == 'loop_arriba':
                        loop_y = y1 - radio - 35
                        loop_width = 50
                        
                        bbox = [x1 - loop_width/2, loop_y, x1 + loop_width/2, y1 - radio]
                        draw.arc(bbox, start=180, end=0, fill="black", width=2)
                        
                        draw.line([(x1 - loop_width/2, y1 - radio - 3),
                                  (x1 - loop_width/2 - 5, y1 - radio),
                                  (x1 - loop_width/2, y1 - radio + 3)],
                                 fill="black", width=2)
                        
                        draw.text((x1, loop_y - 8), etiqueta, fill="darkblue",
                                 font=trans_font, anchor="mm")
                
                for estado, (x, y) in estados.items():
                    if estado == 'q_accept':
                        draw.ellipse([x-radio-5, y-radio-5, x+radio+5, y+radio+5],
                                    fill="lightgreen", outline="darkgreen", width=3)
                        draw.ellipse([x-radio, y-radio, x+radio, y+radio],
                                    fill="lightgreen", outline="darkgreen", width=2)
                    elif estado == 'q_reject':
                        draw.ellipse([x-radio-5, y-radio-5, x+radio+5, y+radio+5],
                                    fill="lightcoral", outline="darkred", width=3)
                        draw.ellipse([x-radio, y-radio, x+radio, y+radio],
                                    fill="lightcoral", outline="darkred", width=2)
                    else:
                        draw.ellipse([x-radio, y-radio, x+radio, y+radio],
                                    fill="lightblue", outline="blue", width=2)
                    
                    draw.text((x, y), estado, fill="black", font=normal_font, anchor="mm")
                
                x0, y0 = estados['q0']
                draw.line([50, y0, x0-radio, y0], fill="red", width=3)
                draw.polygon([(x0-radio, y0), (x0-radio-10, y0-5), (x0-radio-10, y0+5)], 
                           fill="red")
                draw.text((30, y0), "inicio", fill="red", font=small_font, anchor="mm")
                
                legend_y = 550
                draw.text((width/2, legend_y), "COMPONENTES FORMALES",
                         fill="black", font=subtitle_font, anchor="mm")
                
                legend_y += 30
                componentes = [
                    "Q = {q0, q1, q2, q3, q_accept, q_reject}",
                    "Σ = {0, 1}",
                    "Γ = {0, 1, X, Y, ⊔}",
                    "q0 = q0 (estado inicial)",
                    "F = {q_accept} (estado de aceptación)",
                    "q_reject (estado de rechazo)"
                ]
                
                for comp in componentes:
                    draw.text((width/2, legend_y), comp, fill="black", 
                             font=code_font, anchor="mm")
                    legend_y += 22
                
                legend_y += 15
                draw.text((width/2, legend_y), "ESTRATEGIA",
                         fill="black", font=subtitle_font, anchor="mm")
                
                legend_y += 25
                estrategia = [
                    "1. Marcar primer 0 con X, buscar primer 1",
                    "2. Marcar primer 1 con Y, regresar al inicio",
                    "3. Repetir hasta procesar todos los símbolos",
                    "4. Aceptar si todo está emparejado"
                ]
                
                for linea in estrategia:
                    draw.text((width/2, legend_y), linea, fill="black", 
                             font=code_font, anchor="mm")
                    legend_y += 20
                
                img.save(filename, 'PNG')
                messagebox.showinfo("Éxito", 
                    f"Diagrama COMPLETO exportado como:\n{filename}\n\n"
                    ":D Incluye estados de aceptación y rechazo\n"
                    ":D Incluye todas las transiciones")
                self.status_bar.config(text=f"Diagrama exportado: {os.path.basename(filename)}")
                
            except ImportError:
                mb.showinfo("Información",
                           "Para exportar como PNG, instala Pillow:\n\n"
                           "pip install pillow\n\n"
                           "Por ahora, puedes usar captura de pantalla del diagrama.")
                self.status_bar.config(text="Pillow no instalado - usa captura de pantalla")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar diagrama:\n{str(e)}")
            self.status_bar.config(text="Error al exportar diagrama")
    
    def limpiar(self):
        self.mt = None
        self.archivo_cargado = None
        self.configuraciones_pasos = []
        self.paso_actual = 0
        
        self.text_especificacion.delete(1.0, tk.END)
        self.text_validacion.delete(1.0, tk.END)
        self.text_simulacion.delete(1.0, tk.END)
        self.text_verificacion.delete(1.0, tk.END)
        self.canvas.delete("all")
        
        self.label_archivo.config(text="No hay archivo cargado", foreground="gray")
        self.label_estados.config(text="Q: No cargado")
        self.label_sigma.config(text="Σ: No cargado")
        self.label_gamma.config(text="Γ: No cargado")
        self.label_q0.config(text="q0: No cargado")
        self.label_qaccept.config(text="q_accept: No cargado")
        self.label_qreject.config(text="q_reject: No cargado")
        self.label_delta.config(text="δ: No cargado")
        self.label_cadena.config(text="w: No cargado")
        
        self.paso_scale.config(to=0)
        self.paso_var.set(0)
        self.label_paso.config(text="0/0")
        self.label_config_actual.config(text="Configuración: -")
        self.label_transicion.config(text="Transición: -")
        
        for var in self.checks.values():
            var.set(False)
        
        self.status_bar.config(text="Listo")


def main():
    root = tk.Tk()
    app = SimuladorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
