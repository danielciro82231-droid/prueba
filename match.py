cola =  []

def agregar_jugador(id_jugador, nivel):
   
    for jugador in cola:
       
        diferencia = abs(jugador ["nivel"] - nivel)
       
        if diferencia <= 150:
           
            print(f"match encontrado: {jugador['id']} vs {id_jugador}")
           
            cola.remove(jugador)
           
            return
       
    cola.append({"id": id_jugador, "nivel": nivel})

    print(f"jugador{id_jugador} agregado a la cola")
   
   
agregar_jugador(1, 1200)
agregar_jugador(2, 1400)
agregar_jugador(3, 1500)
agregar_jugador(4, 2000)
agregar_jugador(5, 1300)


print("\njugadores en cola:")
for jugador in cola:
    print(jugador)    
