import pygame

pygame.init()

class GameVariables:
    Title = "FlappyPy"
    Screen_width = 300
    Screen_height = 600
    Screen = pygame.display.set_mode((Screen_width, Screen_height))
    GameTitle = pygame.display.set_caption(Title)
    clock = pygame.time.Clock()
    GameOver = False

    player_width = 40
    player_Height = 30

    BackGround_width = 300
    BackGround_Height = 600

    Pipe_width = 50
    Pipe_Height = 300

    Ground_width = 300
    Ground_Height = 100

    Pipe_x = 150
    Pipe_y = 350

    pipeVeloX = 10
    pipeVeloY = 10

    initVelo = 2

    