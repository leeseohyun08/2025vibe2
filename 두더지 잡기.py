import streamlit as st
import random
import time

# 설정
GRID_SIZE = 3
MOLE_REFRESH_SEC = 0.8
GAME_DURATION = 15

# 초기화
if "score" not in st.session_state:
    def init_game():
        return {
            "score": 0,
            "mole_pos": (0, 0),
            "start_time": time.time(),
            "running": True,
            "last_mole_time": 0
        }
    st.session_state.game = init_game()

# 새 게임 버튼
if st.button("🔄 새 게임 시작"):
    st.session_state.game = {
        "score": 0,
        "mole_pos": (0, 0),
        "start_time": time.time(),
        "running": True,
        "last_mole_time": 0
    }

game = st.session_state.game
elapsed = time.time() - game["start_time"]
remaining = max(0, int(GAME_DURATION - elapsed))

# 게임 종료 조건
if elapsed >= GAME_DURATION:
    game["running"] = False

# 두더지 이동
if game["running"] and time.time() - game["last_mole_time"] > MOLE_REFRESH_SEC:
    x = random.randint(0, GRID_SIZE - 1)
    y = random.randint(0, GRID_SIZE - 1)
    game["mole_pos"] = (x, y)
    game["last_mole_time"] = time.time()

# UI 출력
st.title("🐹 두더지 잡기 게임")
st.markdown(f"⏱️ 남은 시간: **{remaining}초**")
st.markdown(f"🎯 점수: **{game['score']}점**")

# 버튼 스타일 적용
button_style = """
    <style>
    .mole-btn {
        font-size: 40px !important;
        height: 80px !important;
        width: 80px !important;
        text-align: center !important;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# 버튼 출력
for i in range(GRID_SIZE):
    cols = st.columns(GRID_SIZE)
    for j in range(GRID_SIZE):
        is_mole = (i, j) == game["mole_pos"]
        key = f"{i}-{j}-{random.random()}"  # 매번 새롭게 그리도록 key 변경
        if is_mole and game["running"]:
            if cols[j].button("🐹", key=key):
                game["score"] += 1
                # 두더지를 즉시 이동
                game["mole_pos"] = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
                game["last_mole_time"] = time.time()
        else:
            cols[j].markdown(f'<button class="mole-btn">⬜</button>', unsafe_allow_html=True)

# 종료 메시지
if not game["running"]:
    st.success(f"🎉 게임 끝! 최종 점수: **{game['score']}점**")
