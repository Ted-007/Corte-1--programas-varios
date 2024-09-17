class Animal:
    """
    Clase base que representa un animal genérico.

    Atributos:
        nombre (str): El nombre del animal.
        edad (int): La edad del animal en años.
    """

    def __init__(self, nombre, edad):
        """
        Inicializa un objeto de la clase Animal.

        Args:
            nombre (str): El nombre del animal.
            edad (int): La edad del animal.
        """
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        """
        Método para simular el sonido que hace un animal.
        Este método debe ser sobrescrito por las clases derivadas.
        """
        raise NotImplementedError("Este método debe ser sobrescrito por una subclase.")

    def descripcion(self):
        """
        Método que proporciona una descripción del animal.

        Returns:
            str: Una descripción básica del animal.
        """
        return f"{self.nombre} tiene {self.edad} años."


class Perro(Animal):
    """
    Clase derivada que representa a un perro.
    Hereda de la clase Animal.

    Atributos adicionales:
        raza (str): La raza del perro.
    """

    def __init__(self, nombre, edad, raza):
        """
        Inicializa un objeto de la clase Perro.

        Args:
            nombre (str): El nombre del perro.
            edad (int): La edad del perro.
            raza (str): La raza del perro.
        """
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        """
        Sobrescribe el método hacer_sonido para que el perro ladre.

        Returns:
            str: El sonido que hace el perro.
        """
        return "Guau guau"

    def descripcion(self):
        """
        Sobrescribe el método descripción para incluir la raza del perro.

        Returns:
            str: Descripción extendida del perro.
        """
        return f"{self.nombre} es un {self.raza} que tiene {self.edad} años."


class Gato(Animal):
    """
    Clase derivada que representa a un gato.
    Hereda de la clase Animal.
    """

    def __init__(self, nombre, edad, color):
        """
        Inicializa un objeto de la clase Gato.

        Args:
            nombre (str): El nombre del gato.
            edad (int): La edad del gato.
            color (str): El color del gato.
        """
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        """
        Sobrescribe el método hacer_sonido para que el gato maúlle.

        Returns:
            str: El sonido que hace el gato.
        """
        return "Miau miau"

    def descripcion(self):
        """
        Sobrescribe el método descripción para incluir el color del gato.

        Returns:
            str: Descripción extendida del gato.
        """
        return f"{self.nombre} es un gato de color {self.color} y tiene {self.edad} años."


# Ejemplo de uso
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Luna", 3, "blanco")

print(perro.descripcion())  # Salida: Rex es un Labrador que tiene 5 años.
print(perro.hacer_sonido())  # Salida: Guau guau

print(gato.descripcion())  # Salida: Luna es un gato de color blanco y tiene 3 años.
print(gato.hacer_sonido())  # Salida: Miau miau
