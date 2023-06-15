import pygame
from GameVariables import *
pygame.init()
class Images:
    Player = pygame.image.load('Sprits\Bird.png')
    BackGround = pygame.image.load('Sprits\BackGround.png')
    Pipe = pygame.image.load('Sprits\pipe.png')
    Ground = pygame.image.load('Sprits\Ground.png')

    Player_scale = pygame.transform.scale(Player, (GameVariables.player_width, GameVariables.player_Height))
    BackGround_scale = pygame.transform.scale(BackGround, (GameVariables.BackGround_width, GameVariables.BackGround_Height))
    Pipe_scale = pygame.transform.scale(Pipe, (GameVariables.Pipe_width, GameVariables.Pipe_Height))
    Ground_scale = pygame.transform.scale(Ground, (GameVariables.Ground_width, GameVariables.Ground_Height))

    