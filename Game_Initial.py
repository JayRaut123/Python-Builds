import pygame
from sys import exit
from random import randint, choice

# Function to display score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def player_animation():
    global player_rect,player_index
    if player_rect.bottom <375:
        player_rect = player_jump

    else:
        player_index += 0.1
        if player_index >= len(player_walk) : player_index = 0

        player_rect = player_walk[int(player_index)]

    


# Function to move and draw obstacles
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            screen.blit(obstacle_surface, obstacle_rect)
        return obstacle_list
    else:
        return []

# Initialize Pygame
pygame.init()
score = 0
start_time = 0
game_active = False

# Set up screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Jay's Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
player_gravity = 0

# Load images
sky_surface = pygame.image.load('Graphics/Sky.png').convert()
ground_surface = pygame.image.load('Graphics/Ground.png').convert()
player_surface = pygame.image.load('Graphics/player3.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(100, 375))
player_jump = pygame.image.load('').convert_alpha()

player_rect.inflate_ip(-20, -10)  # Shrinks the rect for more precise collision

#Animation
player_walk_1 = pygame.image.load('').convert_alpha()
player_walk_2 = pygame.image.load('').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index =0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom= (100,375))


obstacle_animal_1 = pygame.image.load('').convert_aplha()
obstacle_animal_2 = pygame.image.load('').convert_alpha()
obstacle_fly1= pygame.image.load('').convert_alpha()
obstacle_fly2 = pygame.image.load('').convert_alpha()



# Obstacle
obstacle_surface = pygame.image.load('Graphics/obstacle 1.png').convert_alpha()
obstacle_rect_list = []

# Stand image with transform.rotozoom
stand_image_original = pygame.image.load('Graphics/standing_player.png').convert_alpha()
stand_image = pygame.transform.rotozoom(stand_image_original, 0, 0.5)  # Rotate 15 degrees, scale 1.2x
stand_image_rect = stand_image.get_rect(center=(400, 200))

# UI texts
game_title = test_font.render('Pixel Go', False, 'Blue')
game_title_rect = game_title.get_rect(center=(400, 50))

game_message = test_font.render("Press Space to Restart", False, 'Green')
game_message_rect = game_message.get_rect(center=(400, 350))

# Timer event for obstacle spawn
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 360:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                obstacle_rect_list.clear()
    if game_active:
        if event.type == obstacle_timer:
            if randint(0,2):
                obstacle_rect_list.append(obstacle_surface.get_rect(bottomright=(randint(900, 1100), 380)))
            else:
                obstacle_rect_list.append(obstacle_surface.get_rect(bottomright=(randint(900, 1100), 380)))


    if game_active:
        screen.blit(sky_surface, (50, 0))
        screen.blit(ground_surface, (60, 300))

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 360:
            player_rect.bottom = 360

        player_animation()
        screen.blit(player_surface, player_rect)

        # Score
        score = display_score()

        # Obstacles
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        obstacle_rect_list = [obstacle for obstacle in obstacle_rect_list if obstacle.x > -100]

        # Collision check
        for obstacle in obstacle_rect_list:
            if player_rect.colliderect(obstacle):
                game_active = False

    else:
        screen.fill((94, 129, 162))
        screen.blit(game_title, game_title_rect)
        screen.blit(stand_image, stand_image_rect)
        screen.blit(game_message, game_message_rect)

    # Update display
    pygame.display.update()
    clock.tick(60)
