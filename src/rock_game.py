import random
import os
import time 

class RockPaperScissors:
    """
    Rock Paper Scissors Game:
    r VS p => p
    r VS s => s 
    r VS r => r 
    """

    def __init__(self):

        self.options = ['r','p','s']
        self.user_score = 0
        self.computer_score = 0

    def start_game(self):
        """
        Se inicializa el juego con un score = 0 para cada jugador cuando uno de los dos sea igual a 10 ({a,b} >= 10) se ganara la partida.
        Permitiendote hacer dos cosas: 
            -- Salir del Juego
                * end game
            -- Reiniciar Juego
                * eset Scores
        """
        end_game = False
        
        while end_game != True:

            user = str(input('Choose an option\nRock => r\nPaper => p\nScissors => s\n: '))
            user = user.lower()
            if (user == 'r') or (user == 'p') or (user == 's'):
                computer = random.choice(self.options)
            else:
                print('Enter correct values ( r, s, p)')
                user = ''
                computer = ''
                
            self.clear_window(1)

            #! TODO: Create a function that handles the encounters
            if (user == computer):
                print('This is a tie')

            elif(self.player_wins(user,computer)):
                print('You Win !!!! :) ')
                self.user_score += 1
            else:
                print(' You lost !!! :(')
                self.computer_score += 1

            print(f'Computer {self.computer_score} => {computer}  VS {user} <= {self.user_score} User')
            
            #! TODO: Create a function that handles scores
            #! TODO: Create a function that handles the victory of the game 
            if(self.computer_score >= 3) or (self.user_score >= 3):
                choce_option = str(input('Deseas salir del Juego ?? Yes(y) / No(n) '))
                if choce_option == 'y':
                    end_game = True
                else:
                    self.computer_score = 0
                    self.user_score = 0 

            self.clear_window(2.5)
            

    def player_wins(self,user,computer):
        if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
            return True
        return False
        
    def clear_window(self,time_sleep):
        time.sleep(time_sleep)
        os.system('cls')
        

#TODO : Ingresar funciones de entrada de teclado para realizar mas operaciones
#TODO : Ingresar una interfaz de usuario mas agradable.
#TODO : Funcion que nos informe cuantas partidas sean disputado en total y cuantas a ganado cada jugador