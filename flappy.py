import pygame, sys, random
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# Colors & Fonts
WHITE = (255, 255, 255)
font = pygame.font.SysFont(None, 48)
# Bird
bird = pygame.Rect(50, HEIGHT//2, 30, 30)
gravity = 0
bird_movement = 0
# Pipes
pipe_width = 60
pipe_gap = 150
pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)
def create_pipe():
   height = random.randint(100, 400)
   top_pipe = pygame.Rect(WIDTH, height - pipe_gap - HEIGHT, pipe_width, HEIGHT)
   bottom_pipe = pygame.Rect(WIDTH, height, pipe_width, HEIGHT)
   return top_pipe, bottom_pipe
score = 0
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit(); sys.exit()
       if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
           bird_movement = -8
       if event.type == SPAWNPIPE:
           pipes.extend(create_pipe())
   # Bird physics
   bird_movement += gravity
   bird.y += bird_movement
   # Move pipes
   for pipe in pipes:
       pipe.x -= 4
   # Collision detection
   for pipe in pipes:
       if bird.colliderect(pipe):
           pygame.quit(); sys.exit()
   if bird.top <= 0 or bird.bottom >= HEIGHT:
       pygame.quit(); sys.exit()
   # Scoring
   for pipe in pipes[::2]:
       if pipe.centerx == bird.centerx:
           score += 1
   # Drawing
   screen.fill(WHITE)
   pygame.draw.rect(screen, (255, 255, 0), bird)
   for pipe in pipes:
       pygame.draw.rect(screen, (0, 255, 0), pipe)
   score_surface = font.render(str(score), True, (0,0,0))
   screen.blit(score_surface, (WIDTH//2 - score_surface.get_width()//2, 20))
   pygame.display.update()
   clock.tick(60)