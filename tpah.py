from texto import obtener_texto
texto_a_trabajar=obtener_texto()
import string

def limpiador(lista_texto): 
    contador = 0
    for i in lista_texto:
        ##este if esta demas porque ya viene sin los simbolos finales un la funcino del main
        lista_texto[contador] = lista_texto[contador].lower()
        if i[-1:] == "." or i[-1:] == "!" or i[-1:] == "," or i[-1:] == "_":
            lista_texto[contador] = i[:len(i)-1]
        elif i[:1] == "¡" or i[:1] == "_" or i[:1] == "¿":
            lista_texto[contador] = i[1:len(i)]
        contador += 1
    return lista_texto
##########################################################

def borrador(lista):
    posicion = []
    for i in range(len(lista)-1):
        if len(lista[i])< 5:
            posicion.append(i)
    ordenados = sorted(posicion , reverse = True)
    for i in ordenados:
        lista.pop(i)
    print(len(lista))
    return lista
##########################################################

def diccionario_ordenado(frecuencia):
  contadorPalabras={} 
  #Se crea un diccionario vacio 
  for palabra in frecuencia: 
    #Se recorre cada lina en el texto 
    if palabra in contadorPalabras:
      #Se suma 1 cada vez que una palabra se repite, en este caso la palabra seria la key y el numero de repeticiones de esta seria el value.
      contadorPalabras[palabra.lower()]+=1 
      #Usamos el metodo ".lower()" para hacer todas las palabras minusculas, porque si tuvieramos palabras mayusculas contarian como
    else:
      contadorPalabras[palabra.lower()]=1 
      #Si la palabra no esta en el diccionario, la registra y le asigna el valor 1
  return sorted(contadorPalabras.items(),key=lambda x:x[0],reverse=False) 
#usamos el "dict.items()" para obtener los key,value del diccionario y se ordena alfabeticamente con palabra,valor respectivamente
#########################################################

def main():
    ##esta funcion la saque de internet solo sirve con import string saca los simbolos basicos
    texto = obtener_texto().translate(str.maketrans('', '', string.punctuation))
    ##
    lista_texto =  texto.split() 
    lista_texto = limpiador(lista_texto)
    lista_texto = borrador(lista_texto)
    lista_texto = diccionario_ordenado(lista_texto)
    print(lista_texto)
    #diccionario = palabras_enteras(lista)
main()
