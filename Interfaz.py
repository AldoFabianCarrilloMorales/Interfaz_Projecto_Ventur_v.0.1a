import tkinter as tk
from tkinter import ttk, messagebox

class StockPointApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stock Point - Sistema de Inventario y Ventas")
        self.geometry("1150x700")
        
        # Colores de la paleta moderna
        self.bg_color = "#f4f6f9"
        self.sidebar_color = "#1e293b"
        self.card_bg = "#ffffff"
        self.accent_color = "#0ea5e9"
        
        self.configure(bg=self.bg_color)
        
        # Lista de los 11 módulos requeridos
        self.modules = [
            ("Clientes", "Gestión de clientes, fichas y créditos"),
            ("Productos", "Catálogo, precios y stock de artículos"),
            ("Verificación de Inventario", "Auditoría, conteo físico y ajustes"),
            ("Caja", "Punto de venta y cobros rápidos"),
            ("Comisiones Marcas", "Cálculo de comisiones por marca asociada"),
            ("Marcas", "Administración y registro de marcas"),
            ("Registros Caja", "Historial de aperturas, cortes y cierres"),
            ("Categorías", "Clasificación jerárquica de productos"),
            ("Descuentos", "Promociones, vales y rebajas especiales"),
            ("Órdenes", "Pedidos de compra y seguimiento"),
            ("Tickets", "Historial de comprobantes y reimpresiones")
        ]
        
        self.create_widgets()

    def create_widgets(self):
        # 1. Header Superior
        header = tk.Frame(self, bg="#ffffff", height=70)
        header.pack(side=tk.TOP, fill=tk.X)
        header.pack_propagate(False)
        
        title_lbl = tk.Label(header, text="📦 Stock Point - Panel Principal", font=("Arial", 16, "bold"), bg="#ffffff", fg="#1e293b")
        title_lbl.pack(side=tk.LEFT, padx=25)
        
        user_lbl = tk.Label(header, text="Usuario: Administrador  |  Caja: Activa (#01)", font=("Arial", 10), bg="#ffffff", fg="#64748b")
        user_lbl.pack(side=tk.RIGHT, padx=25)
        
        # Separator Line
        ttk.Separator(self, orient="horizontal").pack(side=tk.TOP, fill=tk.X)

        # 2. Contenedor Principal (Sidebar + Área de Tarjetas)
        main_container = tk.Frame(self, bg=self.bg_color)
        main_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # 3. Menú Lateral (Sidebar)
        sidebar = tk.Frame(self, bg=self.sidebar_color, width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        
        tk.Label(sidebar, text="MENÚ RÁPIDO", font=("Arial", 10, "bold"), bg=self.sidebar_color, fg="#94a3b8").pack(pady=(20, 10), anchor="w", padx=20)
        
        for name, desc in self.modules:
            btn = tk.Button(sidebar, text=f"• {name}", font=("Arial", 10), bg=self.sidebar_color, fg="#cbd5e1",
                            activebackground="#334155", activeforeground="#ffffff", bd=0, anchor="w",
                            command=lambda n=name, d=desc: self.open_module(n, d))
            btn.pack(fill=tk.X, padx=15, pady=3)

        # 4. Área Central de Contenido (Grid de Tarjetas con Scroll)
        content_frame = tk.Frame(main_container, bg=self.bg_color)
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(content_frame, text="Módulos del Sistema", font=("Arial", 14, "bold"), bg=self.bg_color, fg="#1e293b").pack(anchor="w", pady=(0, 10))
        
        # Canvas y Scrollbar para las tarjetas
        canvas_container = tk.Canvas(content_frame, bg=self.bg_color, highlightthickness=0)
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas_container.yview)
        scrollable_frame = tk.Frame(canvas_container, bg=self.bg_color)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas_container.configure(scrollregion=canvas_container.bbox("all"))
        )
        
        canvas_container.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas_container.configure(yscrollcommand=scrollbar.set)
        
        canvas_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Generar las tarjetas en formato de cuadrícula (3 columnas)
        row = 0
        col = 0
        for name, desc in self.modules:
            card = tk.Frame(scrollable_frame, bg=self.card_bg, bd=1, relief=tk.SOLID, width=260, height=135)
            card.grid(row=row, column=col, padx=12, pady=12, sticky="nsew")
            card.pack_propagate(False)
            
            # Elementos de la tarjeta
            lbl_name = tk.Label(card, text=name, font=("Arial", 11, "bold"), bg=self.card_bg, fg="#0f172a")
            lbl_name.pack(anchor="w", padx=15, pady=(15, 5))
            
            lbl_desc = tk.Label(card, text=desc, font=("Arial", 9), bg=self.card_bg, fg="#64748b", wraplength=230, justify="left")
            lbl_desc.pack(anchor="w", padx=15)
            
            btn_access = tk.Button(card, text="Acceder →", font=("Arial", 9, "bold"), bg=self.accent_color, fg="#ffffff",
                                   bd=0, activebackground="#0284c7", activeforeground="#ffffff",
                                   command=lambda n=name, d=desc: self.open_module(n, d))
            btn_access.pack(side=tk.BOTTOM, anchor="e", padx=15, pady=10)
            
            col += 1
            if col > 2:
                col = 0
                row += 1

    def open_module(self, name, description):
        """Abre una ventana simulada o interactiva para cada opción seleccionada"""
        win = tk.Toplevel(self)
        win.title(f"Stock Point - Módulo: {name}")
        win.geometry("820x520")
        win.configure(bg="#f4f6f9")
        
        # Cabecera de la ventana secundaria
        header = tk.Frame(win, bg="#1e293b", height=60)
        header.pack(side=tk.TOP, fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(header, text=f"Panel de Control > {name}", font=("Arial", 12, "bold"), bg="#1e293b", fg="#ffffff").pack(side=tk.LEFT, padx=20)
        
        body = tk.Frame(win, bg="#f4f6f9")
        body.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        tk.Label(body, text=description, font=("Arial", 11), bg="#f4f6f9", fg="#475569").pack(anchor="w", pady=(0, 15))
        
        # Vistas personalizadas de ejemplo según el módulo
        if name == "Caja":
            tk.Label(body, text="Simulación de Punto de Venta", font=("Arial", 10, "bold"), bg="#f4f6f9", fg="#0f172a").pack(anchor="w", pady=5)
            
            frame_pos = tk.Frame(body, bg="#ffffff", bd=1, relief=tk.SOLID)
            frame_pos.pack(fill=tk.BOTH, expand=True, pady=10)
            
            tk.Entry(frame_pos, width=40, font=("Arial", 11)).pack(padx=20, pady=20, anchor="w")
            tk.Button(frame_pos, text="Procesar Cobro ($0.00)", bg="#10b981", fg="white", font=("Arial", 10, "bold"), padx=15, pady=8).pack(padx=20, anchor="w")
            
        elif name == "Productos":
            tk.Label(body, text="Inventario Actual de Artículos", font=("Arial", 10, "bold"), bg="#f4f6f9", fg="#0f172a").pack(anchor="w", pady=5)
            
            tree = ttk.Treeview(body, columns=("ID", "Producto", "Precio", "Stock"), show="headings", height=8)
            tree.heading("ID", text="ID")
            tree.heading("Producto", text="Descripción")
            tree.heading("Precio", text="Precio Venta")
            tree.heading("Stock", text="Existencia")
            
            tree.insert("", "end", values=("001", "Camisa Deportiva M", "$320.00", "24"))
            tree.insert("", "end", values=("002", "Pantalón Mezclilla", "$550.00", "12"))
            tree.insert("", "end", values=("003", "Tenis Running", "$1,200.00", "6"))
            tree.pack(fill=tk.BOTH, expand=True, pady=10)
            
        else:
            lbl_placeholder = tk.Label(body, text=f"Área de trabajo para el módulo de [{name}].\nAquí podrás gestionar los registros y filtros correspondientes.", 
                                       font=("Arial", 10), bg="#ffffff", fg="#64748b", bd=1, relief=tk.SOLID, padx=20, pady=40)
            lbl_placeholder.pack(fill=tk.BOTH, expand=True, pady=10)
            
        # Botón para cerrar módulo
        tk.Button(body, text="Regresar al Menú Principal", command=win.destroy, font=("Arial", 9, "bold"), bg="#64748b", fg="white", bd=0, padx=12, pady=6).pack(anchor="e", pady=10)

if __name__ == "__main__":
    app = StockPointApp()
    app.mainloop()