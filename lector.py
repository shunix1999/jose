#! /usr/bin/python3
import argparse
# importacion de librerias


def leer_archivo(path):
                        # path es la ruta del archivo .txt a leer
                        # ejemplo: "C:/Users/My Folder/sample.txt"
                        # ejemplo: "/tmp/episodioX.txt"
                        # fh es nuestra variable fileholder, open es la funcion
                        # para abrir archivos, insertamos la ruta, y "r" indica que leeremos
                        # leemos el archivo y lo asignamos a una variable String
                        # al igual que se abrio para leer, requiere cerrarse
    # fh = open(path, "r")
    try: 
        with open(path, "r") as fh:
            texto = fh.read()
            lineas = texto.splitlines()
            texto_limpio = " ".join(lineas)
    except:
        texto_limpio=""
    return texto_limpio

#ya no se usa esta funcion
#def limpia_texto(texto):
    # Separamos esto para evitar que aparezcan los saltos de linea "\n"
 #   texto = texto.splitlines()
    # concactena dos objetos, en este caso 2 strings
  #  texto_limpio = " ".join(texto)
    #texto_limpio = "string"
    # print lowercase string
    #print("Lowercase string:", string.casefold())
  #  return texto_limpio


def contar_palabras(texto):
    dicc = dict()                       # se crea un diccionario para facilitar el contar
    # indicamos que cada palabra se diferencia por un espacio " "
    lista_palabras = texto.split(" ")

    for palabra in lista_palabras:
        # ignoraremos los puntos y comas de las palabras
        p = palabra.strip(",.")
        if p in dicc:                   # si existe la palabra, se le sumara
            dicc[p] += 1
        else:                           # si no, se creara
            dicc[p] = 1    
        
    if "" in dicc:
        del(dicc[""])            
    return dicc


 #recibe en stopwords: una cadena de las stopwords
 #recibe en texto: una cadena del texto a limpiar
 #regresa el texto limpio 
def eliminar_stopwords(dp, stopwords): 

    diccionario = {} 

    for (k,v) in dp.items(): 

        if k not in stopwords: 

           diccionario[k] = v 

    return diccionario 

'''set_spanish_stopwords = set(spanish_stopwords.split(" "))       
    lista_texto = texto.split(" ")                # se crea una lista del texto
    for palabra in lista_texto:
        print(palabra.strip(",."))                # se ignoran puntos y comas
        if palabra.lower() in set_stopwords:      # si la palabra en minúsculas se encuentra en stopwords
            lista_texto.remove(palabra)           # se elimina
    texto_limpio = " ".join(lista_texto)          # se hace una sola cadena de la lista 
    return texto_limpio

'''
def imprime_diccionario(dicc, minimo):
    #   Crea e imprime un diccionario
    '''
        recibe en dicc: diccionario en palabras
        recibe en minimo: entero con el minimo de palabras a contar
        no regresa nada
    '''
    lista = [(k, v) for k, v in dicc.items() if v >= minimo]
    lista_ordenada = sorted(lista, key=lambda x: x[1], reverse=True)
    for tupla in lista_ordenada:
        print(tupla[0], " = ", tupla[1])
    return


def main(path, min, stopwords):
    #   Imprime las palabras y cuantas veces se repiten
    ''' 
        recibe en path: direccion del archivo
        recibe en min: minimo de palabras contadas a mostrar
    '''
    texto = leer_archivo(path)
    stopwords = leer_archivo(stopwords)
    #texto = eliminar_stopwords(texto,stopwords)
    dicc = contar_palabras(texto)
    texto = eliminar_stopwords(dicc,stopwords) 
    imprime_diccionario(dicc, minimo)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help="nombre de archivo",default = "spanish_stopwords.txt", required=False)
    parser.add_argument('-m', '--minimo', dest='minimo', default = 3, help="minimo de palabras repetidas", type = int, required=False)
    args = parser.parse_args()
    archivo = args.archivo
    minimo = args.minimo
    stopwords = args.stopwords
    main(archivo, minimo, stopwords)
