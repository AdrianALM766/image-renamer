import tkinter as tk
from tkinter import filedialog #! esro es para explorador de archivos nativos.
from tkinter import messagebox
import renamer

def procesar_carpeta():
    ruta = filedialog.askdirectory()
    if not ruta:
        return
    renamer.rename_image_carpet(ruta)
    messagebox.showinfo("Éxito", "Todas las imágenes de la carpeta fueron renombradas con éxito.")

def procesar_imagen():
    ruta_archivo = filedialog.askopenfilename(
        title="selecciona una imagen",
        filetypes=[
            ("Archivos de imagen", "*.png *.jpg *.jpeg *.webp"),
            ("Todos los archivos", "*.*")
        ]
    )
    
    if not ruta_archivo:
        return
    nueva_ruta = renamer.rename_image(ruta_archivo)
    messagebox.showinfo("Imagen Renombrada", f"La imagen se renombró correctamente a:\n{nueva_ruta.name}")
    

# --- Configuración de la Ventana ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Renombrador de Imágenes")
    root.geometry("300x150")

    # Los botones ejecutan las funciones mediante 'command'
    btn_carpeta = tk.Button(root, text="Procesar Carpeta", command=procesar_carpeta)
    btn_carpeta.pack(pady=10)

    btn_imagen = tk.Button(root, text="Procesar Imagen Única", command=procesar_imagen)
    btn_imagen.pack(pady=10)

    root.mainloop()
