import streamlit as st

# 미로 설정
MAZE = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

START = (0, 0)
GOAL = (4, 4)
WALL = 1

# 세션 상태 초기화
if "player_pos" not in st.session_state:
    st.session_state.player_pos = START
if "win" not in st.session_state:
    st.session_state.win = False

# 이동 함수
def move(dx, dy):
    if st.session_state.win:
        return
    x, y = st.session_state.player_pos
    nx, ny = x + dx, y + dy
    if 0 <= nx < 5 and 0 <= ny < 5 and MAZE[ny][nx] != WALL:
        st.session_state.player_pos = (nx, ny)
    if st.session_state.player_pos == GOAL:
        st.session_state.win = True

# 제목
st.title("🧩 미로 탈출 게임")
st.markdown("**⬛ = 벽 / ⬜ = 길 / 🔵 = 나 / 🏁 = 목표**")

# 미로 출력
for y in range(5):
    cols = st.columns(5)
    for x in range(5):
        cell = "⬜"
        if MAZE[y][x] == WALL:
            cell = "⬛"
        if (x, y) == st.session_state.player_pos:
            cell = "🔵"
        if (x, y) == GOAL:
            cell = "🏁" if (x, y) != st.session_state.player_pos else "🎉"
        cols[x].markdown(f"<div style='text-align:center; font-size:30px'>{cell}</div>", unsafe_allow_html=True)

# 이동 버튼
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

# 상태 메시지
if st.session_state.win:
    st.success("🎉 축하합니다! 미로를 탈출했어요!")

# 초기화 버튼
if st.button("🔄 다시 시작"):
    st.session_state.player_pos = START
    st.session_state.win = False
