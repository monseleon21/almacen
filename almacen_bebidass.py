class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

class AlmacenBebidas:
    def __init__(self):
        self.bebidas = []

    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)

    def eliminar_bebida(self, id):
        for bebida in self.bebidas:
            if bebida.id == id:
                self.bebidas.remove(bebida)
                break

    def actualizar_bebida(self, id, nombre, clasificacion, marca, precio):
        for bebida in self.bebidas:
            if bebida.id == id:
                bebida.nombre = nombre
                bebida.clasificacion = clasificacion
                bebida.marca = marca
                bebida.precio = precio
                break

    def mostrar_todas_bebidas(self):
        for bebida in self.bebidas:
            print("ID:", bebida.id)
            print("Nombre:", bebida.nombre)
            print("Clasificación:", bebida.clasificacion)
            print("Marca:", bebida.marca)
            print("Precio:", bebida.precio)
            print("-----------------------")

    def calcular_precio_promedio(self):
        total_precio = sum(bebida.precio for bebida in self.bebidas)
        promedio = total_precio / len(self.bebidas)
        return promedio

    def contar_bebidas_por_marca(self, marca):
        cantidad = sum(1 for bebida in self.bebidas if bebida.marca == marca)
        return cantidad

    def contar_bebidas_por_clasificacion(self, clasificacion):
        cantidad = sum(1 for bebida in self.bebidas if bebida.clasificacion == clasificacion)
        return cantidad


# Ejemplo de uso
almacen = AlmacenBebidas()

# Agregar bebidas
bebida1 = Bebida(1, "Agua", "Sin azúcar", "Marca A", 1.5)
bebida2 = Bebida(2, "Refresco", "Azucarada", "Marca B", 2.0)
bebida3 = Bebida(3, "Bebida Energética", "Energética", "Marca C", 2.5)

almacen.agregar_bebida(bebida1)
almacen.agregar_bebida(bebida2)
almacen.agregar_bebida(bebida3)

# Mostrar todas las bebidas
almacen.mostrar_todas_bebidas()

# Actualizar una bebida
almacen.actualizar_bebida(2, "Refresco de Cola", "Azucarada", "Marca B", 2.5)

# Mostrar todas las bebidas después de la actualización
almacen.mostrar_todas_bebidas()

# Eliminar una bebida
almacen.eliminar_bebida(1)

# Mostrar todas las bebidas después de la eliminación
almacen.mostrar_todas_bebidas()

# Calcular precio promedio de bebidas
promedio_precio = almacen.calcular_precio_promedio()
print("Precio promedio de bebidas:", promedio_precio)

# Contar bebidas de una marca
cantidad_marca = almacen.contar_bebidas_por_marca("Marca B")
print("Cantidad de bebidas de la marca B:", cantidad_marca)

# Contar bebidas por clasificación
cantidad_clasificacion = almacen.contar_bebidas_por_clasificacion("Azucarada")
print("Cantidad de bebidas azucaradas:", cantidad_clasificacion)
