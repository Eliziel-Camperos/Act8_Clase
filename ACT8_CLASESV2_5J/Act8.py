print("Clases v2 Eliziel Camperos")

# Zona de clases
class Datos:
    # Constructor
    def __init__(self, est, peso):
        self.est = est
        self.peso = peso

    def mostrar_datos(self):
        print(f"Estatura: {self.est} mts, Peso: {self.peso} Kg")

    def mi_lista(self):
        personajes = ["Eliziel", "Erick", "Yahir"]
        print("Lista de personajes:")
        print(personajes)
        for x in personajes:
            print(x)

    def mi_dic(self):
        cont = {
            "agua": 80,
            "rayos": 75,
            "fuegos": 60
        }
        print("Contenido del diccionario:")
        print(cont)
        for i, y in cont.items(): 
            print(i, y)

    def mostrar_tupla(self):
        tupla = ("Danna", "Lia", "Santy", "Santy B")
        print("Tupla de nombres:")
        print(tupla)
        for z in tupla:
            print(z)

    def mostrar_set(self):
        sset = {"Theo", "Khiara", "Yahir2", "Ivan"}
        print("Conjunto de nombres:")
        print(sset)
        for w in sset:
            print(w)

# Creación de objeto
info = Datos(1.76, 96)

# Utilizando el objeto
info.mostrar_datos()
print("Lista de personajes de Eliziel Camperos Garcia:")
info.mi_lista()
info.mi_dic()
info.mostrar_tupla() 
info.mostrar_set()
