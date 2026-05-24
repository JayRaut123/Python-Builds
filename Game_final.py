import pygame
from sys import exit
from random import randint 

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The Zombie Rider!")

clock = pygame.time.Clock()

#functions
def animation():
    global player_surf , player_index


    if player_rect.bottom < 375:
        player_surf = player_jump

    else:
        player_index += 0.1
        if player_index >= len(player_list): player_index = 0
        player_surf = player_list[int(player_index)]

def player_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score={current_time}',None, (64,64,64))
    score_rect = score_surf.get_rect(center = (700,50))
    screen.blit(score_surf,score_rect)

def coins():
    global coin_rect,final_coin
    if player_rect.colliderect(coin_rect):
        final_coin += 1

        coin_rect.left = randint(800,1000)
        coin_score = test_font.render(f'Coins = {final_coin}',None,(64,64,64))
        coin_score_rect = coin_score.get_rect(center =(200,50))
        screen.blit(coin_score,coin_score_rect)
        return coin_rect, final_coin
    
def obstacle_movement (obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=6
            screen.blit(obstacle,obstacle_rect)
        return obstacle_list
    else:
        return []
         
       



#variables and constants
player_gravity=0
game_active = True
start_time =0
final_coin= 0

#Background
background_img_original = pygame.image.load('Graphics/Background.jpg').convert()
background_img = pygame.transform.rotozoom(background_img_original,0,1.4)
background_rect = background_img.get_rect(center = (400,200))

ground_img_original = pygame.image.load('Graphics/Ground.png').convert()
ground_img = pygame.transform.rotozoom(ground_img_original,0,0.3)
ground_rect = ground_img.get_rect(center = (650,80))
 

#player
player_run_slow_original = pygame.image.load('Graphics/new.png').convert_alpha()
player_run_slow = pygame.transform.rotozoom(player_run_slow_original,-8,0.5)
player_run_slow_rect = player_run_slow.get_rect(midbottom = (100,375))
player_run_fast_original = pygame.image.load('Graphics/run_fast.png').convert_alpha()
player_run_fast = pygame.transform.rotozoom(player_run_fast_original, 0 ,0.5)
player_run_fast_rect = player_run_fast.get_rect(midbottom = (100,375))

#player jump
player_jump_original = pygame.image.load('Graphics/jump.png').convert_alpha()
player_jump= pygame.transform.rotozoom(player_jump_original, 0 ,0.5)
player_jump_rect = player_jump.get_rect(midbottom = (400,200))

#player stand
player_stand_original = pygame.image.load('Graphics/standing.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand_original, 0 ,0.3)
player_stand_rect = player_stand.get_rect(center = (400,190))

player_list = [player_run_slow,player_run_fast]
player_index = 0
player_surf = player_list[player_index]
player_rect = player_surf.get_rect(midbottom =(100,375))

player_rect.inflate_ip(-20, -10) 


#obstacle
obstacle_original = pygame.image.load('Graphics/zombie.png').convert_alpha()
obstacle = pygame.transform.rotozoom(obstacle_original,0,0.2)
obstacle_rect = obstacle.get_rect(midbottom = (750,330))

obstacle_list = []

obstacle_timer =pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 900)

#coin
coin_surf_original = pygame.image.load('Graphics/coin.png').convert_alpha()
coin_surf = pygame.transform.rotozoom(coin_surf_original,0,0.3)

coin_rect = coin_surf.get_rect(midbottom = (600,360))
coin_rect.inflate_ip(-20, -10)


#Title and Texts
test_font = pygame.font.Font(None, 50)
game_title = test_font.render('Pixel Go', False , 'Blue')
game_title_rect = game_title.get_rect(center = (400,50))

game_message = test_font.render("Press space to Restart", False , 'Green')
game_message_rect = game_message.get_rect(center = (400,350))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 375:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int (pygame.time.get_ticks()/1000)
                    obstacle_list.clear()
    


    if game_active:
        if event.type == obstacle_timer:
            if randint(0,2):
                obstacle_list.append(obstacle_rect)
            else:
                obstacle_list.append(obstacle_rect)

            
    
    
    if game_active:
            
        screen.blit(background_img,background_rect)
        screen.blit(ground_img,ground_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >=375 : 
            player_rect.bottom= 375

        animation()
        screen.blit(player_surf, player_rect)
        screen.blit(obstacle,obstacle_rect)
        screen.blit(coin_surf,coin_rect)

       # obstacle_rect.left -= 6
        coin_rect.left -= 4

        if obstacle_rect.right <-100: obstacle_rect.left =800
        player_score()
        coins()
        coin_score = test_font.render(f'Coins = {final_coin}',None,(64,64,64))
        coin_score_rect = coin_score.get_rect(center =(200,50))
        screen.blit(coin_score,coin_score_rect)

        if player_rect.colliderect(obstacle_rect):
            game_active= False

       
    else:
        screen.fill((94,129,162))
        #screen.blit(game_title,game_title_rect) 
        #screen.blit(stand_image,stand_image_rect)
        #screen.blit(game_message,game_message_rect)
        screen.blit(player_stand,player_stand_rect)
        screen.blit(game_title,game_title_rect)
        screen.blit(game_message,game_message_rect)
    
    pygame.display.update()
    clock.tick(60)

#if event.type == pygame.K_SPACE:
