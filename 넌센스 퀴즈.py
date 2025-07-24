import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="넌센스 퀴즈", layout="centered")
st.title("🧠 넌센스 퀴즈 게임")
st.write("재미있는 넌센스 퀴즈! 얼마나 맞출 수 있을까요?")

# 넌센스 문제 데이터 (문제, 정답, 힌트)
quizzes = [
    {"question": "세상에서 가장 뜨거운 전화는?", "answer": "핫라인", "hint": "Hot + 선"},
    {"question": "소가 웃으면?", "answer": "우유", "hint": "소 = 우, 웃음 = 유"},
    {"question": "바나나가 웃으면?", "answer": "바나나킥", "hint": "바나나 + 웃음소리"},
    {"question": "자동차가 웃으면?", "answer": "카카오", "hint": "Car + ㅋㅋ"},
    {"question": "물고기의 반대말은?", "answer": "불고기", "hint": "물 ↔ 불"},
]

# 문제 고르기
if "quiz" not in st.session_state:
    st.session_state.quiz = random.choice(quizzes)
    st.session_state.show_hint = False
    st.session_state.show_answer = False
    st.session_state.correct = None

quiz = st.session_state.quiz

st.subheader(f"문제: {quiz['question']}")

# 정답 입력
user_answer = st.text_input("정답을 입력하세요").strip()

# 정답 확인
if st.button("제출"):
    if user_answer:
        if user_answer == quiz["answer"]:
            st.session_state.correct = True
        else:
            st.session_state.correct = False

# 힌트 보기
if st.button("힌트 보기"):
    st.session_state.show_hint = True

# 정답 보기
if st.button("정답 보기"):
    st.session_state.show_answer = True

# 결과 출력
if st.session_state.co_
