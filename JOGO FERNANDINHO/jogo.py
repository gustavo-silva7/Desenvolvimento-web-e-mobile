# import pygame
# import random

# pygame.init()

# # Configurações da janela
# LARGURA = 800
# ALTURA = 600
# tela = pygame.display.set_mode((LARGURA, ALTURA))
# pygame.display.set_caption("Coletar Moedas")

# # Jogador
# jogador = pygame.Rect(400, 300, 32, 32)
# velocidade = 5

# # Moeda
# moeda = pygame.Rect(
#     random.randint(0, 768),
#     random.randint(0, 568),
#     32,
#     32
# )

# # Pontuação
# pontos = 0
# fonte = pygame.font.SysFont("Arial", 28)

# clock = pygame.time.Clock()
# rodando = True

# # =================== LOOP PRINCIPAL DO JOGO ===================== #
# while rodando:
#     clock.tick(60)  # 60 FPS

#     # Eventos
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False

#     # Movimento do jogador
#     teclas = pygame.key.get_pressed()
#     if teclas[pygame.K_LEFT]:
#         jogador.x -= velocidade
#     if teclas[pygame.K_RIGHT]:
#         jogador.x += velocidade
#     if teclas[pygame.K_UP]:
#         jogador.y -= velocidade
#     if teclas[pygame.K_DOWN]:
#         jogador.y += velocidade

#     # Limites da tela
#     jogador.x = max(0, min(jogador.x, LARGURA - jogador.width))
#     jogador.y = max(0, min(jogador.y, ALTURA - jogador.height))

#     # Colisão com a moeda
#     if jogador.colliderect(moeda):
#         pontos += 1
#         moeda.x = random.randint(0, 768)
#         moeda.y = random.randint(0, 568)

#     # --- Desenho na tela ---
#     tela.fill((0, 0, 0))  # fundo preto
#     pygame.draw.rect(tela, (0, 120, 255), jogador)  # jogador azul
#     pygame.draw.rect(tela, (255, 215, 0), moeda)  # moeda amarela

#     # Pontuação
#     texto = fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
#     tela.blit(texto, (10, 10))

#     pygame.display.update()

# pygame.quit()



# fase1.py
# Fase 1 jogável - top-down 32x32 tiles - "Fernandinho e os Pães"
# Requisitos: pygame
# Rodar: python fase1.py

import pygame
import random
import sys

pygame.init()
TILE = 32
COLUMNS = 25
ROWS = 18
LARGURA = TILE * COLUMNS
ALTURA = TILE * ROWS
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Fernandinho - Fase 1 (Bairro)")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 18)

# ---------------------------------------
# Helpers para pixel-art procedural
# ---------------------------------------
def small_sprite_from_pattern(pattern, pix=8, scale=TILE):
    """pattern: list of strings with characters representing colors.
       pix: pattern size (len rows). Returns scaled surface (scale x scale)."""
    h = len(pattern)
    w = len(pattern[0])
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    color_map = {
        ".": (0,0,0,0),   # transparent
        "r": (200, 40, 40),
        "d": (120, 20, 20),
        "y": (255, 215, 0),
        "b": (20, 120, 220),
        "g": (30, 180, 30),
        "B": (120, 80, 20),
        "w": (230,230,230),
        "p": (180, 100, 200),
        "o": (255,140,0),
        "k": (40,40,40)
    }
    for y,row in enumerate(pattern):
        for x,ch in enumerate(row):
            if ch != ".":
                surf.set_at((x,y), color_map.get(ch,(255,0,255)))
    surf = pygame.transform.scale(surf, (scale * (w//pix if w==pix else scale), scale))
    # ensure nearest neighbor scaling for pixel look
    surf = pygame.transform.scale(surf, (TILE, TILE))
    return surf

# Simpler: create tiny 8x8 patterns then scale nearest.
def make_sprite(pattern_map):
    # pattern_map is list of strings of equal length (8x8 recommended)
    tiny = pygame.Surface((len(pattern_map[0]), len(pattern_map)), pygame.SRCALPHA)
    palette = {
        ".": (0,0,0,0),
        "P": (100,180,255),   # player color
        "H": (60,120,200),
        "B": (200,160,90),    # bread
        "D": (150,80,20),     # dog
        "C": (160,160,160),   # cat
        "X": (120,120,120),   # box
        "S": (255,100,100),   # switch
        "W": (30,30,30),      # wall
        "G": (80,200,90),     # grass
    }
    for y,row in enumerate(pattern_map):
        for x,ch in enumerate(row):
            tiny.set_at((x,y), palette.get(ch,(255,0,255)))
    surf = pygame.transform.scale(tiny, (TILE, TILE))
    return surf

# We'll define simple 8x8 pixel patterns:
player_pat = [
"........",
"..PPPP..",
".PPPPPP.",
".P.H.PP.",
".PPPPPP.",
"..PPPP..",
"...PP...",
"........",
]
bread_pat = [
"........",
"..BBBB..",
".BBBBBB.",
".BBBBBB.",
".BBBBBB.",
"..BBBB..",
"...BB...",
"........",
]
dog_pat = [
"........",
".DDDDDD.",
".D.D.DD.",
".DDDDDD.",
".D..D.D.",
"..DDDD..",
"...DD...",
"........",
]
cat_pat = [
"........",
".CCCCCC.",
".C.C.CC.",
".CCCCCC.",
".C..C.C.",
"..CCCC..",
"...CC...",
"........",
]
box_pat = [
"XXXXXXXX",
"XXXXXXXX",
"XXXXXXXX",
"XXXXXXXX",
"XXXXXXXX",
"XXXXXXXX",
"XXXXXXXX",
"XXXXXXXX",
]
switch_pat = [
"........",
"........",
"...SS...",
"..SSSS..",
"..SSSS..",
"...SS...",
"........",
"........",
]

SPR_PLAYER = make_sprite(player_pat)
SPR_BREAD = make_sprite(bread_pat)
SPR_DOG = make_sprite(dog_pat)
SPR_CAT = make_sprite(cat_pat)
SPR_BOX = make_sprite(box_pat)
SPR_SWITCH = make_sprite(switch_pat)

# ---------------------------------------
# Map/tiles: 0 floor, 1 wall, 2 bread, 3 box, 4 switch, 5 door (closed)
# We'll store dynamic entities separately (breads list, boxes list, enemies list).
# ---------------------------------------
# Build base map with walls around
tilemap = [[0 for _ in range(COLUMNS)] for __ in range(ROWS)]
for x in range(COLUMNS):
    tilemap[0][x] = 1
    tilemap[ROWS-1][x] = 1
for y in range(ROWS):
    tilemap[y][0] = 1
    tilemap[y][COLUMNS-1] = 1

# Some houses/walls to shape the neighborhood (manually placed)
walls = [
    # a house block left
    *( (y,3) for y in range(3,10) ),
    *( (3,x) for x in range(3,10) ),
    *( (9,x) for x in range(3,10) ),
    # small park right
    *( (5,x) for x in range(14,21) ),
    *( (11,x) for x in range(14,21) ),
    *( (y,14) for y in range(5,12) ),
    *( (y,20) for y in range(5,12) ),
    # a wall block bottom center
    *( (13,x) for x in range(7,13) ),
    *( (13,x) for x in range(16,19) ),
]

for (r,c) in walls:
    if 0<=r<ROWS and 0<=c<COLUMNS:
        tilemap[r][c] = 1

# closed door tile at specific spot (to be opened by switch)
door_pos = (10, 12)  # row,col
tilemap[door_pos[0]][door_pos[1]] = 5

# Place a switch in front of a small wall with box puzzle
switch_pos = (12, 11)
tilemap[switch_pos[0]][switch_pos[1]] = 4

# Place a pushable box that must be moved onto switch to open door or similar
boxes = [ [11, 11] ]  # list of [row,col]

# Bread positions (pães) - collect all
breads = []
# some breads scattered
bread_positions = [
    (2,6),(4,6),(6,6),
    (2,18),(4,18),(8,16),
    (7,10),(10,4),(14,8),(15,17),(8,22)
]
for r,c in bread_positions:
    breads.append([r,c])

# Player starting tile (grid coords)
player = {"r": 16, "c": 2, "x":2*TILE, "y":16*TILE}
player_speed = 4  # pixels per frame
player_rect = pygame.Rect(player["x"], player["y"], TILE, TILE)

# Enemies
class Enemy:
    def __init__(self, r, c, kind="dog"):
        self.r = r
        self.c = c
        self.x = c * TILE
        self.y = r * TILE
        self.dir_timer = 0
        self.vx = 0
        self.vy = 0
        self.kind = kind
        # patrol endpoints or random
        self.path = []
        if kind == "dog":
            # simple horizontal patrol
            self.path = [(r,c),(r,c+3)]
        else:
            self.path = [(r,c),(r+3,c)]
        self.pindex = 0

    def update(self, dt):
        # simple patrol: move toward next waypoint
        tx, ty = self.path[self.pindex][1]*TILE, self.path[self.pindex][0]*TILE
        dx = tx - self.x
        dy = ty - self.y
        speed = 1.6
        if abs(dx) < 2 and abs(dy) < 2:
            self.pindex = (self.pindex+1) % len(self.path)
        else:
            if dx != 0: self.x += speed * (1 if dx>0 else -1)
            if dy != 0: self.y += speed * (1 if dy>0 else -1)

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), TILE, TILE)

enemies = [Enemy(6, 8, "dog"), Enemy(9, 19, "cat")]

# Game state
score = 0
lives = 3
show_message = None
message_timer = 0
door_open = False

# Helpers for map collision
def is_solid(r,c):
    if not (0 <= r < ROWS and 0 <= c < COLUMNS):
        return True
    t = tilemap[r][c]
    if t == 0: return False
    if t == 5 and door_open:  # door but opened
        return False
    return t != 0

def box_at(r,c):
    for b in boxes:
        if b[0]==r and b[1]==c:
            return b
    return None

def bread_at(r,c):
    for b in breads:
        if b[0]==r and b[1]==c:
            return b
    return None

def world_to_tile(px, py):
    return py // TILE, px // TILE

def try_push_box(br, bc, dr, dc):
    """Attempt to push box at br,bc by delta dr,dc (tile delta). Returns True if moved"""
    target_r = br + dr
    target_c = bc + dc
    if not (0 <= target_r < ROWS and 0 <= target_c < COLUMNS):
        return False
    # blocked by wall or another box or closed door
    if is_solid(target_r, target_c):
        return False
    if box_at(target_r, target_c):
        return False
    # move box
    box = box_at(br, bc)
    if box:
        box[0] = target_r
        box[1] = target_c
        return True
    return False

# Draw functions
def draw_map():
    for r in range(ROWS):
        for c in range(COLUMNS):
            t = tilemap[r][c]
            x = c * TILE
            y = r * TILE
            # floor
            pygame.draw.rect(tela, (60,160,60), (x,y,TILE,TILE))
            # small grid lines for pixel feel
            # pygame.draw.rect(tela, (40,120,40), (x,y,TILE,TILE), 1)
            if t == 1:
                pygame.draw.rect(tela, (100,80,60), (x,y,TILE,TILE))
                # roof detail
                pygame.draw.rect(tela, (80,60,40), (x+4,y+4,TILE-8,TILE-8))
            elif t == 5:
                col = (150,90,50) if not door_open else (180,160,120)
                pygame.draw.rect(tela, col, (x,y,TILE,TILE))
                # door lines
                pygame.draw.rect(tela, (120,60,30), (x+4,y+4,TILE-8,TILE-8))
            elif t == 4:
                tela.blit(SPR_SWITCH, (x,y))

    # draw boxes
    for b in boxes:
        tela.blit(SPR_BOX, (b[1]*TILE, b[0]*TILE))

    # draw breads
    for br in breads:
        tela.blit(SPR_BREAD, (br[1]*TILE, br[0]*TILE))

# Reset player position on hit
def reset_player():
    global player
    player["r"], player["c"], player["x"], player["y"] = 16,2,2*TILE,16*TILE
    player_rect.topleft = (player["x"], player["y"])

# Main loop
running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = dy = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = player_speed

    # Movement with simple tile collision (pixel-based but with tile checks)
    # compute intended new position
    new_x = player["x"] + dx
    new_y = player["y"] + dy
    # tile coords of player's bounding box corners
    new_rect = pygame.Rect(new_x, new_y, TILE, TILE)
    # We'll test tile collisions by checking the tile the player is moving into
    # Convert to center tile:
    center_r = (new_y + TILE//2) // TILE
    center_c = (new_x + TILE//2) // TILE

    # If there is a box in that tile, try to push it
    b = box_at(center_r, center_c)
    if b:
        # compute tile delta attempted
        dr = ( (new_y + TILE//2)//TILE ) - b[0]
        dc = ( (new_x + TILE//2)//TILE ) - b[1]
        # If moving, attempt push
        if dx != 0 or dy != 0:
            # determine direction in tile units
            tr = b[0] + (1 if dy>0 else -1 if dy<0 else 0)
            tc = b[1] + (1 if dx>0 else -1 if dx<0 else 0)
            moved = try_push_box(b[0], b[1], tr-b[0], tc-b[1])
            if moved:
                # allow player to move into the box's previous spot
                player["x"] = new_x
                player["y"] = new_y
    else:
        # If target tile is solid (wall or closed door) block movement
        # Check four corners of new_rect to find tiles
        corners = [
            ((new_x)//TILE, (new_y)//TILE),
            (((new_x+TILE-1)//TILE), (new_y)//TILE),
            ((new_x)//TILE, ((new_y+TILE-1)//TILE)),
            (((new_x+TILE-1)//TILE), ((new_y+TILE-1)//TILE)),
        ]
        blocked = False
        for (cc, rr) in [(c,r) for (c,r) in corners]:
            # note: corners uses format (col,row) so swap
            col, row = cc, rr
            if not (0<=row<ROWS and 0<=col<COLUMNS) or is_solid(row, col):
                blocked = True
                break
        if not blocked:
            player["x"] = new_x
            player["y"] = new_y

    player_rect.topleft = (int(player["x"]), int(player["y"]))

    # Update enemies
    for e in enemies:
        e.update(dt)
        # collision with player?
        if player_rect.colliderect(e.rect()):
            # player hurt: respawn and lose life
            lives -= 1
            show_message = "Você foi mordido! -1 vida"
            message_timer = 2.0
            reset_player()
            if lives <= 0:
                show_message = "Game Over! Press R to restart."
                # freeze movement until R
                # we'll allow restart on key press

    # Check bread collection: check tile of player's center
    pr = (player["y"] + TILE//2) // TILE
    pc = (player["x"] + TILE//2) // TILE
    b = bread_at(pr, pc)
    if b:
        breads.remove(b)
        score += 1
        show_message = "Pão coletado!"
        message_timer = 1.0

    # Check switch activation: if a box sits on switch tile -> open door
    box_on_switch = box_at(switch_pos[0], switch_pos[1]) is not None
    if box_on_switch and not door_open:
        door_open = True
        show_message = "Você ouviu um clique na porta..."
        message_timer = 2.0

    # Win condition: all breads collected
    if len(breads) == 0:
        show_message = "Fase completa! Parabéns, você coletou todos os pães!"
        message_timer = 999.0  # long show; press N to quit or R to restart

    # Input for restart after game over or to continue
    if (show_message and "Game Over" in (show_message or "")):
        if keys[pygame.K_r]:
            # restart
            score = 0
            lives = 3
            # reset breads
            breads = [[r,c] for (r,c) in bread_positions]
            boxes = [[11,11]]
            door_open = False
            reset_player()
            show_message = None

    # Also allow restart after win or quit to next via key N (not implemented further)
    if len(breads) == 0:
        if keys[pygame.K_r]:
            # restart same level
            score = 0
            lives = 3
            breads = [[r,c] for (r,c) in bread_positions]
            boxes = [[11,11]]
            door_open = False
            reset_player()
            show_message = None
        if keys[pygame.K_n]:
            running = False

    # Draw everything
    draw_map()
    # draw switch tile sprite (already drawn by draw_map)
    # draw player
    tela.blit(SPR_PLAYER, (player["x"], player["y"]))

    # draw enemies
    for e in enemies:
        if e.kind == "dog":
            tela.blit(SPR_DOG, (e.x, e.y))
        else:
            tela.blit(SPR_CAT, (e.x, e.y))

    # UI
    ui_text = FONT.render(f"Pães: {score}   Vidas: {lives}", True, (255,255,255))
    tela.blit(ui_text, (8,8))

    if show_message:
        message_timer -= dt
        # draw message center
        msgsurf = FONT.render(show_message, True, (255,255,0))
        tela.blit(msgsurf, (LARGURA//2 - msgsurf.get_width()//2, 8))
        if message_timer <= 0:
            show_message = None

    pygame.display.flip()

pygame.quit()
sys.exit()

