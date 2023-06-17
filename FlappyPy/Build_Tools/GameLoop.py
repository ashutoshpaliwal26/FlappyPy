import pygame


pygame.init()


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
pipeVeloX = 3
pipeVeloY = 10
initVelo = 4
Player = pygame.image.load('Sprits\Bird.png')
BackGround = pygame.image.load('Sprits\BackGround.png')
Pipe = pygame.image.load('Sprits\pipe.png')
Ground = pygame.image.load('Sprits\Ground.png')
Player_scale = pygame.transform.scale(Player, (player_width, player_Height))
BackGround_scale = pygame.transform.scale(BackGround, (BackGround_width, BackGround_Height))
Pipe_scale = pygame.transform.scale(Pipe, (Pipe_width, Pipe_Height))
Ground_scale = pygame.transform.scale(Ground, (Ground_width, Ground_Height))
Ground_x = 0
Ground_x2 = -300
Ground_y = 500
PlayerY = 250
runGround_x = []

        


while not GameOver:
    if PlayerY >= 499:
        print("Game Over.......")
        GameOver = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pipeVeloX = pipeVeloX + initVelo


    
    PlayerY = PlayerY + pipeVeloX
    Ground_x = Ground_x + pipeVeloX
    Ground_x2 = Ground_x2 +pipeVeloX


    if Ground_x == 300 :
        Ground_x = 0
    if Ground_x2 == 0:
        Ground_x2 = -300
    
    Screen.blit(BackGround_scale,(Ground_x,0))
    Screen.blit(BackGround_scale,(Ground_x2,0))
    Screen.blit(Player_scale, (100,PlayerY))
    # Screen.blit(Pipe_scale, (Pipe_x, Pipe_y))
    Screen.blit(Ground,(Ground_x, Ground_y))
    Screen.blit(Ground,(Ground_x2, Ground_y))

    runGround = []
    runGround.append(Ground_x)
    runGround.append(Ground_y)
    runGround_x.append(runGround)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()


