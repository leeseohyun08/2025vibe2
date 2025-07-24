import pygame
import sys

# 초기화
pygame.init()
CELL_SIZE = 50
MAZE = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]
ROWS = len(MAZE)
COLS = len(MAZE[0])
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🧩 미로 탈출")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 100, 255)
GREEN = (0, 200, 0)
RED   = (255, 0, 0)

# 위치
player_pos = [0, 0]
goal_pos = [COLS - 1, ROWS - 1]

# 시계
clock = pygame.time.Clock()

# 게임 루프
running = True
won = False
while running:
    clock.tick(60)
    WIN.fill(WHITE)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    x, y = player_pos
    if not won:
        if keys[pygame.K_LEFT]:
            if x > 0 and MAZE[y][x - 1] == 0:
                player_pos[0] -= 1
                pygame.time.wait(150)
        if keys[pygame.K_RIGHT]:
            if x < COLS - 1 and MAZE[y][x + 1] == 0:
                player_pos[0] += 1
                pygame.time.wait(150)
        if keys[pygame.K_UP]:
            if y > 0 and MAZE[y - 1][x] == 0:
                player_pos[1] -= 1
                pygame.time.wait(150)
        if keys[pygame.K_DOWN]:
            if y < ROWS - 1 and MAZE[y + 1][x] == 0:
                player_pos[1] += 1
                pygame.time.wait(150)

    # 승리 체크
    if player_pos == goal_pos:
        won = True

    # 미로 그리기
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if MAZE[row][col] == 1:
                pygame.draw.rect(WIN, BLACK, rect)
            else:
                pygame.draw.rect(WIN, WHITE, rect)
                pygame.draw.rect(WIN, (200, 200, 200), rect, 1)

    # 캐릭터 그리기
    px, py = player_pos
    pygame.draw.rect(WIN, BLUE, (px * CELL_SIZE, py * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 목표지점
    gx, gy = goal_pos
    pygame.draw.rect(WIN, GREEN, (gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 메시지 출력
    if won:
        font = pygame.font.SysFont("consolas", 32)
        text = font.render("🎉 탈출 성공!", True, RED)
        WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.update()

# 종료
pygame.quit()
sys.exit()
