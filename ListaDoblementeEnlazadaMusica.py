#Lista doblemente ligadas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self):
        cancion = input("Ingresa una canción: ")
        nuevo = Nodo(cancion)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self):
        cancion = input("Ingresa una canción: ")
        nuevo = Nodo(cancion)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def actual_cancion(self):
        if self.actual:
            return self.actual.cancion



    def eliminar(self):
        respuesta = input("Deseas eliminar al principio de la playlist o al final?")
        if respuesta == "principio":
            if self.esta_vacia():
                return None
        
            if self.cabeza.dato == self.cola.dato:
                self.cabeza = None
                self.cola = None
            else:
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
        elif respuesta == "final":
            if self.esta_vacia():
                return None
            if self.cabeza.dato == self.cola.dato:
                self.cabeza = None
                self.cola = None
            else:
                self.cola = self.cola.anterior
                self.cola.siguiente = None
        else:
            print("Digite una respuesta valida.")
        
        

   
   
    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.cancion

    def anterior_cancion(self):
        if self.actual:
            return self.actual.cancion
        return None
    
    def recorrer_adelante(self):
        if self.esta_vacia():
            print("Lista vacia")
            return
        
        print("Recorriendo inicio --> Fin")
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" --> ")
            actual = actual.siguiente
        print("Fin")

    def recorrer_final(self):
        if self.esta_vacia():
            print("Lista vacia")
            return
        
        print("Recorriendo Fin --> Inicio")
        actual = self.cola
        while actual:
            print(actual.dato, end=" -->  ")
            actual = actual.anterior
        print("Fin")

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        
        return False



    #LEN = LONGITUD DE LA LISTA
    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    #STR = Imprimir lista
    def __str__(self):
        if self.esta_vacia():
            return "Empty Playlist"
        
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "<=>".join(elementos)
        #JOIN = toma todo lo de la lista y va a poner lo de las comillas en espacios.




    def Menu_Opciones(self):
        while True:
            print("---MENU---\n")
            print("1. Add song\n 2. Delete Song\n 3. Next Song\n 4. Previous Song\n 5. Show Historial\n 6. Exit \n")
            opcion = int(input("Elige una opcion: \n"))
            match opcion:
                case 1:
                    if self.esta_vacia():
                        self.insertar_inicio()
                    else:
                        self.insertar_final()
                
                case 2:
                    if self.esta_vacia():
                        print("There aren't songs to delete\n")
                    else:
                        self.eliminar()
                case 3:
                    if self.esta_vacia():
                        print("There aren't more songs in the playlist...\n")
                    else:
                        self.siguiente_cancion()
                case 4:
                    if self.esta_vacia():
                        print("There aren't more songs in the playlist...\n")
                    else:
                        self.anterior_cancion()
                case 5:
                    if self.esta_vacia():
                        print("There aren't more songs in the playlist...\n")
                    else:
                        print("Showing historial...")
                        self.recorrer_adelante()
                
                case 6:
                    if self.esta_vacia():
                        print("There aren't more songs in the playlist...\n")
                    else:
                        self.actual_cancion

                case 7:
                    break




lista = ListaDoble()
lista.Menu_Opciones()

