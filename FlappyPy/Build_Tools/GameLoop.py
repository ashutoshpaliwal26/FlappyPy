from GameVariables import *
from SomeFunc import *
from images import *
import pygame


pygame.init()

class MainGame:
    def gameLoop():
        GameVariables.Screen
        while not GameVariables.GameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameVariables.GameOver = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        GameVariables.pipeVeloX = GameVariables.pipeVeloX + GameVariables.initVelo
                    
                    

            GameVariables.Pipe_x =GameVariables.Pipe_x + GameVariables.pipeVeloX
            GameVariables.Pipe_y = GameVariables.Pipe_y + GameVariables.pipeVeloY
            

            
            GameVariables.Screen.blit(Images.BackGround_scale,(0,0))
            GameVariables.Screen.blit(Images.Player_scale, (100,250))
            GameVariables.Screen.blit(Images.Pipe_scale, (GameVariables.Pipe_x, GameVariables.Pipe_y))
            GameVariables.Screen.blit(Images.Ground_scale, (0, 500))
            pygame.display.update()
        pygame.quit()
        quit()

MainGame.gameLoop()

