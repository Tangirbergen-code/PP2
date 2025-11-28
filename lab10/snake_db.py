import pygame
import random
import sys
import psycopg2
from pygame.locals import *
from config import config

# --- DATABASE FUNCTIONS ---

def get_user_state(username):
    """Check if user exists and return their saved level/score"""
    sql_check = "SELECT user_id FROM users WHERE username = %s"
    sql_get_score = "SELECT level, score FROM user_score WHERE user_id = %s"
    
    conn = None
    user_id = None
    saved_data = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # 1. Check if user exists
        cur.execute(sql_check, (username,))
        result = cur.fetchone()
        
        if result:
            user_id = result[0]
            # 2. Get saved score
            cur.execute(sql_get_score, (user_id,))
            data = cur.fetchone()
            if data:
                saved_data = {'level': data[0], 'score': data[1]}
                print(f"Welcome back, {username}! Loading Level {data[0]}.")
            else:
                print(f"Welcome back, {username}! No saved game found. Starting fresh.")
        else:
            # Create new user
            print(f"User {username} not found. Creating new user...")
            cur.execute("INSERT INTO users(username) VALUES(%s) RETURNING user_id", (username,))
            user_id = cur.fetchone()[0]
            # Create empty score entry
            cur.execute("INSERT INTO user_score(user_id, level, score) VALUES(%s, 1, 0)", (user_id,))
            conn.commit()
            
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"DB Error: {error}")
    finally:
        if conn is not None:
            conn.close()
            
    return user_id, saved_data

def save_game_state(user_id, level, score):
    """Update the user's level and score in DB"""
    sql = """
    INSERT INTO user_score (user_id, level, score)
    VALUES (%s, %s, %s)
    ON CONFLICT (user_id) 
    DO UPDATE SET level = EXCLUDED.level, score = EXCLUDED.score;
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_id, level, score))
        conn.commit()
        cur.close()
        print(f"Game Saved! Level: {level}, Score: {score}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Save Error: {error}")
    finally:
        if conn is not None:
            conn.close()

# --- GAME LOGIC ---

# 1. Console Input (Before Pygame starts)
current_username = input("Enter your username: ")
current_user_id, saved_state = get_user_state(current_username)

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Snake XD - Player: {current_username}")

# Colours 
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
BLUE    = (0, 0, 255)
GRAY    = (100, 100, 100)
YELLOW  = (255, 255, 0) # For Pause text

# Font
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 50)

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

# Function to generate food
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
        food_pos = food["pos"] if food else (-1,-1)
        if pos not in snake and pos != food_pos and pos not in obs:
            obs.append(pos)
    return obs

# --- INITIALIZE GAME STATE ---
score = 0
level = 1
speed = 5

# If user had saved data, load it
if saved_state:
    score = saved_state['score']
    level = saved_state['level']
    # Increase speed based on level (Simple formula)
    speed = 5 + (level - 1) 

food = new_food(snake, [])
# Obstacles increase with level
obstacles = generate_obstacles(3 + level, snake, food)

clock = pygame.time.Clock()
last_obstacle_change = score // 10  

paused = False # State for pause

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # --- PAUSE AND SAVE CONTROLS ---
            if event.key == pygame.K_p:
                paused = not paused # Toggle pause
            
            if paused and event.key == pygame.K_s:
                save_game_state(current_user_id, level, score)
                # Visual feedback could be added here
            
            # --- MOVEMENT CONTROLS (Only if not paused) ---
            if not paused:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

    # If paused, draw pause screen and skip logic
    if paused:
        screen.fill(BLACK)
        pause_text = big_font.render("PAUSED", True, YELLOW)
        info_text = font.render("Press 'P' to Resume, 'S' to Save", True, WHITE)
        screen.blit(pause_text, (WIDTH//2 - 100, HEIGHT//2 - 50))
        screen.blit(info_text, (WIDTH//2 - 140, HEIGHT//2 + 10))
        pygame.display.flip()
        clock.tick(5) # Low framerate for pause menu
        continue

    # --- GAME LOGIC ---
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

    # Collisions
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

    # Food logic
    food["life"] -= 1
    if new_head == food["pos"]:
        score += food["value"]
        
        # Level Up Logic (Every 3 points)
        if score % 3 == 0:  
            level += 1
            speed += 1
            # Regenerate obstacles on level up with more walls
            obstacles = generate_obstacles(3 + level, snake, food) 
            
        food = new_food(snake, obstacles)
    else:
        snake.pop()

    if food["life"] <= 0:
        food = new_food(snake, obstacles)

    # Dynamic obstacle change based on score (legacy logic from your code)
    current_tens = score // 10
    if current_tens > last_obstacle_change and score >= 10:
        obstacles = generate_obstacles(3 + level, snake, food)
        last_obstacle_change = current_tens

    # --- DRAWING ---
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