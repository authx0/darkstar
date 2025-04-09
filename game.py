import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DarkStar Fighter")
clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load('fighter_jet.png')
enemy_img = pygame.image.load('missile.png')

# Game variables
score = 0
font = pygame.font.SysFont(None, 36)

class Player:
    def __init__(self):
        self.image = player_img
        # Scale image if needed
        self.width = 60
        self.height = 40
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = 100
        self.y = SCREEN_HEIGHT // 2 - self.height // 2
        self.speed = 7
        self.bullets = []
        self.cooldown = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        # Handle cooldown for shooting
        if self.cooldown > 0:
            self.cooldown -= 1
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed
        if keys[pygame.K_SPACE] and self.cooldown == 0:
            self.shoot()
            self.cooldown = 15  # Cooldown between shots
            
        # Update bullets
        for bullet in self.bullets[:]:
            bullet[0] += 10  # Bullet speed
            if bullet[0] > SCREEN_WIDTH:
                self.bullets.remove(bullet)
        
        # Update rect position for collision detection
        self.rect.x = self.x
        self.rect.y = self.y
    
    def shoot(self):
        self.bullets.append([self.x + self.width, self.y + self.height // 2 - 2])
    
    def draw(self):
        # Draw player jet using the loaded image
        screen.blit(self.image, (self.x, self.y))
        
        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.rect(screen, YELLOW, (bullet[0], bullet[1], 10, 4))

class Enemy:
    def __init__(self):
        self.image = enemy_img
        # Scale image if needed
        self.width = 50
        self.height = 25
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = SCREEN_WIDTH
        self.y = random.randint(0, SCREEN_HEIGHT - self.height)
        self.speed = random.randint(3, 6)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        self.x -= self.speed
        # Update rect position for collision detection
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self):
        # Draw enemy missile using the loaded image
        screen.blit(self.image, (self.x, self.y))

def check_collision(player, enemy):
    return player.rect.colliderect(enemy.rect)

def check_bullet_hit(bullets, enemy):
    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], 10, 4)
        if enemy.rect.colliderect(bullet_rect):
            bullets.remove(bullet)
            return True
    return False

def main():
    global score
    player = Player()
    enemies = []
    enemy_spawn_timer = 0
    running = True
    game_over = False
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset the game
                    player = Player()
                    enemies = []
                    score = 0
                    game_over = False
        
        if not game_over:
            # Update game state
            player.update()
            
            # Spawn enemies
            enemy_spawn_timer += 1
            if enemy_spawn_timer > 60:  # Spawn enemy every 60 frames (about 1 second)
                enemies.append(Enemy())
                enemy_spawn_timer = 0
            
            # Update enemies and check collisions
            for enemy in enemies[:]:
                enemy.update()
                
                # Remove enemies that are off-screen
                if enemy.x + enemy.width < 0:
                    enemies.remove(enemy)
                    continue
                
                # Check if bullet hit enemy
                if check_bullet_hit(player.bullets, enemy):
                    enemies.remove(enemy)
                    score += 10
                
                # Check if player collided with enemy
                if check_collision(player, enemy):
                    game_over = True
        
        # Draw everything
        screen.fill(BLACK)
        
        if not game_over:
            player.draw()
            for enemy in enemies:
                enemy.draw()
                
            # Draw score
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
        else:
            # Game over screen
            game_over_text = font.render("GAME OVER", True, RED)
            score_text = font.render(f"Final Score: {score}", True, WHITE)
            restart_text = font.render("Press 'R' to restart", True, GREEN)
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 
                                         SCREEN_HEIGHT // 2 - 60))
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 
                                    SCREEN_HEIGHT // 2))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 
                                      SCREEN_HEIGHT // 2 + 60))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()