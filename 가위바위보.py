import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위바위보 게임", layout="centered")

st.title("✊✋✌️ 가위바위보 게임")
st.write("컴퓨터와 한판 대결!")

# 이모지 매핑
options = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 사용자 선택
user_choice = st.radio("무엇을 낼까요?", list(options.keys()), horizontal=True)

# 결과 처리
if st.button("대결하기!"):
    computer_choice = random.choice(list(options.keys()))

    # 승부 판정
    if user_choice == computer_choice:
        result = "😐 무승부!"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 당신의 승리!"
    else:
        result = "💻 컴퓨터의 승리!"

    # 결과 화면 출력
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧑 당신")
        st.markdown(f"<div style='font-size: 80px; text-align: center;'>{options[user_choice]}</div>", unsafe_allow_html=True)
        st.markdown(f"**{user_choice}**", unsafe_allow_html=True)

    with col2:
        st.markdown("### 💻 컴퓨터")
        st.markdown(f"<div style='font-size: 80px; text-align: center;'>{options[computer_choice]}</div>", unsafe_allow_html=True)
        st.markdown(f"**{computer_choice}**", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>{result}</h2>", unsafe_allow_html=True)
