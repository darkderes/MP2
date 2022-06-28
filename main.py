import parametros as p
import random

###### INICIO PUNTO 1 ######
### Rellenar Clase Automóvil ###
class Automovil:
    def __init__(self, kilometraje, ano):
        self.__kilometraje = kilometraje
        self.ano = ano 
        self.ruedas = []
        self.aceleracion = 0
        self.velocidad = 0
    def avanzar(self,tiempo:int):
        self.__kilometraje += self.velocidad * tiempo

    def acelerar(self,tiempo:int):
        self.aceleracion = tiempo * 0.5
        self.velocidad += self.aceleracion * tiempo * 3.6
        self.avanzar(tiempo)
        self.aceleracion = 0

    def frenar(self,tiempo:int):
        self.aceleracion = -tiempo * 0.5
        self.velocidad += self.aceleracion * tiempo * 3.6 if self.velocidad > 0 else 0
        self.avanzar(tiempo)
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return self.__kilometraje
    # funcion realizada en clases 
    def reemplazar_ruedas(self):
        if len(self.ruedas) == 0:
            return 
        menor_resistencia = self.ruedas[0].resistencia_actual
        rueda_menor_resistencia = self.ruedas[0]

        for rueda in self.ruedas:
            if rueda.resistencia_actual < menor_resistencia:
                menor_resistencia = rueda.resistencia_actual
                rueda_menor_resistencia = rueda
        self.ruedas.remove(rueda_menor_resistencia)
        r = Rueda()
        self.ruedas.append(r)
###### FIN PUNTO 1 ######


###### INICIO PUNTO 2 ######
### Rellenar Clase Moto ###
class Moto(Automovil): 
    def __init__(self, kilometraje, ano,cilindrada):
        super().__init__(kilometraje, ano)
        self.cilindrada = cilindrada
        self.ruedas.append(Rueda())
        self.ruedas.append(Rueda())
    
    def acelerar(self, tiempo: int):
          super().acelerar(tiempo)
    # ejecutar el metodo gastar de la clase Rueda a cada una de las ruedas
          for rueda in self.ruedas:
            rueda.gastar("acelerar")
    def frenar(self, tiempo: int):
        super().frenar(tiempo)
    # ejecutar el metodo gastar de la clase Rueda a cada una de las ruedas
        for rueda in self.ruedas:
            rueda.gastar("frenar")

    def __str__(self):
        return f"Moto del año {self.ano}."
        
###### FIN PUNTO 2 ######


###### INICIO PUNTO 3 ######
### Rellenar Clase Camión ###
class Camion(Automovil):
    def __init__(self, kilometraje, ano, carga):
        super().__init__(kilometraje, ano)
        self.carga = carga
        self.ruedas.append(Rueda())
        self.ruedas.append(Rueda())
        self.ruedas.append(Rueda())
        self.ruedas.append(Rueda())
        self.ruedas.append(Rueda())
        self.ruedas.append(Rueda())
    def acelerar(self, tiempo: int):
        super().acelerar(tiempo)
    # ejecutar el metodo gastar de la clase Rueda a cada una de las ruedas con parametro "acelerar"
        for rueda in self.ruedas:
            rueda.gastar("acelerar")
    def frenar(self, tiempo: int):
        super().frenar(tiempo)
    # ejecutar el metodo gastar de la clase Rueda a cada una de las ruedas con parametro "frenar"
        for rueda in self.ruedas:
            rueda.gastar("frenar")

    def __str__(self):
        return f"Camión del año {self.ano}."
###### FIN PUNTO 3 ######


### Esta clase está completa, NO MODIFICAR ###
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion):
        if accion == "acelerar":
            self.resistencia_actual -= 5
        elif accion == "frenar":
            self.resistencia_actual -= 10
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"

### Esta funcion está completa, NO MODIFICAR ###
def seleccionar(vehiculos):
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())
    
    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo


###### INICIO PUNTO 4.2 ######
### Se debe completar cada opción según lo indicado en el enunciado ###
def accion(vehiculo, opcion):
    if opcion == 2: #Acelerar
        # solicitar tiempo
        tiempo = int(input("Ingrese Tiempo(seg) acelerar: "))
        # ejecutar el metodo acelerar de la clase vehiculo
        vehiculo.acelerar(tiempo)
        print("")
        print(f"Se ha acelerado por {tiempo} segundos llegando a una velocidad de {vehiculo.velocidad} km/h")
        print("")
    elif opcion == 3: #Frenar
        # solicitar tiempo
        tiempo = int(input("Ingrese Tiempo(seg) frenar: "))
        # ejecutar el metodo frenar de la clase vehiculo
        vehiculo.frenar(tiempo)
        print("")
        print(f"Se ha frenado por {tiempo} segundos llegando a una velocidad de {vehiculo.velocidad} km/h")
        print("")
    elif opcion == 4: #Avanzar
        # solicitar tiempo
        tiempo = int(input("Ingrese Tiempo(seg) avanzar: "))
        # ejecutar el metodo avanzar de la clase vehiculo
        vehiculo.avanzar(tiempo)
        print("")
        print(f"Se ha avanzado {tiempo} segundos a una velocidad de {vehiculo.velocidad} km/h")
        print("")
    elif opcion == 5: #Cambiar Rueda
        vehiculo.reemplazar_ruedas()
        print("")
        print(f"Se ha reemplazado una rueda con éxito.")
        print("")
    elif opcion == 6: #Mostrar Estado
        print("")
        print("Estado del vehículo:")
        print(f"Año: {vehiculo.ano}")
        print(f"Velocidad: {vehiculo.velocidad}")
        print(f"Kilometraje: {vehiculo.obtener_kilometraje()}")
        #imprimir el estado de cada rueda
        print("*****Estado Ruedas*****")
        i = 0 
        for rueda in vehiculo.ruedas:
            i += 1
            print(f"Ruedad {i}:{rueda.estado}")
        print("************************")
        print("")
###### FIN PUNTO 4.2 ######


if __name__ == "__main__":

    ###### INICIO PUNTO 4.1 ######
    ### Aca deben instanciar los vehiculos indicados
    ### en el enunciado y agregarlos a la lista vehiculos
    vehiculos = []

    moto = Moto(random.randint(*p.KILOMETRAJE), random.randint(*p.ANO), random.randint(*p.CILINDRADA))

    # crea objeto camion con parametros: kilometraje, ano, carga
    camion = Camion(random.randint(*p.KILOMETRAJE), random.randint(*p.ANO), random.randint(*p.CARGA))

    ### en el enunciado y agregarlos a la lista vehiculos
    vehiculos = [moto, camion]


    ###### FIN PUNTO 4.1 ######

    ### El codigo de abajo NO SE MODIFICA ###
    vehiculo = vehiculos[0] # Por default comienza seleccionado el primer vehículo  

    dict_opciones = {1: ("Seleccionar Vehiculo", seleccionar),
                     2: ("Acelerar", accion),
                     3: ("Frenar", accion),
                     4: ("Avanzar", accion),
                     5: ("Reemplazar Rueda", accion),
                     6: ("Mostrar Estado", accion),
                     0: ("Salir", None)
                    }

    op = -1
    while op != 0:
        
        for k, v in dict_opciones.items():
            print(f"{k}: {v[0]}")
        
        try:
            op = int(input("Opción: "))
        
        except ValueError:
            print(f"Ingrese opción válida.")
            op = -1
        
        if op != 0 and op in dict_opciones.keys():
            if op == 1:
                vehiculo = dict_opciones[op][1](vehiculos)
            else:
                dict_opciones[op][1](vehiculo, op)
        elif op == 0:
            pass
        else:
            print(f"Ingrese opción válida.")
            op = -1
