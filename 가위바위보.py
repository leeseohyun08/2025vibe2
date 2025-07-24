import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="가위바위보 게임", layout="centered")

st.title("✊✋✌️ 가위바위보 게임")
st.write("컴퓨터와 대결해보세요!")

# 선택지 및 이모지 매핑
options = {
    "가위": "✌️",
    "바위": "✊",
    "보": "✋"
}

# 사용자 선택
user_choice = st.radio("무엇을 낼까요?", list(options.keys()), horizontal=True)

# 버튼 클릭 시 결과 처리
if st.button("대결하기!"):
    computer_choice = random.choice(list(options.keys()))

    # 결과 판정
    if user_choice == computer_choice:
        result = "😐 무승부!"
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "🎉 당신의 승리!"
    else:
        result = "💻 컴퓨터의 승리!"

    # 결과 출력
    st.markdown(f"""
    ### 🧑 당신: {options[user_choice]} {user_choice}  
    ### 💻 컴퓨터: {options[computer_choice]} {computer_choice}  
    ---
    ## 🏆 결과: {result}
    """)
