import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

equipo1 = Equipo("Equipo 1")
equipo2 = Equipo("Equipo 2")

def RegistraSet(equipo_ganador):
    
    if equipo_ganador == 1:
        equipo1.setGanados += 1
        if equipo1.setGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0
            
    elif equipo_ganador == 2:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    partidos_iniciales = equipo1.partidosGanados + equipo2.partidosGanados
    
    while (equipo1.partidosGanados + equipo2.partidosGanados) == partidos_iniciales:
        p_e1 = Puntos()
        p_e2 = Puntos()
        
        while True:
            if p_e1 >= 25 or p_e2 >= 25:
                if p_e1 > p_e2:
                    RegistraSet(1)
                    break
                elif p_e2 > p_e1:
                    RegistraSet(2)
                    break
            
            p_e1 += PuntosExtras()
            p_e2 += PuntosExtras()

def ResultadoTorneo():
    print(f"\nEquipo: {equipo1.nombre}")
    print(f"                            ")
    print(f"Ganados: {equipo1.partidosGanados}, Perdidos: {equipo1.partidosPerdidos}")
    print ("=="*20)
    print(f"Equipo: {equipo2.nombre}")
    print(f"                            ")
    print(f"Ganados: {equipo2.partidosGanados}, Perdidos: {equipo2.partidosPerdidos}")

def main():
    while True:
        try:
            n = int(input("¿Cuántos partidos deben jugar?:  "))
            if n > 0: break
        except ValueError:
            pass
            
    for _ in range(n):
        JugarPartido()
        
    ResultadoTorneo()

main()

