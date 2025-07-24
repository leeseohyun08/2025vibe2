import streamlit as st

# 웹앱 기본 설정
st.set_page_config(page_title="오늘의 할 일 리스트", layout="centered")

st.markdown("<h1 style='text-align: center;'>📝 오늘의 할 일 리스트</h1>", unsafe_allow_html=True)
st.write("하루 동안 해야 할 일들을 정리하고 체크해보세요!")

# 세션 상태에 할 일 리스트 저장
if "todos" not in st.session_state:
    st.session_state.todos = []

# 새로운 할 일 추가 폼
with st.form("add_todo", clear_on_submit=True):
    new_todo = st.text_input("할 일을 입력하세요", "")
    submitted = st.form_submit_button("➕ 추가")
    if submitted and new_todo.strip():
        st.session_state.todos.append({"task": new_todo.strip(), "done": False})

# 할 일 리스트 보여주기
st.subheader("📋 할 일 목록")
if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):
        cols = st.columns([0.1, 0.7, 0.2])
        # 완료 여부 체크박스
        done = cols[0].checkbox("", value=todo["done"], key=f"done_{i}")
        st.session_state.todos[i]["done"] = done
        # 할 일 텍스트 출력
        task_display = f"~~{todo['task']}~~" if done else todo["task"]
        cols[1].markdown(task_display)
        # 삭제 버튼
        if cols[2].button("🗑 삭제", key=f"delete_{i}"):
            st.session_state.todos.pop(i)
            st.experimental_rerun()
else:
    st.info("아직 할 일이 없어요. 위에 입력창을 통해 추가해보세요!")

# 전체 삭제 버튼
st.markdown("---")
if st.button("❌ 전체 삭제"):
    st.session_state.todos.clear()
    st.success("모든 할 일이 삭제되었습니다.")
    st.experimental_rerun()
