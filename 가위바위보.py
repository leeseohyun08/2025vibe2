import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위바위보 게임", layout="centered")

st.title("✊✋✌️ 가위바위보 게임")
st.write("컴퓨터와 한판 대결!")

# 가위바위보 선택 이모지 매핑
options = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 사용자 선택
user_choice = st.radio("무엇을 낼까요?", list(options.keys()), horizontal=True)

# 대결 버튼 클릭 시
if st.button("대결하기!"):
    computer_choice = random.choice(list(options.keys()))

    # 승부 판정
    if user_choice == computer_choice:
        result = "😐 무승부!"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 내가 이겼어!"
    else:
        result = "💻 컴퓨터가 이겼어!"

    # 구분선
    st.markdown("---")

    # 결과 시각화 (2열)
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

    # 결과 텍스트
    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center;'>{result}</h2>", unsafe_allow_html=True)
