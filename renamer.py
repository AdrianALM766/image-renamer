from pathlib import Path
import generator


# #! usamos la funcion Path que no solo nos captura el objeto mediante la url directa
# route = Path("/home/adrian/Downloads/image (5).png")
# #? creamos la funcion para renombrar imagenes.
# def rename_image(route):
#     #creamo el nombre llamando a la funcion propia generator
#     new_name = generator.generator_name()
#     #creamos la NUEVA ruta para poder cambiar el nombre
#     new_route = route.parent /f"{new_name}.png"
#     #renombramos con la funcion propia rename
#     route.rename(new_route)
#     return None

# esta fcunion lo que hace es renombrar un unico archivo individual.
def rename_image(image_path):
    #? aseguramos que image_path si sea un path
    path = Path(image_path)
    #? extreamos extension
    extension = path.suffix
    
    #? generamos un nuevo nombre y construimos la nueva ruta en la misma carpeta
    new_name = generator.generator_name() + extension
    new_path = path.parent / new_name
    
    #? verificar que el archivo name no exista para no sobreescribir.
    while new_path.exists():
        new_name = generator.generator_name() + extension
        new_path = path.parent / new_name
    
    #? renombramos el archivo a nivel fisico
    path.rename(new_path)
    return new_path
    

    

if __name__ == "__main__":
    # Prueba rápida ingresando la ruta de una imagen concreta
    ruta_test = input("Ingresa la ruta completa de la imagen a probar: ")
    if Path(ruta_test).exists():
        nueva = rename_image(ruta_test)
        print(f"Imagen renombrada con éxito a: {nueva}")
    else:
        print("La ruta ingresada no existe.")


    

