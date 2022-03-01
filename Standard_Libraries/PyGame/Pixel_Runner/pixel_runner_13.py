from collections import namedtuple
from random import randint
import sys
import pygame


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = text_font.render(
        f"Score: {current_time//1000}", False, (64, 64, 64)
    )
    score_rect = score_surface.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, width=10)
    screen.blit(score_surface, score_rect)

    return current_time // 1000


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            obstacle.right -= 5
            match obstacle.bottom:
                case 200:
                    screen.blit(fly_surface, obstacle)
                case 300:
                    screen.blit(snail_surface, obstacle)

        return [obstacle for obstacle in obstacle_list if obstacle.right > 0]
    else:
        return []


def collision(player, obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player.colliderect(obstacle):
                return False
    return True


def player_animation(player_idx, player_surf):
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_idx += 0.1
        if player_idx >= len(player_walk):
            player_idx = 0
        player_surf = player_walk[int(player_idx)]

    return (player_idx, player_surf)


Window_Size = namedtuple("Window_Size", ["width", "height"])
RGB_Color = namedtuple("RGB_Color", ["Red", "Green", "Blue"])

pygame.init()
screen = pygame.display.set_mode(Window_Size(800, 400))
pygame.display.set_caption("Runner")

clock = pygame.time.Clock()
start_time = 0
score = 0
game_active = False

sky_surface = pygame.image.load(r"./graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load(r"./graphics/ground.png").convert_alpha()

snail_frame_1 = pygame.image.load(r"./graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load(r"./graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surface = snail_frames[snail_index]


# now we add our fly obstacle
fly_frame_1 = pygame.image.load(r"./graphics/Fly/Fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load(r"./graphics/Fly/Fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surface = fly_frames[fly_index]


player_walk_1 = pygame.image.load(
    r"./graphics/Player/player_walk_1.png"
).convert_alpha()
player_walk_2 = pygame.image.load(
    r"./graphics/Player/player_walk_2.png"
).convert_alpha()

player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load(r"./graphics/Player/jump.png").convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

player_stand = pygame.image.load(r"./graphics/Player/player_stand.png")
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

text_font = pygame.font.Font(r"./font/Pixeltype.ttf", 50)

game_name = text_font.render("Pixel Runner", False, RGB_Color(111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = text_font.render("Press space to play", False, RGB_Color(111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 350))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation, 500)

fly_animation = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation, 200)


obstacle_rect_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -21

            if event.type == obstacle_timer:
                if randint(0, 1):
                    obstacle_rect_list.append(
                        snail_surface.get_rect(midbottom=(randint(900, 1200), 300))
                    )
                else:
                    obstacle_rect_list.append(
                        fly_surface.get_rect(midbottom=(randint(900, 1200), 200))
                    )
            if event.type == snail_animation:
                snail_index = int(not snail_index)
                snail_surface = snail_frames[snail_index]

            if event.type == fly_animation:
                fly_index = int(not snail_index)
                fly_surface = fly_frames[snail_index]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -21
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacle_rect_list.clear()
                player_rect = player_surface.get_rect(midbottom=(80, 300))
                player_gravity = 0
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        score = display_score()

        player_gravity = min(1000, player_gravity + 1)
        player_rect.bottom += player_gravity

        if player_rect.bottom > 300:
            player_rect.bottom = 300

        player_index, player_surface = player_animation(player_index, player_surface)
        screen.blit(player_surface, player_rect)

        game_active = collision(player_rect, obstacle_rect_list)

    else:
        screen.fill(RGB_Color(94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)

        score_message = text_font.render(
            f"Your score: {score}", False, RGB_Color(111, 196, 169)
        )
        score_message_rect = score_message.get_rect(center=(400, 350))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
