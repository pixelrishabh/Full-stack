import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
BIRD_COLOR = (255, 255, 0)
PIPE_COLOR = (0, 255, 0)
GRAVITY = 0.25
FLAP_HEIGHT = 5
PIPE_WIDTH = 70
GAP_SIZE = 150

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Game variables
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_dy = 0
pipes = []

# Functions
def draw_bird(x, y):
    pygame.draw.circle(screen, BIRD_COLOR, (x, y), 20)

def generate_pipe():
    random_height = random.randint(100, SCREEN_HEIGHT - GAP_SIZE - 100)
    top_pipe = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, random_height)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, random_height + GAP_SIZE, PIPE_WIDTH, SCREEN_HEIGHT - random_height - GAP_SIZE)
    return top_pipe, bottom_pipe

def move_pipes():
    for pipe_pair in pipes:
        for pipe in pipe_pair:
            pipe.x -= 1
        if pipe_pair[0].x + PIPE_WIDTH < 0:
            pipes.remove(pipe_pair)

def draw_pipes():
    for pipe_pair in pipes:
        for pipe in pipe_pair:
            pygame.draw.rect(screen, PIPE_COLOR, pipe)

def check_collision():
    bird_rect = pygame.Rect(bird_x - 20, bird_y - 20, 40, 40)
    for pipe_pair in pipes:
        for pipe in pipe_pair:
            if bird_rect.colliderect(pipe):
                return True
    if bird_y - 20 <= 0 or bird_y + 20 >= SCREEN_HEIGHT:
        return True
    return False

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_dy = -FLAP_HEIGHT

    # Bird physics
    bird_dy += GRAVITY
    bird_y += bird_dy

    # Generate pipes
    if len(pipes) == 0 or pipes[-1][0].x < SCREEN_WIDTH - 200:
        pipes.append(generate_pipe())

    # Move pipes
    move_pipes()

    # Check for collision
    if check_collision():
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    draw_bird(bird_x, bird_y)
    draw_pipes()

    pygame.display.flip()
    clock.tick(60)

# Quit Pyg
