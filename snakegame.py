import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("King Cobra Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

massage_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill (black)
            game_over_massage = massage_font.render("Game_Over!", True, red )
            game_display.blit(game_over_massage ,[width / 3, height /3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event .key == pygame.K_1:
                        game_over = True 
                        game = close = False 
                        if event.key == pygame.K_2:
                            run_game ()
                            if event.type == pygame.QUIT:
                                 game_over = True 
                        game = close = False 
                        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    y_speed = -snake_size
                    x_speed = 0
                elif event.key == pygame.K_DOWN:
                    y_speed = snake_size
                    x_speed = 0

        # Update the snake's position
        x += x_speed
        y += y_speed

        # Draw the background and the snake
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [target_x, target_y, snake_size, snake_size])
        
        snake_head = [x, y]
        snake_pixels.append(snake_head)

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        # Check if snake hits the boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        # Check if the snake eats the target
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()






    
 


