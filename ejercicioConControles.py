import pygame, sys

class Corredor():
    
    def __init__(self, x=0, y=0, custome='player1'):
        self.custome = pygame.image.load('img/{}.png'.format(custome))
        self.name= 'ROJO'
        self.position = [x, y]
                
        
class Game():
    
    __startLine = 15
    __finishLine = 1430
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((1500, 480))
        self.__background = pygame.image.load('img/fondoCarrera.png')
        pygame.display.set_caption('F1 Drag-Race')
        
        self.runner = Corredor(self.__startLine, 96)
                           
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver=True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.runner.position[1]+=-10
                    elif event.key == pygame.K_DOWN:
                        self.runner.position[1]+=10
                    elif event.key == pygame.K_LEFT:
                        self.runner.position[0]+=-10
                    elif event.key == pygame.K_RIGHT:
                        self.runner.position[0]+=10
                    else:
                        pass
                    
                    
            self.__screen.blit(self.__background, (0,0))
            
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
            
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()        
        
        
    
if __name__ == '__main__':
    
    game = Game()
    pygame.font.init()
    game.competir()
    
