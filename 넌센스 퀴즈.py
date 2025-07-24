import streamlit as st
import random

# -------------------- 페이지 설정 --------------------
st.set_page_config(page_title="넌센스 퀴즈", layout="centered")
st.title("🧠 넌센스 퀴즈 게임")
st.write("재미있는 넌센스 퀴즈! 얼마나 맞출 수 있을까요?")

# -------------------- 넌센스 퀴즈 데이터 --------------------
quizzes = [
    {"question": "세상에서 가장 뜨거운 전화는?", "answer": "핫라인", "hint": "Hot + 선"},
    {"question": "소가 웃으면?", "answer": "우유", "hint": "소 = 우, 웃음 = 유"},
    {"question": "바나나가 웃으면?", "answer": "바나나킥", "hint": "바나나 + 웃음소리"},
    {"question": "자동차가 웃으면?", "answer": "카카오", "hint": "Car + ㅋㅋ"},
    {"question": "물고기의 반대말은?", "answer": "불고기", "hint": "물 ↔ 불"},
    {"question": "세상에서 가장 비싼 새는?", "answer": "백조", "hint": "100조"},
    {"question": "사자가 두 마리면?", "answer": "투사", "hint": "two + 사"},
    {"question": "세상에서 가장 착한 사자는?", "answer": "자원봉사자", "hint": "사자 중에 착한 사자"},
    {"question": "공이 웃으면?", "answer": "풋볼", "hint": "풋(웃음) + 볼"},
    {"question": "깜짝 놀란 소는?", "answer": "오우", "hint": "소 = 우, 놀람 = 오"},
    {"question": "하늘에서 내리는 돈은?", "answer": "월급", "hint": "하늘(회사)에서 떨어짐"},
    {"question": "먹으면 죽는 음식은?", "answer": "죽", "hint": "말장난"},
    {"question": "땅은 영어로 So, 물은?", "answer": "물소", "hint": "소 + 물"},
    {"question": "도둑이 가장 싫어하는 아이스크림은?", "answer": "누가바", "hint": "누가 봤다고 싫어함"},
    {"question": "피자가 웃으면?", "answer": "피식", "hint": "피자 + 식"},
    {"question": "이 세상에서 가장 맛있는 돈은?", "answer": "오천원", "hint": "오! 천 원!"},
    {"question": "자다가 깨는 새는?", "answer": "깨닭", "hint": "깨달음 → 깨닭"},
    {"question": "머리가 세 개 달린 용은?", "answer": "삼룡이", "hint": "세 = 삼 + 용"},
    {"question": "밥을 두 번 먹으면?", "answer": "두밥", "hint": "말장난"},
    {"question": "빵이 놀라면?", "answer": "빵야", "hint": "놀람 + 빵"},
]

# -------------------- 세션 상태 초기화 --------------------
defaults = {
    "quiz": random.choice(quizzes),
    "show_hint": False,
    "show_answer": False,
    "correct": None,
    "user_input": "",
    "score": 0
}

for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# -------------------- 오른쪽 상단 점수 표시 --------------------
st.markdown(
    f"<div style='position: absolute; top: 20px; right: 30px; font-size: 18px; color: gray;'>"
    f"🏅 점수: {st.session_state['score']}개</div>",
    unsafe_allow_html=True
)

# -------------------- 현재 문제 출력 --------------------
quiz = st.session_state["quiz"]
st.subheader(f"문제: {quiz['question']}")

# -------------------- 정답 입력 (엔터로 제출 + 입력창 초기화) --------------------
with st.form(key="answer_form"):
    user_answer = st.text_input("정답을 입력하세요", value=st.session_state["user_input"])
    submit_enter = st.form_submit_button("엔터로 제출")

    if submit_enter:
        user_input_cleaned = user_answer.strip()

        if user_input_cleaned:
            if user_input_cleaned == quiz["answer"]:
                if st.session_state["correct"] is not True:
                    st.session_state["score"] += 1
                st.session_state["correct"] = True
            else:
                st.session_state["correct"] = False

        # ✅ 입력창 초기화
        st.session_state["user_input"] = ""

# -------------------- 버튼 처리 --------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("힌트 보기", key="hint"):
        st.session_state["show_hint"] = True

with col2:
    if st.button("정답 보기", key="answer"):
        st.session_state["show_answer"] = True

with col3:
    if st.button("다음 문제", key="next"):
        current_question = st.session_state["quiz"]["question"]
        other_quizzes = [q for q in quizzes if q["question"] != current_question]

        if other_quizzes:
            st.session_state["quiz"] = random.choice(other_quizzes)
        else:
            st.info("📌 더 이상 새로운 문제가 없어요!")

        st.session_state["correct"] = None
        st.session_state["show_hint"] = False
        st.session_state["show_answer"] = False
        st.session_state["user_input"] = ""

# -------------------- 결과 출력 --------------------
if st.session_state["correct"] is True:
    st.success("🎉 정답입니다! 센스 최고예요!")
elif st.session_state["correct"] is False:
    st.error("😢 틀렸어요. 다시 한 번 생각해보세요!")

# -------------------- 힌트 / 정답 출력 --------------------
if st.session_state["show_hint"]:
    st.info(f"💡 힌트: {quiz['hint']}")

if st.session_state["show_answer"]:
    st.info(f"✅ 정답: {quiz['answer']}")
