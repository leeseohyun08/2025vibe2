import streamlit as st
import random

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="넌센스 퀴즈", layout="centered")
st.title("🧠 넌센스 퀴즈 게임")
st.write("재미있는 넌센스 퀴즈! 얼마나 맞출 수 있을까요?")

# -------------------- 퀴즈 데이터 --------------------
quizzes = [
    {"question": "세상에서 가장 뜨거운 전화는?", "answer": "핫라인", "hint": "Hot + 선"},
    {"question": "소가 웃으면?", "answer": "우유", "hint": "소 = 우, 웃음 = 유"},
    {"question": "바나나가 웃으면?", "answer": "바나나킥", "hint": "바나나 + 웃음소리"},
    {"question": "자동차가 웃으면?", "answer": "카카오", "hint": "Car + ㅋㅋ"},
    {"question": "물고기의 반대말은?", "answer": "불고기", "hint": "물 ↔ 불"},
]

# -------------------- 세션 상태 초기화 --------------------
if "quiz" not in st.session_state:
    st.session_state["quiz"] = random.choice(quizzes)
if "show_hint" not in st.session_state:
    st.session_state["show_hint"] = False
if "show_answer" not in st.session_state:
    st.session_state["show_answer"] = False
if "correct" not in st.session_state:
    st.session_state["correct"] = None
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# -------------------- 현재 퀴즈 출력 --------------------
quiz = st.session_state["quiz"]
st.subheader(f"문제: {quiz['question']}")

# -------------------- 입력창 --------------------
user_answer = st.text_input("정답을 입력하세요", value=st.session_state["user_input"])
st.session_state["user_input"] = user_answer.strip()

# -------------------- 제출 --------------------
if st.button("제출"):
    if st.session_state["user_input"]:
        if st.session_state["user_input"] == quiz["answer"]:
            st.session_state["correct"] = True
        else:
            st.session_state["correct"] = False

# -------------------- 힌트 보기 --------------------
if st.button("힌트 보기"):
    st.session_state["show_hint"] = True

# -------------------- 정답 보기 --------------------
if st.button("정답 보기"):
    st.session_state["show_answer"] = True

# -------------------- 결과 표시 --------------------
if st.session_state["correct"] is True:
    st.success("🎉 정답입니다! 센스 최고예요!")
elif st.session_state["correct"] is False:
    st.error("😢 틀렸어요. 다시 한 번 생각해보세요!")

# -------------------- 힌트 출력 --------------------
if st.session_state["show_hint"]:
    st.info(f"💡 힌트: {quiz['hint']}")

# -------------------- 정답 출력 --------------------
if st.session_state["show_answer"]:
    st.info(f"✅ 정답: {quiz['answer']}")

# -------------------- 다음 문제 --------------------
if st.button("다음 문제"):
    st.session_state["quiz"] = random.choice(quizzes)
    st.session_state["correct"] = None
    st.session_state["show_hint"] = False
    st.session_state["show_answer"] = False
    st.session_state["user_input"] = ""
