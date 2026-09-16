import pygame
import time
import random

# Initialize pygame
pygame.init()

# Setup display
width, height = 600, 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
white = (255, 255, 255)

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)

def show_score(score):
    value = font_style.render("Score: " + str(score), True, white)
    display.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

    # Initial Snake position
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Place first food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            display.fill(black)
            msg = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
            display.blit(msg, [width / 6, height / 3])
            show_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Boundary checks
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check self-collision
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)
        show_score(Length_of_snake - 1)
        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    gameLoop()