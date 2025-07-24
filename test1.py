# 할 일 목록 표시
st.subheader("📋 할 일 목록")

if st.session_state.todos:
    for i, todo in enumerate(st.session_state.todos):  # ← 여기까지 OK
        cols = st.columns([0.05, 0.6, 0.05, 0.15, 0.15])  # ← 이 줄이 반드시 들여쓰기 되어야 함

        # 이하 줄도 모두 들여쓰기 유지
        done = cols[0].checkbox("", value=todo["done"], key=f"done_{i}")
        st.session_state.todos[i]["done"] = done

        if st.session_state.edit_index == i:
            with cols[1]:
                updated_text = st.text_input("수정할 내용을 입력하세요", value=todo["task"], key=f"edit_input_{i}")
            if cols[3].button("💾 저장", key=f"save_{i}"):
                if updated_text.strip():
                    st.session_state.todos[i]["task"] = updated_text.strip()
                st.session_state.edit_index = None
        else:
            task_display = f"~~{todo['task']}~~" if done else todo["task"]
            cols[1].markdown(task_display)

            if cols[3].button("✏️ 수정", key=f"edit_{i}"):
                st.session_state.edit_index = i

        if cols[4].button("🗑 삭제", key=f"delete_{i}"):
            st.session_state.todos.pop(i)
            st.session_state.edit_index = None
            st.experimental_rerun()
else:
    st.info("할 일을 추가해보세요!")
