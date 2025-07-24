import streamlit as st

# 기본 설정
st.set_page_config(page_title="오늘의 할 일 리스트", layout="centered")
st.markdown("<h1 style='text-align: center;'>📝 오늘의 할 일 리스트</h1>", unsafe_allow_html=True)

# 세션 상태 초기화
if "todos" not in st.session_state:
    st.session_state.todos = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

# 할 일 추가 폼
with st.form("add_todo", clear_on_submit=True):
    new_todo = st.text_input("할 일을 입력하세요", "")
    submitted = st.form_submit_button("➕ 추가")
    if submitted and new_todo.strip():
        st.session_state.todos.append({"task": new_todo.strip(), "done": False})

# 할 일 목록
st.subheader("📋 할 일 목록")

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
