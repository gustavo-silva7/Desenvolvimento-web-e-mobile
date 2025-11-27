import pygame
import random

pygame.init()

LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Coletar Moedas")


jogador = pygame.Rect(400, 300, 32, 32)  # x, y, largura, altura
velocidade = 5


moeda = pygame.Rect(
    random.randint(0, 768),
    random.randint(0, 568),
    32,
    32
)


teclas = pygame.key.get_pressed()
if teclas[pygame.K_LEFT]:
    jogador.x -= velocidade
if teclas[pygame.K_RIGHT]:
    jogador.x += velocidade
if teclas[pygame.K_UP]:
    jogador.y -= velocidade
if teclas[pygame.K_DOWN]:
    jogador.y += velocidade


if jogador.colliderect(moeda):
    pontos += 1
    moeda.x = random.randint(0, 768)
    moeda.y = random.randint(0, 568)



tela.fill((0,0,0))  # limpa a tela (preto)

pygame.draw.rect(tela, (0,120,255), jogador)  # jogador azul
pygame.draw.rect(tela, (255,215,0), moeda)    # moeda amarela


fonte = pygame.font.SysFont("Arial", 28)
texto = fonte.render(f"Pontos: {pontos}", True, (255,255,255))
tela.blit(texto, (10,10))


rodando = True
clock = pygame.time.Clock()

while rodando:
    clock.tick(60)  # limita a 60 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # ---- movimentos do jogador ----
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        jogador.x += velocidade
    if teclas[pygame.K_UP]:
        jogador.y -= velocidade
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade

    # ---- colisão com moeda ----
    if jogador.colliderect(moeda):
        pontos += 1
        moeda.x = random.randint(0, 768)
        moeda.y = random.randint(0, 568)

    # ---- desenho ----
    tela.fill((0,0,0))
    pygame.draw.rect(tela, (0,120,255), jogador)
    pygame.draw.rect(tela, (255,215,0), moeda)

    texto = fonte.render(f"Pontos: {pontos}", True, (255,255,255))
    tela.blit(texto, (10,10))

    pygame.display.update()

pygame.quit()
