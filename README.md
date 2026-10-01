# Renombrador Aleatorio de Imágenes (Linux) 🖼️

Una herramienta liviana en Python con interfaz gráfica (GUI) diseñada para solucionar las colisiones de nombres al organizar lotes de imágenes descargadas en Linux.

## 🚀 El Problema
Al descargar imágenes en diferentes momentos desde internet o distintas fuentes, es común recibir nombres secuenciales como `1.jpg`, `2.jpg`, `imagen(1).jpg`, etc. Al intentar unificarlas en una sola carpeta, los nombres chocan, lo que puede provocar sobreescrituras accidentales o desorden.

## 💡 La Solución
Este programa renombra automáticamente las imágenes asignándoles una cadena aleatoria de **8 caracteres** usando un alfabeto de 27 símbolos (26 letras básicas en minúsculas + `_`), conservando siempre la extensión original (`.jpg`, `.png`, `.webp`, etc.).

Con un espacio de más de **282 mil millones de combinaciones posibles** ($27^8$), la probabilidad de colisión en lotes de varios cientos de imágenes es prácticamente nula. Además, incluye una verificación previa para garantizar que ningún archivo existente sea sobreescrito.

---

## 🛠️ Tecnologías y Requisitos
* **Lenguaje:** Python 3.x
* **Interfaz Gráfica:** Tkinter (incluido nativamente o vía `python3-tk` en la mayoría de distros Linux)
* **Librerías estándar utilizadas:** `secrets` / `random`, `pathlib`, `tkinter`

---

## 📋 Características Planeadas
* [ ] **Selección flexible:** Procesar una carpeta completa o elegir archivos de imagen manualmente.
* [ ] **Filtro por extensión:** Opción de renombrar solo formatos específicos (`.png`, `.jpg`, etc.) o todas las imágenes detectadas.
* [ ] **Renombrado seguro:** Validación preventiva en el sistema de archivos antes de renombrar cada elemento.
* [ ] **Interfaz limpia:** Flujo de trabajo visual mediante ventanas de selección de archivos en Linux.

---

## 📁 Estructura del Proyecto
```text
renombrador-imagenes/
├── main.py              # Código fuente principal (GUI + Lógica)
├── .gitignore           # Archivos ignorados por Git
└── README.md            # Documentación del proyecto