

class Player:

    score = 0
    def __init__(self, nombre, id) -> None:
        """
        Contructor.
        IMPORTANT: Todo metodo lleva como primer
        parametro self
        """
        self.__nombre = nombre
        self.id = id
    
    def input(self):
        """
        Es el input del player en mi Juego
        """
        pass
    
    def getNombre(self) -> str:
        return self.__nombre

    def __str__(self) -> str:
        """
        Convierto a String my metodo
        """
        return f"Player name:{self.getNombre()}, id:{self.id}"