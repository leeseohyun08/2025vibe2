import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="숫자 맞추기 게임", layout="centered")
st.title("🔢 숫자 맞추기 게임")
st.write("1부터 20 사이의 숫자를 맞춰보세요!")

# 세션 상태 초기화
if "target" not in st.session_state:
    st.session_state.target = random.randint(1, 20)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "success" not in st.session_state:
    st.session_state.success = False

# 숫자 입력
if not st.session_state.success:
    guess = st.number_input("숫자를 입력하세요 (1~20)", min_value=1, max_value=20, step=1)
    if st.button("제출"):
        st.session_state.attempts += 1
        if guess == st.session_state.target:
            st.success(f"🎉 정답입니다! {st.session_state.attempts}번 만에 맞췄어요.")
            st.session_state.success = True
        elif guess < st.session_state.target:
            st.warning("🔼 더 큰 수를 입력해보세요.")
        else:
            st.warning("🔽 더 작은 수를 입력해보세요.")
else:
    st.success(f"🎯 정답은 {st.session_state.target}이었어요. 다시 도전해보세요!")

# 리셋 버튼
if st.button("🔄 게임 다시 시작"):
    st.session_state.target = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.success = False
    st.experimental_rerun()
