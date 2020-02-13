#! /usr/bin/python3

import argparse
import lector
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


def contar(archivo,stopwords_url):
    texto = lector.leer_archivo(archivo)
    #dicc = dict()                       # se crea un diccionario para facilitar el contar
    #dicc2 = dict()
    # indicamos que cada palabra se diferencia por un espacio " "
    lista_palabras = texto.split(" ")
    total = lista_palabras
    stopwords = lector.leer_stopwords(stopwords_url)
    #palabras_clave = texto.split(" ")
    dpc = dict() #dicc.palabras clave
    dps = dict() #dicc.palabras stopwords
    
    for palabra in lista_palabras:
        # ignoraremos los puntos y comas de las palabras
        p = palabra.lower().strip(",.")
        if p in stopwords:                   #es stopwords?
           if p in dps:                      #ya existe?
              dps[p] += 1                    #agregamos 1
           else:                             # si no, se creara
              dps[p] = 1                     #inicial con 1  
        else:
           if p in dpc:                       #ya existe?
              dpc[p] += 1                    #agregamos 1
           else:
              dpc[p] = 1                     #creamos con 1   
              
    #if "" in dicc:
    #    del(dicc[""])
    print(len(dps),"Palabras stropwords") #imprime el numero de stopwords
    print(len(dpc),"Palabras clave") #imprime las palabras clave
    print(len(total),"Palabras totales") #escribe las palabras totales en el archivo         
    return total
    
   #  for palabra in lista_palabras:
        # ignoraremos los puntos y comas de las palabras
    #    p = palabra.strip(",.")
     #   if p in dicc:                   # si existe la palabra, se le sumara
      #      dicc[p] += 1
       # else:                           # si no, se creara
        #    dicc[p] = 1    
        
    #if "" in dicc:
    #    del(dicc[""])            
    #return dicc  

def main(archivo,minimo,archivo_stopwords):
    texto = leer_archivo(archivo)
    
    #texto = leer_archivo(path)
    #stopwords = leer_archivo(stopwords)
    #texto = eliminar_stopwords(texto,stopwords)
    #dicc = contar_palabras(texto)
    #texto = eliminar_stopwords(dicc,stopwords) 
    #imprime_diccionario(dicc)
    texto = contar(archivo, archivo_stopwords)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)  
    parser.add_argument('-m', '--minimo', dest='minimo', default = 3, help="minimo de palabras repetidas", type = int, required=False)
    parser.add_argument('-s', '--stopwords', dest='stopwords', help="nombre de archivo",default = "spanish_stopwords.txt", required=False)
    args = parser.parse_args()
    archivo = args.archivo
    minimo = args.minimo
    stopwords = args.stopwords
    main(archivo, minimo, stopwords)  