import pygame
import sys

pygame.init()

# -------------------------------------------------------
# CONFIGURAÇÕES DA JANELA
# -------------------------------------------------------
WIDTH, HEIGHT = 960, 540
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fase 1 - Jardim das Perobeiras")
clock = pygame.time.Clock()

# -------------------------------------------------------
# CORES
# -------------------------------------------------------
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
GREEN = (60, 200, 80)
SKY = (130, 200, 255)
YELLOW = (255, 230, 50)
RED = (255, 100, 100)

# -------------------------------------------------------
# CLASSE DO JOGADOR (FERNANDINHO)
# -------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 48))
        self.image.fill((0, 0, 255))  # azul = Fernandinho
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.speed = 5
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        # Movimento horizontal
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Pulo
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -13
            self.on_ground = False

        # Gravidade
        self.vel_y += 0.6
        self.rect.y += self.vel_y

        # Colisão com plataformas e chão
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

# -------------------------------------------------------
# PLATAFORMAS
# -------------------------------------------------------
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

# -------------------------------------------------------
# PÃES COLETÁVEIS
# -------------------------------------------------------
class Bread(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(topleft=(x, y))

# -------------------------------------------------------
# INIMIGOS SIMPLES
# -------------------------------------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, move_range):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)  # vermelho = inimigo
        self.rect = self.image.get_rect(topleft=(x, y))
        self.start_x = x
        self.move_range = move_range
        self.speed = 2

    def update(self):
        self.rect.x += self.speed

        # movimento vai e volta
        if self.rect.x > self.start_x + self.move_range or self.rect.x < self.start_x:
            self.speed *= -1

# -------------------------------------------------------
# CRIAÇÃO DOS OBJETOS DO MAPA
# -------------------------------------------------------
player = Player(100, 300)

platforms = pygame.sprite.Group()
breads = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# chão
ground = Platform(0, 480, WIDTH, 60)
platforms.add(ground)

# plataformas do Jardim das Perobeiras
platforms.add(Platform(200, 420, 150, 30))
platforms.add(Platform(440, 350, 140, 30))
platforms.add(Platform(700, 400, 160, 30))
platforms.add(Platform(850, 300, 100, 30))

# pães da fase
breads.add(Bread(220, 390))
breads.add(Bread(470, 320))
breads.add(Bread(730, 370))
breads.add(Bread(880, 270))
breads.add(Bread(320, 450))
breads.add(Bread(50, 450))

# inimigos:
#  galinha
enemies.add(Enemy(350, 448, 120))

#  pombo (no alto)
enemies.add(Enemy(450, 320, 80))

#  cachorro (velocidade maior)
dog = Enemy(650, 448, 150)
dog.speed = 3
enemies.add(dog)

# porta de saída da fase
exit_rect = pygame.Rect(900, 250, 40, 80)

# HUD
bread_count = 0
font = pygame.font.SysFont("arial", 24)

# -------------------------------------------------------
# LOOP PRINCIPAL DO JOGO
# -------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar objetos
    player.update(platforms)
    enemies.update()

    # Coleta de pão
    for bread in breads.copy():
        if player.rect.colliderect(bread.rect):
            bread.kill()
            bread_count += 1

    # Colisão com inimigos
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            print("Fernandinho foi derrotado! Reiniciando fase...")
            pygame.time.delay(800)
            player.rect.topleft = (100, 300)
            bread_count = 0

    # Chegou na saída
    if player.rect.colliderect(exit_rect):
        print("Fase 1 concluída! Indo para o Jardim das Perobeiras!")
        pygame.time.delay(600)
        pygame.quit()
        sys.exit()

    # -------------------------------------------------------
    # DESENHO NA TELA
    # -------------------------------------------------------
    screen.fill(SKY)

    # plataformas
    for platform in platforms:
        screen.blit(platform.image, platform.rect)

    # pães
    for bread in breads:
        screen.blit(bread.image, bread.rect)

    # inimigos
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)

    # jogador
    screen.blit(player.image, player.rect)

    # saída
    pygame.draw.rect(screen, (0, 0, 0), exit_rect)

    # HUD
    hud = font.render(f"Pães coletados: {bread_count}", True, (0, 0, 0))
    screen.blit(hud, (10, 10))

    pygame.display.flip()
    clock.tick(60)