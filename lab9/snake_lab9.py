import pygame
import random
import sys
from pygame.locals import *

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake XD")

# Colours 
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
BLUE  = (0, 0, 255)
GRAY    = (100, 100, 100)

# Font
font = pygame.font.SysFont("Verdana", 20)

# Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
change_to = direction

# Food types
FOOD_TYPES = [
    (RED, 1, 40),      # normal
    (BLUE, 2, 30),     # medium
    (WHITE, 3, 20)     # rare
]

def generate_food(snake, obstacles):
    while True:
        food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
        food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)
        pos = (food_x, food_y)
        if pos not in snake and pos not in obstacles:
            return pos

def new_food(snake, obstacles):
    color, value, life = random.choice(FOOD_TYPES)
    pos = generate_food(snake, obstacles)
    return {"pos": pos, "color": color, "value": value, "life": life}

# Obstacles
def generate_obstacles(count, snake, food):
    obs = []
    while len(obs) < count:
        x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
        y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)
        pos = (x, y)
        if pos not in snake and pos != food["pos"] and pos not in obs:
            obs.append(pos)
    return obs

# Snake creation
food = new_food(snake, [])
obstacles = generate_obstacles(4, snake, food)

score = 0
level = 1
speed = 5
clock = pygame.time.Clock()

last_obstacle_change = 0  

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    direction = change_to

    # Snake's move
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE
    elif direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! Hit wall.")
        pygame.quit()
        sys.exit()
    if new_head in snake[1:]:
        print("Game Over! Hit self.")
        pygame.quit()
        sys.exit()
    if new_head in obstacles:
        print("Game Over! Hit obstacle.")
        pygame.quit()
        sys.exit()

    food["life"] -= 1
    if new_head == food["pos"]:
        score += food["value"]
        if score % 3 == 0:  
            level += 1
            speed += 1
        food = new_food(snake, obstacles)
    else:
        snake.pop()

    if food["life"] <= 0:
        food = new_food(snake, obstacles)

    current_tens = score // 10
    if current_tens > last_obstacle_change and score >= 10:
        obstacles = generate_obstacles(4, snake, food)
        last_obstacle_change = current_tens

    screen.fill(BLACK)

    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, food["color"], (food["pos"][0], food["pos"][1], CELL_SIZE, CELL_SIZE))

    for (ox, oy) in obstacles:
        pygame.draw.rect(screen, GRAY, (ox, oy, CELL_SIZE, CELL_SIZE))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (500, 10))

    pygame.display.flip()
    clock.tick(speed)