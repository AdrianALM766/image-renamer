import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import renamer

def _centrar(win, w, h):
    win.update_idletasks()
    x = (win.winfo_screenwidth()  - w) // 2
    y = (win.winfo_screenheight() - h) // 2
    win.geometry(f"{w}x{h}+{x}+{y}")

def procesar_carpeta():
    ruta = filedialog.askdirectory(title="Selecciona la carpeta")
    if not ruta:
        return
    
    # Leemos la selección del desplegable
    seleccion = combo_extension.get()
    filtro = None if "Todas" in seleccion else seleccion

    renamer.rename_image_carpet(ruta, extension_filtro=filtro)
    messagebox.showinfo("Éxito", "Las imágenes de la carpeta fueron renombradas.")

def procesar_imagen():
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.webp"), ("Todos los archivos", "*.*")])
    if not ruta:
        return
    nueva = renamer.rename_image(ruta)
    messagebox.showinfo("Imagen renombrada", f"Nuevo nombre:\n{nueva.name}")

def main():
    global combo_extension

    root = tk.Tk()
    root.title("Renombrador de Imágenes")
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), 
        padding=(16, 10), relief="flat", background="#ff7316", foreground="black")
    style.map("Accent.TButton", background=[("active", "#45ff28"), ("disabled", "#93c5fd")])
    style.configure("Sub.TButton", font=("Segoe UI", 10, "bold"),
        padding=(16, 10), relief="flat", background="#ff7316", foreground="black")
    style.map("Sub.TButton", background=[("active", "#45ff28"), ("disabled", "#93fdf8")])
    style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"), foreground="#0f172a")
    style.configure("Sub.TLabel", font=("Segoe UI", 9), foreground="#64748b")

    frame = ttk.Frame(root, padding=24)
    frame.grid()

    # --- FILA 0: Título ---
    ttk.Label(frame, text="Renombrador de Imágenes", style="Title.TLabel").grid(row=0, column=0, columnspan=2)
    
    # --- FILA 1: Subtítulo ---
    ttk.Label(frame, text="Renombra archivos de forma masiva o individual", style="Sub.TLabel").grid(row=1, column=0, columnspan=2, pady=(4, 12))

    # --- FILA 2: Desplegable (Con espacio vertical de 18px hacia los botones) ---
    combo_extension = ttk.Combobox(
        frame, 
        values=["Todas (*.png, *.jpg, *.webp)", ".png", ".jpg", ".jpeg", ".webp"],
        state="readonly",
        width=30
    )
    combo_extension.current(0)
    combo_extension.grid(row=2, column=0, columnspan=2, pady=(0, 18))

    # --- FILA 3: Botones (Ubicados debajo del desplegable) ---
    ttk.Button(frame, text="Procesar carpeta", style="Accent.TButton", command=procesar_carpeta).grid(row=3, column=0, padx=8)
    ttk.Button(frame, text="Procesar imagen única", style="Sub.TButton", command=procesar_imagen).grid(row=3, column=1, padx=8)

    # --- Ajuste de tamaño de ventana a 260px de alto ---
    _centrar(root, 480, 260)
    root.mainloop()

if __name__ == "__main__":
    main()