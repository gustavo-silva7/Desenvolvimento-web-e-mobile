import pygame
import random

pygame.init()

# Configurações da janela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletar Moedas")

# Jogador
jogador = pygame.Rect(400, 300, 32, 32)
velocidade = 5

# Moeda
moeda = pygame.Rect(
    random.randint(0, 768),
    random.randint(0, 568),
    32,
    32
)

# Pontuação
pontos = 0
fonte = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()
rodando = True

# =================== LOOP PRINCIPAL DO JOGO ===================== #
while rodando:
    clock.tick(60)  # 60 FPS

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador.x += velocidade
    if teclas[pygame.K_UP]:
        jogador.y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    # Limites da tela
    jogador.x = max(0, min(jogador.x, LARGURA - jogador.width))
    jogador.y = max(0, min(jogador.y, ALTURA - jogador.height))

    # Colisão com a moeda
    if jogador.colliderect(moeda):
        pontos += 1
        moeda.x = random.randint(0, 768)
        moeda.y = random.randint(0, 568)

    # --- Desenho na tela ---
    tela.fill((0, 0, 0))  # fundo preto
    pygame.draw.rect(tela, (0, 120, 255), jogador)  # jogador azul
    pygame.draw.rect(tela, (255, 215, 0), moeda)  # moeda amarela

    # Pontuação
    texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()
