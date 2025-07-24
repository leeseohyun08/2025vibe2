import streamlit as st
import random

# ---------------------
# 무작위 미로 생성 함수
# ---------------------
def generate_maze(size):
    # size는 홀수여야 함
    maze = [[1 for _ in range(size)] for _ in range(size)]
    start = (1, 1)

    def dfs(x, y):
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy // 2][x + dx // 2] = 0
                dfs(nx, ny)

    maze[start[1]][start[0]] = 0
    dfs(*start)

    # 출발점과 도착점 열어두기
    maze[0][0] = 0
    maze[size - 1][size - 1] = 0
    return maze

# ---------------------
# 상태 초기화
# ---------------------
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "maze" not in st.session_state:
    st.session_state.maze = generate_maze(7)
if "player_pos" not in st.session_state:
    st.session_state.player_pos = (0, 0)
if "win" not in st.session_state:
    st.session_state.win = False

# ---------------------
# 이동 함수
# ---------------------
def move(dx, dy):
    if st.session_state.win:
        return
    x, y = st.session_state.player_pos
    nx, ny = x + dx, y + dy
    maze = st.session_state.maze
    if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0:
        st.session_state.player_pos = (nx, ny)
    if st.session_state.player_pos == (len(maze[0]) - 1, len(maze) - 1):
        st.session_state.win = True

# ---------------------
# UI 출력
# ---------------------
maze = st.session_state.maze
width = len(maze[0])
height = len(maze)

st.title(f"🧩 무작위 미로 탈출 - 스테이지 {st.session_state.stage}")
st.markdown("⬛ = 벽 / ⬜ = 길 / 🔵 = 나 / 🏁 = 목표")

# 미로 출력
for y in range(height):
    cols = st.columns(width)
    for x in range(width):
        cell = "⬜"
        if maze[y][x] == 1:
            cell = "⬛"
        if (x, y) == st.session_state.player_pos:
            cell = "🔵"
        if (x, y) == (width - 1, height - 1):
            if st.session_state.player_pos == (x, y):
                cell = "🎉"
            else:
                cell = "🏁"
        cols[x].markdown(f"<div style='text-align:center; font-size:30px'>{cell}</div>", unsafe_allow_html=True)

# 이동 버튼 - 키보드 방향키 스타일
st.markdown("### 🔀 이동")
top = st.columns(3)
with top[1]:
    if st.button("⬆️ 위로"): move(0, -1)
mid = st.columns(3)
with mid[0]:
    if st.button("⬅️ 왼쪽"): move(-1, 0)
with mid[1]:
    if st.button("⬇️ 아래"): move(0, 1)
with mid[2]:
    if st.button("➡️ 오른쪽"): move(1, 0)

# ---------------------
# 성공 시 다음 스테이지로
# ---------------------
if st.session_state.win:
    st.success("🎉 탈출 성공! 새로운 미로로 이동하세요.")
    if st.button("➡️ 다음 스테이지"):
        st.session_state.stage += 1
        st.session_state.maze = generate_maze(5 + 2 * st.session_state.stage)  # 점점 커짐 (7x7, 9x9, ...)
        st.session_state.player_pos = (0, 0)
        st.session_state.win = False

# ---------------------
# 다시 시작
# ---------------------
if st.button("🔄 현재 미로 다시 시작"):
    size = len(st.session_state.maze)
    st.session_state.maze = generate_maze(size)
    st.session_state.player_pos = (0, 0)
    st.session_state.win = False
