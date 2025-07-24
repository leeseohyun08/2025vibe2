import streamlit as st
import random
import time

# -------------------- 설정 --------------------
st.set_page_config(page_title="가위바위보 게임", layout="centered")
st.title("✊✋✌️ 가위바위보 게임")
st.write("먼저 2번 이기면 승리! 컴퓨터와 한판 붙어보자!")

# -------------------- 이모지 매핑 --------------------
options = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# -------------------- 세션 상태 초기화 --------------------
defaults = {
    "wins": 0,
    "losses": 0,
    "draws": 0,
    "final_result": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------- 게임 종료 여부 --------------------
game_over = st.session_state.wins == 2 or st.session_state.losses == 2

# -------------------- 게임 리셋 --------------------
if st.button("🔄 게임 리셋"):
    for key in defaults:
        st.session_state[key] = defaults[key]
    st.experimental_rerun()

# -------------------- 게임 진행 --------------------
if not game_over:
    user_choice = st.radio("무엇을 낼까요?", list(options.keys()), horizontal=True)

    if st.button("대결하기!"):
        # ⏳ 카운트다운 + "가위바위보!"
        with st.empty() as countdown_area:
            for count in ["3", "2", "1"]:
                countdown_area.markdown(f"<h1 style='text-align: center;'>{count}</h1>", unsafe_allow_html=True)
                time.sleep(0.8)
            countdown_area.markdown(f"<h1 style='text-align: center;'>가위바위보!</h1>", unsafe_allow_html=True)
            time.sleep(0.8)

        # 💻 컴퓨터 선택
        computer_choice = random.choice(list(options.keys()))

        # 결과 판정
        if user_choice == computer_choice:
            result_emoji = "😐"
            result_text = "비겼습니다!"
            st.session_state.draws += 1
        elif (
            (user_choice == "가위" and computer_choice == "보") or
            (user_choice == "바위" and computer_choice == "가위") or
            (user_choice == "보" and computer_choice == "바위")
        ):
            result_emoji = "🎉"
            result_text = "이겼습니다!"
            st.session_state.wins += 1
        else:
            result_emoji = "😢"
            result_text = "졌습니다!"
            st.session_state.losses += 1

        # -------------------- 결과 표시 --------------------
        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🙋‍♂️ 나")
            st.markdown(
                f"<div style='font-size: 80px; text-align: center;'>{options.get(user_choice, '❓')}</div>",
                unsafe_allow_html=True
            )
            st.markdown(f"<div style='text-align: center; font-weight: bold;'>{user_choice}</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("### 💻 컴퓨터")
            st.markdown(
                f"<div style='font-size: 80px; text-align: center;'>{options.get(computer_choice, '❓')}</div>",
                unsafe_allow_html=True
            )
            st.markdown(f"<div style='text-align: center; font-weight: bold;'>{computer_choice}</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center;'>{result_emoji} {result_text}</h2>", unsafe_allow_html=True)

# -------------------- 최종 결과 --------------------
if st.session_state.wins == 2:
    st.session_state.final_result = "🎉 당신이 최종 승자입니다!"
elif st.session_state.losses == 2:
    st.session_state.final_result = "💻 컴퓨터가 최종 승자입니다!"

if st.session_state.final_result:
    st.markdown("---")
    st.markdown(f"<h1 style='text-align: center; color: green;'>{st.session_state.final_result}</h1>", unsafe_allow_html=True)

# -------------------- 점수판 --------------------
st.markdown("---")
st.markdown(f"""
### 🔢 현재 점수
- ✅ 승리: {st.session_state.wins}
- ❌ 패배: {st.session_state.losses}
- ⚖️ 무승부: {st.session_state.draws}
""")
