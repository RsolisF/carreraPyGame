import pygame, sys
import random

class Corredor():
    
    def __init__(self, x=0, y=0, custome='player1'):
        self.custome = pygame.image.load('img/{}.png'.format(custome))
        self.name= custome
        self.position = [x, y]
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        
class Game():
    
    runners = []
    __names=['Rojo', 'Azul', 'Amarillo', 'Verde']
    __posY=[99, 180, 270, 350]
    __customes=['player1','player2', 'player3','player4']
    __startLine = 15
    __finishLine = 1430
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((1500, 480))
        self.__background = pygame.image.load('img/fondoCarrera.png')
        pygame.display.set_caption('F1 Drag-Race')
        
        for i in range (0,4):
            runner = Corredor(self.__startLine, self.__posY[i])
            runner.name = self.__names[i]
            self.runners.append(runner)
            
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver=True
            
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    print('El ganador es el coche {}'.format(runner.name))
                    gameOver=True
                
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome,runner.position)
            
            pygame.display.flip()
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()        
        
        
    
if __name__ == '__main__':
    
    game = Game()
    pygame.font.init()
    game.competir()
    