#from math.utils import *
from game.game import *
from game.tictactoe import *
from game.player import *
from game.my_pro_game import *

def main():
    """
    main() -> None
    """
    
    myPlayer1 = Player("Ale", 1)
    myPlayer2 = Player("Lolo", 2)

    print(f"Player1: {myPlayer1} and Player2: {myPlayer2}")

    myGame = MyProGame()

    myGame.player1 = myPlayer1
    myGame.player2 = myPlayer2

    myPlayer1.id = 158

    myGame.start()

    print(Player.score)

    while(myGame.update()):
        print(myGame)

    print(myPlayer1.getNombre())

    print(Player.score)

    myGame.end()

    return None




if __name__ == "__main__":
    main()
    
 
    