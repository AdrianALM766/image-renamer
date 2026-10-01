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
    

def rename_image_carpet(file_path):
    #? aseguramos que file_path si sea un path
    path_file = Path(file_path)
    #una lista de las extensiones de los archivos permitidas a modficar
    extensiones_permitidas =  {".png", ".webp", ".jpg"}
    """
    #item for item in es compresion de listas.
    # el if item.is_file() es para aber que el archivo existe
    # and item.suffix.lower() existe para tomar la extension del archivo (y ponerla en minisculas) para buscar si existe en extensiones permitidas
    """
    archivos = [
        item for item in path_file.iterdir() 
        if item.is_file() and item.suffix.lower() in extensiones_permitidas]
    
    #llamamos la funcion de rename image en bucle
    for element in archivos:
        rename_image(element)
    return None
    

if __name__ == "__main__":
    # Prueba rápida ingresando la ruta de una imagen concreta
    ruta_test = input("Ingresa la ruta completa de la carpeta a probar: ")
    if Path(ruta_test).exists():
        nueva = rename_image_carpet(ruta_test)
        # for i in nueva:
        #     print(i)
    else:
        print("La ruta ingresada no existe.")



    

