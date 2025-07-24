import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 할 일 리스트", layout="centered")

# 제목
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
        # 열 구성: 체크박스 / 텍스트 / 여백 / 수정 / 삭제
        cols = st.columns([0.05, 0.6, 0.05, 0.15, 0.15])

        # 완료 체크박스
        done = cols[0].checkbox("", value=todo["done"], key=f"done_{i}")
        st.session_state.todos[i]["done"] = done

        # 수정 중이면 입력창 표시
        if st.session_state.edit_index == i:
            with cols[1]:
                updated_text = st.text_input("수정할 내용을 입력하세요", value=todo["task"], key=f"edit_input_{i}")
            if cols[3].button("💾 저장", key=f"save_{i}"):
                if updated_text.strip():
                    st.session_state.todos[i]["task"] = updated_text.strip()
                st.session_state.edit_index = None
        else:
            # 할 일 텍스트 출력
            task_display = f"~~{todo['task']}~~" if done else todo["task"]
            cols[1].markdown(task_display)

            # 수정 버튼
            if cols[3].button("✏️ 수정", key=f"edit_{i}"):
                st.session_state.edit_index = i

        # 삭제 버튼
        if cols[4].button("🗑 삭제", key=f"delete_{i}"):
            st.session_state.todos.pop(i)
            st.session_state.edit_index = None
            st.experimental_rerun()
else:
    st.info("할 일을 추가해보세요!")

# 전체 삭제 버튼
st.markdown("---")
if st.button("❌ 전체 삭제"):
    st.session_state.todos.clear()
    st.session_state.edit_index = None
    st.success("모든 할 일이 삭제되었습니다.")
    st.experimental_rerun()
