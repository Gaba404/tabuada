import pygame
import random

# Inicializar o pygame
pygame.init()

# Definir as cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Definir o tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Título da janela
pygame.display.set_caption("Pegue a Bolinha!")

# Definir o relógio
clock = pygame.time.Clock()

# Classe do jogador (quadrado)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

# Classe da bolinha
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 30)

# Função principal do jogo
def main():
    # Criar o jogador e a bolinha
    player = Player()
    ball = Ball()

    # Grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(ball)

    # Pontuação
    score = 0
    font = pygame.font.SysFont(None, 36)

    # Loop do jogo
    running = True
    while running:
        screen.fill(WHITE)

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentar o jogador
        keys = pygame.key.get_pressed()
        player.update(keys)

        # Verificar se o jogador pegou a bolinha
        if player.rect.colliderect(ball.rect):
            score += 1
            ball.reset_position()

        # Desenhar tudo
        all_sprites.draw(screen)

        # Mostrar pontuação
        score_text = font.render(f"Pontuação: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Atualizar a tela
        pygame.display.flip()

        # Definir FPS
        clock.tick(60)

    # Finalizar o pygame
    pygame.quit()

# Rodar o jogo
if __name__ == "__main__":
    main()
