import streamlit as st

# 단계별 미로 설정 (0 = 길, 1 = 벽)
MAZES = [
    [  # Stage 1: 5x5
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ],
    [  # Stage 2: 7x7
        [0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0],
    ],
    [  # Stage 3: 9x9 (더 어렵게)
        [0, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ],
]

START = (0, 0)
WALL = 1
MAX_STAGE = len(MAZES)

# 상태 초기화
if "stage" not in st.session_state:
    st.session_state.stage = 0
if "player_pos" not in st.session_state:
    st.session_state.player_pos = START
if "win" not in st.session_state:
    st.session_state.win = False

# 현재 미로
stage = st.session_state.stage
maze = MAZES[stage]
height = len(maze)
width = len(maze[0])
GOAL = (width - 1, height - 1)

# 이동 함수
def move(dx, dy):
    if st.session_state.win:
        return
    x, y = st.session_state.player_pos
    nx, ny = x + dx, y + dy
    if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] != WALL:
        st.session_state.player_pos = (nx, ny)
    if st.session_state.player_pos == GOAL:
        st.session_state.win = True

# UI 출력
st.title(f"🧭 미로 탈출 게임 - 스테이지 {stage + 1}")
st.markdown("**⬛ = 벽 / ⬜ = 길 / 🔵 = 나 / 🏁 = 목표**")

# 미로 시각화
for y in range(height):
    cols = st.columns(width)
    for x in range(width):
        cell = "⬜"
        if maze[y][x] == WALL:
            cell = "⬛"
        if (x, y) == st.session_state.player_pos:
            cell = "🔵"
        if (x, y) == GOAL:
            cell = "🏁" if (x, y) != st.session_state.player_pos else "🎉"
        cols[x].markdown(f"<div style='text-align:center; font-size:30px'>{cell}</div>", unsafe_allow_html=True)

# 이동 버튼 UI
st.markdown("### 🔀 이동")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("⬆️ 위로"): move(0, -1)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️ 왼쪽"): move(-1, 0)
with col2:
    if st.button("⬇️ 아래"): move(0, 1)
with col3:
    if st.button("➡️ 오른쪽"): move(1, 0)

# 성공 시 다음 단계로
if st.session_state.win:
    if stage + 1 < MAX_STAGE:
        st.success("🎉 탈출 성공! 다음 스테이지로 이동합니다.")
        if st.button("➡️ 다음 스테이지"):
            st.session_state.stage += 1
            st.session_state.player_pos = START
            st.session_state.win = False
            st.experimental_rerun()
    else:
        st.success("🏆 모든 스테이지를 클리어했습니다! 게임 끝!")

# 다시 시작 버튼
if st.button("🔄 현재 스테이지 다시 시작"):
    st.session_state.player_pos = START
    st.session_state.win = False
