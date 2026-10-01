import secrets
ABC = "abcdefghijklmnopqrstuvwxyz_"
def generator_name():
    result = ""
    # for _ in range(8):
    #     result = result + secrets.choice(ABC)
    
    """
        se usa join nos sirve para concatenar numeros y 
        strings de forma rapida de toda una cadena/lista, etc
        el for i in range solo define cuantos de alli toma.
        El secrets es una funcion que toma una poscion aleatorio de la
        cadena que tenemos
    """
    result = "".join(secrets.choice(ABC) for i in range(8))
    return result



# esto es para probar codigo solo cuando se ejecute este mismo archivo y no desde otro lado.
if __name__ == "__main__":
    for i in range(100):
        nam = generator_name()
        print(nam)