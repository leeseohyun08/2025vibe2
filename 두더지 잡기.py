import streamlit as st
import random
import time

# 설정
GRID_SIZE = 3
MOLE_REFRESH_SEC = 1.0  # 두더지가 이동하는 시간 간격
GAME_DURATION = 15      # 게임 시간 (초)

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.mole_pos = (0, 0)
    st.session_state.start_time = time.time()
    st.session_state.running = True

# 새 게임 버튼
if st.button("🔄 새 게임 시작"):
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.running = True

# 타이머 갱신
elapsed = time.time() - st.session_state.start_time
remaining = max(0, int(GAME_DURATION - elapsed))

# 게임 종료 처리
if elapsed >= GAME_DURATION:
    st.session_state.running = False

# 두더지 위치 랜덤 이동
if st.session_state.running:
    if "last_mole_time" not in st.session_state or time.time() - st.session_state.last_mole_time > MOLE_REFRESH_SEC:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        st.session_state.mole_pos = (x, y)
        st.session_state.last_mole_time = time.time()

# UI 출력
st.title("🐹 두더지 잡기 게임!")
st.markdown(f"⏱️ 남은 시간: **{remaining}초**")
st.markdown(f"🎯 점수: **{st.session_state.score}점**")

for i in range(GRID_SIZE):
    cols = st.columns(GRID_SIZE)
    for j in range(GRID_SIZE):
        label = "🐹" if (i, j) == st.session_state.mole_pos and st.session_state.running else "⬜"
        if cols[j].button(label, key=f"{i}-{j}"):
            if (i, j) == st.session_state.mole_pos and st.session_state.running:
                st.session_state.score += 1
                # 두더지 즉시 이동
                x = random.randint(0, GRID_SIZE - 1)
                y = random.randint(0, GRID_SIZE - 1)
                st.session_state.mole_pos = (x, y)
                st.session_state.last_mole_time = time.time()

if not st.session_state.running:
    st.success(f"게임 종료! 🎉 최종 점수: **{st.session_state.score}점**")
