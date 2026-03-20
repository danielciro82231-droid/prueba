







# tengo un usuario y tengo mis gegeros favoritos_: accion, crimen, aventura
# que peliculas me recomiendan y con que porcentaje
# 1 que tiene los 3: 100%, si tiene 2: 66.6% y si solo tiene 1: 33.3%
# oprdenados de menor a mayor

favoritos = {"accion", "crimen", "aventura"}
recomendaciones = []

for pelicula, generos in catalogo.items():
    generos_comunes = favoritos.interserccion(generos)
    if generos_comunes:
        porcentaje_similitud = (len(generos_comunes)/len(favoritos))*100
        recomendaciones.append(pelicula, porcentaje_similitud)



def obtener_porcentaje(elemento):
    return elemento[1]


recomendaciones.sort(kjey=obtener_porcentaje, reverse = true)
print(recomendaciones)    




#como mostrar todos los generos que hay en el catalogo
generos unicods = set()

for generos in catalogo.values():
    generos_unicos = generos_unicos.union(generos)


generos_ordenados = sorted(generos_unicos)
print(generos_ordenados)


# mostrar peliculas por genero

peliculas_por_genero = {}

for pelicula, genero in catalogo.item():
    for genero in genero:
            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = set()


            peliculas_por_genero[genero].add(pelicula)
print(peliculas_por_genero)                
        

# metodo que reciba dos peliculas 
# devuelva el indice de similitud jaccard

def calcular_indice(p1, p2):

    g1 = catalogo[p1]
    g2 = catalogo[p2]

    interserccion = len(g1 & g2)
    union = len (g1 | g2)

    return interserccion / union




# leer dos textos
# calcular su indice de similitud, ignorando los STOPWORDS
# si el indice es mayor a 0.6, se copiaron


STOPWORDS = {"el", "la", "los", "las", "un", "una", "unos", "unas",
            "de", "del", "al", "a", "en", "con", "por", "para", 
            "y", "o", "que", "es", "son", "se", "su", "sus", 
            "como", "perro", "mas", "este", "esta", "estos", "estas", }

def limpiar_texto(texto):
    return set(texto.lower().split())- STOPWORDS
                



        
