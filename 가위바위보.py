import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="가위바위보", layout="centered")

# 제목
st.title("✊✋✌️ 가위바위보 게임")
st.write("3판 2선승제! 컴퓨터와 대결해보세요.")

# 선택지
options = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 세션 상태 초기화
for key in ["wins", "losses", "draws", "final_result"]:
    if key not in st.session_state:
        st.session_state[key] = 0 if key != "final_result" else ""

# 게임 종료 여부
if st.session_state["wins"] == 2:
    st.session_state["final_result"] = "🎉 당신이 최종 승자입니다!"
elif st.session_state["losses"] == 2:
    st.session_state["final_result"] = "💻 컴퓨터가 최종 승자입니다!"

# 게임 리셋
if st.button("🔄 게임 리셋"):
    for key in ["wins", "losses", "draws", "final_result"]:
        st.session_state[key] = 0 if key != "final_result" else ""
    st.experimental_rerun()

# 게임 진행
if not st.session_state["final_result"]:
    user_choice = st.radio("무엇을 낼까요?", list(options.keys()), horizontal=True)

    if st.button("대결하기!"):
        with st.empty():
            for n in ["3", "2", "1"]:
                st.markdown(f"<h1 style='text-align: center;'>{n}</h1>", unsafe_allow_html=True)
                time.sleep(0.8)
            st.markdown(f"<h1 style='text-align: center;'>가위바위보!</h1>", unsafe_allow_html=True)
            time.sleep(0.8)

        computer_choice = random.choice(list(options.keys()))

        # 결과 판정
        if user_choice == computer_choice:
            emoji, msg = "😐", "비겼습니다!"
            st.session_state["draws"] += 1
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            emoji, msg = "🎉", "이겼습니다!"
            st.session_state["wins"] += 1
        else:
            emoji, msg = "😢", "졌습니다!"
            st.session_state["losses"] += 1

        # 결과 출력
        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center;'>{emoji} {msg}</h2>", unsafe_allow_html=True)

        # 선택 이모지 출력
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🙋‍♂️ 나")
            st.markdown(f"<div style='font-size: 80px; text-align: center;'>{options.get(user_choice, '❓')}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown("### 💻 컴퓨터")
            st.markdown(f"<div style='font-size: 80px; text-align: center;'>{options.get(computer_choice, '❓')}</div>", unsafe_allow_html=True)

# 최종 결과 출력
if st.session_state["final_result"]:
    st.markdown("---")
    st.markdown(f"<h1 style='text-align: center; color: green;'>{st.session_state['final_result']}</h1>", unsafe_allow_html=True)

# 점수판
st.markdown("---")
st.markdown(f"""
### 🔢 현재 점수
- ✅ 승리: {st.session_state["wins"]}
- ❌ 패배: {st.session_state["losses"]}
- ⚖️ 무승부: {st.session_state["draws"]}
""")
