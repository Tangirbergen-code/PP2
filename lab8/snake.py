import pygame
import random


pygame.init()

# Game field dimensions
CELL_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake by Tangirbergen")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

# Font for score display
font = pygame.font.SysFont(None, 35)


def draw_text(text, color, x, y):

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def generate_food(snake_body):

    while True:
        food_x = random.randrange(0, SCREEN_WIDTH, CELL_SIZE)
        food_y = random.randrange(0, SCREEN_HEIGHT, CELL_SIZE)
        
        new_food_pos = [food_x, food_y]
        
        if new_food_pos not in snake_body:
            return new_food_pos


def game_loop():

    game_over = False
    running = True

    snake_speed = 10 
    
    # Initial snake setup
    snake_body = [
        [100, 100],
        [100 - CELL_SIZE, 100],
        [100 - (2 * CELL_SIZE), 100]
    ]
    dx = CELL_SIZE 
    dy = 0
    

    score = 0
    level = 1
    food_eaten_this_level = 0
    

    food_pos = generate_food(snake_body)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
                # Snake controls 
                if event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -CELL_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = CELL_SIZE
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = CELL_SIZE
                    dy = 0

        if not game_over:
            
            old_head = snake_body[0]
            new_head = [old_head[0] + dx, old_head[1] + dy]



            # Check for wall collision
            if (new_head[0] >= SCREEN_WIDTH or new_head[0] < 0 or
                new_head[1] >= SCREEN_HEIGHT or new_head[1] < 0):
                game_over = True
            
            # Check for self-collision
            if new_head in snake_body[1:]:
                game_over = True
            
            snake_body.insert(0, new_head)


            if new_head == food_pos:
                # Snake grows
                score += 1
                food_eaten_this_level += 1
                food_pos = generate_food(snake_body)
                

                # Check for level up
                if food_eaten_this_level == 4:
                    level += 1
                    food_eaten_this_level = 0 
                    
                    snake_speed += 2 
            else:
                # Remove tail if no food was eaten
                snake_body.pop()


        
        screen.fill(BLACK)
        
        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            
        # Draw food
        pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
        
        # Display score and level
        draw_text(f"Score: {score}", WHITE, 10, 10)
        draw_text(f"Level: {level}", WHITE, SCREEN_WIDTH - 150, 10)
        
        if game_over:
            draw_text("GAME OVER", GRAY, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
            draw_text("Press 'Esc' to exit", WHITE, SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2)

        pygame.display.flip()
        
        # Control game speed (FPS)
        clock.tick(snake_speed)

    pygame.quit()

game_loop()