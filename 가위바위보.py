import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위바위보 게임", layout="centered")

st.title("✊✋✌️ 가위바위보 게임")
st.write("컴퓨터와 한판 대결!")

# 선택지와 이모지 매핑
options = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 사용자 선택
user_choice = st.radio("무엇을 낼까요?", list(options.keys()), horizontal=True)

# 대결 버튼
if st.button("대결하기!"):
    computer_choice = random.choice(list(options.keys()))

    # 결과 판정
    if user_choice == computer_choice:
        result_emoji = "😐"
        result_text = "비겼습니다!"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result_emoji = "🎉"
        result_text = "이겼습니다!"
    else:
        result_emoji = "💻"
        result_text = "졌습니다!"

    # 구분선
    st.markdown("---")

    # 나와 컴퓨터 선택 표시
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🙋‍♂️ 나")
        st.markdown(
            f"<div style='font-size: 80px; text-align: center;'>{options[user_choice]}</div>",
            unsafe_allow_html=True
        )
        st.markdown(f"<div style='text-align: center; font-weight: bold;'>{user_choice}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 💻 컴퓨터")
        st.markdown(
            f"<div style='font-size: 80px; text-align: center;'>{options[computer_choice]}</div>",
            unsafe_allow_html=True
        )
        st.markdown(f"<div style='text-align: center; font-weight: bold;'>{computer_choice}</div>", unsafe_allow_html=True)

    # 결과 출력
    st.markdown("---")
    st.markdown(
        f"<h2 style='text-align: center;'>{result_emoji} {result_text}</h2>",
        unsafe_allow_html=True
    )
